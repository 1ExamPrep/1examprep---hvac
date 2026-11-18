"""Write a STAND-IN catalog from tools/test-titles.txt (real titles and prices, pulled from Shopify collection 497735663673
on 2026-11-18) so the site can be built and checked before the dashboard is connected.

  python3 tools/standin_catalog.py && python3 build.py

The stand-in has no real product ids, handles, images or descriptions: Buy buttons open a store search for the product
title, and product descriptions are short generated summaries. The dashboard's Sync now replaces shared/catalog.js and
store/products-full.json with the real catalog; do not run this script after that.
"""
import json, os, re, sys
from urllib.parse import quote
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import hvclass, hvcopy

rows = [l.rsplit("|", 1) for l in open(os.path.join(ROOT, "tools", "test-titles.txt"), encoding="utf-8").read().splitlines() if l.strip()]
cat, full = [], {}
for i, (t, pr) in enumerate(rows):
    t = t.replace("&amp;", "&")
    c = hvclass.classify(t, "")
    pid = "pv%04d" % i
    st = hvclass.STATE_NAME.get(c["group"], "")
    blurb = hvcopy.TYPE_BLURB.get(c["type"], "exam prep")
    desc = ("%s is %s for the %s %s exam. %s licenses this work, and the candidate bulletin for your exam lists the references and editions allowed. "
            "Book packages ship free from 1 Exam Prep by USPS Media Mail; online courses and practice questions arrive by email after purchase. "
            "Rental, Ultimate and 1 Package prices include a refundable book deposit, and those orders take up to 15 business days to prepare. "
            "Licensing exam questions are confidential, so the courses and practice questions are original material written to the same subjects. "
            "Buying study material does not register you for the exam; the board approves your application first." % (t, blurb, st, c["clsName"], (lambda b: b[:1].upper() + b[1:])(hvcopy.STATE.get(c["group"], {}).get("board") or "The licensing board") if c["group"] != "books" else "Your state board"))
    cat.append({"id": pid, "handle": re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-"), "title": t, "type": "", "price": pr, "maxPrice": pr, "compareAt": None, "image": "",
                "url": "https://1examprep.com/search?type=product&q=" + quote(t), "desc": desc,
                "variants": [{"id": "pv-" + quote(t), "title": "Default Title", "price": pr, "compareAt": None, "available": True}]})
    full[pid] = {"html": "<p>%s</p>" % desc, "images": []}
open(os.path.join(ROOT, "shared", "catalog.js"), "w", encoding="utf-8").write(
    "/* STAND-IN catalog from tools/test-titles.txt (%d products). Replace with the dashboard sync. */\nwindow.CATALOG=%s;\nwindow.CATALOG_STATES=[];\n" % (len(cat), json.dumps(cat, ensure_ascii=False)))
json.dump(full, open(os.path.join(ROOT, "store", "products-full.json"), "w", encoding="utf-8"), ensure_ascii=False)
print("stand-in catalog:", len(cat), "products")
