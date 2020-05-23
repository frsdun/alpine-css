# [alpine-css](https://frsdun.github.io/alpine-css/)

Alpine style styles

TL;DR: normalize + milligram + utilities. Taking the part I like from the css libraries I have used.

## References / inspiration

-   [css-base](https://github.com/frsdun/css-base)
-   [css-utilities](https://github.com/frsdun/css-utilities)
-   [web-design-in-4-minutes](https://jgthms.com/web-design-in-4-minutes/)
-   [normalize ](https://github.com/necolas/normalize.css/)
-   [milligram](https://github.com/milligram/milligram)
-   [new.css](https://github.com/xz/new.css/blob/master/new.css)
-   [uk-kit](https://github.com/uikit/uikit/tree/develop/src/scss)
-   [Bootstrap ](https://github.com/twbs/bootstrap/tree/master/scss)
-   [mvp.css](https://github.com/andybrewer/mvp/blob/master/mvp.css)
-   [Strip](https://leerob.io/blog/how-stripe-designs-beautiful-websites)
-   [Blunt-css](https://github.com/f-prime/Blunt)

## Install

### Javascript (Node)

```bash
# Install dependencies
npm i

# Edit paths in package.json -> scripts to match your folder structure

# Build and minify
npm run scss

# Watch (does not minify)
npm run watch-scss

# Minify css
npm run minify-css
```

```json
"scripts": {
    "scss": "npm run build-scss && npm run minify-css",
    "build-scss": "node ./node_modules/node-sass/bin/node-sass src/styles.scss dist/styles.css",
    "watch-scss": "node ./node_modules/node-sass/bin/node-sass --watch src/styles.scss dist/styles.css",
    "minify-css": "node ./node_modules/uglifycss/uglifycss dist/css.css > dist/styles.min.css"
},
"devDependencies": {
    "node-sass": "4.12.0",
    "uglifycss": "0.0.29"
}
```

### Python

```bash
# Activate any venv you may have

# Install dependencies
pip install -r requirements.txt

# Set scss_filepath and output_filepath at the bottom of build.py

# Build
python build.py
```

## Other

```bash
# Gzip. (-k = keep the original)
cd dist
gzip -k styles.min.css
```
