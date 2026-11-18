"""Copy for passyourhvacexam.com: who licenses HVAC in each state and what the packages are.

build.py imports this as vacopy. Groups are states (codes from hvclass.STATES). Facts here come from the state board
pages listed in STATE[...]["url"], or from the 1 Exam Prep product pages for that license; anything not confirmed is
written as "check your candidate bulletin" rather than guessed. Checked 2026-11-18. Re-check when a board changes rules.

Confirmed on 2026-11-18:
  - Oklahoma HVACR Unlimited exam: PSI, open book, 90 questions, 240 minutes, 70% (63 correct); 2024 IMC and IFGC only
    from December 15, 2026 (1 Exam Prep product pages).
  - Arizona C-39: open book, plus a business and law exam (1 Exam Prep product page).
  - Arkansas: exams proctored by Prov, board approval needed first, no reciprocity (labor.arkansas.gov).
  - West Virginia: Contractor Licensing Board with the Division of Labor, exams by Prov (labor.wv.gov).
  - Idaho: DOPL HVAC Board; contractor applicants first hold a journeyman or specialty journeyman license (dopl.idaho.gov).
  - Texas ACR facts carried over from the Texas site (TDLR, PSI), checked 2026-10-28.
"""

EPA_608 = ("EPA Section 608 technician certification", "https://www.epa.gov/section608")

# One record per state: board name, short label, official page, exam provider (only when confirmed), book rule, facts.
STATE = {
    "al": dict(board="the Alabama Board of Heating, Air Conditioning and Refrigeration Contractors", short="AL HACR Board", url="https://hacr.alabama.gov/",
               provider="", book="",
               facts=["The Alabama Board of Heating, Air Conditioning and Refrigeration Contractors certifies HVAC and refrigeration contractors statewide.",
                      "Heating and air conditioning and refrigeration are separate Alabama certifications, so pick the package for the exam you are approved for."]),
    "az": dict(board="the Arizona Registrar of Contractors (ROC)", short="Arizona ROC", url="https://roc.az.gov/", provider="", book="some",
               facts=["The Arizona Registrar of Contractors licenses air conditioning and refrigeration work in residential (R), commercial (C) and dual (CR) classifications.",
                      "The C-39 trade exam is open book, and Arizona contractor applicants also prepare for a business and law exam.",
                      "Exam-room book packages contain only the references the testing center lets you bring in."]),
    "ar": dict(board="the Arkansas HVACR Licensing Board (Department of Labor and Licensing)", short="AR HVACR Board", url="https://labor.arkansas.gov/labor/code-enforcement/hvac-r/",
               provider="Prov", book="",
               facts=["Arkansas HVACR licenses run from Class A to Class E; Class A has no limit on BTUH or horsepower.",
                      "Prov proctors the Arkansas HVACR exams, and the board must approve you before you can sit for one.",
                      "Arkansas has no reciprocal HVACR licensing agreements with other states."]),
    "ca": dict(board="the Contractors State License Board (CSLB)", short="CSLB", url="https://www.cslb.ca.gov/", provider="", book="",
               facts=["The CSLB licenses C-20 warm-air heating, ventilating and air conditioning, C-38 refrigeration and C-4 boiler contractors.",
                      "California applicants take the Law and Business exam as well as the trade exam, so the packages pair both courses.",
                      "One package adds the application, the state fees and the first-year bond."]),
    "co": dict(board="the City and County of Denver", short="City of Denver", url="https://www.denvergov.org/", provider="ICC", book="",
               facts=["Denver licenses refrigeration operators locally and uses the ICC 228 exam.",
                      "ICC exams list their allowed references in the bulletin for each exam."]),
    "ct": dict(board="the Connecticut Department of Consumer Protection, Occupational and Professional Licensing", short="CT DCP", url="https://portal.ct.gov/dcp",
               provider="", book="some",
               facts=["Connecticut D licenses cover warm air, air conditioning and refrigeration (D-1 to D-4); S licenses cover heating, piping and cooling (S-1 to S-10).",
                      "Each license code has its own exam, and several S exams allow approved books in the exam room."]),
    "de": dict(board="the Delaware Board of Plumbing, Heating, Ventilation, Air Conditioning and Refrigeration Examiners", short="DE PHVACR Board",
               url="https://dpr.delaware.gov/boards/plumbers/", provider="", book="",
               facts=["Delaware issues a Master HVACR license plus restricted master licenses for air conditioning, refrigeration, forced air, hydronic heating and gas piping.",
                      "A restricted license covers a narrower scope of work than the full Master HVACR license, with its own exam."]),
    "dc": dict(board="the DC Department of Licensing and Consumer Protection (DLCP)", short="DC DLCP", url="https://dlcp.dc.gov/", provider="", book="",
               facts=["Washington DC licenses air conditioning and refrigeration mechanics at journeyman and master level.",
                      "Master licenses come in limited and unlimited versions."]),
    "fl": dict(board="the Florida Construction Industry Licensing Board (CILB)", short="Florida CILB", url="https://www2.myfloridalicense.com/construction-industry/",
               provider="Pearson VUE", book="",
               facts=["The Florida Construction Industry Licensing Board certifies Class A and Class B air conditioning contractors statewide.",
                      "Pearson VUE gives the state Air A and Air B trade exams.",
                      "Some Florida counties, such as Broward and Palm Beach, also license air conditioning contractors with their own exams."]),
    "ga": dict(board="the Georgia State Construction Industry Licensing Board, Division of Conditioned Air Contractors", short="GA Conditioned Air Division",
               url="https://sos.ga.gov/state-construction-industry-licensing-board", provider="", book="",
               facts=["Georgia licenses conditioned air contractors in Class I (Restricted) and Class II (Unrestricted).",
                      "Georgia candidates also study the NASCLA business and law guide written for the Georgia board."]),
    "hi": dict(board="the Hawaii Contractors License Board", short="HI Contractors Board", url="https://cca.hawaii.gov/pvl/boards/contractor/", provider="", book="",
               facts=["Hawaii licenses ventilating and air conditioning contractors under the C-52 specialty classification.",
                      "Boiler, hot water heating and steam fitting work is the separate C-4 classification."]),
    "id": dict(board="the Idaho HVAC Board in the Division of Occupational and Professional Licenses (DOPL)", short="Idaho DOPL HVAC Board", url="https://dopl.idaho.gov/hvac/",
               provider="", book="some",
               facts=["The Idaho HVAC Board licenses apprentices, journeymen, specialty journeymen and contractors.",
                      "A contractor applicant first holds an Idaho journeyman or specialty journeyman license."]),
    "ia": dict(board="the Iowa Plumbing and Mechanical Systems Board", short="IA PMSB", url="https://dial.iowa.gov/", provider="", book="",
               facts=["Iowa licenses HVAC and refrigeration work at journeyperson and master level, with gas included in the license.",
                      "Disconnecting and reconnecting air conditioning and refrigeration systems is its own Iowa license."]),
    "ky": dict(board="the Kentucky Department of Housing, Buildings and Construction, HVAC Division", short="KY HBC", url="https://dhbc.ky.gov/", provider="ICC or ProV", book="",
               facts=["Kentucky licenses Master HVAC Contractors and Journeyman HVAC Mechanics.",
                      "Prep is listed for the ICC versions (595 master, 598 journeyman) and for the state exam, so check which one your approval names."]),
    "la": dict(board="the Louisiana State Licensing Board for Contractors (LSLBC)", short="LSLBC", url="https://lslbc.louisiana.gov/", provider="", book="",
               facts=["The LSLBC licenses mechanical work, including heat, air conditioning, ventilation, duct work and refrigeration.",
                      "New Orleans also tests stationary engineers in air conditioning and refrigeration with ICC exams 635, 636, 639, 640 and 645."]),
    "me": dict(board="the Maine Electricians' Examining Board", short="ME Electricians' Board", url="https://www.maine.gov/pfr/professionallicensing/professions/electricians-examining-board",
               provider="", book="",
               facts=["Maine licenses the electrical side of refrigeration work as a limited electrician license.",
                      "The Electricians' Examining Board issues the license and approves exam candidates."]),
    "md": dict(board="the Maryland Board of Heating, Ventilation, Air-Conditioning and Refrigeration Contractors", short="MD HVACR Board",
               url="https://www.labor.maryland.gov/license/hvacr/", provider="PSI", book="",
               facts=["Maryland licenses master, master restricted, limited and journeyman HVACR, with restricted licenses for air conditioning or refrigeration only.",
                      "PSI gives the Maryland HVACR exams."]),
    "mn": dict(board="the City of Minneapolis", short="City of Minneapolis", url="https://www.minneapolismn.gov/", provider="ICC", book="",
               facts=["Minneapolis licenses refrigeration journeymen and masters locally, using ICC exams 768 and 769.",
                      "ICC exams list their allowed references in the bulletin for each exam."]),
    "ms": dict(board="the Mississippi State Board of Contractors", short="MS Board of Contractors", url="https://www.msboc.us/", provider="", book="",
               facts=["The Mississippi State Board of Contractors licenses HVAC, residential HVAC, refrigeration and ductwork contractors.",
                      "Application accelerator packages add help with the Mississippi license application to the books."]),
    "mo": dict(board="Kansas City or St. Louis County", short="Kansas City or St. Louis County", url="https://www.kcmo.gov/", provider="ICC", book="",
               facts=["Missouri has no statewide HVAC license; Kansas City and St. Louis County license HVAC and refrigeration work locally.",
                      "Both use ICC exams: 228 for Kansas City refrigeration operators, 588 and 589 for St. Louis County HVAC."]),
    "ne": dict(board="the city where you work", short="Local city license", url="", provider="", book="",
               facts=["Nebraska has no statewide HVAC contractor license; cities license mechanical and air conditioning contractors.",
                      "Check with your city for the exam it uses before you order."]),
    "nv": dict(board="the Nevada State Contractors Board (NSCB)", short="NSCB", url="https://www.nscb.nv.gov/", provider="", book="some",
               facts=["The Nevada State Contractors Board licenses HVAC work under C-21 and its subclassifications, C-1F and the C-37 solar classifications.",
                      "Several Nevada trade exams let you bring approved books, so exam-room book packages are offered beside the full sets."]),
    "nj": dict(board="the New Jersey State Board of Examiners of Master HVACR Contractors", short="NJ Master HVACR Board", url="https://www.njconsumeraffairs.gov/hvacr/",
               provider="", book="",
               facts=["New Jersey licenses Master HVACR contractors through the State Board of Examiners of Master HVACR Contractors.",
                      "The course here covers the business and law part of the New Jersey exam."]),
    "nm": dict(board="the New Mexico Construction Industries Division", short="NM CID", url="https://www.rld.nm.gov/construction-industries/", provider="", book="",
               facts=["New Mexico's MM-3 classification covers heating, ventilation and air conditioning.",
                      "The Construction Industries Division issues the license and approves exam candidates."]),
    "nc": dict(board="the North Carolina State Board of Examiners of Plumbing, Heating and Fire Sprinkler Contractors", short="NC PHFS Board", url="https://www.nclicensing.org/",
               provider="", book="",
               facts=["North Carolina licenses heating contractors in Groups 1, 2 and 3, with Class 1 and Class 2 contractor licenses and technician certificates.",
                      "The SP-PH special restricted license covers limited plumbing and heating work."]),
    "oh": dict(board="the Ohio Construction Industry Licensing Board (OCILB)", short="Ohio OCILB", url="https://com.ohio.gov/", provider="PSI", book="",
               facts=["The Ohio Construction Industry Licensing Board licenses HVAC and refrigeration contractors.",
                      "PSI gives the Ohio HVAC contractor exam."]),
    "ok": dict(board="the Oklahoma Construction Industries Board (CIB)", short="Oklahoma CIB", url="https://oklahoma.gov/cib.html", provider="PSI", book="some",
               facts=["The HVACR Unlimited Contractor trade exam is open book: 90 questions in 240 minutes, with a 70 percent passing score (63 correct).",
                      "From December 15, 2026 the affected HVACR exams use the 2024 International Mechanical Code and International Fuel Gas Code only.",
                      "An active Oklahoma mechanical contractor keeps a $5,000 surety bond and at least $50,000 in general liability insurance."]),
    "or": dict(board="the Oregon Department of Environmental Quality (DEQ)", short="Oregon DEQ", url="https://www.oregon.gov/deq/", provider="ICC", book="",
               facts=["Oregon DEQ licenses heating oil tank service providers and supervisors.",
                      "The supervisor exam is ICC U8."]),
    "sc": dict(board="the South Carolina Department of Labor, Licensing and Regulation (LLR)", short="SC LLR", url="https://llr.sc.gov/", provider="PSI", book="",
               facts=["Residential HVAC contractors are licensed by the SC Residential Builders Commission; commercial air conditioning, heating and refrigeration by the SC Contractor's Licensing Board.",
                      "PSI gives the South Carolina exams."]),
    "tn": dict(board="the Tennessee Board for Licensing Contractors", short="TN Contractors Board", url="https://www.tn.gov/commerce/regboards/contractors.html", provider="Prov",
               book="",
               facts=["The Tennessee CMC-C classification covers mechanical HVAC and refrigeration contracting.",
                      "Prov gives the Tennessee CMC-C trade exam."]),
    "tx": dict(board="the Texas Department of Licensing and Regulation (TDLR)", short="TDLR", url="https://www.tdlr.texas.gov/acr/contractor-apply.htm", provider="PSI", book="open",
               facts=["TDLR licenses air conditioning and refrigeration contractors in two classes: Class B up to 25 tons cooling and 1.5 million BTU per hour heating, and Class A with no limit.",
                      "PSI gives the exams, and they are open book; since September 1, 2026 they reference the 2024 IMC, UMC and IFGC."]),
    "ut": dict(board="the Utah Division of Professional Licensing (DOPL)", short="Utah DOPL", url="https://dopl.utah.gov/", provider="", book="",
               facts=["Utah DOPL licenses HVAC contractors.", "The book package covers the Utah HVAC written exam references."]),
    "va": dict(board="the Virginia Board for Contractors (DPOR)", short="Virginia DPOR", url="https://www.dpor.virginia.gov/", provider="", book="",
               facts=["The Virginia Board for Contractors certifies HVAC tradesmen as journeyman and master, plus residential HVAC tradesman.",
                      "Refrigeration contractor prep is listed separately from the HVAC tradesman licenses."]),
    "wa": dict(board="the Washington Department of Labor and Industries (L&I)", short="Washington L&I", url="https://lni.wa.gov/licensing-permits/electrical/", provider="", book="",
               facts=["Washington's HVAC/R electrical specialties cover the electrical side of HVAC and refrigeration work.",
                      "The A-HVAC/R and restricted B-HVAC/R books are listed for administrators, electricians and master electricians."]),
    "wv": dict(board="the West Virginia Contractor Licensing Board and Division of Labor", short="WV Division of Labor", url="https://labor.wv.gov/", provider="Prov", book="",
               facts=["West Virginia requires an HVAC technician certification from the Division of Labor for HVAC work.",
                      "Contractor licenses come from the West Virginia Contractor Licensing Board, and Prov gives the exams."]),
    "wy": dict(board="the city where you work", short="Local city license", url="", provider="ICC", book="",
               facts=["Wyoming has no statewide HVAC license; cities that license HVAC technicians use ICC exams such as the 600 Limited HVAC Technician.",
                      "Check with your city for the exam it uses before you order."]),
    "books": dict(board="the board for the license you are testing for", short="Depends on the license", url="", provider="", book="",
                  facts=["These reference books sit beside the state exam prep and show up on many HVAC exam reference lists.",
                         "Check the candidate bulletin for your exam to see which editions it allows."]),
}

def _src(g):
    s = STATE[g]; out = []
    if s["url"]: out.append(((s["short"] if s["short"] != "Local city license" else "Licensing board") + " (official site)", s["url"]))
    if g == "mo": out.append(("St. Louis County (official site)", "https://stlouiscountymo.gov/"))
    if g == "la": out.append(("City of New Orleans Safety and Permits", "https://nola.gov/safety-and-permits/"))
    if g == "wv": out.append(("WV Division of Labor: Prov exams", "https://labor.wv.gov/article/prov-exam-inc"))
    out.append(EPA_608)
    return out
SOURCES = {g: _src(g) for g in STATE}
MAIN_SOURCES = [EPA_608, ("Oklahoma Construction Industries Board", "https://oklahoma.gov/cib.html"), ("Arizona Registrar of Contractors", "https://roc.az.gov/")]

SCOPE = {}  # per-license one-liners; build.py falls back to a generated sentence
CLASS_FACTS = {
    "oklahoma-hvacr-unlimited-contractor": ["The trade exam is open book: 90 questions in 240 minutes, passing score 70 percent (63 correct).", "PSI gives the exam for the Oklahoma Construction Industries Board."],
    "arizona-c-39-air-conditioning-refrigeration": ["The C-39 trade exam is open book.", "Arizona applicants also prepare for the business and law exam."],
}
OFFICIAL_SCOPE = "{name} exam prep."

def _how(g):
    s = STATE[g]
    p = (" %s gives the exam." % s["provider"]) if s["provider"] and " or " not in s["provider"] else (" The exam is given by %s." % s["provider"] if s["provider"] else "")
    return "The {name} license comes from " + s["board"] + "." + p + " The board approves your application first; then you schedule the exam and bring only the references the candidate bulletin allows."
GROUP_HOW = {g: _how(g) for g in STATE}
GROUP_FACTS = {g: STATE[g]["facts"] for g in STATE}
def _open(g):
    b = STATE[g]["book"]
    if b == "open": return "Yes. The trade exam for this license is open book, with the references listed in the candidate bulletin. Highlighted and tabbed books save the most time."
    if b == "some": return "Several exams in this state let you bring approved books, which is why exam-room book packages are offered. Your candidate bulletin lists the books allowed for your exam."
    return "Many HVAC trade exams are open book, but the rule depends on the exam. Your candidate bulletin lists the references allowed; if books are allowed, highlighted and tabbed sets save the most time."
OPEN_BOOK = {g: _open(g) for g in STATE}
WHO_ISSUES = {g: STATE[g]["board"] for g in STATE}
ISSUER_SHORT = {g: STATE[g]["short"] + ((", exams by %s" % STATE[g]["provider"]) if STATE[g]["provider"] else "") for g in STATE}
BOOK_SHORT = {g: {"open": "Open book", "some": "Approved books for several exams"}.get(STATE[g]["book"], "See the candidate bulletin") for g in STATE}
GROUP_FAQ = {g: [("Do I need EPA 608 certification as well as the {name} license?", "Usually, yes, if you handle refrigerant. EPA Section 608 is a federal certification and the state or city license is separate; most working HVAC contractors hold both."),
                 ("How long does the {name} prep take to arrive?", "Online courses and practice questions arrive by email after purchase. Book packages ship free by USPS Media Mail; allow up to 15 business days for rental, Ultimate and 1 Package orders.")] for g in STATE}

# what each package type is, in one line
TYPE_BLURB = {
    "tabs": "pre-printed tabs for the reference books",
    "tabs-highlights": "pre-printed tabs plus highlighting guides for the reference books",
    "flash-cards": "study flash cards for quick review",
    "online-practice-exams": "online practice questions with explanations",
    "intro-course": "a short introduction to becoming a licensed contractor in the state",
    "online-course": "a self-study online course built around the exam",
    "ca-business-trade-courses": "online courses for the business and law exam and the trade exam",
    "live-training": "live virtual classes with an instructor plus the self-study course",
    "exam-room-books": "only the books the testing center lets you bring in",
    "exam-room-highlighted": "the exam-room books, already highlighted and tabbed",
    "book-package": "every reference book the exam is written to, new and unmarked",
    "reference-book": "a reference book used on HVAC licensing exams",
    "highlighted-tabbed": "the reference books already highlighted and tabbed",
    "accelerator": "the book set plus help with the state license application",
    "rental-exam-room": "the exam-room books on rental plus the online course",
    "rental-package": "the reference books on rental plus the online course, returned after your exam",
    "ca-ultimate-courses-application": "the business and trade courses plus help with the license application",
    "ultimate-exam-room": "exam-room books, the online course and help with the application",
    "ultimate-rental": "highlighted and tabbed rental books, a year of course access and help with the application",
    "ca-courses-application-fees-bond": "the business and trade courses, the application, the state fees and the first-year bond",
    "the-1-package": "everything in the Ultimate package plus LLC or corporation setup, EIN filing and compliance guidance",
    "other": "exam prep",
}

# home page
HOME_H1 = "HVAC license exam prep for your state"
HOME_TITLE = "HVAC License Exam Prep by State | Pass Your HVAC Exam"
HOME_DESC = "Exam prep for {n} HVAC, refrigeration and heating licenses in 35 states and DC: books, highlighted and tabbed sets, online courses and live classes."
HOME_LEAD = ("Pass Your HVAC Exam has prep for {n} HVAC, refrigeration and heating licenses in 35 states and Washington DC. Pick your state to see who issues "
             "the license and how the exam works, then compare every package for that exam, from $64.99 tabs to The 1 Package, with one-click checkout.")
HOME_SEARCH_PLACEHOLDER = "Try Arizona C-39, Florida Air A or NC Heating Group 2"
LICENSES_COVERED = "HVAC licenses covered"
HOME_TAKEAWAYS = [
    "Every state runs its own HVAC exam; a few, such as Missouri, Nebraska and Wyoming, leave licensing to cities.",
    "EPA Section 608 is a separate federal certification for handling refrigerant; most contractors need both.",
    "Highlighted and tabbed books save the most time on open-book exams such as Arizona C-39 and Oklahoma HVACR.",
]
HOME_FAQ = [
    ("Which HVAC license do I need?", "The right license depends on your state and the work you do. Each state page lists the HVAC, refrigeration and heating licenses we have prep for, who issues them and what each exam covers. Start with your state on the map."),
    ("Do I need EPA 608 certification for a state HVAC license?", "They are separate. EPA Section 608 is a federal certification for anyone who handles refrigerant. Your state or city license has its own trade exam and often a business and law exam. Most working HVAC contractors hold both."),
    ("Is the HVAC contractor exam open book?", "Many are. The Arizona C-39 and Oklahoma HVACR exams are open book, for example, and several Nevada, Connecticut and Idaho exams allow approved books. Your candidate bulletin lists the references allowed."),
    ("What is the difference between the book package and highlighted and tabbed books?", "The book package is the full set of references for your exam. The highlighted and tabbed version is the same set, already marked up by instructors so you can find answers fast during an open-book exam."),
    ("What do the Ultimate Package and The 1 Package include?", "The Ultimate Package bundles highlighted and tabbed rental books, a year of online course access and help with your license application. The 1 Package adds LLC or corporation setup, EIN filing and compliance guidance."),
    ("Are these the real exam questions?", "No. Licensing exam questions are confidential. The courses and practice questions are original material written to the same subjects and format, with explanations."),
    ("Does buying a package register me for the exam?", "No. Your state board or city approves your application first, then the testing provider schedules the exam. A package gets you ready for the test itself."),
    ("How do orders arrive?", "Books ship free from our fulfillment center, {ful}, by USPS Media Mail. Online courses and practice questions arrive by email after purchase. Allow up to 15 business days for rental, Ultimate and 1 Package orders."),
]
GENERAL_FAQ_LEAD = "Here are {n} answers about HVAC license exams: who issues the license in each state, EPA 608 versus a state license, open-book rules, the testing providers, package types, rentals, shipping and ordering. Each of the {k} license pages and every state page adds questions of its own, so check yours too."
FAQ_TAKEAWAYS = [
    "Each state, and in some places each city, sets its own HVAC exam; the state page tells you who issues your license.",
    "EPA Section 608 is federal and separate from the state license.",
    "Rental, Ultimate and 1 Package prices include a refundable book deposit.",
]
BLOG_FAQ = [
    ("How long should I study for an HVAC contractor exam?", "Most candidates plan six to eight weeks at about an hour a day: learning the references, practicing load and duct calculations, and taking timed practice exams. Open-book exams reward knowing where answers are."),
    ("Is the HVAC exam open book?", "Many state trade exams are, including Arizona C-39 and Oklahoma HVACR. Your candidate bulletin lists the books and editions allowed."),
    ("Do I need EPA 608 as well?", "If you handle refrigerant, yes. EPA Section 608 is federal and separate from the state license."),
    ("Are the practice questions the real exam questions?", "No. Licensing exam questions are confidential. Our courses and practice questions are original material written to the same subjects."),
    ("Does buying a package register me for the exam?", "No. Your board approves you first, then the testing provider schedules the exam."),
    ("How do orders arrive?", "Books ship from our fulfillment center, {ful}; online courses arrive by email after purchase."),
]
FAQ_GROUP_INTRO = {}
LLM_SUMMARY = "Exam prep for {n} HVAC, refrigeration and heating licenses in 35 states and Washington DC, grouped by state, plus HVAC reference books."
LLM_FACTS = [
    "- Every state, and in some places each city, licenses HVAC work separately; each state page names the board and the exam provider where confirmed.",
    "- EPA Section 608 is a federal refrigerant certification, separate from any state license.",
    "- Oklahoma HVACR Unlimited Contractor: PSI, open book, 90 questions, 240 minutes, 70% to pass; 2024 IMC and IFGC only from December 15, 2026.",
    "- Arizona C-39: open book trade exam plus a business and law exam, licensed by the Arizona Registrar of Contractors.",
    "- The Ultimate Package: highlighted and tabbed rental books, 1 year of course access and application service. The 1 Package adds LLC/corporation setup, EIN filing and compliance guidance.",
    "- Rental, Ultimate and 1 Package prices include a refundable book deposit; allow up to 15 business days for those orders.",
]
BLOG_LEAD = "This blog has study plans, state licensing rules and exam strategy for HVAC, refrigeration and heating license exams, written for people who work full days and study at night. Each post links to the state and license it covers, and every rule we quote links to the board that sets it."
PROMO = "Free shipping on every book package. Online courses start the day you buy."
COLLAGE = []
MAX_ALIASES = {}
