// Backend used when the page is served from GitHub Pages.
//
// No server: the repository is the database. Reads and writes go through the
// GitHub Contents API with a fine-grained token kept only in this browser.
(() => {
  const API = "https://api.github.com";
  const TOKEN_KEY = "prep.planner.token";
  const OPS_KEY = "prep.planner.pendingOps";
  const DEBOUNCE_MS = 4000;
  const PROGRESS = "webapp/progress.json";
  const SCHEDULE = "webapp/schedule.json";

  // btoa() alone throws outside Latin-1, and these files are full of em dashes.
  function b64encode(str) {
    const bytes = new TextEncoder().encode(str);
    let bin = "";
    for (let i = 0; i < bytes.length; i += 0x8000) bin += String.fromCharCode.apply(null, bytes.subarray(i, i + 0x8000));
    return btoa(bin);
  }
  function b64decode(b64) {
    const bin = atob(String(b64).replace(/\s/g, ""));
    return new TextDecoder().decode(Uint8Array.from(bin, (c) => c.charCodeAt(0)));
  }
  function load(key, fallback) {
    try { const raw = localStorage.getItem(key); return raw ? JSON.parse(raw) : fallback; } catch { return fallback; }
  }
  function store(key, value) {
    try { localStorage.setItem(key, JSON.stringify(value)); } catch { /* private mode: memory only */ }
  }

  window.createGitHubBackend = (config) => {
    const T = window.PrepTemplates;
    const repo = config.repo;
    const base = `${API}/repos/${repo.owner}/${repo.name}/contents`;
    const ref = repo.branch || "main";
    let token = "";
    try { token = localStorage.getItem(TOKEN_KEY) || ""; } catch { token = ""; }

    let templates = null;
    let progress = { version: 1, done: {} };
    const shas = new Map();
    let pendingOps = load(OPS_KEY, []);
    let flushTimer = null;
    let flushing = false;
    const listeners = [];
    const emit = (text, kind) => listeners.forEach((cb) => cb(text, kind));

    function headers(extra) {
      const h = Object.assign({ Accept: "application/vnd.github+json" }, extra || {});
      if (token) h.Authorization = `Bearer ${token}`;
      return h;
    }
    async function ghFetch(url, opts) {
      const res = await fetch(url, opts);
      if (res.status === 401) throw new Error("Token rejected. Re-paste it in Settings.");
      if (res.status === 403) {
        const body = await res.json().catch(() => ({}));
        if (/rate limit/i.test(body.message || "")) throw new Error(token ? "GitHub rate limit hit. Wait a few minutes." : "Rate limited. Add your token in Settings.");
        throw new Error(body.message || "GitHub refused the request (403).");
      }
      return res;
    }
    async function getContents(path) {
      const res = await ghFetch(`${base}/${encodeURI(path)}?ref=${encodeURIComponent(ref)}&t=${Date.now()}`, { headers: headers(), cache: "no-store" });
      if (res.status === 404) return null;
      if (!res.ok) { const b = await res.json().catch(() => ({})); throw new Error(b.message || `Couldn't read ${path} (${res.status})`); }
      const data = await res.json();
      shas.set(path, data.sha);
      return { content: b64decode(data.content || ""), sha: data.sha };
    }
    async function putContents(path, content, message, sha) {
      if (!token) throw new Error("Add your GitHub token in Settings before saving.");
      const body = { message, content: b64encode(content), branch: ref };
      if (sha) body.sha = sha;
      const res = await ghFetch(`${base}/${encodeURI(path)}`, { method: "PUT", headers: headers({ "Content-Type": "application/json" }), body: JSON.stringify(body) });
      if (res.status === 409 || res.status === 422) return { conflict: true };
      if (!res.ok) { const b = await res.json().catch(() => ({})); throw new Error(b.message || `Couldn't save ${path} (${res.status})`); }
      const data = await res.json();
      shas.set(path, data.content.sha);
      return { sha: data.content.sha };
    }

    // ---- progress: replay an op log, never merge two states --------------
    // Unticking deletes a key, so a union of two states would resurrect it.
    function applyOps(done, ops) {
      for (const op of ops) { if (op.done) done[op.id] = op.at; else delete done[op.id]; }
      return done;
    }
    const localView = () => applyOps(Object.assign({}, progress.done), pendingOps);
    function commitMessage(ops) {
      const plus = ops.filter((o) => o.done).length, minus = ops.length - plus;
      const ids = [...new Set(ops.map((o) => o.id))];
      const tail = ids.length <= 3 ? ids.join(", ") : `${ids.slice(0, 3).join(", ")} +${ids.length - 3} more`;
      return `progress: ${[plus && `+${plus}`, minus && `-${minus}`].filter(Boolean).join(" ")} (${tail})`;
    }
    async function flush() {
      clearTimeout(flushTimer);
      flushTimer = null;
      if (flushing || !pendingOps.length) return;
      if (!token) { emit("Not saved — add your token", "error"); return; }
      if (!navigator.onLine) { emit(`Offline — ${pendingOps.length} queued`, "warn"); return; }
      flushing = true;
      emit("Syncing…", "busy");
      try {
        for (let attempt = 0; attempt < 3; attempt++) {
          const taking = pendingOps.slice();
          const remote = await getContents(PROGRESS);
          const state = remote ? JSON.parse(remote.content) : { version: 1, done: {} };
          state.done = applyOps(state.done || {}, taking);
          const r = await putContents(PROGRESS, `${JSON.stringify(state, null, 2)}\n`, commitMessage(taking), remote && remote.sha);
          if (r.conflict) continue;
          progress = state;
          pendingOps = pendingOps.slice(taking.length);
          store(OPS_KEY, pendingOps);
          emit(pendingOps.length ? `${pendingOps.length} queued` : "Synced", "ok");
          flushing = false;
          if (pendingOps.length) schedule();
          return;
        }
        flushing = false;
        emit("Sync conflict — retrying", "warn");
        schedule();
      } catch (err) {
        flushing = false;
        emit(`Not synced: ${err.message}`, "error");
      }
    }
    function schedule() { clearTimeout(flushTimer); flushTimer = setTimeout(flush, DEBOUNCE_MS); }
    window.addEventListener("online", () => { if (pendingOps.length) flush(); });
    window.addEventListener("beforeunload", (e) => { if (pendingOps.length) { e.preventDefault(); e.returnValue = ""; } });

    // ---- files ------------------------------------------------------------
    function guard(path) {
      const safe = T.safePath(templates, path);
      if (!safe) throw new Error("That file isn't inside the prep folders.");
      return safe;
    }
    async function writeFile(path, content) {
      const safe = guard(path);
      let sha = shas.get(safe);
      if (sha === undefined) { const cur = await getContents(safe); sha = cur ? cur.sha : null; }
      let r = await putContents(safe, content, `planner: update ${safe}`, sha);
      if (r.conflict) {
        const fresh = await getContents(safe);
        r = await putContents(safe, content, `planner: update ${safe}`, fresh ? fresh.sha : null);
        if (r.conflict) throw new Error(`${safe} changed elsewhere. Reload and try again.`);
      }
      return { ok: true, path: safe, created: !sha };
    }
    async function readFile(path) {
      const safe = guard(path);
      const cur = await getContents(safe);
      if (cur) return { ok: true, path: safe, content: cur.content, created: false };
      // Not in the repo yet: hand back the template unsaved; the first Save creates it.
      const skel = T.skeletonFor(templates, safe);
      if (skel === null) throw new Error(`${safe.split("/").pop()} doesn't exist yet.`);
      return { ok: true, path: safe, content: skel, created: true };
    }
    let scheduleCache = null;
    async function getSchedule() {
      const cur = await getContents(SCHEDULE);
      scheduleCache = T.normalise(cur ? JSON.parse(cur.content) : {});
      return scheduleCache;
    }
    async function createDailyLog(date) {
      const path = `daily-logs/${date}.md`;
      const cur = await getContents(path);
      if (cur) return { ok: true, path, content: cur.content, created: false };
      return { ok: true, path, content: T.dailyLog(templates, date, scheduleCache || await getSchedule()), created: true };
    }

    return {
      kind: "github",
      repo,
      canWrite: () => Boolean(token),
      needsSetup: () => !token,
      onStatus: (cb) => listeners.push(cb),
      async setToken(value) {
        const candidate = String(value || "").trim();
        if (!candidate) throw new Error("Paste a token first.");
        const res = await fetch(`${base}/${PROGRESS}?ref=${encodeURIComponent(ref)}`, {
          headers: { Accept: "application/vnd.github+json", Authorization: `Bearer ${candidate}` },
        });
        if (!res.ok) throw new Error(res.status === 401 ? "GitHub rejected that token." : res.status === 404 ? "That token can't see this repository. Check its repository access." : `GitHub returned ${res.status}.`);
        token = candidate;
        try { localStorage.setItem(TOKEN_KEY, token); } catch { /* private mode */ }
        if (pendingOps.length) flush();
        return true;
      },
      clearToken() { token = ""; try { localStorage.removeItem(TOKEN_KEY); } catch { /* ignore */ } },
      async getPlan() {
        const res = await fetch(`data/plan.json?t=${Date.now()}`, { cache: "no-store" });
        if (!res.ok) throw new Error(`Couldn't load the plan (${res.status}). The site build may still be running.`);
        const plan = await res.json();
        templates = plan.templates;
        return plan;
      },
      async getProgress() {
        const cur = await getContents(PROGRESS);
        progress = cur ? JSON.parse(cur.content) : { version: 1, done: {} };
        if (pendingOps.length) schedule();
        return { version: 1, done: localView() };
      },
      async setTask(id, done) {
        pendingOps.push({ id, done: Boolean(done), at: new Date().toISOString() });
        store(OPS_KEY, pendingOps);
        emit(`${pendingOps.length} queued`, "busy");
        schedule();
        return { ok: true, done: localView() };
      },
      getSchedule,
      // Read fresh, apply the change, write with the fresh sha; retry on a race.
      async updateSchedule(mutate) {
        for (let attempt = 0; attempt < 3; attempt++) {
          const cur = await getContents(SCHEDULE);
          const next = T.normalise(mutate(T.normalise(cur ? JSON.parse(cur.content) : {})));
          const r = await putContents(SCHEDULE, T.scheduleText(next), "schedule: update start date / skipped days", cur && cur.sha);
          if (!r.conflict) { scheduleCache = next; return next; }
        }
        throw new Error("The schedule changed on another device. Reload and try again.");
      },
      readFile,
      writeFile,
      createDailyLog,
      async saveDailyProgress(date, ctx) {
        const path = `daily-logs/${date}.md`;
        const cur = await getContents(path);
        const base = cur ? cur.content : T.dailyLog(templates, date, scheduleCache || await getSchedule());
        const { block, completed, total } = T.progressBlock(templates, ctx.day, ctx.done, T.stampNow());
        const content = T.applyProgressBlock(base, templates, block);
        await writeFile(path, content);
        return { ok: true, path, content, completed, total };
      },
      offlineCount: () => pendingOps.length,
      flush,
      describe: () => `${repo.owner}/${repo.name}`,
    };
  };
})();
