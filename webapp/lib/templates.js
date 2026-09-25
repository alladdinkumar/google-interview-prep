// Browser twins of the Python that decides dates and creates files.
//
// The hosted planner has no server, so it must compute calendar dates from
// schedule.json and build new Markdown files exactly as webapp/server.py and
// webapp/schedule.py do. Every template string comes from plan.json (emitted from
// server.py's own constants); only the interpolation is written here.
// tests/parity.mjs asserts byte-identical output for a fixed set of inputs.
(() => {
  const DAY_NAMES = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"];
  const WEEKDAY_LONG = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];
  const pad = (n) => String(n).padStart(2, "0");

  // Local midnight, so arithmetic never slips a day across a timezone.
  function parseIso(iso) {
    const [y, m, d] = iso.split("-").map(Number);
    return new Date(y, m - 1, d);
  }
  function isoOf(date) {
    return `${date.getFullYear()}-${pad(date.getMonth() + 1)}-${pad(date.getDate())}`;
  }
  function addDays(iso, n) {
    const d = parseIso(iso);
    d.setDate(d.getDate() + n);
    return isoOf(d);
  }
  function daysBetween(a, b) {
    return Math.round((parseIso(b) - parseIso(a)) / 86400000);
  }

  // ---- schedule.py ---------------------------------------------------------
  function normalise(s) {
    const skips = [...new Set((s.skips || []).filter((x) => /^\d{4}-\d{2}-\d{2}$/.test(x)))].sort();
    return { version: 1, start: s.start || "2026-09-14", skips };
  }
  function dateOf(dayNumber, sched) {
    let date = addDays(sched.start, dayNumber - 1);
    for (const s of sched.skips) {
      if (s < sched.start) continue;
      if (s <= date) date = addDays(date, 1);
      else break;
    }
    return date;
  }
  // Plan day on a date: 0 before the start, null on a skipped date.
  function dayOf(iso, sched) {
    if (sched.skips.includes(iso)) return null;
    if (iso < sched.start) return 0;
    const skipped = sched.skips.filter((s) => s >= sched.start && s < iso).length;
    return daysBetween(sched.start, iso) + 1 - skipped;
  }
  // json.dumps(data, indent=2, sort_keys=True) + "\n"
  function scheduleText(sched) {
    const s = normalise(sched);
    const skips = s.skips.length ? `[\n${s.skips.map((x) => `    "${x}"`).join(",\n")}\n  ]` : "[]";
    return `{\n  "skips": ${skips},\n  "start": "${s.start}",\n  "version": 1\n}\n`;
  }

  // ---- server.py: notes --------------------------------------------------
  function noteTitle(path) {
    const stem = path.slice(path.lastIndexOf("/") + 1).replace(/\.md$/, "");
    const parts = stem.split("-");
    const tail = parts.length > 2 ? parts.slice(2).join("-") : parts[parts.length - 1];
    const words = tail.replace(/-/g, " ");
    return words.slice(0, 1).toUpperCase() + words.slice(1);
  }
  function skeletonFor(t, path) {
    if (path.startsWith("notes/")) {
      const segs = path.split("/");
      const folder = segs.length >= 3 ? segs[1] : "";
      const tpl = Object.prototype.hasOwnProperty.call(t.notes, folder) ? t.notes[folder] : t.noteDefault;
      return tpl.split("{title}").join(noteTitle(path));
    }
    if (path.startsWith("reviews/weekly/")) return t.reviewWeekly;
    if (path.startsWith("reviews/monthly/")) return t.reviewMonthly;
    return null;
  }

  // ---- server.py: daily log ---------------------------------------------
  function phaseOfWeek(t, week) {
    if (week < 1) return 1;
    let best = 1;
    for (const [p, v] of Object.entries(t.phases)) if (week >= v.startWeek && Number(p) > best) best = Number(p);
    return best;
  }
  function dailyLog(t, iso, sched) {
    const n = dayOf(iso, sched) || 0;
    const week = n >= 1 ? Math.floor((n - 1) / 7) + 1 : 0;
    const phase = phaseOfWeek(t, week);
    const weekday = WEEKDAY_LONG[(parseIso(iso).getDay() + 6) % 7];
    const planWeekday = n >= 1 ? DAY_NAMES[(n - 1) % 7] : "-";
    const hours = { Sat: "3.75", Sun: "2.0" }[planWeekday] || "0.75";
    const fields = {
      date: iso, day_of_week: weekday, plan_day: String(n), plan_weekday: planWeekday,
      phase: t.phases[phase].slug, overall_week: String(week), target_hours: hours,
    };
    let text = t.dailyLog;
    for (const [k, v] of Object.entries(fields)) text = text.replace(new RegExp(`^${k}: .*$`, "m"), `${k}: ${v}`);
    return text;
  }

  // ---- server.py: progress snapshot -------------------------------------
  function progressBlock(t, day, done, stamp) {
    const completed = day.tasks.filter((x) => done[x.id]).length;
    const lines = [t.progressStart, "## Planner progress",
      `Saved from the planner: ${stamp}. **${completed}/${day.tasks.length} sessions completed.**`, ""];
    for (const x of day.tasks) {
      lines.push(`- [${done[x.id] ? "x" : " "}] **${x.slot} (${x.time})** — ${x.focus.replace(/`([^`]+)`/g, "$1")}`);
      if (x.outputText) lines.push(`  - Record: ${x.outputText}`);
    }
    lines.push("", t.progressEnd);
    return { block: lines.join("\n"), completed, total: day.tasks.length };
  }
  const escapeRe = (s) => s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
  function applyProgressBlock(text, t, block) {
    const re = new RegExp(`${escapeRe(t.progressStart)}[\\s\\S]*?${escapeRe(t.progressEnd)}`);
    if (re.test(text)) return text.replace(re, () => block);
    return `${text.replace(/\s+$/, "")}\n\n${block}\n`;
  }
  function stampNow() {
    const n = new Date();
    return `${isoOf(n)} ${pad(n.getHours())}:${pad(n.getMinutes())}`;
  }

  // ---- server.py: safe_path ---------------------------------------------
  function safePath(t, rel) {
    const path = String(rel || "").replace(/\\/g, "/").replace(/^\/+/, "");
    if (!path.endsWith(".md") || path.split("/").includes("..")) return null;
    return t.allowedDirs.includes(path.split("/")[0]) ? path : null;
  }

  window.PrepTemplates = {
    DAY_NAMES, WEEKDAY_LONG, parseIso, isoOf, addDays, daysBetween,
    normalise, dateOf, dayOf, scheduleText, noteTitle, skeletonFor, dailyLog,
    progressBlock, applyProgressBlock, stampNow, safePath,
  };
})();
