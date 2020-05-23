npm run build-scss
npm run minify-css
cp dist/styles.css docs/css/styles.css
cp dist/styles.min.css docs/css/styles.min.css
# gzip -k docs/css/styles.min.css