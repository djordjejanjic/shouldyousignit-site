#!/bin/sh
# Assembles the Render site: the landing page plus the support and privacy pages that GitHub Pages also serves.
set -eu
rm -rf dist
mkdir -p dist
cp -R landing/. dist/
cp privacy.html dist/privacy.html
cp index.html dist/support.html
