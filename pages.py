# -*- coding: utf-8 -*-
"""Page content for the PAMAS Global site. Run `python3 build.py` to render."""


def build(g):
    write, hero, figure, credit, tbd = (
        g["write"], g["hero"], g["figure"], g["credit"], g["tbd"])
    C = g["COMPANY"]

    # =======================================================================
    # HOME
    # =======================================================================
    write("index.html",
      "PAMAS Global Sdn Bhd — Physical trade in palm oil, soft oils and biomass",
      "PAMAS Global Sdn Bhd is a Malaysia-based physical commodity trader supplying crude and "
      "refined palm oil products, soft oils and palm biomass to refiners, feed producers and "
      "energy buyers worldwide.",
      hero(
        f'Physical commodity trade &middot; Est. {tbd(C["year_founded"])}',
        "Palm oil, soft oils and biomass, delivered against specification.",
        "We source from Malaysian and Indonesian mills and refiners, and ship to refiners, feed "
        "producers and energy buyers across Asia, the Middle East, Africa and Europe. Every parcel "
        "moves on a stated specification, an independent inspection and a contract you can hold us to.",
        "estate-telupid.jpg", "",
        '<div class="btn-row">\n'
        '        <a class="btn btn--primary" href="contact.html">Request a quote</a>\n'
        '        <a class="btn btn--ghost" href="products.html">See product specifications</a>\n'
        '      </div>')
      + f'''
  <!-- SIGNATURE: the specification strip.
       In physical trade the governing document is the certificate of analysis,
       so the site opens with the parameters a counterparty actually needs. -->
  <section class="specstrip" aria-label="Standard trading parameters">
    <div class="wrap">
      <ul class="specstrip__list">
        <li class="specstrip__item"><span class="specstrip__k">Contract terms</span><span class="specstrip__v">PORAM <em>/</em> FOSFA</span></li>
        <li class="specstrip__item"><span class="specstrip__k">Incoterms 2020</span><span class="specstrip__v">FOB <em>·</em> CFR <em>·</em> CIF</span></li>
        <li class="specstrip__item"><span class="specstrip__k">Load ports</span><span class="specstrip__v">Klang <em>·</em> P. Gudang</span></li>
        <li class="specstrip__item"><span class="specstrip__k">Inspection</span><span class="specstrip__v">SGS <em>·</em> Intertek</span></li>
        <li class="specstrip__item"><span class="specstrip__k">Parcel size</span><span class="specstrip__v">24 &ndash; 12,500 MT</span></li>
      </ul>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <p class="eyebrow">What we trade</p>
      <div class="grid grid--sidebar">
        <div>
          <h2>Three books, one desk.</h2>
          <p class="lede">
            We keep the range deliberately narrow. Palm, soft oils and palm biomass share the same
            origins, the same ports and largely the same buyers &mdash; so the market intelligence,
            surveyor relationships and freight positions we hold in one book work across all three.
          </p>
          <div class="btn-row"><a class="btn btn--primary" href="products.html">Full specification sheet</a></div>
        </div>
        {figure("ffb-bunch-alt.jpg", "Ripe fresh fruit bunch on an oil palm", "Fresh fruit bunches at the point of harvest &mdash; where every parcel starts.<br>" + credit("ffb-bunch-alt"))}
      </div>

      <div class="grid grid--3" style="margin-top: var(--s5)">
        <article class="coa">
          <div class="coa__media"><img src="assets/img/ffb-fruit.jpg" alt="Mature oil palm bearing a fresh fruit bunch" loading="lazy"></div>
          <div class="coa__body">
            <p class="coa__code">Book 01 / Palm complex</p>
            <h3>Palm oil &amp; fractions</h3>
            <p class="coa__desc">CPO, RBD Palm Oil, Olein, Stearin and Superolein &mdash; bulk vessel parcels, flexitank and drums.</p>
            <table class="coa__table">
              <caption>Indicative &mdash; RBD Palm Olein</caption>
              <tbody>
                <tr><th scope="row">FFA (as palmitic)</th><td>0.1% max</td></tr>
                <tr><th scope="row">Moisture &amp; impurities</th><td>0.1% max</td></tr>
                <tr><th scope="row">Iodine value</th><td>56 min</td></tr>
                <tr><th scope="row">Cloud point</th><td>10 &deg;C max</td></tr>
              </tbody>
            </table>
          </div>
        </article>
        <article class="coa">
          <div class="coa__media"><img src="assets/img/mill-interior.jpg" alt="Interior of a working palm oil mill in Tawau, Sabah" loading="lazy"></div>
          <div class="coa__body">
            <p class="coa__code">Book 02 / Soft oils</p>
            <h3>Soft oils</h3>
            <p class="coa__desc">Crude degummed soybean, RBD sunflower and RBD canola, traded on FOSFA terms into food and feed.</p>
            <table class="coa__table">
              <caption>Indicative &mdash; RBD Sunflower Oil</caption>
              <tbody>
                <tr><th scope="row">FFA (as oleic)</th><td>0.1% max</td></tr>
                <tr><th scope="row">Moisture &amp; volatiles</th><td>0.1% max</td></tr>
                <tr><th scope="row">Peroxide value</th><td>1.0 meq/kg max</td></tr>
                <tr><th scope="row">Colour (Lovibond)</th><td>1.5 R max</td></tr>
              </tbody>
            </table>
          </div>
        </article>
        <article class="coa">
          <div class="coa__media"><img src="assets/img/mill-sterilizer.jpg" alt="Fresh fruit bunches delivered by truck to a palm oil mill" loading="lazy"></div>
          <div class="coa__body">
            <p class="coa__code">Book 03 / Biomass</p>
            <h3>Palm biomass</h3>
            <p class="coa__desc">Palm Kernel Shell and Palm Kernel Expeller for co-firing and compound feed, in bulk and jumbo bags.</p>
            <table class="coa__table">
              <caption>Indicative &mdash; Palm Kernel Shell</caption>
              <tbody>
                <tr><th scope="row">Gross calorific value</th><td>4,200 kcal/kg</td></tr>
                <tr><th scope="row">Moisture</th><td>15% max</td></tr>
                <tr><th scope="row">Ash content</th><td>5% max</td></tr>
                <tr><th scope="row">Sulphur</th><td>0.1% max</td></tr>
              </tbody>
            </table>
          </div>
        </article>
      </div>
    </div>
  </section>

  <section class="section section--dark">
    <div class="wrap">
      <p class="eyebrow">Why counterparties clear with us</p>
      <h2 style="max-width: 20ch">Trust in this trade is a document, not a promise.</h2>
      <p class="lede" style="margin-bottom: var(--s4)">
        Nobody buys a 5,000 tonne parcel on the strength of a testimonial. They buy on
        specification, inspection, contract, and the counterparty's ability to actually perform.
        Here is what stands behind every contract we sign.
      </p>
    </div>
    <div class="wrap">
      <ul class="tiles tiles--4">
        <li class="tile"><span class="tile__k">Quality</span><h3>Independent inspection</h3>
          <p>Quality and quantity determined at load port by SGS, Intertek or a surveyor of your nomination. Certificate of analysis issued before shipment.</p></li>
        <li class="tile"><span class="tile__k">Contract</span><h3>PORAM &amp; FOSFA terms</h3>
          <p>Palm contracts on PORAM standard terms; soft oils on FOSFA. Arbitration clauses left intact, so a dispute has a defined venue.</p></li>
        <li class="tile"><span class="tile__k">Licensing</span><h3>MPOB licensed</h3>
          <p>Licensed by the Malaysian Palm Oil Board to deal in palm products. Licence no. {tbd(C["mpob_licence"])}, verifiable on the public MPOB register.</p></li>
        <li class="tile"><span class="tile__k">Settlement</span><h3>Documentary credit</h3>
          <p>L/C at sight, D/P, or confirmed irrevocable credit through a first-class bank. Payment terms are agreed before fixture, not after.</p></li>
      </ul>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="grid grid--sidebar-r">
        {figure("harvest-cutter.jpg", "Harvesting fresh fruit bunches on a Sabah estate", credit("harvest-cutter"))}
        <div>
          <p class="eyebrow">Origin</p>
          <h2>Close to the mill, close to the port.</h2>
          <p>
            Malaysia and Indonesia together account for roughly 85% of world palm oil production.
            Sitting in that origin is the whole advantage: we deal with mills and refiners in their
            own market and their own working hours, and we can put a surveyor on a tank the same
            week you ask a question about it.
          </p>
          <ul class="list-check">
            <li>Supply relationships across Peninsular Malaysia, Sabah and Sarawak</li>
            <li>Loading at Port Klang, Pasir Gudang, Lahad Datu, Sandakan and Bintulu</li>
            <li>Bulk parcels, ISO tanks, flexitanks, drums and jumbo bags</li>
            <li>Consolidated documents: B/L, COA, certificate of origin, phytosanitary where required</li>
          </ul>
          <div class="btn-row"><a class="btn btn--primary" href="process.html">How a shipment works</a></div>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--tight section--dark">
    <div class="wrap">
      <div class="grid grid--sidebar">
        <div>
          <h2>Tell us the specification and the destination.</h2>
          <p class="lede">Send the product, quantity, delivery term and discharge port. We come back
            with an offer, a full specification and an indicative laycan.</p>
        </div>
        <div style="align-self:center">
          <div class="btn-row" style="margin-top:0">
            <a class="btn btn--primary" href="contact.html">Request a quote</a>
            <a class="btn btn--ghost" href="mailto:{C["email"]}">Email the trading desk</a>
          </div>
        </div>
      </div>
    </div>
  </section>
''')

    # =======================================================================
    # ABOUT
    # =======================================================================
    write("about.html",
      "About PAMAS Global Sdn Bhd — Malaysian physical commodity trader",
      "PAMAS Global Sdn Bhd trades palm oil products, soft oils and palm biomass from origin in "
      "Malaysia. How we are structured, how we take positions, and how we manage counterparty risk.",
      hero("About us", "A trading desk, not a middleman.",
        "PAMAS Global takes title, carries the position and performs on the contract. That "
        "distinction matters: it decides who carries the risk when a market moves or a vessel runs late.",
        "estate-berayung.jpg", "")
      + f'''
  <section class="section">
    <div class="wrap">
      <div class="grid grid--sidebar">
        <div>
          <p class="eyebrow">Who we are</p>
          <h2>Built around origin knowledge.</h2>
          <p>
            PAMAS Global Sdn Bhd is a Malaysian-incorporated physical commodity trading company,
            registered under company number {tbd(C["reg_no"])} and licensed by the Malaysian Palm Oil
            Board to deal in palm products.
          </p>
          <p>
            We trade three connected books &mdash; the palm complex, soft oils, and palm biomass.
            All three originate within a few hundred kilometres of the same ports, which is why one
            desk can cover them properly rather than spreading thin across unrelated markets.
          </p>
          <p>
            We are a principal, not a broker. When we sell you a parcel we have bought it, we carry
            the price and performance risk on it, and our name is on the contract. If a cargo is
            off-spec, that is our problem to resolve, not yours to chase upstream.
          </p>
        </div>
        {figure("estate-telupid.jpg", "Established oil palm plantation at Telupid, Sabah, beside forest edge", credit("estate-telupid"))}
      </div>
    </div>
  </section>

  <section class="section section--dark">
    <div class="wrap">
      <p class="eyebrow">How we operate</p>
      <h2 style="max-width:22ch">Four disciplines that keep contracts performing.</h2>
    </div>
    <div class="wrap">
      <ul class="tiles tiles--4">
        <li class="tile"><span class="tile__k">01 / Sourcing</span><h3>Direct mill and refinery supply</h3>
          <p>We buy from licensed mills and refiners rather than through layers of intermediaries, which keeps traceability intact and the cost stack short.</p></li>
        <li class="tile"><span class="tile__k">02 / Risk</span><h3>Positions are hedged, not hoped</h3>
          <p>Flat price exposure on palm is managed against FCPO on Bursa Malaysia Derivatives. We do not run unhedged length against a customer's forward contract.</p></li>
        <li class="tile"><span class="tile__k">03 / Credit</span><h3>Counterparty screening</h3>
          <p>New counterparties are screened before we contract: company standing, sanctions exposure, and a payment instrument that suits the risk on both sides.</p></li>
        <li class="tile"><span class="tile__k">04 / Execution</span><h3>One point of contact</h3>
          <p>The person who prices your cargo also follows it through nomination, loading, documents and discharge. Nothing gets handed to a department that was not in the conversation.</p></li>
      </ul>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="grid grid--sidebar-r">
        {figure("plantation-melaka.jpg", "Oil palm plantation in Melaka, Malaysia", credit("plantation-melaka"))}
        <div>
          <p class="eyebrow">Markets served</p>
          <h2>Where our cargoes go.</h2>
          <p>
            Demand for the palm complex is concentrated in South and East Asia; biomass demand sits
            largely in North Asia, where Palm Kernel Shell is co-fired in biomass power plants.
          </p>
          <ul class="list-check">
            <li><strong>South Asia</strong> &mdash; India, Pakistan, Bangladesh: refined palm oil and olein for food manufacture</li>
            <li><strong>East Asia</strong> &mdash; China, Japan, South Korea: kernel oil, PKE and Palm Kernel Shell</li>
            <li><strong>Middle East &amp; Africa</strong> &mdash; olein and stearin into repacking and food processing</li>
            <li><strong>Europe</strong> &mdash; oleochemical and feed buyers, subject to EU deforestation due diligence</li>
          </ul>
          <p class="mono" style="font-size:.8rem; color:var(--slate)">
            Countries shipped to: {tbd(C["countries"])} &nbsp;·&nbsp; Trading since: {tbd(C["year_founded"])}
          </p>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--tight section--dark">
    <div class="wrap" style="text-align:center">
      <h2>Want our company profile and bank references?</h2>
      <p class="lede" style="margin-inline:auto">Standard for new counterparties. We will send our
        registration documents, MPOB licence and trade references on request.</p>
      <div class="btn-row" style="justify-content:center">
        <a class="btn btn--primary" href="contact.html">Contact the desk</a>
      </div>
    </div>
  </section>
''')

    # =======================================================================
    # PRODUCTS
    # =======================================================================
    write("products.html",
      "Products &amp; specifications — PAMAS Global Sdn Bhd",
      "Full trading specifications for palm oil and fractions, palm kernel products, soft oils and "
      "palm biomass, with packaging, load ports and contract terms.",
      hero("Products &amp; services", "Every product, on a published specification.",
        "These are the parameters we contract against. Tighter specifications are available on "
        "request and will be confirmed in the firm offer &mdash; but nothing here is vague, and "
        "nothing changes after you have signed.",
        "ffb-fruit.jpg", "",
        '<div class="btn-row"><a class="btn btn--primary" href="contact.html">Request a firm offer</a></div>')
      + f'''
  <section class="section" id="palm">
    <div class="wrap">
      <p class="eyebrow">01 / Palm oil &amp; fractions</p>
      <h2>Palm oil and fractions</h2>
      <p class="lede">From crude palm oil at the mill gate through to fractionated olein and
        stearin. Traded on PORAM standard contract terms.</p>
      <div class="tablewrap" style="margin-top:var(--s3)">
        <table class="spectable">
          <caption>Indicative trading specifications &mdash; palm oil complex</caption>
          <thead>
            <tr><th scope="col">Product</th><th scope="col">FFA</th><th scope="col">M&amp;I</th>
                <th scope="col">Iodine value</th><th scope="col">Melting / cloud pt</th><th scope="col">Colour</th></tr>
          </thead>
          <tbody>
            <tr><th scope="row">Crude Palm Oil (CPO)</th><td>5.0% max</td><td>0.25% max</td><td>50&ndash;55</td><td>&mdash;</td><td>DOBI 2.3 min</td></tr>
            <tr><th scope="row">RBD Palm Oil</th><td>0.1% max</td><td>0.1% max</td><td>50&ndash;55</td><td>MP 33&ndash;39 &deg;C</td><td>3.0 R max</td></tr>
            <tr><th scope="row">RBD Palm Olein</th><td>0.1% max</td><td>0.1% max</td><td>56 min</td><td>CP 10 &deg;C max</td><td>3.0 R max</td></tr>
            <tr><th scope="row">RBD Palm Superolein</th><td>0.1% max</td><td>0.1% max</td><td>60 / 62 / 65</td><td>CP 6 &deg;C max</td><td>3.0 R max</td></tr>
            <tr><th scope="row">RBD Palm Stearin</th><td>0.2% max</td><td>0.15% max</td><td>48 max</td><td>MP 44&ndash;56 &deg;C</td><td>3.0 R max</td></tr>
          </tbody>
        </table>
      </div>
      <p class="mono" style="font-size:.78rem;color:var(--slate);margin-top:var(--s2)">
        FFA as palmitic. Colour on Lovibond 5&frac14;&Prime; cell. CP = cloud point, MP = slip melting point.
      </p>
    </div>
  </section>

  <section class="section section--paper2" id="kernel">
    <div class="wrap">
      <div class="grid grid--sidebar">
        <div>
          <p class="eyebrow">02 / Kernel products</p>
          <h2>Palm kernel oil and expeller</h2>
          <p class="lede">Kernel oil runs a very different fatty acid profile to palm oil &mdash;
            high lauric, and priced against the coconut complex rather than the palm one.</p>
          <div class="tablewrap" style="margin-top:var(--s3)">
            <table class="spectable" style="min-width:520px">
              <caption>Indicative &mdash; kernel products</caption>
              <thead><tr><th scope="col">Product</th><th scope="col">Key parameters</th></tr></thead>
              <tbody>
                <tr><th scope="row">Crude Palm Kernel Oil</th><td>FFA 5.0% max &middot; M&amp;I 0.5% max &middot; IV 16&ndash;19</td></tr>
                <tr><th scope="row">RBD Palm Kernel Oil</th><td>FFA 0.1% max &middot; M&amp;I 0.1% max &middot; colour 1.5 R max</td></tr>
                <tr><th scope="row">Palm Kernel Expeller</th><td>Protein 14&ndash;16% &middot; oil 6&ndash;9% &middot; fibre 18% max &middot; moisture 10% max</td></tr>
              </tbody>
            </table>
          </div>
        </div>
        {figure("harvest-cutter.jpg", "Harvesting fresh fruit bunches, the origin of both palm oil and kernel", credit("harvest-cutter"))}
      </div>
    </div>
  </section>

  <section class="section" id="soft">
    <div class="wrap">
      <p class="eyebrow">03 / Soft oils</p>
      <h2>Soft oils</h2>
      <p class="lede">Traded on FOSFA contract terms into food manufacture, repacking and feed.</p>
      <div class="tablewrap" style="margin-top:var(--s3)">
        <table class="spectable">
          <caption>Indicative trading specifications &mdash; soft oils</caption>
          <thead>
            <tr><th scope="col">Product</th><th scope="col">FFA</th><th scope="col">Moisture &amp; volatiles</th>
                <th scope="col">Iodine value</th><th scope="col">Notes</th></tr>
          </thead>
          <tbody>
            <tr><th scope="row">Crude Degummed Soybean Oil</th><td>0.75% max</td><td>0.2% max</td><td>120&ndash;141</td><td>Phosphorus 200 ppm max</td></tr>
            <tr><th scope="row">RBD Sunflower Oil</th><td>0.1% max</td><td>0.1% max</td><td>118&ndash;141</td><td>Peroxide 1.0 meq/kg max</td></tr>
            <tr><th scope="row">RBD Canola / Rapeseed Oil</th><td>0.1% max</td><td>0.1% max</td><td>110&ndash;126</td><td>Low erucic acid</td></tr>
          </tbody>
        </table>
      </div>
    </div>
  </section>

  <section class="section section--dark" id="biomass">
    <div class="wrap">
      <div class="grid grid--sidebar-r">
        {figure("mill-sterilizer.jpg", "Fresh fruit bunches delivered by truck to a palm oil mill", credit("mill-sterilizer"))}
        <div>
          <p class="eyebrow">04 / Biomass &amp; renewables</p>
          <h2>Palm biomass</h2>
          <p class="lede">Palm Kernel Shell is one of the densest agricultural residues available at
            scale, which is why Japanese and Korean biomass power plants take it in preference to
            most wood pellets.</p>
          <ul class="list-check">
            <li><strong>Palm Kernel Shell (PKS)</strong> &mdash; GCV 4,200&ndash;4,400 kcal/kg (ar), moisture 15&ndash;20%, ash 5% max, sulphur 0.1% max, sizing 5&ndash;25 mm</li>
            <li><strong>Palm Kernel Expeller (PKE)</strong> &mdash; compound feed ingredient, bulk or 50 kg bags</li>
            <li><strong>EFB fibre and pellets</strong> &mdash; available subject to enquiry</li>
          </ul>
          <p style="color:#B6C7D0">Shipped in bulk vessel parcels or jumbo bags. Radiation, sizing
            and calorific value certificates issued at load port where the destination requires them.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--paper2">
    <div class="wrap">
      <p class="eyebrow">Packing, shipment &amp; terms</p>
      <h2>How it ships</h2>
      <div class="grid grid--3" style="margin-top:var(--s3)">
        <div class="card"><span class="card__k">Packing</span><h3>Bulk to drums</h3>
          <p>Bulk vessel parcels; ISO tanks (24&ndash;26 MT); flexitanks (24 MT); new steel drums (185 kg net); jerrycans and PET for retail-ready volumes; jumbo bags for biomass.</p></div>
        <div class="card"><span class="card__k">Load ports</span><h3>Malaysia &amp; Indonesia</h3>
          <p>Port Klang (Westport / Northport), Pasir Gudang, Lahad Datu, Sandakan, Bintulu, and Indonesian origin ports including Belawan and Dumai subject to enquiry.</p></div>
        <div class="card"><span class="card__k">Terms</span><h3>Incoterms 2020</h3>
          <p>FOB, CFR and CIF as standard; FCA for container shipments. Contracts on PORAM terms for palm and FOSFA terms for soft oils.</p></div>
        <div class="card"><span class="card__k">Inspection</span><h3>Independent survey</h3>
          <p>Quality and quantity final at load port per an independent surveyor &mdash; SGS, Intertek, AmSpec or Bureau Veritas, or a surveyor you nominate.</p></div>
        <div class="card"><span class="card__k">Payment</span><h3>Documentary credit</h3>
          <p>Irrevocable L/C at sight, confirmed where required; D/P and telegraphic transfer considered for established counterparties.</p></div>
        <div class="card"><span class="card__k">Documents</span><h3>Full document set</h3>
          <p>Bill of lading, certificate of analysis, certificate of origin, weight and quality certificates, phytosanitary and fumigation certificates where the destination requires them.</p></div>
      </div>
    </div>
  </section>

  <section class="section section--tight section--dark">
    <div class="wrap">
      <div class="grid grid--sidebar">
        <div><h2>Need a tighter specification?</h2>
          <p class="lede">Most parameters above can be tightened. Tell us what your process needs
            and we will confirm what origin can actually deliver &mdash; including when it cannot.</p></div>
        <div style="align-self:center"><div class="btn-row" style="margin-top:0">
          <a class="btn btn--primary" href="contact.html">Request a firm offer</a></div></div>
      </div>
    </div>
  </section>
''')

    # =======================================================================
    # PROCESS
    # =======================================================================
    write("process.html",
      "How we work — enquiry to discharge | PAMAS Global Sdn Bhd",
      "The seven steps of a physical commodity shipment with PAMAS Global: enquiry, firm offer, "
      "contract, payment instrument, nomination and loading, documents, and discharge.",
      hero("How we work", "From enquiry to discharge, in seven steps.",
        "Physical trade goes wrong in predictable places: a loose specification, a payment "
        "instrument agreed too late, a nomination that slips. This is the sequence we run, and "
        "what has to be true at each stage before the next one starts.",
        "harvest-cutter.jpg", "")
      + f'''
  <section class="section">
    <div class="wrap">
      <ol class="steps">
        <li class="step">
          <div class="step__n"></div>
          <div><h3>Enquiry and indication</h3>
            <p>You send product, quantity, delivery term and discharge port. We respond with an
              indicative price and the specification we can meet at that level. Indications are
              subject to change &mdash; they are a starting point for a conversation, not an offer.</p></div>
          <div class="step__meta"><div><strong>You provide</strong></div><div>Product &middot; quantity &middot; incoterm &middot; discharge port &middot; target laycan</div></div>
        </li>
        <li class="step">
          <div class="step__n"></div>
          <div><h3>Firm offer</h3>
            <p>A firm offer states price, full specification, quantity tolerance, packing, load port,
              laycan, payment terms and validity. It is open for a stated period, usually the same
              working day, because the underlying market moves.</p></div>
          <div class="step__meta"><div><strong>We provide</strong></div><div>Price &middot; full spec &middot; tolerance &middot; laycan &middot; payment terms &middot; validity</div></div>
        </li>
        <li class="step">
          <div class="step__n"></div>
          <div><h3>Contract</h3>
            <p>On acceptance we issue a sale contract incorporating PORAM standard terms for palm
              products or FOSFA terms for soft oils. Both parties sign before anything is nominated.
              The arbitration clause stays in.</p></div>
          <div class="step__meta"><div><strong>Governed by</strong></div><div>PORAM standard contract &middot; FOSFA &middot; Incoterms 2020</div></div>
        </li>
        <li class="step">
          <div class="step__n"></div>
          <div><h3>Payment instrument</h3>
            <p>The letter of credit is opened and checked against the contract before we nominate a
              vessel. Discrepancies between an L/C and a contract are the single most common cause
              of delayed shipment, so we review the draft text before it is issued.</p></div>
          <div class="step__meta"><div><strong>Typical</strong></div><div>Irrevocable L/C at sight &middot; confirmed where required &middot; D/P by agreement</div></div>
        </li>
        <li class="step">
          <div class="step__n"></div>
          <div><h3>Nomination and loading</h3>
            <p>Vessel or container nomination goes out against the agreed laycan. An independent
              surveyor draws samples and determines quality and quantity at the load port. The
              certificate of analysis is issued before the cargo sails.</p></div>
          <div class="step__meta"><div><strong>Surveyors</strong></div><div>SGS &middot; Intertek &middot; AmSpec &middot; Bureau Veritas &middot; or your nomination</div></div>
        </li>
        <li class="step">
          <div class="step__n"></div>
          <div><h3>Documents</h3>
            <p>The full set is presented against the credit: bill of lading, certificate of analysis,
              certificate of origin, weight and quality certificates, and any phytosanitary,
              fumigation or radiation certificates the destination requires.</p></div>
          <div class="step__meta"><div><strong>Set includes</strong></div><div>B/L &middot; COA &middot; C/O &middot; weight &amp; quality &middot; phyto / fumigation as required</div></div>
        </li>
        <li class="step">
          <div class="step__n"></div>
          <div><h3>Discharge and follow-up</h3>
            <p>We track the vessel to discharge and stay reachable after it. If a discharge-port
              analysis disagrees with the load-port certificate, that is dealt with under the
              contract's arbitration terms &mdash; which is exactly why we leave them in.</p></div>
          <div class="step__meta"><div><strong>After shipment</strong></div><div>Vessel tracking &middot; discharge support &middot; claims under PORAM / FOSFA</div></div>
        </li>
      </ol>
    </div>
  </section>

  <section class="section section--dark">
    <div class="wrap">
      <div class="grid grid--sidebar-r">
        {figure("mill-interior.jpg", "Processing plant and storage tanks at a palm oil mill in Sabah", credit("mill-interior"))}
        <div>
          <p class="eyebrow">What we ask of you</p>
          <h2>A good enquiry gets a fast offer.</h2>
          <p class="lede">The more of this we have up front, the tighter the price we can hold.</p>
          <ul class="list-check">
            <li>Exact product and any specification your process requires</li>
            <li>Quantity and whether it is a single parcel or a programme</li>
            <li>Delivery term and discharge port</li>
            <li>Target laycan or delivery window</li>
            <li>Packing preference &mdash; bulk, flexitank, ISO tank or drums</li>
            <li>Payment instrument you can open, and the issuing bank</li>
          </ul>
          <div class="btn-row"><a class="btn btn--primary" href="contact.html">Start an enquiry</a></div>
        </div>
      </div>
    </div>
  </section>
''')

    # =======================================================================
    # SUSTAINABILITY
    # =======================================================================
    write("sustainability.html",
      "Sustainability and traceability — PAMAS Global Sdn Bhd",
      "Certification, traceability and deforestation due diligence in the palm supply chain: MSPO, "
      "RSPO, EUDR readiness and what PAMAS Global can evidence for a given parcel.",
      hero("Sustainability", "Traceability you can evidence, not adjectives.",
        "Palm oil carries a real and well-documented environmental history. The useful response is "
        "not a statement of values &mdash; it is knowing which mill a parcel came from and being "
        "able to prove it to a regulator.",
        "plantation-melaka.jpg", "")
      + f'''
  <section class="section">
    <div class="wrap">
      <div class="grid grid--sidebar">
        <div>
          <p class="eyebrow">Certification</p>
          <h2>What the certificates actually mean.</h2>
          <p>
            There are two schemes that matter for Malaysian palm, and they do different jobs.
            Buyers frequently conflate them, so it is worth being precise.
          </p>
          <p>
            <strong>MSPO</strong> (Malaysian Sustainable Palm Oil) is the national scheme and is
            mandatory for Malaysian producers and mills. It covers legal land title, labour standards
            and environmental management. Practically all Malaysian-origin palm we handle sits within
            an MSPO-certified chain.
          </p>
          <p>
            <strong>RSPO</strong> (Roundtable on Sustainable Palm Oil) is voluntary, international,
            and generally what European and multinational buyers mean when they ask for "certified"
            palm. It runs several supply chain models &mdash; Identity Preserved, Segregated, Mass
            Balance and Book &amp; Claim &mdash; and they are not interchangeable. If your
            specification requires a particular model, say so at enquiry stage: it materially
            affects both price and which mills can supply.
          </p>
          <p class="mono" style="font-size:.82rem;color:var(--slate);border-left:2px solid var(--carotene);padding-left:1rem">
            PAMAS Global RSPO membership status: {tbd("[CONFIRM — RSPO member no. or 'not currently a member']")}<br>
            Supply chain certification held: {tbd("[CONFIRM — e.g. Mass Balance / not held]")}
          </p>
        </div>
        {figure("estate-berayung.jpg", "Managed oil palm estate at Berayung, Sabah", credit("estate-berayung"))}
      </div>
    </div>
  </section>

  <section class="section section--dark">
    <div class="wrap">
      <p class="eyebrow">Regulatory</p>
      <h2 style="max-width:24ch">Deforestation due diligence for EU-bound cargo.</h2>
      <p class="lede" style="margin-bottom:var(--s4)">
        The EU Deforestation Regulation places the compliance burden on the operator placing goods
        on the EU market &mdash; but that operator can only comply if origin supplies the data.
        For EU-destined parcels we work to provide what the due diligence statement requires.
      </p>
    </div>
    <div class="wrap">
      <ul class="tiles tiles--3">
        <li class="tile"><span class="tile__k">Geolocation</span><h3>Plot-level coordinates</h3>
          <p>Geolocation data for the plots of production, collected through the mill, at the granularity the regulation requires.</p></li>
        <li class="tile"><span class="tile__k">Chain</span><h3>Traceability to mill</h3>
          <p>Parcel traced to the supplying mill, with the mill's own sourcing declaration behind it.</p></li>
        <li class="tile"><span class="tile__k">Legality</span><h3>Legal production evidence</h3>
          <p>Land title, operating licences and MSPO certification evidencing production under Malaysian law.</p></li>
      </ul>
      <p class="mono" style="font-size:.78rem;color:var(--slate-lt);margin-top:var(--s3);max-width:80ch">
        Note: EUDR obligations and their application dates have been amended more than once. Confirm
        the requirements applicable to your shipment with your own compliance function &mdash; we
        supply origin data, we do not give legal advice.
      </p>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="grid grid--sidebar-r">
        {figure("estate-pd.jpg", "Established oil palm plantation in Malaysia", credit("estate-pd"))}
        <div>
          <p class="eyebrow">Position</p>
          <h2>Where we stand.</h2>
          <p>
            Palm is the highest-yielding oil crop by a wide margin &mdash; several times the oil per
            hectare of soy, sunflower or rapeseed. Displacing it does not remove the demand for
            vegetable oil; it moves that demand to crops that need more land for the same volume.
            The serious question is not whether palm should exist but whether a given parcel came
            from land that was cleared for it.
          </p>
          <p>That question is answerable, and answering it is the job.</p>
          <ul class="list-check">
            <li>We buy from licensed mills that can identify their supply base</li>
            <li>We pass origin documentation through to the buyer rather than summarising it</li>
            <li>Where a buyer needs a specific certification model, we source against it or decline the business</li>
            <li>We do not represent a parcel as certified unless a valid certificate covers it</li>
          </ul>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--tight section--dark">
    <div class="wrap" style="text-align:center">
      <h2>Need certified supply or EUDR documentation?</h2>
      <p class="lede" style="margin-inline:auto">Tell us the scheme, the supply chain model and the
        destination at enquiry stage, and we will tell you what origin can evidence.</p>
      <div class="btn-row" style="justify-content:center">
        <a class="btn btn--primary" href="contact.html">Talk to the desk</a></div>
    </div>
  </section>
''')

    # =======================================================================
    # CONTACT
    # =======================================================================
    write("contact.html",
      "Contact the trading desk — PAMAS Global Sdn Bhd",
      "Send an enquiry to PAMAS Global Sdn Bhd. Include product, quantity, delivery term and "
      "discharge port for a same-day indication.",
      hero("Contact", "Send us an enquiry.",
        "Include product, quantity, delivery term and discharge port and we can usually come back "
        "with an indication the same working day.",
        "hero-plantation.jpg", "")
      + f'''
  <section class="section">
    <div class="wrap">
      <div class="grid grid--sidebar">
        <div>
          <p class="eyebrow">Enquiry form</p>
          <h2>Request a quote</h2>
          <p class="lede">Fields marked <span class="req" style="color:var(--carotene)">*</span> are
            needed before we can price. Everything else helps us hold the price tighter.</p>

          <p class="field__hint" style="margin-top:var(--s3)">Form endpoint not yet connected: {tbd("[FORM ENDPOINT URL]")} &mdash; until it is set, the button below will not send.</p>
          <form method="post" action="" style="margin-top:var(--s2)">
            <div class="grid grid--2" style="gap:0 var(--s3)">
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
                <optgroup label="Palm oil &amp; fractions">
                  <option>Crude Palm Oil (CPO)</option>
                  <option>RBD Palm Oil</option>
                  <option>RBD Palm Olein</option>
                  <option>RBD Palm Superolein</option>
                  <option>RBD Palm Stearin</option>
                </optgroup>
                <optgroup label="Kernel products">
                  <option>Crude Palm Kernel Oil</option>
                  <option>RBD Palm Kernel Oil</option>
                  <option>Palm Kernel Expeller (PKE)</option>
                </optgroup>
                <optgroup label="Soft oils">
                  <option>Crude Degummed Soybean Oil</option>
                  <option>RBD Sunflower Oil</option>
                  <option>RBD Canola / Rapeseed Oil</option>
                </optgroup>
                <optgroup label="Biomass">
                  <option>Palm Kernel Shell (PKS)</option>
                  <option>EFB fibre / pellets</option>
                </optgroup>
                <option>Other &mdash; described below</option>
              </select>
            </div>

            <div class="grid grid--2" style="gap:0 var(--s3)">
              <div class="field">
                <label for="quantity">Quantity <span class="req">*</span></label>
                <input type="text" id="quantity" name="quantity" required placeholder="e.g. 5,000 MT">
                <p class="field__hint">Per shipment, or the monthly volume if this is a programme.</p>
              </div>
              <div class="field">
                <label for="incoterm">Delivery term <span class="req">*</span></label>
                <select id="incoterm" name="incoterm" required>
                  <option value="">Select</option>
                  <option>FOB</option><option>CFR</option><option>CIF</option>
                  <option>FCA</option><option>Not sure yet</option>
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
              <textarea id="message" name="message" placeholder="Any specification your process requires, packing preference, the payment instrument you can open, and any certification you need (MSPO, RSPO model, EUDR documentation)."></textarea>
            </div>

            <button class="btn btn--primary" type="submit">Send enquiry</button>
            <p class="field__hint" style="margin-top:var(--s2)">
              We reply to enquiries within one Malaysian working day. Your details are used to
              respond to this enquiry and are not shared with third parties.
            </p>
          </form>
        </div>

        <div>
          <div class="card" style="background:var(--ink);color:#B6C7D0;border-color:var(--rule-dk)">
            <span class="card__k" style="color:var(--carotene-lt)">Trading desk</span>
            <h3 style="color:#fff">PAMAS Global Sdn Bhd</h3>
            <p class="mono" style="font-size:.88rem;color:#B6C7D0;line-height:1.8">
              {tbd(C["street"])}<br>
              {tbd(C["city"])}<br>
              Malaysia
            </p>
            <p class="mono" style="font-size:.88rem;color:#B6C7D0;line-height:1.8;margin-top:1rem">
              T &nbsp;<a href="tel:{C["phone_href"]}" style="color:#fff">{tbd(C["phone"])}</a><br>
              E &nbsp;<a href="mailto:{C["email"]}" style="color:#fff">{tbd(C["email"])}</a>
            </p>
            <p class="mono" style="font-size:.75rem;color:var(--slate-lt);margin-top:1.5rem;border-top:1px solid var(--rule-dk);padding-top:1rem">
              Company no. {tbd(C["reg_no"])}<br>
              MPOB licence {tbd(C["mpob_licence"])}
            </p>
          </div>

          <div class="card" style="margin-top:var(--s3)">
            <span class="card__k">Office hours</span>
            <h3>Malaysian Standard Time</h3>
            <p>Monday to Friday, 9:00 &ndash; 18:00 MYT (UTC+8).<br>
               Outside those hours, email reaches the desk fastest.</p>
          </div>

          <div class="card" style="margin-top:var(--s3)">
            <span class="card__k">New counterparty?</span>
            <h3>What we will send</h3>
            <p>Company registration documents, MPOB licence, bank details for verification and trade
               references. We will ask you for the equivalent &mdash; it protects both sides.</p>
          </div>
        </div>
      </div>
    </div>
  </section>
''')

    # =======================================================================
    # CREDITS  (required by CC BY-SA)
    # =======================================================================
    M = g["MANIFEST"]
    rows = "\n".join(
        f'''            <tr>
              <th scope="row">{m["title"]}</th>
              <td>{m["author"]}</td>
              <td>{m["license"]}</td>
              <td><a href="{m["descurl"]}">File page</a></td>
            </tr>'''
        for _, m in sorted(M.items(), key=lambda kv: kv[1]["title"]))

    write("credits.html",
      "Photo credits and licences — PAMAS Global Sdn Bhd",
      "Attribution for the photographs used on this site, all sourced from Wikimedia Commons under "
      "public domain or Creative Commons licences.",
      f'''
  <section class="section">
    <div class="wrap">
      <p class="eyebrow">Attribution</p>
      <h1 style="font-size:clamp(2rem,4vw,3rem)">Photo credits and licences</h1>
      <p class="lede">
        Every photograph on this site is sourced from Wikimedia Commons and is either in the public
        domain or licensed under a Creative Commons licence. Attribution is given below as those
        licences require.
      </p>
      <p style="font-size:.95rem;color:var(--slate)">
        Images licensed CC BY-SA may be reused, including commercially, provided the author is
        credited and any modified version is shared under the same licence. Public domain and CC0
        images carry no attribution requirement; they are credited here as good practice. Neither
        Wikimedia Commons nor any photographer listed endorses PAMAS Global Sdn Bhd.
      </p>

      <div class="tablewrap" style="margin-top:var(--s4)">
        <table class="spectable">
          <caption>Photographs used on this site</caption>
          <thead>
            <tr><th scope="col">File</th><th scope="col">Author</th>
                <th scope="col">Licence</th><th scope="col">Source</th></tr>
          </thead>
          <tbody>
{rows}
          </tbody>
        </table>
      </div>

      <p class="mono" style="font-size:.78rem;color:var(--slate);margin-top:var(--s3)">
        Images have been resized and recompressed for web delivery. No other modifications made.
      </p>
    </div>
  </section>
''')
