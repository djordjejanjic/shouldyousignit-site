// Cloudflare Web Analytics site token (Cloudflare dashboard > Analytics & Logs > Web Analytics > your site).
// Cookieless and without fingerprinting; empty means nothing is loaded.
const CF_ANALYTICS_TOKEN = "";
if (CF_ANALYTICS_TOKEN) {
  var beacon = document.createElement("script");
  beacon.defer = true;
  beacon.src = "https://static.cloudflareinsights.com/beacon.min.js";
  beacon.setAttribute("data-cf-beacon", JSON.stringify({ token: CF_ANALYTICS_TOKEN }));
  document.head.appendChild(beacon);
}

// Set this to the App Store link once the app is live, e.g. "https://apps.apple.com/app/id1234567890".
// Until then, every download button reads "Coming soon to the App Store".
const APP_STORE_URL = "";
document.querySelectorAll("[data-store]").forEach(function (el) {
  if (APP_STORE_URL) { el.href = APP_STORE_URL; return; }
  el.classList.add("soon");
  el.removeAttribute("href");
  el.setAttribute("aria-disabled", "true");
  var label = el.querySelector("[data-store-label]");
  if (label) label.textContent = "Coming soon to the App Store";
  else el.textContent = "Coming soon";
});

// Report inside the hero phone: tap a clause to expand or collapse it, like in the app.
document.querySelectorAll(".ios-toggle").forEach(function (btn) {
  btn.addEventListener("click", function () {
    var row = btn.closest(".ios-concern");
    var open = row.classList.toggle("open");
    btn.setAttribute("aria-expanded", open ? "true" : "false");
  });
});
