/* Walk every day in a real browser and check what each session actually renders.
 *
 * Paste into the console on the planner (local or hosted), or run it through a browser
 * automation tool. It clicks through all days and inspects the DOM that came out.
 *
 * Why: the catalogue test reads plan.json, the input to rendering. On the GATE planner
 * that passed twice while the page showed a channel page, because the bad link was
 * built during rendering. This is the check that sees what you see.
 */
(async () => {
  const WATCH = /^https:\/\/www\.youtube\.com\/watch\?v=[A-Za-z0-9_-]{11}$/;
  const CHANNEL = /youtube\.com\/(@|channel\/|c\/)|[?&]list=/;
  const GEM = /^https:\/\/(www\.google\.com\/search\?udm=50&q=|gemini\.google\.com\/app$)/;
  const next = document.getElementById("nextBtn"), jump = document.getElementById("jumpInput");
  if (!next || !jump) return console.error("Not the planner page.");
  jump.value = 1; jump.dispatchEvent(new Event("change"));
  const total = Number(jump.max), problems = [], videos = new Set();
  const n = { days: 0, sessions: 0, topicBlocks: 0, problemCards: 0, videoChips: 0, gemini: 0, questions: 0, practice: 0 };
  for (let i = 0; i < total; i++) {
    const day = jump.value;
    const list = [...document.querySelectorAll("#sessions .session")];
    n.days++;
    if (!list.length) problems.push(`day ${day}: no sessions`);
    for (const s of list) {
      n.sessions++;
      for (const a of s.querySelectorAll("a[href]")) {
        const h = a.getAttribute("href") || "";
        if (!h || /undefined|null/.test(h)) problems.push(`day ${day}: broken href "${h}"`);
        if (CHANNEL.test(h)) problems.push(`day ${day}: channel/playlist ${h}`);
        if (!h.startsWith("https://")) problems.push(`day ${day}: non-https ${h}`);
      }
      for (const a of s.querySelectorAll(".links.rows a.chip.video")) {
        n.videoChips++;
        const h = a.getAttribute("href");
        if (!WATCH.test(h)) problems.push(`day ${day}: bad video ${h}`); else videos.add(h.slice(-11));
      }
      for (const g of s.querySelectorAll("a.chip.gem")) {
        n.gemini++;
        if (!GEM.test(g.getAttribute("href"))) problems.push(`day ${day}: bad Gemini link`);
        if (g.href.includes("udm=50") && decodeURIComponent(g.href).length > 9000) problems.push(`day ${day}: prompt URL too long`);
      }
      for (const card of s.querySelectorAll(".problem")) {
        n.problemCards++;
        if (!card.querySelector("a.chip.practice")) problems.push(`day ${day}: problem card without a solve link`);
        if (!card.querySelector(".links.rows a.chip.video")) problems.push(`day ${day}: problem card without a solution video`);
        if (card.querySelectorAll("a.chip.gem").length !== 4) problems.push(`day ${day}: problem card without its 4 prompts`);
      }
      for (const t of s.querySelectorAll(".topic")) {
        n.topicBlocks++;
        const id = t.querySelector(".tid").textContent;
        const vids = t.querySelectorAll(":scope > .topicbody > div > .links.rows a.chip.video");
        if (vids.length < 3) problems.push(`day ${day}: ${id} shows ${vids.length} videos`);
        const qs = t.querySelectorAll(".qs li");
        n.questions += qs.length;
        if (qs.length !== 10) problems.push(`day ${day}: ${id} shows ${qs.length} questions`);
        if ([...qs].some((li) => !li.querySelector("a.chip.gem"))) problems.push(`day ${day}: ${id} question without a Gemini link`);
        const prac = [...t.querySelectorAll("h5")].find((h) => h.textContent.startsWith("Practice"));
        const count = prac ? prac.nextElementSibling.querySelectorAll("a.chip").length : 0;
        n.practice += count;
        if (/^(DS|AL)-/.test(id) && count < 4) problems.push(`day ${day}: ${id} shows ${count} practice items`);
        if (t.querySelectorAll(":scope > .topicbody a.chip.gem").length < 5 + qs.length) problems.push(`day ${day}: ${id} missing prompts`);
      }
    }
    const firstTopic = document.querySelector(".topic");
    if (firstTopic && !firstTopic.open) problems.push(`day ${day}: first topic block is collapsed`);
    if (i < total - 1) next.click();
  }
  const result = Object.assign(n, { distinctVideos: videos.size, problems: problems.length, sample: problems.slice(0, 30) });
  console.log(result);
  return result;
})();
