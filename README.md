# Should You Sign It? website

- `landing/` is the landing page, deployed on Render with `render.yaml` (a Blueprint). `build.sh` copies it into `dist/` together with the support page (`index.html`, served as `support.html`) and `privacy.html`.
- The repo root (`index.html`, `privacy.html`) is also served by GitHub Pages; those are the support and privacy URLs in App Store Connect.
- When the app is live, set `APP_STORE_URL` in `landing/site.js` and every download button links to the App Store.
- Live at https://www.shouldyousignit.com (the bare domain redirects there). DNS is on Cloudflare, DNS only, pointing at Render.
- Cloudflare Web Analytics: put the site token in `CF_ANALYTICS_TOKEN` in `landing/site.js`. It is cookieless; the CSP in `render.yaml` allows its script and beacon.

The site uses system fonts and local images and sets no cookies. The only third-party request is Cloudflare Web Analytics, once a token is set. The Content-Security-Policy in `render.yaml` allows nothing else.
