# PAMAS Global Sdn Bhd — website

Static marketing site for a Malaysian physical commodity trading company dealing in the palm oil
complex, soft oils and palm biomass.

No build tooling is required to **serve** the site — it is plain HTML, CSS and one small inline
script. `build.py` exists only so that the header, footer and company details live in one place.

---

## Before this goes live

The site is complete apart from facts only you can supply. Every unverified value renders as
**yellow highlighted text** on the page, so nothing false can ship unnoticed. There are 63 of them.

### 1. Fill in the company details

Edit the `COMPANY` dictionary at the top of `build.py`, then run `python3 build.py`. One edit
updates every page.

| Key | What it needs |
|---|---|
| `year_founded` | Year of incorporation |
| `reg_no` | SSM company registration number |
| `mpob_licence` | MPOB licence number — **see the warning below** |
| `street`, `city` | Registered / trading office address |
| `phone`, `phone_href` | Contact number (display form, and the `tel:` form) |
| `email` | Trading desk email |
| `countries`, `years_active` | Used on the About page |

### 2. Resolve the four claims I could not verify

These are asserted in the copy because they are normal for a Malaysian palm trader. **Confirm each
one applies to PAMAS Global, or remove it.** An unfounded licensing or certification claim is a
regulatory problem, not a copy problem.

- **MPOB licence** — stated on the home page and in the footer. Malaysian law requires a licence to
  deal in palm products. If PAMAS does not hold one yet, remove the claim.
- **RSPO membership** — flagged on `sustainability.html` as an explicit "confirm" placeholder.
  Do not claim RSPO status without a membership number.
- **PORAM / FOSFA contract terms** — the copy says contracts are issued on these standard terms.
  True only if that is genuinely your practice.
- **Product specifications** — the tables are *typical industry trading specifications*, not
  PAMAS's own tested values. Check them against what you can actually source before publishing.

### 3. Connect the enquiry form

`contact.html` has a complete, accessible enquiry form but **no backend**. It currently posts
nowhere and shows a visible notice saying so. Point it at a form handler (Formspree, Basin,
Netlify Forms, or your own endpoint) by setting the `action` attribute in `pages.py`.

### 4. Replace the photography

Every image is from Wikimedia Commons under a public-domain or Creative Commons licence, with
attribution on `credits.html` as CC BY-SA requires. They are documentary photographs, not brand
photography — good enough to launch, not ideal long term.

Seven images from the original source list were **discarded** as unusable: several showed other
palm companies' branded signage, and others were informal snapshots (a market stall, a person on
a guardrail). Do not reinstate them.

If you commission or license replacements, drop them into `assets/img/` under the same filenames
and delete the corresponding rows from `assets/img/manifest.json` so the credits page stays honest.

---

## Structure

```
index.html              Home — hero, spec strip, three books, credibility, origin
about.html              Who we are, how we operate, markets served
products.html           Full trading specifications for all four product groups
process.html            Seven-step shipment sequence, enquiry to discharge
sustainability.html     MSPO vs RSPO, EUDR due diligence, position
contact.html            Enquiry form and desk details
credits.html            Photo attribution (required by CC BY-SA)

assets/css/site.css     All styling; design tokens at the top
assets/img/             Photographs + manifest.json (licence metadata)
build.py                Page shell, company details, credit generation
components.py           The fraction axis and the opening block
pages.py                Page content
```

Regenerate after editing either Python file:

```bash
python3 build.py
```

Preview locally:

```bash
python3 -m http.server 8000
# then open http://localhost:8000
```

---

## Design notes

**Organising idea: the fraction.** Everything PAMAS trades is one raw material separated by
temperature. Chill crude palm oil and it splits into a hard stearin and a soft olein. Every
parameter the trade quotes, iodine value, cloud point, melting point, measures the same
thing: where on the hardness axis a fraction sits.

So the site is built on that axis rather than on a generic corporate template. The product
range is drawn as a range chart plotted against real iodine values, from palm kernel oil at
IV 16 through to sunflower at 141. It is the page's main content, it answers the buyer's
actual question (which fraction does my process need), and it could not be transplanted to
any other company. The chart lives in `components.py`; edit `FRACTIONS` and every instance
updates.

**Palette.** Taken from the appearance of the fractions themselves rather than from
corporate blue: a warm near-black ground, off-white type, and a ramp running from the pale
solids through amber to crude palm oil's deep red. The colour system and the organising idea
are the same thing. Theme is locked dark throughout; a trading screen is dark, and the
material ramp only reads properly against it.

**Type.** Archivo at 900 for display, Schibsted Grotesk for body, Martian Mono for every
specification value, port and incoterm. The monospace does real work: it is what makes a
parameter read as a measured value rather than marketing copy.

**Structure.** There is no photograph behind the headline. A stock plantation shot with a
dark scrim and white type over it is the single move every generated site makes, and it says
nothing this business does not share with every other palm company. The opening states the
thesis and hands straight to the axis. Section identity sits in a margin rail the way a
contract carries its clause reference, not in an eyebrow label stacked above every headline.
Six layout families appear once each.

**Why there are no testimonials.** The credibility case is built from things a counterparty
can verify: published specifications, named inspection agencies, standard contract terms,
settlement instruments, licence numbers. Invented client quotes and logos would be trivially
falsifiable in a market this small. Add real ones when you have them; the layout has room.

## Accessibility

Verified at build: WCAG AA contrast on every text pair against the dark ground, visible focus
rings, skip link, semantic landmarks and headings, labelled form fields, alt text on every
image, 46px minimum touch targets, `prefers-reduced-motion` respected, valid HTML on all
seven pages, and the range chart's scale aligned to its plot at every breakpoint.
