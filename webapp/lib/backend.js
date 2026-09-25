// Picks the data layer for however this page is being served.
//
//   localhost      -> webapp/server.py, reading and writing the local disk
//   anything else  -> GitHub Pages, reading and writing the repo via the API
//
// index.html talks only to the object this returns.
(() => {
  const LOCAL_HOSTS = ["127.0.0.1", "localhost", "[::1]"];

  window.selectBackend = async () => {
    if (LOCAL_HOSTS.includes(location.hostname)) return window.createLocalBackend();
    const res = await fetch(`data/config.json?t=${Date.now()}`, { cache: "no-store" });
    if (!res.ok) {
      throw new Error("This page needs the planner server (webapp\\start.bat) or the hosted GitHub Pages copy.");
    }
    return window.createGitHubBackend(await res.json());
  };
})();
