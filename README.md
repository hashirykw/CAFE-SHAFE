# Cafe Shafe · Chai Station — website

```
cafe-shafe/
  index.html        ← the whole site (HTML + CSS + JS). Logo, favicon and illustrations are embedded.
  embed-photos.py   ← one command to bake the food photos into the HTML as well
  PHOTO-CREDITS.md  ← where each photo comes from
  README.md
```

Pages (hash-routed): Home · `#/menu` · `#/deals` · `#/table` · `#/visit`

## Photos
The 8 food/chai photos load from Unsplash (free licence, commercial use allowed, no attribution required).
To make the file 100% self-contained, run once on your PC:

    python embed-photos.py --inplace

That downloads each photo and writes it into `index.html` as base64 — no external image links left.
When the cafe sends real photos, swap the ids in the `PH` block of the script (or paste a base64 data URI).

## Deploy
Push the folder to GitHub → import in Vercel (preset **Other**, no build command). GitHub Pages works too.

## Edit
- Menu + prices: `MENU` array · Deals: `DEALS` · Chai colours/descriptions: `CHAI`
- Hours / phone: `.tbc` placeholders on the Visit page · Instagram: search `cafeshafechaistation9`
