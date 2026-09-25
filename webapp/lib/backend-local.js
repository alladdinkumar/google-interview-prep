// Backend used when webapp/server.py serves the page on localhost.
(() => {
  async function api(path, body) {
    const opts = body === undefined
      ? { cache: "no-store" }
      : { method: "POST", headers: { "Content-Type": "application/json", "X-Prep-Planner": "1" }, body: JSON.stringify(body) };
    const res = await fetch(path, opts);
    const data = await res.json().catch(() => ({}));
    if (!res.ok) throw new Error(data.error || `Request failed (${res.status})`);
    return data;
  }

  window.createLocalBackend = () => {
    const T = window.PrepTemplates;
    let templates = null;
    return {
      kind: "local",
      canWrite: () => true,
      needsSetup: () => false,
      async getPlan() { const p = await api("/api/plan"); templates = p.templates; return p; },
      getProgress: () => api("/api/progress"),
      setTask: (id, done) => api("/api/progress", { id, done }),
      getSchedule: () => api("/api/schedule"),
      // mutate(schedule) -> schedule. Read fresh, apply, write: the same contract the
      // GitHub backend uses, so a change made on another device is never overwritten.
      async updateSchedule(mutate) {
        const fresh = T.normalise(await api("/api/schedule"));
        return api("/api/schedule", T.normalise(mutate(fresh)));
      },
      readFile: (path) => api(`/api/file?path=${encodeURIComponent(path)}`),
      writeFile: (path, content) => api("/api/file", { path, content }),
      createDailyLog: (date) => api("/api/daily-log", { date }),
      async saveDailyProgress(date, ctx) {
        const log = await api("/api/daily-log", { date });
        const { block, completed, total } = T.progressBlock(templates, ctx.day, ctx.done, T.stampNow());
        const content = T.applyProgressBlock(log.content, templates, block);
        await api("/api/file", { path: log.path, content });
        return { ok: true, path: log.path, content, completed, total };
      },
      offlineCount: () => 0,
      flush: async () => {},
      describe: () => "the local planner server",
    };
  };
})();
