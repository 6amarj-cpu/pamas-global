# -*- coding: utf-8 -*-
"""
Page content for the PAMAS Global site. Run `python3 build.py` to render.

House rules enforced here:
  no em-dashes, no stacked eyebrow labels (the rail carries section identity),
  no three-equal-card rows, no hairline under every table row.
"""


def build(g):
    write, hero, band, imgbreak, tbd = (
        g["write"], g["hero"], g["band"], g["imgbreak"], g["tbd"])
    C = g["COMPANY"]

    # =======================================================================
    # HOME
    # =======================================================================
    ledger_home = '''
          <h2>What we trade</h2>
          <p class="lede">Three connected books. All originate within a few hundred
            kilometres of the same ports, which is why one desk covers them properly
            instead of spreading thin across unrelated markets.</p>

          <div class="tablescroll" style="margin-top:2rem">
            <table class="ledger">
              <thead>
                <tr><th scope="col">Product</th><th scope="col">Key parameters</th>
                    <th scope="col">Packing</th><th scope="col">Terms</th></tr>
              </thead>
              <tbody>
                <tr class="cluster"><th colspan="4" scope="colgroup">Palm oil and fractions</th></tr>
                <tr><th scope="row">RBD Palm Olein</th><td>FFA 0.1% max, IV 56 min, CP 10 &deg;C max</td><td>Bulk, flexitank, drums</td><td>PORAM</td></tr>
                <tr><th scope="row">RBD Palm Oil</th><td>FFA 0.1% max, IV 50 to 55, MP 33 to 39 &deg;C</td><td>Bulk, flexitank</td><td>PORAM</td></tr>
                <tr><th scope="row">RBD Palm Stearin</th><td>FFA 0.2% max, IV 48 max, MP 44 to 56 &deg;C</td><td>Bulk, drums</td><td>PORAM</td></tr>
                <tr><th scope="row">Crude Palm Oil</th><td>FFA 5.0% max, M&amp;I 0.25% max, DOBI 2.3 min</td><td>Bulk vessel</td><td>PORAM</td></tr>

                <tr class="cluster"><th colspan="4" scope="colgroup">Soft oils</th></tr>
                <tr><th scope="row">RBD Sunflower Oil</th><td>FFA 0.1% max, PV 1.0 meq/kg max</td><td>Flexitank, ISO tank</td><td>FOSFA</td></tr>
                <tr><th scope="row">Crude Degummed Soybean Oil</th><td>FFA 0.75% max, phosphorus 200 ppm max</td><td>Bulk vessel</td><td>FOSFA</td></tr>
                <tr><th scope="row">RBD Canola Oil</th><td>FFA 0.1% max, IV 110 to 126, low erucic</td><td>Flexitank, drums</td><td>FOSFA</td></tr>

                <tr class="cluster"><th colspan="4" scope="colgroup">Palm biomass</th></tr>
                <tr><th scope="row">Palm Kernel Shell</th><td>GCV 4,200 kcal/kg, moisture 15% max, sulphur 0.1% max</td><td>Bulk, jumbo bags</td><td>By contract</td></tr>
                <tr><th scope="row">Palm Kernel Expeller</th><td>Protein 14 to 16%, oil 6 to 9%, fibre 18% max</td><td>Bulk, 50 kg bags</td><td>By contract</td></tr>
              </tbody>
            </table>
          </div>
          <p class="note" style="margin-top:1rem">Indicative trading specifications.
            Tighter parameters are available on request and are confirmed in the firm offer.</p>
          <div class="btn-row" style="margin-top:1.5rem">
            <a class="btn btn--line" href="products.html">Full specifications</a>
          </div>'''

    credibility = '''
          <div class="statement">
            <div>
              <h2>Trust here is a document, not a promise.</h2>
              <p class="lede">Nobody buys a 5,000 tonne parcel on the strength of a
                testimonial. They buy on specification, inspection, contract, and whether
                the counterparty can actually perform.</p>
            </div>
            <dl class="deflist">
              <div>
                <dt>Quality</dt>
                <dd><b>Independent inspection at load port</b>
                    Quality and quantity determined by SGS, Intertek, or a surveyor you
                    nominate. Certificate of analysis issued before the cargo sails.</dd>
              </div>
              <div>
                <dt>Contract</dt>
                <dd><b>PORAM and FOSFA standard terms</b>
                    Palm on PORAM, soft oils on FOSFA, arbitration clauses left intact so
                    a dispute has a defined venue.</dd>
              </div>
              <div>
                <dt>Licensing</dt>
                <dd><b>Licensed by the Malaysian Palm Oil Board</b>
                    Licence no. ''' + tbd(C["mpob_licence"]) + ''', verifiable on the public MPOB register.</dd>
              </div>
              <div>
                <dt>Settlement</dt>
                <dd><b>Documentary credit</b>
                    Irrevocable L/C at sight, confirmed where required. Payment terms are
                    agreed before fixture, not after.</dd>
              </div>
            </dl>
          </div>'''

    origin = '''
          <div class="wideprose">
            <h2>Close to the mill, close to the port.</h2>
            <p>Malaysia and Indonesia together account for roughly 85% of world palm oil
              production. Sitting in that origin is the whole advantage. We deal with mills
              and refiners in their own market and their own working hours, and we can put a
              surveyor on a tank the same week you ask about it.</p>
          </div>
          <ul class="marks cols2">
            <li>Supply relationships across Peninsular Malaysia, Sabah and Sarawak</li>
            <li>Loading at Port Klang, Pasir Gudang, Lahad Datu, Sandakan and Bintulu</li>
            <li>Bulk parcels, ISO tanks, flexitanks, drums and jumbo bags</li>
            <li>Consolidated documents: B/L, COA, certificate of origin, phytosanitary where required</li>
            <li>Parcel sizes from a single 24 MT flexitank to 12,500 MT vessel lots</li>
            <li>Same time zone as the mills, so questions are answered the same day</li>
          </ul>
          <div class="btn-row" style="margin-top:2rem">
            <a class="btn btn--line" href="process.html">How a shipment works</a>
          </div>'''

    cta = '''
          <div class="panel panel--dark">
            <div class="ctarow">
              <div>
                <h2 style="margin-bottom:.6rem">Tell us the specification and the destination.</h2>
                <p style="margin:0">Send the product, quantity, delivery term and discharge
                  port. We come back with an offer, a full specification and an indicative laycan.</p>
              </div>
              <div class="btn-row">
                <a class="btn btn--primary" href="contact.html">Request a quote</a>
                <a class="btn btn--ondark" href="mailto:''' + C["email"] + '''">Email the desk</a>
              </div>
            </div>
          </div>'''

    write("index.html",
      "PAMAS Global Sdn Bhd, physical trade in palm oil, soft oils and biomass",
      "Malaysia-based physical commodity trader supplying crude and refined palm oil "
      "products, soft oils and palm biomass to refiners, feed producers and energy "
      "buyers worldwide.",
      hero(
        "Palm oil, soft oils and biomass, delivered against specification.",
        "We source from Malaysian and Indonesian mills and ship to refiners, feed "
        "producers and energy buyers worldwide.",
        "estate-telupid.jpg",
        ("Request a quote", "contact.html"),
        ("See specifications", "products.html"),
        terms=[("Contract", "PORAM / FOSFA"),
               ("Incoterms", "FOB, CFR, CIF"),
               ("Load ports", "Klang, P. Gudang"),
               ("Inspection", "SGS, Intertek"),
               ("Parcel", "24 to 12,500 MT")])
      + band(ledger_home, rail=("Book", "Palm, soft oils,<br>biomass"), flush=True)
      + band(credibility, rail=("Standing", "What backs<br>the contract"))
      + imgbreak("harvest-cutter.jpg",
                 "Every parcel starts at a mill we can name and a surveyor you can nominate.")
      + band(origin, rail=("Origin", "Malaysia and<br>Indonesia"), flush=True)
      + band(cta))

    # =======================================================================
    # ABOUT
    # =======================================================================
    who = '''
          <div class="statement">
            <div>
              <h2>A trading desk, not a middleman.</h2>
              <p>PAMAS Global Sdn Bhd is a Malaysian-incorporated physical commodity
                trading company, registered under company number ''' + tbd(C["reg_no"]) + '''
                and licensed by the Malaysian Palm Oil Board to deal in palm products.</p>
              <p>We are a principal, not a broker. When we sell you a parcel we have
                bought it, we carry the price and performance risk on it, and our name is
                on the contract. If a cargo is off specification, that is our problem to
                resolve, not yours to chase upstream.</p>
            </div>
            <figure class="fig">
              <img src="assets/img/estate-berayung.jpg" alt="Managed oil palm estate at Berayung, Sabah" loading="lazy">
            </figure>
          </div>'''

    how = '''
          <h2>Four disciplines that keep contracts performing.</h2>
          <dl class="deflist" style="margin-top:1.5rem">
            <div><dt>Sourcing</dt>
              <dd><b>Direct mill and refinery supply</b>
                  We buy from licensed mills and refiners rather than through layers of
                  intermediaries, which keeps traceability intact and the cost stack short.</dd></div>
            <div><dt>Risk</dt>
              <dd><b>Positions are hedged, not hoped</b>
                  Flat price exposure on palm is managed against FCPO on Bursa Malaysia
                  Derivatives. We do not run unhedged length against a forward contract.</dd></div>
            <div><dt>Credit</dt>
              <dd><b>Counterparty screening</b>
                  New counterparties are screened before we contract: company standing,
                  sanctions exposure, and a payment instrument that suits the risk on both sides.</dd></div>
            <div><dt>Execution</dt>
              <dd><b>One point of contact</b>
                  Whoever prices your cargo follows it through nomination, loading,
                  documents and discharge. Nothing is handed to a department that was not
                  in the conversation.</dd></div>
          </dl>'''

    markets = '''
          <div class="statement">
            <div>
              <h2>Where our cargoes go.</h2>
              <p>Demand for the palm complex is concentrated in South and East Asia.
                Biomass demand sits largely in North Asia, where Palm Kernel Shell is
                co-fired in biomass power plants.</p>
              <p class="note">Countries shipped to: ''' + tbd(C["countries"]) + '''
                &nbsp;&nbsp; Trading since: ''' + tbd(C["year_founded"]) + '''</p>
            </div>
            <dl class="deflist">
              <div><dt>South Asia</dt><dd>India, Pakistan, Bangladesh. Refined palm oil and olein for food manufacture.</dd></div>
              <div><dt>East Asia</dt><dd>China, Japan, South Korea. Kernel oil, PKE and Palm Kernel Shell.</dd></div>
              <div><dt>Middle East</dt><dd>Olein and stearin into repacking and food processing.</dd></div>
              <div><dt>Europe</dt><dd>Oleochemical and feed buyers, subject to EU deforestation due diligence.</dd></div>
            </dl>
          </div>'''

    write("about.html",
      "About PAMAS Global Sdn Bhd, Malaysian physical commodity trader",
      "How PAMAS Global is structured, how it takes positions, and how it manages "
      "counterparty risk in physical palm and soft oil trade.",
      hero("We take title, carry the position, and perform on the contract.",
        "That distinction decides who carries the risk when a market moves or a vessel runs late.",
        "estate-pd.jpg",
        ("Contact the desk", "contact.html"))
      + band(who, rail=("Company", "Who we are"), flush=True)
      + band(how, rail=("Method", "How we<br>operate"))
      + band(markets, rail=("Markets", "Where cargoes<br>discharge")))

    # =======================================================================
    # PRODUCTS
    # =======================================================================
    palm = '''
          <h2 id="palm">Palm oil and fractions</h2>
          <p class="lede">From crude palm oil at the mill gate through to fractionated
            olein and stearin. Traded on PORAM standard contract terms.</p>
          <div class="tablescroll" style="margin-top:1.75rem">
            <table class="ledger">
              <thead>
                <tr><th scope="col">Product</th><th scope="col">FFA</th><th scope="col">M&amp;I</th>
                    <th scope="col">Iodine value</th><th scope="col">Melting / cloud</th><th scope="col">Colour</th></tr>
              </thead>
              <tbody>
                <tr><th scope="row">Crude Palm Oil</th><td>5.0% max</td><td>0.25% max</td><td>50 to 55</td><td>n/a</td><td>DOBI 2.3 min</td></tr>
                <tr><th scope="row">RBD Palm Oil</th><td>0.1% max</td><td>0.1% max</td><td>50 to 55</td><td>MP 33 to 39 &deg;C</td><td>3.0 R max</td></tr>
                <tr><th scope="row">RBD Palm Olein</th><td>0.1% max</td><td>0.1% max</td><td>56 min</td><td>CP 10 &deg;C max</td><td>3.0 R max</td></tr>
                <tr><th scope="row">RBD Palm Superolein</th><td>0.1% max</td><td>0.1% max</td><td>60 / 62 / 65</td><td>CP 6 &deg;C max</td><td>3.0 R max</td></tr>
                <tr><th scope="row">RBD Palm Stearin</th><td>0.2% max</td><td>0.15% max</td><td>48 max</td><td>MP 44 to 56 &deg;C</td><td>3.0 R max</td></tr>
              </tbody>
            </table>
          </div>
          <p class="note" style="margin-top:.9rem">FFA as palmitic. Colour on Lovibond
            5&frac14; inch cell. CP is cloud point, MP is slip melting point.</p>'''

    kernel = '''
          <div class="statement">
            <div>
              <h2 id="kernel">Palm kernel oil and expeller</h2>
              <p>Kernel oil runs a very different fatty acid profile to palm oil. It is
                high lauric, and prices against the coconut complex rather than the palm one.</p>
              <dl class="deflist" style="margin-top:1.25rem">
                <div><dt>CPKO</dt><dd>FFA 5.0% max, M&amp;I 0.5% max, IV 16 to 19</dd></div>
                <div><dt>RBD PKO</dt><dd>FFA 0.1% max, M&amp;I 0.1% max, colour 1.5 R max</dd></div>
                <div><dt>PKE</dt><dd>Protein 14 to 16%, oil 6 to 9%, fibre 18% max, moisture 10% max</dd></div>
              </dl>
            </div>
            <figure class="fig">
              <img src="assets/img/ffb-fruit.jpg" alt="Mature oil palm bearing a fresh fruit bunch" loading="lazy">
            </figure>
          </div>'''

    soft = '''
          <h2 id="soft">Soft oils</h2>
          <p class="lede">Traded on FOSFA contract terms into food manufacture,
            repacking and feed.</p>
          <div class="tablescroll" style="margin-top:1.75rem">
            <table class="ledger">
              <thead>
                <tr><th scope="col">Product</th><th scope="col">FFA</th>
                    <th scope="col">Moisture and volatiles</th><th scope="col">Iodine value</th>
                    <th scope="col">Notes</th></tr>
              </thead>
              <tbody>
                <tr><th scope="row">Crude Degummed Soybean Oil</th><td>0.75% max</td><td>0.2% max</td><td>120 to 141</td><td>Phosphorus 200 ppm max</td></tr>
                <tr><th scope="row">RBD Sunflower Oil</th><td>0.1% max</td><td>0.1% max</td><td>118 to 141</td><td>Peroxide 1.0 meq/kg max</td></tr>
                <tr><th scope="row">RBD Canola Oil</th><td>0.1% max</td><td>0.1% max</td><td>110 to 126</td><td>Low erucic acid</td></tr>
              </tbody>
            </table>
          </div>'''

    biomass = '''
          <div class="statement">
            <div>
              <h2 id="biomass">Palm biomass</h2>
              <p>Palm Kernel Shell is one of the densest agricultural residues available
                at scale, which is why Japanese and Korean biomass power plants take it in
                preference to most wood pellets.</p>
              <ul class="marks">
                <li><strong>Palm Kernel Shell.</strong> GCV 4,200 to 4,400 kcal/kg as received,
                    moisture 15 to 20%, ash 5% max, sulphur 0.1% max, sizing 5 to 25 mm</li>
                <li><strong>Palm Kernel Expeller.</strong> Compound feed ingredient, bulk or 50 kg bags</li>
                <li><strong>EFB fibre and pellets.</strong> Available subject to enquiry</li>
              </ul>
              <p class="note">Radiation, sizing and calorific value certificates issued at
                load port where the destination requires them.</p>
            </div>
            <figure class="fig">
              <img src="assets/img/mill-sterilizer.jpg" alt="Fresh fruit bunches delivered by truck to a palm oil mill" loading="lazy">
            </figure>
          </div>'''

    shipping = '''
          <h2>How it ships</h2>
          <dl class="deflist" style="margin-top:1.5rem">
            <div><dt>Packing</dt><dd>Bulk vessel parcels, ISO tanks of 24 to 26 MT, flexitanks of 24 MT, new steel drums at 185 kg net, jerrycans and PET for retail-ready volumes, jumbo bags for biomass.</dd></div>
            <div><dt>Load ports</dt><dd>Port Klang (Westport and Northport), Pasir Gudang, Lahad Datu, Sandakan, Bintulu. Indonesian origin ports including Belawan and Dumai subject to enquiry.</dd></div>
            <div><dt>Terms</dt><dd>FOB, CFR and CIF as standard, FCA for container shipments. Incoterms 2020.</dd></div>
            <div><dt>Inspection</dt><dd>Quality and quantity final at load port per an independent surveyor: SGS, Intertek, AmSpec, Bureau Veritas, or a surveyor you nominate.</dd></div>
            <div><dt>Payment</dt><dd>Irrevocable L/C at sight, confirmed where required. D/P and telegraphic transfer considered for established counterparties.</dd></div>
            <div><dt>Documents</dt><dd>Bill of lading, certificate of analysis, certificate of origin, weight and quality certificates, phytosanitary and fumigation certificates where the destination requires them.</dd></div>
          </dl>'''

    write("products.html",
      "Products and specifications, PAMAS Global Sdn Bhd",
      "Full trading specifications for palm oil and fractions, palm kernel products, "
      "soft oils and palm biomass, with packing, load ports and contract terms.",
      hero("Every product, on a published specification.",
        "These are the parameters we contract against. Nothing here is vague, and "
        "nothing changes after you have signed.",
        "ffb-bunch-alt.jpg",
        ("Request a firm offer", "contact.html"))
      + band(palm, rail=("01", "Palm oil and<br>fractions"), flush=True)
      + band(kernel, rail=("02", "Kernel<br>products"))
      + band(soft, rail=("03", "Soft oils"))
      + band(biomass, rail=("04", "Biomass and<br>renewables"))
      + band(shipping, rail=("Terms", "Packing and<br>shipment")))

    # =======================================================================
    # PROCESS
    # =======================================================================
    steps = [
      ("Enquiry and indication",
       "You send product, quantity, delivery term and discharge port. We respond with "
       "an indicative price and the specification we can meet at that level. Indications "
       "are subject to change. They start a conversation, they are not an offer.",
       "<b>You provide</b><br>Product, quantity, incoterm, discharge port, target laycan"),
      ("Firm offer",
       "A firm offer states price, full specification, quantity tolerance, packing, load "
       "port, laycan, payment terms and validity. It is open for a stated period, usually "
       "the same working day, because the underlying market moves.",
       "<b>We provide</b><br>Price, full spec, tolerance, laycan, payment terms, validity"),
      ("Contract",
       "On acceptance we issue a sale contract incorporating PORAM standard terms for "
       "palm products or FOSFA terms for soft oils. Both parties sign before anything is "
       "nominated, and the arbitration clause stays in.",
       "<b>Governed by</b><br>PORAM standard contract, FOSFA, Incoterms 2020"),
      ("Payment instrument",
       "The letter of credit is opened and checked against the contract before we "
       "nominate a vessel. Discrepancies between an L/C and a contract are the single "
       "most common cause of delayed shipment, so we review the draft text before issue.",
       "<b>Typical</b><br>Irrevocable L/C at sight, confirmed where required, D/P by agreement"),
      ("Nomination and loading",
       "Vessel or container nomination goes out against the agreed laycan. An independent "
       "surveyor draws samples and determines quality and quantity at the load port. The "
       "certificate of analysis is issued before the cargo sails.",
       "<b>Surveyors</b><br>SGS, Intertek, AmSpec, Bureau Veritas, or your nomination"),
      ("Documents",
       "The full set is presented against the credit: bill of lading, certificate of "
       "analysis, certificate of origin, weight and quality certificates, and any "
       "phytosanitary, fumigation or radiation certificates the destination requires.",
       "<b>Set includes</b><br>B/L, COA, C/O, weight and quality, phyto and fumigation as required"),
      ("Discharge and follow-up",
       "We track the vessel to discharge and stay reachable after it. If a discharge-port "
       "analysis disagrees with the load-port certificate, that is dealt with under the "
       "contract's arbitration terms, which is exactly why we leave them in.",
       "<b>After shipment</b><br>Vessel tracking, discharge support, claims under PORAM and FOSFA"),
    ]
    seq = "\n".join(f'''            <li>
              <div class="seq__n"></div>
              <div><h3>{t}</h3><p>{b}</p></div>
              <div class="seq__meta">{m}</div>
            </li>''' for t, b, m in steps)

    asks = '''
          <div class="statement">
            <div>
              <h2>A good enquiry gets a fast offer.</h2>
              <p>The more of this we have up front, the tighter the price we can hold.</p>
              <div class="btn-row"><a class="btn btn--primary" href="contact.html">Start an enquiry</a></div>
            </div>
            <ul class="marks">
              <li>Exact product, and any specification your process requires</li>
              <li>Quantity, and whether it is a single parcel or a programme</li>
              <li>Delivery term and discharge port</li>
              <li>Target laycan or delivery window</li>
              <li>Packing preference: bulk, flexitank, ISO tank or drums</li>
              <li>Payment instrument you can open, and the issuing bank</li>
            </ul>
          </div>'''

    write("process.html",
      "How we work, enquiry to discharge, PAMAS Global Sdn Bhd",
      "The seven steps of a physical commodity shipment with PAMAS Global: enquiry, "
      "firm offer, contract, payment instrument, nomination and loading, documents, discharge.",
      hero("From enquiry to discharge, in seven steps.",
        "Physical trade goes wrong in predictable places. This is the sequence we run, "
        "and what has to be true before each stage starts.",
        "mill-interior.jpg",
        ("Start an enquiry", "contact.html"))
      + f'''
  <section class="band band--flush">
    <div class="wrap band__inner">
      <ol class="seq">
{seq}
      </ol>
    </div>
  </section>
'''
      + band(asks, rail=("Enquiry", "What we<br>ask of you")))

    # =======================================================================
    # SUSTAINABILITY
    # =======================================================================
    certs = '''
          <div class="statement">
            <div>
              <h2>What the certificates actually mean.</h2>
              <p>Two schemes matter for Malaysian palm and they do different jobs.
                Buyers frequently conflate them, so it is worth being precise.</p>
              <p><strong>MSPO</strong> (Malaysian Sustainable Palm Oil) is the national
                scheme and is mandatory for Malaysian producers and mills. It covers legal
                land title, labour standards and environmental management. Practically all
                Malaysian-origin palm we handle sits within an MSPO-certified chain.</p>
              <p><strong>RSPO</strong> is voluntary, international, and generally what
                European and multinational buyers mean when they ask for certified palm. It
                runs several supply chain models, Identity Preserved, Segregated, Mass
                Balance and Book and Claim, and they are not interchangeable. If your
                specification requires a particular model, say so at enquiry stage. It
                materially affects both price and which mills can supply.</p>
            </div>
            <div class="panel">
              <p class="note" style="margin:0 0 .75rem"><b>To confirm before publication</b></p>
              <dl class="deflist" style="margin:0">
                <div style="border-top:0"><dt>RSPO</dt><dd>''' + tbd("[Membership no., or 'not currently a member']") + '''</dd></div>
                <div><dt>Chain</dt><dd>''' + tbd("[Supply chain certification held, or 'not held']") + '''</dd></div>
              </dl>
            </div>
          </div>'''

    eudr = '''
          <h2>Deforestation due diligence for EU-bound cargo.</h2>
          <p class="lede">The EU Deforestation Regulation places the compliance burden on
            the operator placing goods on the EU market, but that operator can only comply
            if origin supplies the data.</p>
          <dl class="deflist" style="margin-top:1.5rem">
            <div><dt>Geolocation</dt><dd><b>Plot-level coordinates</b>
              Geolocation data for the plots of production, collected through the mill,
              at the granularity the regulation requires.</dd></div>
            <div><dt>Chain</dt><dd><b>Traceability to mill</b>
              Parcel traced to the supplying mill, with the mill's own sourcing
              declaration behind it.</dd></div>
            <div><dt>Legality</dt><dd><b>Legal production evidence</b>
              Land title, operating licences and MSPO certification evidencing production
              under Malaysian law.</dd></div>
          </dl>
          <p class="note" style="margin-top:1.25rem; max-width:76ch">EUDR obligations and
            their application dates have been amended more than once. Confirm the
            requirements applicable to your shipment with your own compliance function.
            We supply origin data, we do not give legal advice.</p>'''

    position = '''
          <div class="statement">
            <div>
              <h2>Where we stand.</h2>
              <p>Palm is the highest-yielding oil crop by a wide margin, several times the
                oil per hectare of soy, sunflower or rapeseed. Displacing it does not
                remove the demand for vegetable oil, it moves that demand to crops that
                need more land for the same volume. The serious question is not whether
                palm should exist, but whether a given parcel came from land that was
                cleared for it. That question is answerable, and answering it is the job.</p>
            </div>
            <ul class="marks">
              <li>We buy from licensed mills that can identify their supply base</li>
              <li>We pass origin documentation through to the buyer rather than summarising it</li>
              <li>Where a buyer needs a specific certification model, we source against it or decline the business</li>
              <li>We do not represent a parcel as certified unless a valid certificate covers it</li>
            </ul>
          </div>'''

    write("sustainability.html",
      "Sustainability and traceability, PAMAS Global Sdn Bhd",
      "Certification, traceability and deforestation due diligence in the palm supply "
      "chain: MSPO, RSPO, EUDR readiness, and what can be evidenced for a given parcel.",
      hero("Traceability you can evidence, not adjectives.",
        "The useful response to palm's environmental history is knowing which mill a "
        "parcel came from and being able to prove it to a regulator.",
        "plantation-melaka.jpg",
        ("Talk to the desk", "contact.html"))
      + band(certs, rail=("Schemes", "MSPO and<br>RSPO"), flush=True)
      + band(eudr, rail=("EUDR", "Regulatory<br>evidence"))
      + band(position, rail=("Position", "Where<br>we stand")))

    # =======================================================================
    # CONTACT
    # =======================================================================
    form = '''
          <div class="statement">
            <div>
              <h2>Request a quote</h2>
              <p class="lede">Fields marked <span class="req" style="color:var(--accent)">*</span> are required before we can price. Everything else helps us hold the price tighter.</p>

              <p class="note" style="border-left:2px solid var(--accent); padding-left:.9rem">
                Form endpoint not yet connected: ''' + tbd("[FORM ENDPOINT URL]") + '''<br>
                Until it is set, this form will not send.</p>

              <form method="post" action="" style="margin-top:1.5rem">
                <div class="pair">
                  <div class="field">
                    <label for="name">Your name <span class="req">*</span></label>
                    <input type="text" id="name" name="name" required autocomplete="name">
                  </div>
                  <div class="field">
                    <label for="company">Company <span class="req">*</span></label>
                    <input type="text" id="company" name="company" required autocomplete="organization">
                  </div>
                  <div class="field">
                    <label for="email">Email <span class="req">*</span></label>
                    <input type="email" id="email" name="email" required autocomplete="email">
                  </div>
                  <div class="field">
                    <label for="phone">Phone</label>
                    <input type="tel" id="phone" name="phone" autocomplete="tel">
                  </div>
                </div>

                <div class="field">
                  <label for="product">Product <span class="req">*</span></label>
                  <select id="product" name="product" required>
                    <option value="">Select a product</option>
                    <optgroup label="Palm oil and fractions">
                      <option>Crude Palm Oil</option><option>RBD Palm Oil</option>
                      <option>RBD Palm Olein</option><option>RBD Palm Superolein</option>
                      <option>RBD Palm Stearin</option>
                    </optgroup>
                    <optgroup label="Kernel products">
                      <option>Crude Palm Kernel Oil</option><option>RBD Palm Kernel Oil</option>
                      <option>Palm Kernel Expeller</option>
                    </optgroup>
                    <optgroup label="Soft oils">
                      <option>Crude Degummed Soybean Oil</option><option>RBD Sunflower Oil</option>
                      <option>RBD Canola Oil</option>
                    </optgroup>
                    <optgroup label="Biomass">
                      <option>Palm Kernel Shell</option><option>EFB fibre or pellets</option>
                    </optgroup>
                    <option>Other, described below</option>
                  </select>
                </div>

                <div class="pair">
                  <div class="field">
                    <label for="quantity">Quantity <span class="req">*</span></label>
                    <input type="text" id="quantity" name="quantity" required placeholder="e.g. 5,000 MT">
                    <p class="field__hint">Per shipment, or monthly volume for a programme.</p>
                  </div>
                  <div class="field">
                    <label for="incoterm">Delivery term <span class="req">*</span></label>
                    <select id="incoterm" name="incoterm" required>
                      <option value="">Select</option><option>FOB</option><option>CFR</option>
                      <option>CIF</option><option>FCA</option><option>Not sure yet</option>
                    </select>
                  </div>
                  <div class="field">
                    <label for="port">Discharge port <span class="req">*</span></label>
                    <input type="text" id="port" name="port" required placeholder="e.g. Nhava Sheva">
                  </div>
                  <div class="field">
                    <label for="laycan">Target laycan</label>
                    <input type="text" id="laycan" name="laycan" placeholder="e.g. second half October">
                  </div>
                </div>

                <div class="field">
                  <label for="message">Specification, packing and payment terms</label>
                  <textarea id="message" name="message" placeholder="Any specification your process requires, packing preference, the payment instrument you can open, and any certification you need."></textarea>
                </div>

                <button class="btn btn--primary" type="submit">Send enquiry</button>
                <p class="field__hint" style="margin-top:1rem">We reply within one Malaysian
                  working day. Your details are used to answer this enquiry and are not
                  shared with third parties.</p>
              </form>
            </div>

            <div>
              <div class="panel panel--dark">
                <h3 style="font-family:var(--mono); font-size:.68rem; letter-spacing:.12em; text-transform:uppercase; color:#E0995F; margin-bottom:1rem">Trading desk</h3>
                <p class="mono" style="font-size:.86rem; line-height:1.9; color:#C8D5DB">
                  ''' + tbd(C["street"]) + '''<br>
                  ''' + tbd(C["city"]) + '''<br>Malaysia
                </p>
                <p class="mono" style="font-size:.86rem; line-height:1.9; margin-bottom:0">
                  <a href="tel:''' + C["phone_href"] + '''">''' + tbd(C["phone"]) + '''</a><br>
                  <a href="mailto:''' + C["email"] + '''">''' + tbd(C["email"]) + '''</a>
                </p>
              </div>

              <div class="panel" style="margin-top:1.25rem">
                <h3>Office hours</h3>
                <p style="margin:0; font-size:.93rem; color:var(--ink-soft)">Monday to Friday,
                  9:00 to 18:00 Malaysian Standard Time (UTC+8). Outside those hours, email
                  reaches the desk fastest.</p>
              </div>

              <div class="panel" style="margin-top:1.25rem">
                <h3>New counterparty</h3>
                <p style="margin:0; font-size:.93rem; color:var(--ink-soft)">We will send
                  registration documents, MPOB licence, bank details for verification and
                  trade references. We will ask you for the equivalent. It protects both sides.</p>
              </div>
            </div>
          </div>'''

    write("contact.html",
      "Contact the trading desk, PAMAS Global Sdn Bhd",
      "Send an enquiry to PAMAS Global. Include product, quantity, delivery term and "
      "discharge port for a same-day indication.",
      hero("Send us an enquiry.",
        "Include product, quantity, delivery term and discharge port, and we can usually "
        "come back the same working day.",
        "hero-plantation.jpg",
        ("Jump to the form", "#form"))
      + f'<div id="form"></div>' + band(form, flush=True))

    # =======================================================================
    # CREDITS. Required by CC BY-SA. Consolidating every credit here keeps the
    # attribution obligation met without captioning each image on every page.
    # =======================================================================
    M = g["MANIFEST"]
    rows = "\n".join(
        f'''                <tr>
                  <th scope="row">{m["title"]}</th>
                  <td>{m["author"]}</td>
                  <td>{m["license"]}</td>
                  <td><a href="{m["descurl"]}">File page</a></td>
                </tr>'''
        for _, m in sorted(M.items(), key=lambda kv: kv[1]["title"]))

    credits_body = f'''
          <h1 style="font-size:clamp(1.9rem,3.6vw,2.8rem)">Photo credits and licences</h1>
          <p class="lede">Every photograph on this site comes from Wikimedia Commons and is
            either in the public domain or licensed under Creative Commons. Attribution is
            given below as those licences require.</p>
          <p style="font-size:.94rem; color:var(--ink-soft)">Images licensed CC BY-SA may be
            reused, including commercially, provided the author is credited and any modified
            version is shared under the same licence. Public domain and CC0 images carry no
            attribution requirement and are credited here as good practice. Neither Wikimedia
            Commons nor any photographer listed endorses PAMAS Global Sdn Bhd.</p>
          <div class="tablescroll" style="margin-top:2rem">
            <table class="ledger">
              <thead>
                <tr><th scope="col">File</th><th scope="col">Author</th>
                    <th scope="col">Licence</th><th scope="col">Source</th></tr>
              </thead>
              <tbody>
{rows}
              </tbody>
            </table>
          </div>
          <p class="note" style="margin-top:1.25rem">Images have been resized and
            recompressed for web delivery. No other modifications made.</p>'''

    write("credits.html",
      "Photo credits and licences, PAMAS Global Sdn Bhd",
      "Attribution for photographs used on this site, sourced from Wikimedia Commons "
      "under public domain and Creative Commons licences.",
      band(credits_body, rail=("Notice", "Attribution"), flush=True))
