# -*- coding: utf-8 -*-
"""
Page components for the PAMAS Global site.

THE FRACTION AXIS is the site's organising device. Iodine value measures
unsaturation, which is what decides whether a fat is solid or liquid at ambient
temperature. Plotting the whole range on one axis is the honest way to show
that every product traded here is the same raw material separated at a
different cut point, and it answers the buyer's real question directly:
which fraction do I need.
"""

AXIS_MIN, AXIS_MAX = 10, 145

# name, sub-label, iodine low, iodine high, state note, colour token
FRACTIONS = [
    ("Palm Kernel Oil",        "CPKO and RBD PKO",     16,  19,  "Melts 24 to 26 &deg;C",  "--f-hard"),
    ("RBD Palm Stearin",       "Hard fraction",        33,  48,  "Melts 44 to 56 &deg;C",  "--f-hard"),
    ("Crude Palm Oil",         "Before fractionation", 50,  55,  "Melts 33 to 39 &deg;C",  "--crude"),
    ("RBD Palm Oil",           "Whole refined oil",    50,  55,  "Melts 33 to 39 &deg;C",  "--f-mid"),
    ("RBD Palm Olein",         "Soft fraction",        56,  60,  "Clouds at 10 &deg;C",    "--f-mid"),
    ("RBD Palm Superolein",    "Double fractionated",  60,  65,  "Clouds at 6 &deg;C",     "--f-mid"),
    ("RBD Canola Oil",         "Soft oil",            110, 126,  "Liquid below 0 &deg;C",  "--f-soft"),
    ("RBD Sunflower Oil",      "Soft oil",            118, 141,  "Liquid below 0 &deg;C",  "--f-soft"),
    ("Crude Degummed Soybean", "Soft oil",            120, 141,  "Liquid below 0 &deg;C",  "--f-soft"),
]

NL = "\n"


def _pos(v):
    return (v - AXIS_MIN) / (AXIS_MAX - AXIS_MIN) * 100


def axis(rows=None, caption=True):
    """Draw the traded range against real iodine values."""
    data = FRACTIONS if rows is None else rows
    items = []
    for name, sub, lo, hi, state, col in data:
        left = _pos(lo)
        width = max(_pos(hi) - _pos(lo), 0.9)
        items.append(
            '          <li class="axis__row">' + NL +
            f'            <div class="axis__name">{name}<small>{sub}</small></div>' + NL +
            '            <div class="axis__track">' + NL +
            f'              <div class="axis__span" style="left:{left:.1f}%; width:{width:.1f}%; --bar:var({col})"></div>' + NL +
            '            </div>' + NL +
            f'            <div class="axis__val"><b>IV {lo} to {hi}</b><br>{state}</div>' + NL +
            '          </li>')
    ticks = "".join(
        f'<span style="left:{_pos(v):.1f}%">{v}</span>' for v in (10, 40, 70, 100, 145))
    cap = ('        <figcaption class="note" style="margin-top:1rem">' + NL +
           '          Horizontal axis is iodine value, the measure of unsaturation that decides' + NL +
           '          whether a fat is solid or liquid at ambient temperature. Ranges are' + NL +
           '          indicative trading specifications.' + NL +
           '        </figcaption>' + NL) if caption else ""
    return (
        '      <figure class="axis">' + NL +
        '        <div class="axis__head">' + NL +
        '          <div class="axis__unit">Iodine value</div>' + NL +
        '          <div class="axis__scale" aria-hidden="true"></div>' + NL +
        f'          <div class="axis__ticks" aria-hidden="true">{ticks}</div>' + NL +
        '        </div>' + NL +
        '        <ul class="axis__rows">' + NL +
        NL.join(items) + NL +
        '        </ul>' + NL +
        '        <div class="axis__legend">' + NL +
        '          <span><i style="background:var(--f-hard)"></i> Solid at ambient</span>' + NL +
        '          <span><i style="background:var(--f-mid)"></i> Semi-solid</span>' + NL +
        '          <span><i style="background:var(--f-soft)"></i> Liquid</span>' + NL +
        '          <span><i style="background:var(--crude)"></i> Unrefined</span>' + NL +
        '        </div>' + NL +
        cap +
        '      </figure>')


def opening(h1, sub, cta_primary, cta_secondary=None):
    """
    The opening states the thesis and hands straight to the axis. There is no
    photograph behind the headline: the separation is the idea, and a stock
    plantation shot behind white type is the one move every site makes.
    """
    second = (f'<a class="btn btn--line" href="{cta_secondary[1]}">{cta_secondary[0]}</a>'
              if cta_secondary else "")
    return (
        NL + '  <section class="open">' + NL +
        '    <div class="wrap">' + NL +
        '      <div class="open__grid">' + NL +
        f'        <div><h1>{h1}</h1></div>' + NL +
        '        <div>' + NL +
        f'          <p class="open__sub">{sub}</p>' + NL +
        '          <div class="btn-row" style="margin-top:1.5rem">' + NL +
        f'            <a class="btn btn--primary" href="{cta_primary[1]}">{cta_primary[0]}</a>' + NL +
        f'            {second}' + NL +
        '          </div>' + NL +
        '        </div>' + NL +
        '      </div>' + NL +
        '    </div>' + NL +
        '  </section>' + NL)
