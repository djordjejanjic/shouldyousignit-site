# Should You Sign It? website

- `landing/` is the landing page, deployed on Render with `render.yaml` (a Blueprint). `build.sh` copies it into `dist/` together with the support page (`index.html`, served as `support.html`) and `privacy.html`.
- The repo root (`index.html`, `privacy.html`) is also served by GitHub Pages; those are the support and privacy URLs in App Store Connect.
- When the app is live, set `APP_STORE_URL` in `landing/site.js` and every download button links to the App Store.
- If you add a custom domain on Render, replace `shouldyousignit.onrender.com` in `landing/index.html`, `landing/robots.txt` and `landing/sitemap.xml`.

The site loads nothing from third parties: system fonts, local images, no analytics, and a strict Content-Security-Policy set in `render.yaml`.
