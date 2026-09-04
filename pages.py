# -*- coding: utf-8 -*-
"""Page content for the PAMAS Global site. Run `python3 build.py` to render."""


# Eight product lines, presented the way the reference site presents its eight
# subsidiaries: photo, heading, short description, key spec, and a link through.
PRODUCTS = [
    ("RBD Palm Olein", "ffb-bunch-alt.jpg",
     "The workhorse cooking oil of South and South East Asia. Refined, bleached and "
     "deodorised, clear and stable at ambient temperature.",
     "FFA 0.1% max &middot; IV 56 min &middot; Cloud point 10 &deg;C max", "products.html#palm"),
    ("RBD Palm Oil", "mill-interior.jpg",
     "Whole refined palm oil for food manufacture, frying fats and oleochemical "
     "feedstock. Supplied in bulk and flexitank.",
     "FFA 0.1% max &middot; IV 50 to 55 &middot; MP 33 to 39 &deg;C", "products.html#palm"),
    ("RBD Palm Stearin", "mill-sterilizer.jpg",
     "The hard fraction. Used in margarine, shortening, soap and candle manufacture "
     "where a solid fat is required.",
     "FFA 0.2% max &middot; IV 48 max &middot; MP 44 to 56 &deg;C", "products.html#palm"),
    ("Crude Palm Oil", "harvest-cutter.jpg",
     "Mill gate CPO for refiners running their own process. Traded in bulk vessel "
     "parcels on PORAM standard terms.",
     "FFA 5.0% max &middot; M&amp;I 0.25% max &middot; DOBI 2.3 min", "products.html#palm"),
    ("Palm Kernel Oil", "ffb-fruit.jpg",
     "High lauric oil pressed from the kernel, priced against the coconut complex. "
     "Crude and refined grades available.",
     "FFA 0.1 to 5.0% &middot; IV 16 to 19", "products.html#kernel"),
    ("Palm Kernel Expeller", "estate-berayung.jpg",
     "Protein rich compound feed ingredient for dairy and beef rations. Shipped in "
     "bulk and 50 kg bags to feed millers.",
     "Protein 14 to 16% &middot; Oil 6 to 9% &middot; Fibre 18% max", "products.html#kernel"),
    ("Soft Oils", "plantation-melaka.jpg",
     "Sunflower, canola and crude degummed soybean oil traded on FOSFA terms into "
     "food manufacture, repacking and feed.",
     "FFA 0.1% max &middot; PV 1.0 meq/kg max", "products.html#soft"),
    ("Palm Kernel Shell", "estate-pd.jpg",
     "Dense agricultural residue for biomass co-firing, taken by Japanese and Korean "
     "power plants in preference to most wood pellets.",
     "GCV 4,200 kcal/kg &middot; Moisture 15% max &middot; Sulphur 0.1% max", "products.html#biomass"),
]


def build(g):
    (write, hero, contactbar, shead, section, ctaband, icon, tbd) = (
        g["write"], g["hero"], g["contactbar"], g["shead"], g["section"],
        g["ctaband"], g["icon"], g["tbd"])
    C = g["COMPANY"]

    def cards():
        out = []
        for name, img, desc, spec, link in PRODUCTS:
            out.append(f'''        <article class="card">
          <div class="card__media"><img src="assets/img/{img}" alt="{name}" loading="lazy"></div>
          <div class="card__body">
            <h3>{name}</h3>
            <p>{desc}</p>
            <div class="card__spec">{spec}</div>
            <a class="card__link" href="{link}">Full specification</a>
          </div>
        </article>''')
        return '      <div class="cards cards--4">\n' + "\n".join(out) + '\n      </div>'

    # =======================================================================
    # HOME
    # =======================================================================
    reasons = [
      ("shield", "Independent Inspection",
       "Quality and quantity determined at load port by SGS, Intertek or a surveyor of "
       "your nomination, with the certificate of analysis issued before the cargo sails."),
      ("doc", "Standard Contract Terms",
       "Palm contracts on PORAM standard terms and soft oils on FOSFA, with arbitration "
       "clauses left intact so that any dispute has a defined venue."),
      ("check", "MPOB Licensed",
       f"Licensed by the Malaysian Palm Oil Board to deal in palm products under licence "
       f"number {tbd(C['mpob_licence'])}, verifiable on the public MPOB register."),
      ("ship", "Origin Logistics",
       "Loading at Port Klang, Pasir Gudang, Lahad Datu, Sandakan and Bintulu, in bulk "
       "parcels, ISO tanks, flexitanks, drums and jumbo bags."),
      ("globe", "One Point Of Contact",
       "Whoever prices your cargo follows it through nomination, loading, documents and "
       "discharge. Nothing is handed to a department that was not in the conversation."),
      ("leaf", "Traceable Supply",
       "We buy from licensed mills that can identify their supply base, and pass origin "
       "documentation through to the buyer rather than summarising it."),
    ]
    reason_html = "\n".join(f'''        <div class="reason">
          <div class="reason__icon">{icon(k, 24)}</div>
          <h3>{t}</h3>
          <p>{b}</p>
        </div>''' for k, t, b in reasons)

    stats = [(C["years_trading"], "Years Trading"),
             (C["countries"], "Countries Shipped To"),
             (C["annual_tonnes"], "Tonnes Traded Annually"),
             (C["counterparties"], "Active Counterparties")]
    stats_html = "\n".join(f'''        <div>
          <div class="stat__n">{tbd(v)}</div>
          <div class="stat__l">{l}</div>
        </div>''' for v, l in stats)

    standards = [("MPOB", "Malaysian Palm Oil Board"), ("PORAM", "Palm oil contracts"),
                 ("FOSFA", "Soft oil contracts"), ("MSPO", "Malaysian sustainable palm oil"),
                 ("Incoterms 2020", "Delivery terms")]
    std_html = "\n".join(
        f'        <div class="standard">{n}<small>{d}</small></div>' for n, d in standards)

    write("index.html",
      "PAMAS Global Sdn Bhd | Palm Oil, Soft Oils and Biomass Trading, Malaysia",
      "PAMAS Global Sdn Bhd is a Malaysia based physical commodity trading company "
      "supplying crude and refined palm oil products, soft oils and palm biomass to "
      "refiners, feed producers and energy buyers worldwide.",

      hero("Physical Commodity Trading",
           "Palm Oil, Soft Oils and Biomass, Delivered To Specification",
           "PAMAS Global Sdn Bhd sources from Malaysian and Indonesian mills and refiners "
           "and ships to refiners, feed producers and energy buyers across Asia, the Middle "
           "East, Africa and Europe.",
           "estate-telupid.jpg",
           ("Request a Quote", "contact.html"),
           ("View Our Products", "products.html"))
      + contactbar()

      # Welcome, matching the reference's heritage and philosophy block
      + section(shead("Welcome to PAMAS Global",
                      "A Trading House Built On Origin Knowledge",
                      "Established in " + tbd(C["year_founded"]) + " and headquartered in Malaysia, "
                      "PAMAS Global Sdn Bhd trades the palm oil complex, soft oils and palm biomass "
                      "as a principal, not as a broker.")
        + '''      <div class="split split--wide-l" style="margin-top:1rem">
        <div>
          <h3>Our Philosophy</h3>
          <p>We take title, carry the position and perform on the contract. That distinction
            decides who carries the risk when a market moves or a vessel runs late. When we
            sell you a parcel we have bought it, and our name is on the contract.</p>
          <h3 style="margin-top:1.75rem">Our Mission</h3>
          <p>To be the counterparty our buyers reach for first, by keeping a narrow range we
            genuinely know, quoting specifications we can actually meet, and settling every
            contract exactly as written.</p>
          <div class="btn-row" style="margin-top:1.5rem">
            <a class="btn btn--outline" href="about.html">More About Us</a>
          </div>
        </div>
        <div class="split__media">
          <img src="assets/img/estate-berayung.jpg" alt="Managed oil palm estate in Sabah, Malaysia" loading="lazy">
        </div>
      </div>''')

      # Product grid, mirroring the reference's subsidiary grid
      + section(shead("What We Trade",
                      "Our Product Range",
                      "Eight product lines across the palm complex, soft oils and biomass. "
                      "Every parcel moves on a stated specification and an independent inspection.")
                + cards()
                + '''
      <div class="btn-row" style="justify-content:center; margin-top:2.5rem">
        <a class="btn btn--navy" href="products.html">View Full Specifications</a>
      </div>''', grey=True)

      # Stats band
      + section(f'''      <div class="stats">
{stats_html}
      </div>''', navy=True, label="Company at a glance")

      # Why choose us
      + section(shead("Why Choose Us",
                      "What Stands Behind Every Contract",
                      "Nobody buys a 5,000 tonne parcel on the strength of a testimonial. "
                      "These are the things a counterparty can verify before signing.")
                + f'''      <div class="reasons">
{reason_html}
      </div>''')

      # Standards strip in place of a client logo wall
      + section(shead("Standards We Work To",
                      "Licensed, Inspected and Contracted",
                      "We are not able to publish counterparty names under our confidentiality "
                      "terms. These are the licences and standard contracts our business runs on.")
                + f'''      <div class="standards">
{std_html}
      </div>''', grey=True)

      + ctaband("Tell Us The Specification And The Destination",
                "Send the product, quantity, delivery term and discharge port. We come back "
                "with an offer, a full specification and an indicative laycan.",
                ("Request a Quote", "contact.html"),
                ("How We Work", "process.html")))

    # =======================================================================
    # ABOUT
    # =======================================================================
    write("about.html",
      "About Us | PAMAS Global Sdn Bhd",
      "PAMAS Global Sdn Bhd is a Malaysian incorporated physical commodity trading "
      "company dealing in palm oil products, soft oils and palm biomass.",

      hero("About Us", "A Trading Desk, Not A Middleman",
           "We take title, carry the position and perform on the contract.",
           "estate-pd.jpg", ("Contact The Desk", "contact.html"), small=True)
      + contactbar()

      + section(shead("Who We Are", "Built Around Origin Knowledge", left=True)
        + f'''      <div class="split split--wide-l">
        <div>
          <p>PAMAS Global Sdn Bhd is a Malaysian incorporated physical commodity trading
            company, registered under company number {tbd(C["reg_no"])} and licensed by the
            Malaysian Palm Oil Board to deal in palm products.</p>
          <p>We trade three connected books: the palm complex, soft oils, and palm biomass.
            All three originate within a few hundred kilometres of the same ports, which is
            why one desk can cover them properly rather than spreading thin across unrelated
            markets.</p>
          <p>Malaysia and Indonesia together account for roughly 85% of world palm oil
            production. Sitting in that origin is the whole advantage. We deal with mills
            and refiners in their own market and their own working hours, and we can put a
            surveyor on a tank the same week you ask about it.</p>
        </div>
        <div class="split__media">
          <img src="assets/img/plantation-melaka.jpg" alt="Oil palm plantation in Melaka, Malaysia" loading="lazy">
        </div>
      </div>''')

      + section(shead("How We Operate", "Four Disciplines That Keep Contracts Performing")
        + '''      <div class="reasons">
        <div class="reason"><h3>Sourcing</h3>
          <p>We buy from licensed mills and refiners rather than through layers of
            intermediaries, which keeps traceability intact and the cost stack short.</p></div>
        <div class="reason"><h3>Risk</h3>
          <p>Flat price exposure on palm is managed against FCPO on Bursa Malaysia
            Derivatives. We do not run unhedged length against a forward contract.</p></div>
        <div class="reason"><h3>Credit</h3>
          <p>New counterparties are screened before we contract: company standing, sanctions
            exposure, and a payment instrument that suits the risk on both sides.</p></div>
        <div class="reason"><h3>Execution</h3>
          <p>Whoever prices your cargo follows it through nomination, loading, documents and
            discharge, so nothing is lost in a handover.</p></div>
        <div class="reason"><h3>Documentation</h3>
          <p>Bill of lading, certificate of analysis, certificate of origin, weight and
            quality certificates, and phytosanitary papers where the destination needs them.</p></div>
        <div class="reason"><h3>Settlement</h3>
          <p>Irrevocable letter of credit at sight, confirmed where required. Terms are
            agreed before fixture, not after.</p></div>
      </div>''', grey=True)

      + section(shead("Markets Served", "Where Our Cargoes Discharge", left=True)
        + '''      <div class="split split--top">
        <div>
          <ul class="ticks">
            <li><strong>South Asia.</strong> India, Pakistan and Bangladesh, taking refined
              palm oil and olein for food manufacture.</li>
            <li><strong>East Asia.</strong> China, Japan and South Korea, taking kernel oil,
              palm kernel expeller and palm kernel shell.</li>
          </ul>
        </div>
        <div>
          <ul class="ticks">
            <li><strong>Middle East and Africa.</strong> Olein and stearin into repacking and
              food processing.</li>
            <li><strong>Europe.</strong> Oleochemical and feed buyers, subject to EU
              deforestation due diligence.</li>
          </ul>
        </div>
      </div>''')

      + ctaband("Want Our Company Profile And Trade References?",
                "Standard for new counterparties. We will send our registration documents, "
                "MPOB licence and bank details for verification on request.",
                ("Contact Us", "contact.html")))

    # =======================================================================
    # PRODUCTS
    # =======================================================================
    write("products.html",
      "Products &amp; Specifications | PAMAS Global Sdn Bhd",
      "Full trading specifications for palm oil and fractions, palm kernel products, "
      "soft oils and palm biomass, with packing, load ports and contract terms.",

      hero("Products", "Every Product, On A Published Specification",
           "These are the parameters we contract against. Tighter specifications are "
           "available on request and are confirmed in the firm offer.",
           "ffb-bunch-alt.jpg", ("Request a Firm Offer", "contact.html"), small=True)
      + contactbar()

      + section(shead("Palm Oil &amp; Fractions", "Crude Through To Fractionated Grades",
                      "Traded on PORAM standard contract terms.", left=True)
        + '''      <div class="tablewrap" id="palm">
        <table class="spectable">
          <caption>Indicative trading specifications</caption>
          <thead><tr><th scope="col">Product</th><th scope="col">FFA</th><th scope="col">M&amp;I</th>
            <th scope="col">Iodine Value</th><th scope="col">Melting / Cloud</th><th scope="col">Colour</th></tr></thead>
          <tbody>
            <tr><th scope="row">Crude Palm Oil</th><td>5.0% max</td><td>0.25% max</td><td>50 to 55</td><td>MP 33 to 39 &deg;C</td><td>DOBI 2.3 min</td></tr>
            <tr><th scope="row">RBD Palm Oil</th><td>0.1% max</td><td>0.1% max</td><td>50 to 55</td><td>MP 33 to 39 &deg;C</td><td>3.0 R max</td></tr>
            <tr><th scope="row">RBD Palm Olein</th><td>0.1% max</td><td>0.1% max</td><td>56 min</td><td>CP 10 &deg;C max</td><td>3.0 R max</td></tr>
            <tr><th scope="row">RBD Palm Superolein</th><td>0.1% max</td><td>0.1% max</td><td>60 / 62 / 65</td><td>CP 6 &deg;C max</td><td>3.0 R max</td></tr>
            <tr><th scope="row">RBD Palm Stearin</th><td>0.2% max</td><td>0.15% max</td><td>48 max</td><td>MP 44 to 56 &deg;C</td><td>3.0 R max</td></tr>
          </tbody>
        </table>
      </div>
      <p class="field__hint">FFA as palmitic. Colour on Lovibond 5&frac14; inch cell.
        CP is cloud point, MP is slip melting point.</p>''')

      + section(shead("Kernel Products", "Palm Kernel Oil And Expeller",
                      "Kernel oil runs a very different fatty acid profile to palm oil. It is "
                      "high lauric, and prices against the coconut complex.", left=True)
        + '''      <div class="tablewrap" id="kernel">
        <table class="spectable" style="min-width:520px">
          <caption>Indicative trading specifications</caption>
          <thead><tr><th scope="col">Product</th><th scope="col">Key Parameters</th></tr></thead>
          <tbody>
            <tr><th scope="row">Crude Palm Kernel Oil</th><td>FFA 5.0% max &middot; M&amp;I 0.5% max &middot; IV 16 to 19</td></tr>
            <tr><th scope="row">RBD Palm Kernel Oil</th><td>FFA 0.1% max &middot; M&amp;I 0.1% max &middot; Colour 1.5 R max</td></tr>
            <tr><th scope="row">Palm Kernel Expeller</th><td>Protein 14 to 16% &middot; Oil 6 to 9% &middot; Fibre 18% max &middot; Moisture 10% max</td></tr>
          </tbody>
        </table>
      </div>''', grey=True)

      + section(shead("Soft Oils", "Sunflower, Canola And Soybean",
                      "Traded on FOSFA contract terms into food manufacture, repacking and feed.", left=True)
        + '''      <div class="tablewrap" id="soft">
        <table class="spectable">
          <caption>Indicative trading specifications</caption>
          <thead><tr><th scope="col">Product</th><th scope="col">FFA</th>
            <th scope="col">Moisture &amp; Volatiles</th><th scope="col">Iodine Value</th><th scope="col">Notes</th></tr></thead>
          <tbody>
            <tr><th scope="row">Crude Degummed Soybean Oil</th><td>0.75% max</td><td>0.2% max</td><td>120 to 141</td><td>Phosphorus 200 ppm max</td></tr>
            <tr><th scope="row">RBD Sunflower Oil</th><td>0.1% max</td><td>0.1% max</td><td>118 to 141</td><td>Peroxide 1.0 meq/kg max</td></tr>
            <tr><th scope="row">RBD Canola Oil</th><td>0.1% max</td><td>0.1% max</td><td>110 to 126</td><td>Low erucic acid</td></tr>
          </tbody>
        </table>
      </div>''')

      + section(shead("Biomass &amp; Renewables", "Palm Kernel Shell And Expeller",
                      "Palm kernel shell is one of the densest agricultural residues available "
                      "at scale, which is why Japanese and Korean biomass power plants take it "
                      "in preference to most wood pellets.", left=True)
        + '''      <div class="split split--wide-l" id="biomass">
        <div>
          <ul class="ticks">
            <li><strong>Palm Kernel Shell.</strong> GCV 4,200 to 4,400 kcal/kg as received,
              moisture 15 to 20%, ash 5% max, sulphur 0.1% max, sizing 5 to 25 mm.</li>
            <li><strong>Palm Kernel Expeller.</strong> Compound feed ingredient, shipped in
              bulk or 50 kg bags.</li>
            <li><strong>EFB fibre and pellets.</strong> Available subject to enquiry.</li>
          </ul>
          <p>Radiation, sizing and calorific value certificates are issued at load port where
            the destination requires them.</p>
        </div>
        <div class="split__media">
          <img src="assets/img/mill-sterilizer.jpg" alt="Fresh fruit bunches delivered to a palm oil mill" loading="lazy">
        </div>
      </div>''', grey=True)

      + section(shead("Packing &amp; Shipment", "How It Ships")
        + '''      <div class="reasons">
        <div class="reason"><h3>Packing</h3><p>Bulk vessel parcels, ISO tanks of 24 to 26 MT,
          flexitanks of 24 MT, new steel drums at 185 kg net, jerrycans and PET for retail
          ready volumes, and jumbo bags for biomass.</p></div>
        <div class="reason"><h3>Load Ports</h3><p>Port Klang (Westport and Northport), Pasir
          Gudang, Lahad Datu, Sandakan and Bintulu. Indonesian origin ports including Belawan
          and Dumai subject to enquiry.</p></div>
        <div class="reason"><h3>Delivery Terms</h3><p>FOB, CFR and CIF as standard, FCA for
          container shipments, under Incoterms 2020.</p></div>
        <div class="reason"><h3>Inspection</h3><p>Quality and quantity final at load port per
          an independent surveyor: SGS, Intertek, AmSpec, Bureau Veritas, or a surveyor you
          nominate.</p></div>
        <div class="reason"><h3>Payment</h3><p>Irrevocable letter of credit at sight, confirmed
          where required. Documents against payment and telegraphic transfer considered for
          established counterparties.</p></div>
        <div class="reason"><h3>Documents</h3><p>Bill of lading, certificate of analysis,
          certificate of origin, weight and quality certificates, and phytosanitary or
          fumigation certificates where required.</p></div>
      </div>''')

      + ctaband("Need A Tighter Specification?",
                "Most parameters above can be tightened. Tell us what your process needs and "
                "we will confirm what origin can actually deliver, including when it cannot.",
                ("Request a Firm Offer", "contact.html")))

    # =======================================================================
    # PROCESS
    # =======================================================================
    steps = [
      ("Enquiry And Indication",
       "You send product, quantity, delivery term and discharge port. We respond with an "
       "indicative price and the specification we can meet at that level.",
       "<b>You provide</b><br>Product, quantity, incoterm, discharge port, target laycan"),
      ("Firm Offer",
       "A firm offer states price, full specification, quantity tolerance, packing, load "
       "port, laycan, payment terms and validity, open for a stated period.",
       "<b>We provide</b><br>Price, full spec, tolerance, laycan, payment terms, validity"),
      ("Contract",
       "On acceptance we issue a sale contract incorporating PORAM standard terms for palm "
       "products or FOSFA terms for soft oils. Both parties sign before anything is nominated.",
       "<b>Governed by</b><br>PORAM standard contract, FOSFA, Incoterms 2020"),
      ("Payment Instrument",
       "The letter of credit is opened and checked against the contract before we nominate "
       "a vessel. We review the draft text before it is issued.",
       "<b>Typical</b><br>Irrevocable L/C at sight, confirmed where required"),
      ("Nomination And Loading",
       "Vessel or container nomination goes out against the agreed laycan. An independent "
       "surveyor draws samples and determines quality and quantity at the load port.",
       "<b>Surveyors</b><br>SGS, Intertek, AmSpec, Bureau Veritas, or your nomination"),
      ("Documents",
       "The full set is presented against the credit, including any phytosanitary, "
       "fumigation or radiation certificates the destination requires.",
       "<b>Set includes</b><br>B/L, COA, C/O, weight and quality certificates"),
      ("Discharge And Follow Up",
       "We track the vessel to discharge and stay reachable after it. A disputed analysis "
       "is dealt with under the contract's arbitration terms.",
       "<b>After shipment</b><br>Vessel tracking, discharge support, claims under PORAM"),
    ]
    steps_html = "\n".join(f'''        <li class="step">
          <div class="step__n"></div>
          <h3>{t}</h3>
          <p>{b}</p>
          <div class="step__meta">{m}</div>
        </li>''' for t, b, m in steps)

    write("process.html",
      "How We Work | PAMAS Global Sdn Bhd",
      "The seven stages of a physical commodity shipment with PAMAS Global, from "
      "enquiry and firm offer through contract, loading, documents and discharge.",

      hero("How We Work", "From Enquiry To Discharge In Seven Stages",
           "Physical trade goes wrong in predictable places. This is the sequence we run, "
           "and what has to be true before each stage starts.",
           "mill-interior.jpg", ("Start An Enquiry", "contact.html"), small=True)
      + contactbar()
      + section(shead("Our Process", "Every Stage, Documented")
                + f'''      <ol class="steps">
{steps_html}
      </ol>''')
      + section(shead("Before You Enquire", "A Good Enquiry Gets A Fast Offer",
                      "The more of this we have up front, the tighter the price we can hold.", left=True)
        + '''      <ul class="ticks cols2">
        <li>Exact product, and any specification your process requires</li>
        <li>Quantity, and whether it is a single parcel or a programme</li>
        <li>Delivery term and discharge port</li>
        <li>Target laycan or delivery window</li>
        <li>Packing preference: bulk, flexitank, ISO tank or drums</li>
        <li>Payment instrument you can open, and the issuing bank</li>
      </ul>''', grey=True)
      + ctaband("Ready To Start?",
                "Send us the details above and we will come back with an indication the "
                "same Malaysian working day.",
                ("Start An Enquiry", "contact.html")))

    # =======================================================================
    # SUSTAINABILITY
    # =======================================================================
    write("sustainability.html",
      "Sustainability &amp; Traceability | PAMAS Global Sdn Bhd",
      "Certification, traceability and deforestation due diligence in the palm supply "
      "chain: MSPO, RSPO and EUDR readiness.",

      hero("Sustainability", "Traceability You Can Evidence",
           "Palm oil carries a real and well documented environmental history. The useful "
           "response is knowing which mill a parcel came from and being able to prove it.",
           "plantation-melaka.jpg", ("Talk To The Desk", "contact.html"), small=True)
      + contactbar()

      + section(shead("Certification", "What The Certificates Actually Mean", left=True)
        + f'''      <div class="split split--wide-l split--top">
        <div>
          <p>Two schemes matter for Malaysian palm and they do different jobs. Buyers
            frequently conflate them, so it is worth being precise.</p>
          <p><strong>MSPO</strong>, Malaysian Sustainable Palm Oil, is the national scheme and
            is mandatory for Malaysian producers and mills. It covers legal land title, labour
            standards and environmental management. Practically all Malaysian origin palm we
            handle sits within an MSPO certified chain.</p>
          <p><strong>RSPO</strong> is voluntary and international, and is generally what
            European and multinational buyers mean when they ask for certified palm. It runs
            several supply chain models, Identity Preserved, Segregated, Mass Balance and Book
            and Claim, and they are not interchangeable. If your specification requires a
            particular model, say so at enquiry stage, because it materially affects both
            price and which mills can supply.</p>
        </div>
        <div class="panel">
          <h3>To Confirm Before Publication</h3>
          <p><strong>RSPO membership:</strong><br>{tbd("[Membership no., or 'not currently a member']")}</p>
          <p><strong>Supply chain certification:</strong><br>{tbd("[Model held, or 'not held']")}</p>
        </div>
      </div>''')

      + section(shead("Regulatory", "Deforestation Due Diligence For EU Bound Cargo",
                      "The EU Deforestation Regulation places the compliance burden on the "
                      "operator placing goods on the EU market, but that operator can only "
                      "comply if origin supplies the data.")
        + '''      <div class="reasons">
        <div class="reason"><h3>Geolocation Data</h3><p>Coordinates for the plots of
          production, collected through the mill, at the granularity the regulation requires.</p></div>
        <div class="reason"><h3>Traceability To Mill</h3><p>Parcel traced to the supplying
          mill, with the mill's own sourcing declaration behind it.</p></div>
        <div class="reason"><h3>Evidence Of Legality</h3><p>Land title, operating licences and
          MSPO certification evidencing production under Malaysian law.</p></div>
      </div>
      <p class="field__hint" style="margin-top:1.5rem">EUDR obligations and their application
        dates have been amended more than once. Confirm the requirements applicable to your
        shipment with your own compliance function. We supply origin data, we do not give
        legal advice.</p>''', grey=True)

      + section(shead("Our Position", "Where We Stand", left=True)
        + '''      <div class="split split--wide-l split--top">
        <div>
          <p>Palm is the highest yielding oil crop by a wide margin, several times the oil per
            hectare of soy, sunflower or rapeseed. Displacing it does not remove the demand for
            vegetable oil, it moves that demand to crops that need more land for the same
            volume. The serious question is not whether palm should exist, but whether a given
            parcel came from land that was cleared for it. That question is answerable, and
            answering it is the job.</p>
        </div>
        <div>
          <ul class="ticks">
            <li>We buy from licensed mills that can identify their supply base</li>
            <li>We pass origin documentation through rather than summarising it</li>
            <li>Where a buyer needs a specific certification model, we source against it or
              decline the business</li>
            <li>We do not represent a parcel as certified unless a valid certificate covers it</li>
          </ul>
        </div>
      </div>''')

      + ctaband("Need Certified Supply Or EUDR Documentation?",
                "Tell us the scheme, the supply chain model and the destination at enquiry "
                "stage, and we will tell you what origin can evidence.",
                ("Talk To The Desk", "contact.html")))

    # =======================================================================
    # CONTACT
    # =======================================================================
    write("contact.html",
      "Contact Us | PAMAS Global Sdn Bhd",
      "Send an enquiry to PAMAS Global Sdn Bhd. Include product, quantity, delivery "
      "term and discharge port for a same day indication.",

      hero("Contact Us", "Send Us An Enquiry",
           "Include product, quantity, delivery term and discharge port and we can usually "
           "come back with an indication the same working day.",
           "hero-plantation.jpg", ("Jump To The Form", "#form"), small=True)
      + contactbar()

      + section(f'''      <div class="split split--wide-l split--top" id="form">
        <div>
          <div class="shead shead--left">
            <p class="shead__kicker">Enquiry Form</p>
            <h2>Request A Quote</h2>
            <div class="shead__rule"></div>
          </div>
          <p class="panel" style="margin-bottom:1.75rem">Form endpoint not yet connected:
            {tbd("[FORM ENDPOINT URL]")}. Until it is set, this form will not send.</p>

          <form method="post" action="">
            <div class="pair">
              <div class="field"><label for="name">Your Name <span class="req">*</span></label>
                <input type="text" id="name" name="name" required autocomplete="name"></div>
              <div class="field"><label for="company">Company <span class="req">*</span></label>
                <input type="text" id="company" name="company" required autocomplete="organization"></div>
              <div class="field"><label for="email">Email <span class="req">*</span></label>
                <input type="email" id="email" name="email" required autocomplete="email"></div>
              <div class="field"><label for="phone">Phone</label>
                <input type="tel" id="phone" name="phone" autocomplete="tel"></div>
            </div>
            <div class="field">
              <label for="product">Product <span class="req">*</span></label>
              <select id="product" name="product" required>
                <option value="">Select a product</option>
                <optgroup label="Palm Oil &amp; Fractions">
                  <option>Crude Palm Oil</option><option>RBD Palm Oil</option>
                  <option>RBD Palm Olein</option><option>RBD Palm Superolein</option>
                  <option>RBD Palm Stearin</option>
                </optgroup>
                <optgroup label="Kernel Products">
                  <option>Crude Palm Kernel Oil</option><option>RBD Palm Kernel Oil</option>
                  <option>Palm Kernel Expeller</option>
                </optgroup>
                <optgroup label="Soft Oils">
                  <option>Crude Degummed Soybean Oil</option><option>RBD Sunflower Oil</option>
                  <option>RBD Canola Oil</option>
                </optgroup>
                <optgroup label="Biomass">
                  <option>Palm Kernel Shell</option><option>EFB Fibre or Pellets</option>
                </optgroup>
                <option>Other, described below</option>
              </select>
            </div>
            <div class="pair">
              <div class="field"><label for="quantity">Quantity <span class="req">*</span></label>
                <input type="text" id="quantity" name="quantity" required placeholder="e.g. 5,000 MT">
                <p class="field__hint">Per shipment, or monthly volume for a programme.</p></div>
              <div class="field"><label for="incoterm">Delivery Term <span class="req">*</span></label>
                <select id="incoterm" name="incoterm" required>
                  <option value="">Select</option><option>FOB</option><option>CFR</option>
                  <option>CIF</option><option>FCA</option><option>Not sure yet</option>
                </select></div>
              <div class="field"><label for="port">Discharge Port <span class="req">*</span></label>
                <input type="text" id="port" name="port" required placeholder="e.g. Nhava Sheva"></div>
              <div class="field"><label for="laycan">Target Laycan</label>
                <input type="text" id="laycan" name="laycan" placeholder="e.g. second half October"></div>
            </div>
            <div class="field">
              <label for="message">Specification, Packing And Payment Terms</label>
              <textarea id="message" name="message" placeholder="Any specification your process requires, packing preference, the payment instrument you can open, and any certification you need."></textarea>
            </div>
            <button class="btn btn--navy" type="submit">Send Enquiry</button>
            <p class="field__hint" style="margin-top:1rem">We reply within one Malaysian
              working day. Your details are used to answer this enquiry and are not shared
              with third parties.</p>
          </form>
        </div>

        <div>
          <div class="panel panel--navy">
            <h3>Trading Desk</h3>
            <p>{tbd(C["street"])}<br>{tbd(C["city"])}<br>Malaysia</p>
            <p style="margin-bottom:0">
              <a href="tel:{C["phone_href"]}">{tbd(C["phone"])}</a><br>
              <a href="mailto:{C["email"]}">{tbd(C["email"])}</a>
            </p>
          </div>
          <div class="panel" style="margin-top:1.5rem">
            <h3>Office Hours</h3>
            <p>Monday to Friday, 9:00 to 18:00 Malaysian Standard Time, UTC+8. Outside those
              hours, email reaches the desk fastest.</p>
          </div>
          <div class="panel" style="margin-top:1.5rem">
            <h3>New Counterparty</h3>
            <p>We will send registration documents, MPOB licence, bank details for
              verification and trade references. We will ask you for the equivalent, which
              protects both sides.</p>
          </div>
        </div>
      </div>'''))

    # =======================================================================
    # CREDITS, required by CC BY-SA
    # =======================================================================
    M = g["MANIFEST"]
    rows = "\n".join(
        f'''            <tr><th scope="row">{m["title"]}</th><td>{m["author"]}</td>
              <td>{m["license"]}</td><td><a href="{m["descurl"]}">File page</a></td></tr>'''
        for _, m in sorted(M.items(), key=lambda kv: kv[1]["title"]))

    write("credits.html",
      "Photo Credits &amp; Licences | PAMAS Global Sdn Bhd",
      "Attribution for photographs used on this site, sourced from Wikimedia Commons "
      "under public domain and Creative Commons licences.",
      section(shead("Attribution", "Photo Credits And Licences",
                    "Every photograph on this site comes from Wikimedia Commons and is either "
                    "in the public domain or licensed under Creative Commons.")
        + f'''      <p class="field__hint" style="max-width:80ch; margin-bottom:2rem">Images licensed
        CC BY-SA may be reused, including commercially, provided the author is credited and any
        modified version is shared under the same licence. Public domain and CC0 images carry no
        attribution requirement and are credited here as good practice. Neither Wikimedia Commons
        nor any photographer listed endorses PAMAS Global Sdn Bhd. Images have been resized and
        recompressed for web delivery, with no other modification.</p>
      <div class="tablewrap">
        <table class="spectable">
          <caption>Photographs used on this site</caption>
          <thead><tr><th scope="col">File</th><th scope="col">Author</th>
            <th scope="col">Licence</th><th scope="col">Source</th></tr></thead>
          <tbody>
{rows}
          </tbody>
        </table>
      </div>'''))
