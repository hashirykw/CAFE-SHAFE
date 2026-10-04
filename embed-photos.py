"""
Bake every Unsplash photo used by the site straight into the HTML (base64),
so the page has zero external image links.

    python embed-photos.py            -> writes index-embedded.html next to index.html
    python embed-photos.py --inplace  -> overwrites index.html

Needs Python 3 and an internet connection. No extra packages.
"""
import base64, pathlib, re, sys, urllib.request

here = pathlib.Path(__file__).resolve().parent
src = here / "index.html"
html = src.read_text(encoding="utf-8")

# The site builds photo URLs from ids: U('1612846213933-916a1f56d859')
ids = sorted(set(re.findall(r"U\('([0-9a-f]+-[0-9a-f]+)'\)", html)))
if not ids:
    sys.exit("No Unsplash photo ids found - already embedded?")

for pid in ids:
    url = f"https://images.unsplash.com/photo-{pid}?w=1200&q=65&fm=webp&fit=crop"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    data = urllib.request.urlopen(req, timeout=60).read()
    mime = "image/webp" if data[8:12] == b"WEBP" else "image/jpeg"
    uri = f"data:{mime};base64," + base64.b64encode(data).decode()
    html = html.replace(f"U('{pid}')", f"'{uri}'")
    print(f"embedded {pid}  ({len(data)//1024} KB)")

out = src if "--inplace" in sys.argv else here / "index-embedded.html"
out.write_text(html, encoding="utf-8")
print(f"done -> {out.name}  ({out.stat().st_size//1024} KB)")
