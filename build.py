#!/usr/bin/env python3
"""
PAMAS Global static site generator.

Layout follows the Al-Hamza Group corporate template supplied as reference:
navy and gold, top contact bar, sticky nav, photo hero, contact bar, a
business-unit card grid, stats band, and a four-column footer.

    python3 build.py

Edit COMPANY below and re-run to replace a placeholder everywhere. Values still
wrapped in [SQUARE BRACKETS] render highlighted on the page, so nothing
unverified can ship unnoticed.
"""
import json, pathlib, re

ROOT = pathlib.Path(__file__).parent

# ---------------------------------------------------------------------------
# COMPANY FACTS. Replace the bracketed values, then re-run.
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
    # stats band
    "years_trading":  "[N]",
    "countries":      "[N]",
    "annual_tonnes":  "[N]",
    "counterparties": "[N]",
}

NAV = [
    ("index.html",          "Home"),
    ("about.html",          "About Us"),
    ("products.html",       "Products"),
    ("process.html",        "How We Work"),
    ("sustainability.html", "Sustainability"),
]

ICON = {
  "pin":   '<path d="M12 21s7-6.2 7-11a7 7 0 1 0-14 0c0 4.8 7 11 7 11z"/><circle cx="12" cy="10" r="2.6"/>',
  "mail":  '<rect x="3" y="5" width="18" height="14" rx="1.5"/><path d="m3.5 6.5 8.5 6 8.5-6"/>',
  "tel":   '<path d="M6.5 3.5h3l1.5 4-2 1.5a12 12 0 0 0 6 6l1.5-2 4 1.5v3a1.5 1.5 0 0 1-1.6 1.5A16.5 16.5 0 0 1 3.5 5.1 1.5 1.5 0 0 1 5 3.5z"/>',
  "check": '<path d="m4.5 12.5 5 5 10-11"/>',
  "doc":   '<path d="M6 3h8l4 4v14H6z"/><path d="M14 3v4h4"/><path d="M9 12h6M9 16h6"/>',
  "ship":  '<path d="M4 17.5 12 21l8-3.5"/><path d="M5.5 13.5 12 16l6.5-2.5"/><path d="M12 3v13"/><path d="M7 8.5h10"/>',
  "shield":'<path d="M12 3 5 6v5.5c0 4.2 2.9 7.6 7 9.5 4.1-1.9 7-5.3 7-9.5V6z"/>',
  "globe": '<circle cx="12" cy="12" r="8.5"/><path d="M3.5 12h17M12 3.5a15 15 0 0 1 0 17 15 15 0 0 1 0-17z"/>',
  "leaf":  '<path d="M5 19C4 12 8.5 5.5 19 5c.5 8.5-4.5 13.5-11 13.5H5z"/><path d="M5 19c3-4.5 6.5-7 11-9"/>',
}


def icon(name, size=22, sw=1.7):
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" '
            f'stroke="currentColor" stroke-width="{sw}" stroke-linecap="round" '
            f'stroke-linejoin="round" aria-hidden="true">{ICON[name]}</svg>')


def tbd(value: str) -> str:
    """Wrap an unverified placeholder so it is impossible to miss on the page."""
    if value.startswith("[") and value.endswith("]"):
        return f'<span class="tbd">{value}</span>'
    return value


def head(title, desc, current):
    c = COMPANY
    nav = "\n".join(
        '      <a href="{h}"{cur}>{l}</a>'.format(
            h=h, l=l, cur=' aria-current="page"' if h == current else "")
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

<div class="topbar">
  <div class="wrap topbar__in">
    <span>{icon("pin", 15)} {tbd(c["city"])}, Malaysia</span>
    <span>{icon("mail", 15)} <a href="mailto:{c["email"]}">{tbd(c["email"])}</a></span>
    <span class="topbar__spacer">{icon("tel", 15)} <a href="tel:{c["phone_href"]}">{tbd(c["phone"])}</a></span>
  </div>
</div>

<header class="masthead">
  <div class="wrap masthead__bar">
    <a class="brand" href="index.html">
      <span class="brand__mark">PG</span>
      <span class="brand__text">
        <span class="brand__name">PAMAS GLOBAL</span>
        <span class="brand__sub">Sdn Bhd</span>
      </span>
    </a>
    <button class="nav-toggle" aria-expanded="false" aria-controls="nav" aria-label="Open menu">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M3 6h18M3 12h18M3 18h18"/></svg>
    </button>
    <nav class="nav" id="nav" aria-label="Primary">
{nav}
      <a class="btn btn--gold nav__cta" href="contact.html">Request a Quote</a>
    </nav>
  </div>
</header>

<main id="main">'''


def hero(kicker, h1, sub, img, primary, secondary=None, small=False):
    sec = (f'\n        <a class="btn btn--onphoto" href="{secondary[1]}">{secondary[0]}</a>'
           if secondary else "")
    return f'''
  <section class="hero{' hero--sm' if small else ''}">
    <div class="hero__bg"><img src="assets/img/{img}" alt="" fetchpriority="high"></div>
    <div class="wrap hero__in">
      <p class="hero__kicker">{kicker}</p>
      <h1>{h1}</h1>
      <p class="hero__sub">{sub}</p>
      <div class="btn-row">
        <a class="btn btn--gold" href="{primary[1]}">{primary[0]}</a>{sec}
      </div>
    </div>
  </section>
'''


def contactbar():
    c = COMPANY
    return f'''
  <section class="cbar" aria-label="Contact details">
    <div class="wrap">
      <div class="cbar__grid">
        <div class="cbar__item">{icon("pin", 22)}
          <div><span class="cbar__k">Trading Desk</span>
            <span class="cbar__v">{tbd(c["street"])}, {tbd(c["city"])}</span></div></div>
        <div class="cbar__item">{icon("mail", 22)}
          <div><span class="cbar__k">Email Us</span>
            <span class="cbar__v"><a href="mailto:{c["email"]}">{tbd(c["email"])}</a></span></div></div>
        <div class="cbar__item">{icon("tel", 22)}
          <div><span class="cbar__k">Call Us</span>
            <span class="cbar__v"><a href="tel:{c["phone_href"]}">{tbd(c["phone"])}</a></span></div></div>
      </div>
    </div>
  </section>
'''


def shead(kicker, h2, sub=None, left=False):
    s = f'<p class="lede">{sub}</p>' if sub else ""
    return f'''      <div class="shead{' shead--left' if left else ''}">
        <p class="shead__kicker">{kicker}</p>
        <h2>{h2}</h2>
        <div class="shead__rule"></div>
        {s}
      </div>'''


def section(inner, grey=False, navy=False, label=None):
    cls = "section" + (" section--grey" if grey else "") + (" section--navy" if navy else "")
    lab = f' aria-label="{label}"' if label else ""
    return f'''
  <section class="{cls}"{lab}>
    <div class="wrap">
{inner}
    </div>
  </section>
'''


def ctaband(h2, p, primary, secondary=None):
    sec = (f'\n        <a class="btn btn--onphoto" href="{secondary[1]}">{secondary[0]}</a>'
           if secondary else "")
    return f'''
  <section class="ctaband">
    <div class="wrap ctaband__in">
      <div>
        <h2>{h2}</h2>
        <p>{p}</p>
      </div>
      <div class="btn-row">
        <a class="btn btn--gold" href="{primary[1]}">{primary[0]}</a>{sec}
      </div>
    </div>
  </section>
'''


def foot():
    c = COMPANY
    return f'''</main>

<footer class="foot">
  <div class="wrap foot__in">
    <div class="foot__grid">
      <div>
        <h2>PAMAS Global Sdn Bhd</h2>
        <p style="max-width:34ch">
          Physical trade in palm oil products, soft oils and palm biomass, from
          origin in Malaysia to refiners, feed producers and energy buyers worldwide.
        </p>
        <p class="mono" style="font-size:.8rem; color:#8FA3BA">
          Company no. {tbd(c["reg_no"])}<br>
          MPOB licence {tbd(c["mpob_licence"])}
        </p>
      </div>
      <div>
        <h3>Company</h3>
        <ul>
          <li><a href="about.html">About Us</a></li>
          <li><a href="process.html">How We Work</a></li>
          <li><a href="sustainability.html">Sustainability</a></li>
          <li><a href="contact.html">Contact Us</a></li>
        </ul>
      </div>
      <div>
        <h3>Products</h3>
        <ul>
          <li><a href="products.html#palm">Palm Oil &amp; Fractions</a></li>
          <li><a href="products.html#kernel">Kernel Products</a></li>
          <li><a href="products.html#soft">Soft Oils</a></li>
          <li><a href="products.html#biomass">Palm Biomass</a></li>
        </ul>
      </div>
      <div>
        <h3>Get In Touch</h3>
        <ul>
          <li>{tbd(c["street"])}</li>
          <li>{tbd(c["city"])}, Malaysia</li>
          <li><a href="tel:{c["phone_href"]}">{tbd(c["phone"])}</a></li>
          <li><a href="mailto:{c["email"]}">{tbd(c["email"])}</a></li>
        </ul>
      </div>
    </div>
    <div class="foot__base">
      <span>&copy; {tbd(c["year_founded"])} PAMAS Global Sdn Bhd. All rights reserved.</span>
      <span><a href="credits.html">Photo Credits &amp; Licences</a></span>
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


MANIFEST = json.loads((ROOT / "assets/img/manifest.json").read_text())


def write(name, title, desc, body):
    html = head(title, desc, name) + body + foot()
    (ROOT / name).write_text(html)
    print(f"  {name:24} {len(html)//1024:>3} KB")


if __name__ == "__main__":
    import pages
    print("Building PAMAS Global...")
    pages.build(globals())
    files = list(ROOT.glob("*.html"))
    dashes = sum(len(re.findall(r"—|&mdash;", f.read_text())) for f in files)
    tbds = sum(len(re.findall(r'class="tbd"', f.read_text())) for f in files)
    print(f"\n  em-dashes ......... {dashes}")
    print(f"  placeholders ...... {tbds}  (fill COMPANY above)")
