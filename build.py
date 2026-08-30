#!/usr/bin/env python3
"""
PAMAS Global — static site generator.

The published site is plain HTML; this script only assembles it so that the
header, footer and company details live in one place.

    python3 build.py

To replace a placeholder everywhere, edit COMPANY below and re-run.
Values still wrapped in [SQUARE BRACKETS] render with a yellow highlight on the
page, so nothing unverified can ship unnoticed.
"""
import json, pathlib, re

ROOT = pathlib.Path(__file__).parent

# ---------------------------------------------------------------------------
# COMPANY FACTS — replace the bracketed values, then re-run this script.
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
    "years_active": "[N]",
    "annual_volume":"[N]",
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
      <span class="brand__name">PAMAS<span class="brand__mark">.</span>GLOBAL</span>
      <span class="brand__sub">Sdn Bhd &middot; Malaysia</span>
    </a>
    <button class="nav-toggle" aria-expanded="false" aria-controls="nav" aria-label="Open menu">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M3 6h18M3 12h18M3 18h18"/></svg>
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
  <div class="wrap">
    <div class="foot__grid">
      <div>
        <h2>PAMAS Global Sdn Bhd</h2>
        <p style="color:#B6C7D0; font-size:.93rem">
          Physical trade in palm oil products, soft oils and palm biomass, from origin in Malaysia
          to refiners, feed producers and energy buyers worldwide.
        </p>
        <p class="mono" style="font-size:.75rem; color:#93A6B0">
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
          <li><a href="products.html#palm">Palm oil &amp; fractions</a></li>
          <li><a href="products.html#kernel">Kernel products</a></li>
          <li><a href="products.html#soft">Soft oils</a></li>
          <li><a href="products.html#biomass">Palm biomass</a></li>
        </ul>
      </div>
      <div>
        <h3>Trading desk</h3>
        <ul class="mono" style="font-size:.85rem">
          <li>{tbd(c["street"])}</li>
          <li>{tbd(c["city"])}, Malaysia</li>
          <li><a href="tel:{c["phone_href"]}">{tbd(c["phone"])}</a></li>
          <li><a href="mailto:{c["email"]}">{tbd(c["email"])}</a></li>
        </ul>
      </div>
    </div>
    <div class="foot__base">
      <span>&copy; {tbd(c["year_founded"])} PAMAS Global Sdn Bhd. All rights reserved.</span>
      <span><a href="credits.html">Photo credits &amp; licences</a></span>
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


def hero(eyebrow, h1, lede, img, alt, buttons=""):
    return f'''
  <section class="hero">
    <div class="hero__media">
      <img src="assets/img/{img}" alt="{alt}" fetchpriority="high">
    </div>
    <div class="wrap hero__inner">
      <p class="hero__eyebrow">{eyebrow}</p>
      <h1>{h1}</h1>
      <p class="hero__lede">{lede}</p>
      {buttons}
    </div>
  </section>
'''


def figure(img, alt, credit):
    return f'''<figure class="figure">
          <img src="assets/img/{img}" alt="{alt}" loading="lazy">
          <figcaption>{credit}</figcaption>
        </figure>'''


# ---------------------------------------------------------------------------
# Photo credit lines, generated from the Commons metadata captured at fetch time
# ---------------------------------------------------------------------------
MANIFEST = json.loads((ROOT / "assets/img/manifest.json").read_text())


def credit(slug):
    m = MANIFEST[slug]
    lic, url = m["license"], m.get("licenseurl") or ""
    if lic.lower().startswith("public") or lic == "CC0":
        return (f'Image: {m["title"]} by {m["author"]}, via '
                f'<a href="{m["descurl"]}">Wikimedia Commons</a>, {lic}.')
    licence = f'<a href="{url}">{lic}</a>' if url else lic
    return (f'Image: {m["title"]} by {m["author"]}, via '
            f'<a href="{m["descurl"]}">Wikimedia Commons</a>, licensed under {licence}.')


def write(name, title, desc, body):
    html = head(title, desc, name) + body + foot()
    (ROOT / name).write_text(html)
    print(f"  wrote {name:24} {len(html)//1024:>3} KB")


if __name__ == "__main__":
    import pages
    print("Building PAMAS Global site...")
    pages.build(globals())
    unresolved = sum(
        len(re.findall(r'class="tbd"', (ROOT / f).read_text()))
        for f in ROOT.glob("*.html"))
    print(f"\nDone. {unresolved} placeholder(s) still to fill — "
          f"edit COMPANY in build.py and re-run.")
