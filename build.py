#!/usr/bin/env python3
"""
PAMAS Global static site generator.

The published site is plain HTML; this script only assembles it so the header,
footer and company details live in one place.

    python3 build.py

To replace a placeholder everywhere, edit COMPANY below and re-run. Values still
wrapped in [SQUARE BRACKETS] render highlighted on the page, so nothing
unverified can ship unnoticed.
"""
import json, pathlib, re

ROOT = pathlib.Path(__file__).parent

# ---------------------------------------------------------------------------
# COMPANY FACTS. Replace the bracketed values, then re-run this script.
# ---------------------------------------------------------------------------
COMPANY = {
    "year_founded": "[YEAR]",
    "reg_no":       "[SSM REG. NO.]",
    "mpob_licence": "[MPOB LICENCE NO.]",
    "street":       "[STREET ADDRESS]",
    "city":         "[POSTCODE, CITY]",
    "phone":        "[+60 PHONE]",
    "phone_href":   "[PHONE]",
    "email":        "[EMAIL]",
    "countries":    "[N]",
}

NAV = [
    ("index.html",          "Home"),
    ("about.html",          "About"),
    ("products.html",       "Products"),
    ("process.html",        "How we work"),
    ("sustainability.html", "Sustainability"),
]


def tbd(value: str) -> str:
    """Wrap an unverified placeholder so it is impossible to miss on the page."""
    if value.startswith("[") and value.endswith("]"):
        return f'<span class="tbd">{value}</span>'
    return value


def head(title, desc, current):
    nav = "\n".join(
        '      <a href="{h}"{c}>{l}</a>'.format(
            h=h, l=l, c=' aria-current="page"' if h == current else "")
        for h, l in NAV)
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="stylesheet" href="assets/css/site.css">
</head>
<body>
<a class="skip" href="#main">Skip to main content</a>

<header class="masthead">
  <div class="wrap masthead__bar">
    <a class="brand" href="index.html">
      <span class="brand__name">PAMAS<i>.</i>GLOBAL</span>
      <span class="brand__sub">Sdn Bhd</span>
    </a>
    <button class="nav-toggle" aria-expanded="false" aria-controls="nav" aria-label="Open menu">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M3 6h18M3 12h18M3 18h18"/></svg>
    </button>
    <nav class="nav" id="nav" aria-label="Primary">
{nav}
      <a class="btn btn--primary nav__cta" href="contact.html">Request a quote</a>
    </nav>
  </div>
</header>

<main id="main">'''


def foot():
    c = COMPANY
    return f'''</main>

<footer class="foot">
  <div class="wrap foot__inner">
    <div class="foot__grid">
      <div>
        <h2>PAMAS Global Sdn Bhd</h2>
        <p style="color:#A8B8C0; font-size:.88rem; max-width:34ch">
          Physical trade in palm oil products, soft oils and palm biomass, from
          origin in Malaysia to refiners, feed producers and energy buyers worldwide.
        </p>
        <p class="mono" style="font-size:.7rem; color:#7D919B">
          Company no. {tbd(c["reg_no"])}<br>
          MPOB licence {tbd(c["mpob_licence"])}
        </p>
      </div>
      <div>
        <h3>Company</h3>
        <ul>
          <li><a href="about.html">About us</a></li>
          <li><a href="process.html">How we work</a></li>
          <li><a href="sustainability.html">Sustainability</a></li>
          <li><a href="contact.html">Contact</a></li>
        </ul>
      </div>
      <div>
        <h3>Products</h3>
        <ul>
          <li><a href="products.html#palm">Palm oil and fractions</a></li>
          <li><a href="products.html#kernel">Kernel products</a></li>
          <li><a href="products.html#soft">Soft oils</a></li>
          <li><a href="products.html#biomass">Palm biomass</a></li>
        </ul>
      </div>
      <div>
        <h3>Trading desk</h3>
        <ul class="mono" style="font-size:.8rem">
          <li>{tbd(c["street"])}</li>
          <li>{tbd(c["city"])}, Malaysia</li>
          <li><a href="tel:{c["phone_href"]}">{tbd(c["phone"])}</a></li>
          <li><a href="mailto:{c["email"]}">{tbd(c["email"])}</a></li>
        </ul>
      </div>
    </div>
    <div class="foot__base">
      <span>&copy; {tbd(c["year_founded"])} PAMAS Global Sdn Bhd. All rights reserved.</span>
      <span><a href="credits.html">Photo credits and licences</a></span>
    </div>
  </div>
</footer>

<script>
  var t = document.querySelector('.nav-toggle'), n = document.getElementById('nav');
  t.addEventListener('click', function () {{
    var open = n.getAttribute('data-open') === 'true';
    n.setAttribute('data-open', String(!open));
    t.setAttribute('aria-expanded', String(!open));
    t.setAttribute('aria-label', open ? 'Open menu' : 'Close menu');
  }});
</script>
</body>
</html>
'''


# --- section helpers -------------------------------------------------------

def hero(h1, sub, img, cta_primary, cta_secondary=None, terms=None):
    """Layout family A: full-bleed media, asymmetric split, terms ledger."""
    second = (f'<a class="btn btn--ondark" href="{cta_secondary[1]}">{cta_secondary[0]}</a>'
              if cta_secondary else "")
    tm = ""
    if terms:
        rows = "\n".join(
            f'        <div><dt>{k}</dt><dd>{v}</dd></div>' for k, v in terms)
        tm = f'\n      <dl class="terms">\n{rows}\n      </dl>'
    return f'''
  <section class="hero">
    <div class="hero__bg"><img src="assets/img/{img}" alt="" fetchpriority="high"></div>
    <div class="wrap hero__inner">
      <div class="hero__grid">
        <div>
          <h1>{h1}</h1>
          <p class="hero__sub">{sub}</p>
          <div class="btn-row">
            <a class="btn btn--primary" href="{cta_primary[1]}">{cta_primary[0]}</a>
            {second}
          </div>
        </div>{tm}
      </div>
    </div>
  </section>
'''


def band(inner, rail=None, flush=False):
    """A ruled section. The rail replaces a stacked eyebrow label."""
    cls = "band band--flush" if flush else "band"
    if rail is None:
        return f'''
  <section class="{cls}">
    <div class="wrap band__inner">
{inner}
    </div>
  </section>
'''
    mark, sub = rail
    return f'''
  <section class="{cls}">
    <div class="wrap band__inner">
      <div class="railed">
        <div class="rail"><b>{mark}</b>{sub}</div>
        <div>
{inner}
        </div>
      </div>
    </div>
  </section>
'''


def imgbreak(img, text):
    """Layout family D: full-bleed image with one line of text."""
    return f'''
  <section class="break">
    <div class="break__bg"><img src="assets/img/{img}" alt="" loading="lazy"></div>
    <div class="wrap"><p class="break__text">{text}</p></div>
  </section>
'''


MANIFEST = json.loads((ROOT / "assets/img/manifest.json").read_text())


def write(name, title, desc, body):
    html = head(title, desc, name) + body + foot()
    (ROOT / name).write_text(html)
    print(f"  {name:24} {len(html)//1024:>3} KB")


if __name__ == "__main__":
    import pages
    print("Building PAMAS Global...")
    pages.build(globals())

    # Guard rails: these are the checks the previous build failed.
    files = [f for f in ROOT.glob("*.html")]
    dashes = sum(len(re.findall(r"—|&mdash;|–|&ndash;", f.read_text())) for f in files)
    tbds = sum(len(re.findall(r'class="tbd"', f.read_text())) for f in files)
    print(f"\n  em-dashes ......... {dashes}  (must be 0)")
    print(f"  placeholders ...... {tbds}  (fill COMPANY above)")
    if dashes:
        for f in files:
            n = len(re.findall(r"—|&mdash;|–|&ndash;", f.read_text()))
            if n:
                print(f"      {f.name}: {n}")
