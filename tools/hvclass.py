"""Sort the HVAC catalog into states, licenses and package types.

build.py imports this (as vaclass, so the shared code reads the same as the Texas and Virginia repos). Everything is
worked out from the product title, so the catalog can come from the dashboard sync or tools/sync_shopify.py.

Groups are states. To add a license: put a row in CLASSES (the first pattern that matches a title wins, so specific
rows go above general ones). Run python3 build.py and check the "unclassified" line it prints.
Test against the real titles with: python3 tools/hvclass.py catalog/titles.txt
"""
import re

STATE = "State"  # every product here is written for one state's exam, so no region notes are shown

STATES = [("al", "Alabama"), ("az", "Arizona"), ("ar", "Arkansas"), ("ca", "California"), ("co", "Colorado"), ("ct", "Connecticut"),
          ("de", "Delaware"), ("dc", "Washington DC"), ("fl", "Florida"), ("ga", "Georgia"), ("hi", "Hawaii"), ("id", "Idaho"), ("ia", "Iowa"),
          ("ky", "Kentucky"), ("la", "Louisiana"), ("me", "Maine"), ("md", "Maryland"), ("mn", "Minnesota"), ("ms", "Mississippi"),
          ("mo", "Missouri"), ("ne", "Nebraska"), ("nv", "Nevada"), ("nj", "New Jersey"), ("nm", "New Mexico"), ("nc", "North Carolina"),
          ("oh", "Ohio"), ("ok", "Oklahoma"), ("or", "Oregon"), ("sc", "South Carolina"), ("tn", "Tennessee"), ("tx", "Texas"), ("ut", "Utah"),
          ("va", "Virginia"), ("wa", "Washington"), ("wv", "West Virginia"), ("wy", "Wyoming")]
STATE_NAME = dict(STATES)
GROUPS = [(k, n, "") for k, n in STATES] + [("books", "HVAC reference books", "")]  # blurbs come from hvcopy.STATE_BLURB

# (slug, display name, group, regex on the title)
C = []
def L(g, slug, name, rx): C.append(("%s-%s" % (STATE_NAME[g].lower().replace(" ", "-"), slug), name, g, rx))
# Alabama
L("al", "heating-air-conditioning-contractor", "Heating and Air Conditioning Contractor", r"Alabama Heating and Air Conditioning")
L("al", "refrigeration-contractor", "Refrigeration Contractor", r"Alabama Refrigeration")
# Arizona: the codes in brackets decide
L("az", "c-49-industrial-refrigeration", "Industrial Refrigeration Commercial (C-49)", r"\(C-49\)")
L("az", "r-39-air-conditioning-refrigeration-solar", "A/C and Refrigeration incl. Solar, Residential (R-39)", r"\(R-39\)")
L("az", "cr-79-air-conditioning-refrigeration-solar", "A/C and Refrigeration incl. Solar, Residential and Commercial (CR-79)", r"\(CR-79\)")
L("az", "c-79-air-conditioning-refrigeration-solar", "A/C and Refrigeration incl. Solar, Commercial (C-79)", r"\(C-79\)")
L("az", "r-39r-air-conditioning-refrigeration", "A/C and Refrigeration, Residential (R-39R)", r"\(R-39R\)")
L("az", "cr-39-air-conditioning-refrigeration", "A/C and Refrigeration, Residential and Commercial (CR-39)", r"\(CR-39\)")
L("az", "c-39-air-conditioning-refrigeration", "A/C and Refrigeration, Commercial (C-39)", r"\(C-39\)")
# Arkansas
for k in "ABCDE": L("ar", "class-%s-hvacr-contractor" % k.lower(), "Class %s HVACR Contractor" % k, r"Arkansas Class %s HVACR" % k)
L("ar", "electrical-heating-ac-installation", "Electrical Heating and A/C Installation Contractor", r"Arkansas Electrical Heating")
# California
L("ca", "c-20-warm-air-heating-ventilating-ac", "Warm-Air Heating, Ventilating and A/C (C-20)", r"California Warm-Air.*C-20")
L("ca", "c-38-refrigeration", "Refrigeration (C-38)", r"California Refrigeration \(C-38\)")
L("ca", "c-4-boiler-hot-water-heating-steam-fitting", "Boiler, Hot-Water Heating and Steam Fitting (C-4)", r"California Boiler.*C-4")
# Colorado
L("co", "denver-refrigeration-operator", "Denver Refrigeration Operator (ICC 228)", r"Denver.*Refrigeration Operator|Refrigeration Operator.*228_CO")
# Connecticut: license codes
for code, name in [("D-1", "Limited Warm Air, A/C and Refrigeration Contractor (D-1)"), ("D-2", "Limited Warm Air, A/C and Refrigeration Journeyperson (D-2)"),
                   ("D-3", "Limited Heating-Cooling Contractor (D-3)"), ("D-4", "Limited Heating-Cooling Journeyperson (D-4)"),
                   ("S-10", "Limited Heating and Cooling Journeyperson (S-10)"), ("S-9", "Limited Heating and Cooling Contractor (S-9)"),
                   ("S-1", "Unlimited Heating, Piping and Cooling Contractor (S-1)"), ("S-2", "Unlimited Heating, Piping and Cooling Journeyperson (S-2)"),
                   ("S-3", "Limited Heating, Cooling and Piping Contractor (S-3)"), ("S-4", "Limited Heating, Cooling and Piping Contractor (S-4)"),
                   ("S-5", "Limited Heating, Hot Water and Steam Contractor (S-5)"), ("S-6", "Limited Heating, Hot Water and Steam Journeyperson (S-6)")]:
    L("ct", code.lower() + "-" + re.sub(r"[^a-z0-9]+", "-", name.split(" (")[0].lower()).strip("-"), name, r"Connecticut.*\b%s\b" % code)
# Delaware: restricted classes before the full license
L("de", "master-hvacr-restricted-gas-piping", "Master HVACR Restricted: Gas Piping", r"Delaware Master HVACR\s+Restricted Gas Piping")
L("de", "master-hvacr-restricted-air-conditioning", "Master HVACR Restricted: Air Conditioning", r"Delaware Master HVACR Restricted Air Conditioning")
L("de", "master-hvacr-restricted-forced-air", "Master HVACR Restricted: Forced Air, Ventilation and Gas Piping", r"Delaware Master HVACR Restricted.*Forced Air")
L("de", "master-hvacr-restricted-hydronic", "Master HVACR Restricted: Hydronic Heating and Gas Piping", r"Delaware Master HVACR Restricted.*Hydronic")
L("de", "master-hvacr-restricted-refrigeration", "Master HVACR Restricted: Refrigeration", r"Delaware Master HVACR Restricted Refrigeration")
L("de", "master-hvacr", "Master HVACR Contractor", r"Delaware Master HVACR")
# Washington DC before Washington state
L("dc", "master-ac-refrigeration-unlimited", "Master A/C and Refrigeration Mechanical, Unlimited", r"Washington DC Master A(/C|ir Conditioning) & Refrigeration Mechanical Unlimited")
L("dc", "master-refrigeration-ac-limited", "Master Refrigeration and A/C Mechanical, Limited", r"Washington DC Master Refrigeration & Air Conditioning Mechanical Limited")
L("dc", "journeyman-ac-refrigeration", "Journeyman A/C and Refrigeration", r"Washington DC Journeyman")
# Florida
L("fl", "rooftop-solar-heating-specialty", "Rooftop Solar Heating Specialty Contractor", r"Florida Rooftop Solar Heating")
L("fl", "county-class-a-air-conditioning-mce1b", "County Class A Air Conditioning Contractor (MCE1B)", r"MCE1B")
L("fl", "county-class-b-air-conditioning-mde1b", "County Class B Air Conditioning Contractor (MDE1B)", r"MDE1B")
L("fl", "palm-beach-harv", "Palm Beach County HARV Contractor", r"\bHARV\b")
L("fl", "broward-class-b-air-conditioning", "Broward County Class B Air Conditioning Contractor", r"Broward")
L("fl", "county-journeyman-air-conditioning", "County Journeyman Air Conditioning", r"Journeyman Air Conditioning.*County - Florida")
L("fl", "air-a-air-b-contractor", "Class A and Class B Air Conditioning Contractor (Air A, Air B)", r"Florida Air [AB]|Air A/B|Becoming a Florida Air")
# Georgia
L("ga", "business-and-law-nascla", "Business and Law Reference (NASCLA, Georgia edition)", r"Georgia NASCLA")
L("ga", "conditioned-air-class-ii-unrestricted", "Conditioned Air Contractor Class II (Unrestricted)", r"Georgia Conditioned Air.*Class II")
L("ga", "conditioned-air-class-i-restricted", "Conditioned Air Contractor Class I (Restricted)", r"Georgia Conditioned Air")
# Hawaii
L("hi", "c-52-ventilating-air-conditioning", "Ventilating and Air Conditioning Contractor (C-52)", r"Hawaii Ventilating")
L("hi", "c-4-boiler-hot-water-heating-steam-fitting", "Boiler, Hot Water Heating and Steam Fitting Contractor (C-4)", r"Hawaii Boiler")
# Idaho
L("id", "hvac-specialty-journeyman", "HVAC Specialty Journeyman", r"Idaho HVAC Specialty Journeyman")
L("id", "hvac-journeyman", "HVAC Journeyman", r"Idaho HVAC Journeyman")
L("id", "hvac-contractor", "HVAC Contractor", r"Idaho HVAC Contractor")
L("id", "limited-electrical-refrigeration-heating-ac-installer", "Limited Electrical: Refrigeration, Heating and A/C Installer", r"Idaho Limited Electrical Refrigeration")
# Iowa
L("ia", "disconnecting-reconnecting-ac-refrigeration", "Disconnecting and Reconnecting A/C and Refrigeration Systems", r"Iowa Disconnecting")
L("ia", "journeyperson-hvac-refrigeration-gas", "Journeyperson HVAC and Refrigeration with Gas", r"Iowa Journeyperson HVAC")
L("ia", "master-hvac-refrigeration-gas", "Master HVAC and Refrigeration with Gas", r"Iowa Master HVAC")
# Kentucky
L("ky", "journeyman-hvac-mechanic-icc-598", "Journeyman HVAC Mechanic (ICC 598)", r"Kentucky.*598")
L("ky", "master-hvac-contractor-icc-595", "Master HVAC Contractor (ICC 595)", r"Kentucky.*595")
L("ky", "journeyman-hvac", "Journeyman HVAC (state exam)", r"Kentucky Journeyman HVAC")
L("ky", "master-hvac-contractor", "Master HVAC Contractor (state exam)", r"Kentucky Master HVAC")
# Louisiana, with the New Orleans stationary engineer exams
for code, name in [("636", "New Orleans First Class Stationary Air Conditioning (ICC 636)"), ("635", "New Orleans First Class Stationary Refrigeration (ICC 635)"),
                   ("640", "New Orleans Second Class Stationary Air Conditioning (ICC 640)"), ("639", "New Orleans Second Class Stationary Refrigeration (ICC 639)"),
                   ("645", "New Orleans Third Class Stationary Air Conditioning (ICC 645)")]:
    L("la", "new-orleans-%s" % code + "-" + re.sub(r"[^a-z0-9]+", "-", name.split("New Orleans ")[1].split(" (")[0].lower()).strip("-"), name, r"\b%s\b\s*-?\s*LA" % code)
L("la", "hvac-contractor", "Heat, Air Conditioning, Ventilation, Duct Work and Refrigeration Contractor", r"Louisiana Heat, Air Conditioning")
# Maine
L("me", "limited-electrician-refrigeration", "Limited Electrician: Refrigeration", r"Maine Limited Electrician")
# Maryland: restricted first
L("md", "master-restricted-air-conditioning", "Master Restricted Air Conditioning Contractor", r"Maryland Master Restricted Air Conditioning")
L("md", "master-restricted-refrigeration", "Master Restricted Refrigeration Contractor", r"Maryland Master Restricted Refrigeration")
L("md", "restricted-air-conditioning-journeyman", "Restricted Air Conditioning Journeyman", r"Maryland Restricted Air Conditioning Journeyman")
L("md", "restricted-refrigeration-journeyman", "Restricted Refrigeration Journeyman", r"Maryland Restricted Refrigeration Journeyman")
L("md", "hvacr-journeyman", "HVACR Journeyman", r"Maryland HVACR Journeyman")
L("md", "limited-hvacr-contractor", "Limited HVACR Contractor", r"Maryland Limited HVACR")
L("md", "master-hvacr-contractor", "Master HVACR Contractor", r"Maryland\s+Master HVACR?")
# Minnesota
L("mn", "minneapolis-journeyman-refrigeration-icc-768", "Minneapolis Journeyman Refrigeration (ICC 768)", r"Minneapolis Journeyman Refrigeration")
L("mn", "minneapolis-master-refrigeration-icc-769", "Minneapolis Master Refrigeration (ICC 769)", r"Minneapolis Master Refrigeration")
# Mississippi
L("ms", "ductwork-heating-ac-ventilation", "Ductwork for Heating, A/C and Ventilation Contractor", r"Mississippi Ductwork")
L("ms", "refrigeration-contractor", "Refrigeration Contractor", r"Mississippi Refrigeration")
L("ms", "residential-hvac-contractor", "Residential HVAC Contractor", r"Mississippi Residential HVAC")
L("ms", "hvac-contractor", "HVAC Contractor", r"Mississippi HVAC")
# Missouri
L("mo", "kansas-city-refrigeration-operator-icc-228", "Kansas City Refrigeration Operator (ICC 228)", r"Kansas City Refrigeration Operator")
L("mo", "st-louis-county-commercial-hvac-icc-588", "St. Louis County Commercial HVAC Servicer/Installer (ICC 588)", r"St\. Louis County Commercial HVAC")
L("mo", "st-louis-county-residential-hvac-icc-589", "St. Louis County Residential HVAC Servicer/Installer (ICC 589)", r"St\. Louis County Residential HVAC")
# Nebraska
L("ne", "commercial-air-conditioning-contractor", "Commercial Air Conditioning Contractor", r"Nebraska Commercial Air Conditioning")
# Nevada: classification codes
for code, name in [("C-21B", "Air Conditioning (C-21B)"), ("C-1F", "Heating, Cooling and Circulating Air (C-1F)"), ("C-21D", "Refrigeration and A/C (C-21D)"),
                   ("C-21A", "Refrigeration (C-21A)"), ("C-21E", "Solar Air Conditioning (C-21E)"), ("C-37C", "Solar Air Conditioning (C-37C)"),
                   ("C-37D", "Solar Pool Heating (C-37D)"), ("C-37B", "Solar Space Heating (C-37B)"), ("C-37A", "Solar Water Heating (C-37A)"),
                   ("C-21", "Refrigeration and Air Conditioning (C-21)"), ("C-1", "Plumbing and Heating (C-1)")]:
    L("nv", code.lower() + "-" + re.sub(r"[^a-z0-9]+", "-", name.split(" (")[0].lower()).strip("-"), name, r"Nevada.*\(%s\)" % code)
# New Jersey, New Mexico
L("nj", "hvacr-business-and-law", "HVACR Contractor Business and Law", r"New Jersey Business and Law.*HVACR")
L("nm", "mm-3-heat-vent-air-conditioning", "Heat, Vent and Air Conditioning Contractor (MM-3)", r"New Mexico Heat, Vent")
# North Carolina: technicians before contractors (their titles say "Technician Contractor")
L("nc", "special-restricted-plumbing-heating-sp-ph", "Special Restricted Plumbing and Heating (SP-PH)", r"SP-PH")
for g in "123":
    L("nc", "heating-group-%s-technician" % g, "Heating Group %s Technician" % g, r"Heating Group %s Technician" % g)
L("nc", "heating-group-1-class-1", "Heating Group 1 Class 1 Contractor", r"Heating Group 1 Class (1|I)\b")
L("nc", "heating-group-1-class-2", "Heating Group 1 Class 2 Contractor", r"Heating Group 1 Class 2")
L("nc", "heating-group-2-contractor", "Heating Group 2 Contractor", r"Heating Group 2 Contractor")
L("nc", "heating-group-3-class-1", "Heating Group 3 Class 1 Contractor", r"Heating Group 3 Class (1|I)\b")
L("nc", "heating-group-3-class-2", "Heating Group 3 Class 2 Contractor", r"Heating Group 3 Class 2")
# Ohio
L("oh", "hvac-contractor", "HVAC Contractor", r"Ohio HVAC")
L("oh", "refrigeration-contractor-icc", "Refrigeration Contractor (ICC)", r"Ohio Refrigeration")
# Oklahoma
L("ok", "refrigeration-journeyman", "Refrigeration Journeyman", r"Oklahoma Refrigeration Journeyman")
L("ok", "refrigeration-contractor", "Refrigeration Contractor", r"Oklahoma Refrigeration Contractor")
L("ok", "hvacr-limited-journeyman", "HVACR Limited Journeyman", r"Oklahoma HVACR (Limited Journeyman|Journeyman Limited)")
L("ok", "hvacr-unlimited-journeyman", "HVACR Unlimited Journeyman", r"Oklahoma HVACR (Journeyman Unlimited|Unlimited Journeyman)")
L("ok", "hvacr-limited-contractor", "HVACR Limited Contractor", r"Oklahoma (HVACR )?Limited")
L("ok", "hvacr-unlimited-contractor", "HVACR Unlimited Contractor", r"Oklahoma (HVACR )?Unlimited")
# Oregon
L("or", "heating-oil-tank-supervisor-icc-u8", "Heating Oil Tank Supervisor (ICC U8)", r"Oregon Heating Oil Tank")
# South Carolina
L("sc", "commercial-air-conditioning-contractor", "Commercial Air Conditioning Contractor", r"South Carolina (Commercial )?Air Conditioning")
L("sc", "heating-contractor", "Heating Contractor", r"South Carolina Heating")
L("sc", "refrigeration-contractor", "Refrigeration Contractor", r"South Carolina Refrigeration")
L("sc", "residential-hvac-contractor", "Residential HVAC Contractor", r"South Carolina Residential HVAC")
# Tennessee, Texas, Utah
L("tn", "cmc-c-mechanical-hvac-refrigeration", "CMC-C Mechanical HVAC and Refrigeration Contractor", r"Tennessee CMC-C")
L("tx", "certified-ac-refrigeration-technician", "Certified A/C and Refrigeration Technician", r"Texas Certified Air Conditioning")
L("tx", "commercial-refrigeration-class-a", "ACR Contractor Class A, Commercial Refrigeration", r"Texas Commercial Refrigeration Class A")
L("tx", "commercial-refrigeration-class-b", "ACR Contractor Class B, Commercial Refrigeration", r"Texas Commercial Refrigeration Class B")
L("ut", "hvac-written-exam", "HVAC Contractor Written Exam", r"Utah HVAC")
# Virginia
L("va", "refrigeration-contractor", "Refrigeration Contractor", r"Virginia Refrigeration")
L("va", "residential-hvac-tradesman", "Residential HVAC Tradesman", r"Virginia Residential HVAC")
L("va", "journeyman-hvac", "Journeyman HVAC", r"Virginia Journeyman HVAC")
L("va", "master-hvac", "Master HVAC", r"Virginia Master HVAC")
# Washington state (after DC)
for cls, lab in [("A", ""), ("B", "Restricted ")]:
    L("wa", "%s-hvacr-%smaster-electrician" % (cls.lower(), lab.lower().replace(" ", "-")), "%s-HVAC/R %sMaster Electrician" % (cls, lab), r"Washington %s-HVAC/R %sMaster Electrician" % (cls, lab))
    L("wa", "%s-hvacr-%selectrician" % (cls.lower(), lab.lower().replace(" ", "-")), "%s-HVAC/R %sElectrician" % (cls, lab), r"Washington %s-HVAC/R %sElectrician" % (cls, lab))
    L("wa", "%s-hvacr-%sadministrator" % (cls.lower(), lab.lower().replace(" ", "-")), "%s-HVAC/R %sAdministrator" % (cls, lab), r"Washington %s-HVAC/R %sAdministrator" % (cls, lab))
L("wv", "hvac-contractor", "HVAC Contractor", r"West Virginia HVAC")
L("wy", "limited-hvac-technician-icc-600", "Limited HVAC Technician (ICC 600)", r"Wyoming.*600")
CLASSES = C
OTHER = ("hvac-reference-books", "HVAC Reference Books", "books")
SKIP = re.compile(r"Free Demo|Personal AI Tutor", re.I)  # $0 demos are not listed

# package types, lowest rank first: (slug, name, test(title, productType)). Order of the tests below is the matching order.
def _t(rx): return lambda t, ty: re.search(rx, t, re.I) is not None
_MATCH = [
    ("ca-courses-application-fees-bond", "Courses, Application, State Fees and Bond", _t(r"State Fees \+ 1st-Year Bond")),
    ("ca-ultimate-courses-application", "Ultimate Courses and Application", _t(r"Ultimate Business & Trade Courses & Application")),
    ("ca-business-trade-courses", "Business and Trade Online Courses", _t(r"Business & Trade Online Courses")),
    ("the-1-package", "The 1 Package (all-inclusive)", _t(r"^The 1 Package")),
    ("ultimate-exam-room", "Ultimate Exam-Room Package", _t(r"Ultimate Books Exam Room Approved")),
    ("rental-exam-room", "Exam-Room Books and Course Rental", _t(r"Rental - Exam Room Approved")),
    ("exam-room-highlighted", "Highlighted and Tabbed Exam-Room Books", _t(r"Highlighted & Tabbed Books Allowed into Exam")),
    ("exam-room-books", "Books Allowed into the Exam", _t(r"Books Allowed into Exam")),
    ("ultimate-rental", "Ultimate Exam Prep Package", _t(r"Ultimate (Exam Prep )?(Rental|Package)|Exam Ultimate Package|Ultimate Package\b")),
    ("accelerator", "Books and Application Accelerator", _t(r"Application Accelerator")),
    ("rental-package", "Books and Courses Rental", _t(r"Rental")),
    ("live-training", "Live Virtual Training", _t(r"Live Virtual")),
    ("online-practice-exams", "Online Practice Questions", _t(r"Practice Questions|Online Practice\b")),
    ("intro-course", "Introduction Course", _t(r"^Introduction to Becoming")),
    ("flash-cards", "Flash Cards", _t(r"Flash Card")),
    ("tabs-highlights", "Pre-Printed Tabs and Highlights", _t(r"Pre-Printed Tabs and Highlights")),
    ("tabs", "Pre-Printed Tabs", _t(r"Pre-?\s?Printed Tabs")),
    ("highlighted-tabbed", "Highlighted and Tabbed Books", _t(r"Highlighted")),
    ("online-course", "Online Exam Prep Course", _t(r"Online|Course|^GITS")),
    ("book-package", "Complete Book Package", _t(r"Book (Package|Set|Reference Package)|Book package")),
]
# display order on license pages (cheapest kinds first)
TYPES = [t for t in _MATCH] + [("reference-book", "Reference Book", lambda t, ty: True)]
_RANK_ORDER = ["tabs", "tabs-highlights", "flash-cards", "online-practice-exams", "intro-course", "online-course", "ca-business-trade-courses", "live-training",
               "exam-room-books", "exam-room-highlighted", "book-package", "reference-book", "highlighted-tabbed", "accelerator", "rental-exam-room", "rental-package",
               "ca-ultimate-courses-application", "ultimate-exam-room", "ultimate-rental", "ca-courses-application-fees-bond", "the-1-package"]
TYPE_RANK = {s: i for i, s in enumerate(_RANK_ORDER)}

def slugify(s): return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
def region(title): return STATE

def classify(title, ptype):
    cls = next((c for c in CLASSES if re.search(c[3], title, re.I)), None) or OTHER
    if cls is OTHER: typ = ("reference-book", "Reference Book")
    else: typ = next(((s, n) for s, n, f in TYPES if f(title, ptype or "")), ("reference-book", "Reference Book"))
    return {"cls": cls[0], "clsName": cls[1], "group": cls[2], "type": typ[0], "typeName": typ[1], "rank": TYPE_RANK.get(typ[0], 99),
            "region": STATE, "year": ""}

def clean_title(t):
    t = t.replace("&amp;", "&")
    return re.sub(r"\s+", " ", t).strip()

def assign(products):
    """Give every product its license, package type and a short URL slug that is unique inside its license."""
    used, out = {}, []
    for p in sorted(products, key=lambda p: (p["title"], p["id"])):
        if SKIP.search(p["title"]) or float(p.get("price") or 0) <= 0: continue
        c = classify(p["title"], p.get("type", ""))
        base = c["type"] if c["cls"] != OTHER[0] else slugify(clean_title(p["title"]))[:50].rstrip("-")
        if c["cls"] == "florida-air-a-air-b-contractor":  # one license page covers Air A and Air B; keep the class in the slug
            m = re.search(r"Air (A|B)\b(?! or)(?!/)(?! and)", p["title"])
            if m and not re.search(r"Air A (or|and) Air B|Air A or B|Air A/B", p["title"]): base += "-air-" + m.group(1).lower()
        key = (c["cls"], base); n = used.get(key, 0) + 1; used[key] = n
        sl = base if n == 1 else "%s-%d" % (base, n)
        out.append(dict(p, **c, slug=sl, path="%s/%s/" % (c["cls"], sl), short=clean_title(p["title"])))
    return out

DISPLAY_ORDER = []  # licenses are listed by state, in the order of CLASSES

if __name__ == "__main__":
    import sys, collections
    rows = [l.rsplit("|", 1) for l in open(sys.argv[1]).read().splitlines() if l.strip()]
    ps = [{"id": str(i), "title": t, "price": p, "variants": [{"id": "0", "price": p}]} for i, (t, p) in enumerate(rows)]
    got = assign(ps)
    by = collections.OrderedDict()
    for p in got: by.setdefault((p["group"], p["clsName"]), []).append(p["typeName"])
    for (g, n), ts in by.items(): print("%-5s %-70s %2d  %s" % (g, n[:70], len(ts), ", ".join(sorted(set(ts)))[:150]))
    print("\nproducts %d, licenses %d, states %d, skipped %d" % (len(got), len(by), len({g for g, _ in by}), len(ps) - len(got)))
    unused = [c[1] for c in CLASSES if c[0] not in {p["cls"] for p in got}]
    print("licenses with no product:", unused)
    print("in reference books:", [p["title"] for p in got if p["cls"] == OTHER[0]])
