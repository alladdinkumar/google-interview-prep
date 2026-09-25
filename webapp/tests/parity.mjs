// Assert the JavaScript twins (lib/templates.js) produce exactly what the Python does.
//
//     python webapp/build_site.py && python webapp/tests/make_fixtures.py && node webapp/tests/parity.mjs
//
// A divergence means the phone would compute a different date for a plan day, or write
// a different file, than the laptop — the failure this whole design exists to prevent.
import { readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import vm from "node:vm";

const here = dirname(fileURLToPath(import.meta.url));
const webapp = dirname(here);
const root = dirname(webapp);
const sandbox = { window: {}, console };
vm.createContext(sandbox);
vm.runInContext(readFileSync(join(webapp, "lib", "templates.js"), "utf8"), sandbox);
const T = sandbox.window.PrepTemplates;
const plan = JSON.parse(readFileSync(join(root, "site", "data", "plan.json"), "utf8"));
const t = plan.templates;
const fx = JSON.parse(readFileSync(join(here, "fixtures.json"), "utf8"));

let checks = 0, failures = 0;
function check(name, expected, actual) {
  checks++;
  if (JSON.stringify(expected) === JSON.stringify(actual)) return;
  failures++;
  console.error(`FAIL  ${name}\n   python: ${JSON.stringify(expected).slice(0, 200)}\n   js    : ${JSON.stringify(actual).slice(0, 200)}`);
}

for (const s of fx.schedules) {
  const sched = T.normalise(s.sched);
  check(`normalise ${s.sched.start}`, s.sched, sched);
  check(`scheduleText ${s.sched.start}`, s.text, T.scheduleText(sched));
  for (const [n, d] of Object.entries(s.dateOf)) check(`dateOf ${n} @${sched.start}`, d, T.dateOf(Number(n), sched));
  for (const [d, n] of Object.entries(s.dayOf)) check(`dayOf ${d} @${sched.start}`, n, T.dayOf(d, sched));
  for (const [d, text] of Object.entries(s.dailyLog)) check(`dailyLog ${d} @${sched.start}`, text, T.dailyLog(t, d, sched));
}
for (const [p, text] of Object.entries(fx.notes)) check(`skeleton ${p}`, text, T.skeletonFor(t, p));
for (const [p, ok] of Object.entries(fx.safe)) check(`safePath ${p}`, ok, T.safePath(t, p) !== null);
const byNum = new Map(plan.days.map((d) => [d.dayNumber, d]));
for (const e of fx.progress) {
  const r = T.progressBlock(t, byNum.get(e.day), e.done, fx.stamp);
  check(`progressBlock day ${e.day}`, e.block, r.block);
  check(`progress count day ${e.day}`, e.completed, r.completed);
}
// append / replace use the daily log for 2026-10-01 on the default schedule
const sched0 = T.normalise(fx.schedules[0].sched);
for (const e of fx.progress) {
  const base = T.dailyLog(t, "2026-10-01", sched0);
  check(`append day ${e.day}`, e.appended, T.applyProgressBlock(base, t, e.block));
  check(`replace day ${e.day}`, e.replaced, T.applyProgressBlock(T.applyProgressBlock(base, t, e.block), t, e.block));
}

// Round trip: every plan day maps to a date that maps back to it, across skips.
for (const s of fx.schedules) {
  const sched = T.normalise(s.sched);
  for (let n = 1; n <= plan.days.length; n++) {
    const d = T.dateOf(n, sched);
    if (T.dayOf(d, sched) !== n) { failures++; console.error(`FAIL  round trip day ${n} -> ${d} @${sched.start}`); break; }
  }
  checks++;
}
console.log(`${checks - failures}/${checks} parity checks passed`);
process.exit(failures ? 1 : 0);
