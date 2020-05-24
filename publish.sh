# Regular build process
npm run build-scss
npm run minify-css

# Copy to docs folder
cp dist/styles.css docs/css/styles.css
cp dist/styles.min.css docs/css/styles.min.css
# gzip -k docs/css/styles.min.css

# Also build a utilities only version
node ./node_modules/node-sass/bin/node-sass src/utilities.scss dist/utilities.css
node ./node_modules/uglifycss/uglifycss dist/utilities.css > dist/utilities.min.css