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
