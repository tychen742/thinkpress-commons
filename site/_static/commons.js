// Show the guides to staff (every role except students). Press enforces
// access on the server; this only avoids links that bounce visitors away.
(async () => {
  const STAFF = new Set(["ta", "instructor", "editor", "author", "admin"]);
  try {
    const r = await fetch("/api/me", { credentials: "include", cache: "no-store" });
    if (!r.ok) return;
    const me = await r.json();
    if (me.authenticated && STAFF.has(me.user.role)) document.documentElement.classList.add("tp-staff");
  } catch (e) { /* keep the visitor view */ }
})();
