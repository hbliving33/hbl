"""Builds the HBLiving site: index.html (home) and logos.html (logo options, not linked, noindex)."""
import pathlib, math, hashlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
YEAR = 2026

# Palette: deep Pacific, sea glass, warm sand, sunset coral, golden hour
INK, SEA, GLASS, SAND, CORAL, GOLD, FOAM = '#161310', '#138a43', '#9bd8a4', '#f3e4c8', '#d62b1f', '#f8b800', '#fbf7ef'

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,600;9..144,700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">'


def ver(path):
    return hashlib.md5((ROOT / path).read_bytes()).hexdigest()[:8]


# ---------- Hero illustration: golden hour at the pier ----------
def pier_scene():
    pil = ''.join(f'<path d="M{x} 250 V{280 + (x % 3) * 2}"/>' for x in range(560, 1380, 30))
    return f'''<svg class="scene" viewBox="0 0 1440 320" preserveAspectRatio="xMidYMax slice" aria-hidden="true">
  <defs>
    <linearGradient id="dusk" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#14110e"/><stop offset=".55" stop-color="#3a1d12"/><stop offset=".85" stop-color="#b5431f"/><stop offset="1" stop-color="#f08a2c"/></linearGradient>
    <linearGradient id="deep" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1c3b3a"/><stop offset="1" stop-color="#0d1c1c"/></linearGradient>
    <radialGradient id="sunr" r=".5"><stop offset="0" stop-color="#ffe7a1"/><stop offset=".7" stop-color="#f8b800"/><stop offset="1" stop-color="#e88a12"/></radialGradient>
  </defs>
  <rect width="1440" height="320" fill="url(#dusk)"/>
  <circle cx="980" cy="246" r="120" fill="#f8b800" opacity=".10"/>
  <circle cx="980" cy="246" r="54" fill="url(#sunr)"/>
  <rect y="244" width="1440" height="76" fill="url(#deep)"/>
  <path d="M900 256 H1060 M930 268 H1030 M955 280 H1005" stroke="#f8b800" stroke-width="3" stroke-linecap="round" opacity=".55"/>
  <g stroke="#0b0a08" stroke-width="5" stroke-linecap="round">{pil}</g>
  <path d="M540 247 H1390" stroke="#0b0a08" stroke-width="8" stroke-linecap="round"/>
  <path d="M1300 247 V224 H1372 V247Z M1294 225 L1336 208 L1378 225Z" fill="#0b0a08"/>
  <path d="M0 270 C 200 258 360 260 560 282 L 600 320 H0Z" fill="#0f0d0b"/>
  <g fill="none" stroke="#0b0a08" stroke-linecap="round"><path d="M180 286 C 176 240 180 204 194 168" stroke-width="7"/><path d="M262 286 C 266 250 262 224 252 198" stroke-width="6"/></g>
  <g fill="#0b0a08">
    <path d="M194 168 c-22 -10 -48 -4 -60 12 c18 -8 40 -8 60 -6 c-16 -14 -38 -22 -56 -14 c22 0 42 6 56 14 c2 -20 -10 -38 -26 -44 c12 12 22 28 26 40 c12 -18 36 -26 58 -18 c-22 4 -40 12 -52 24 c24 -6 44 2 56 18 c-18 -12 -40 -14 -62 -8z"/>
    <path transform="translate(96.8 63.6) scale(.8)" d="M194 168 c-22 -10 -48 -4 -60 12 c18 -8 40 -8 60 -6 c-16 -14 -38 -22 -56 -14 c22 0 42 6 56 14 c2 -20 -10 -38 -26 -44 c12 12 22 28 26 40 c12 -18 36 -26 58 -18 c-22 4 -40 12 -52 24 c24 -6 44 2 56 18 c-18 -12 -40 -14 -62 -8z"/>
  </g>
</svg>'''


def head(title, desc, extra='', noindex=False):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
{'<meta name="robots" content="noindex">' if noindex else ''}
<meta name="theme-color" content="{INK}">
<link rel="icon" href="assets/img/mark.svg" type="image/svg+xml">
<link rel="manifest" href="manifest.webmanifest">
<link rel="apple-touch-icon" href="assets/img/icon-180.png">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="HBLiving">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
{FONTS}
<link rel="stylesheet" href="assets/css/site.css?v={ver('assets/css/site.css')}">
{extra}
</head>'''



# ---------- Advertiser form ----------
# Leave FORM_TO empty until the address that receives advertiser requests is chosen.
# When it is set, the form posts through FormSubmit and lands on thanks.html.
FORM_TO = ''

NAV = [('#why', 'Why HBLiving'), ('#map', 'Map'), ('#communities', 'Communities'), ('#plans', 'Plans'), ('#how', 'How it works'), ('#categories', 'Categories'), ('#faq', 'Questions')]
CITIES = ['Huntington Beach', 'Fountain Valley', 'Seal Beach', 'Sunset Beach', 'Westminster', 'Costa Mesa', 'Newport Beach']
CATS = [('food', 'Food and drink'), ('tool', 'Home services'), ('wave', 'Surf and outdoor'), ('heart', 'Health and fitness'), ('scissors', 'Beauty and spa'),
        ('paw', 'Pets'), ('home', 'Real estate'), ('car', 'Auto'), ('kids', 'Kids and family'), ('brief', 'Professional services'), ('bag', 'Shops and boutiques'), ('star', 'Events and entertainment')]


def header():
    links = ''.join(f'<a href="{h}">{t}</a>' for h, t in NAV)
    return f'''<header class="top">
  <div class="top-in">
    <a class="brand" href="index.html"><img src="assets/img/mark.svg" alt="" width="40" height="40"><span>HB<em>Living</em></span></a>
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="nav">Menu</button>
    <nav id="nav" class="nav" aria-label="Main">{links}<a class="nav-cta" href="#advertise">Advertise</a></nav>
  </div>
</header>'''


def footer():
    return f'''<footer class="foot">
  <div class="foot-in">
    <div><a class="brand brand-foot" href="index.html"><img src="assets/img/mark.svg" alt="" width="36" height="36"><span>HB<em>Living</em></span></a>
    <p>Local advertising for Huntington Beach businesses and the towns next door.  Independently owned.  Not affiliated with the City of Huntington Beach.</p></div>
    <nav aria-label="Footer">{''.join(f'<a href="{h}">{t}</a>' for h, t in NAV)}<a href="#advertise">Advertise</a></nav>
    <small>&copy; {YEAR} HBLiving.</small>
  </div>
</footer>
<script src="assets/js/site.js?v={ver('assets/js/site.js')}"></script>'''


ICON = {'pin': '<path d="M12 21s-7-6.2-7-11.5A7 7 0 0 1 19 9.5C19 14.8 12 21 12 21Z"/><circle cx="12" cy="9.5" r="2.5"/>', 'tag': '<path d="M3 12V4h8l10 10-8 8Z"/><circle cx="7.5" cy="8.5" r="1.5"/>', 'shake': '<path d="M3 11l4-4 5 3 5-3 4 4-9 9Z"/><path d="M8 14l2 2M11 13l2 2"/>', 'chart': '<path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/>', 'food': '<path d="M5 3v8a2 2 0 0 0 4 0V3M7 11v10M16 3c-2 2-2 7 0 9v9"/>', 'tool': '<path d="M14 6a4 4 0 0 0 5 5l-9 9a2 2 0 0 1-3-3l9-9a4 4 0 0 0-2-2Z"/>', 'wave': '<path d="M2 16c3 0 3-3 6-3s3 3 6 3 3-3 6-3M2 20c3 0 3-3 6-3s3 3 6 3 3-3 6-3M7 10c1-4 6-6 10-4"/>', 'heart': '<path d="M12 20s-8-5-8-11a4.5 4.5 0 0 1 8-2.5A4.5 4.5 0 0 1 20 9c0 6-8 11-8 11Z"/>', 'scissors': '<circle cx="6" cy="6" r="3"/><circle cx="6" cy="18" r="3"/><path d="M8.5 8 20 19M8.5 16 20 5"/>', 'paw': '<circle cx="6" cy="10" r="2"/><circle cx="10" cy="6" r="2"/><circle cx="14" cy="6" r="2"/><circle cx="18" cy="10" r="2"/><path d="M8 18c0-3 2-5 4-5s4 2 4 5-2 2-4 2-4 1-4-2Z"/>', 'home': '<path d="M3 11 12 4l9 7v9H3Z"/><path d="M10 20v-5h4v5"/>', 'car': '<path d="M3 16v-4l2-5h14l2 5v4Z"/><circle cx="7" cy="17" r="2"/><circle cx="17" cy="17" r="2"/>', 'kids': '<circle cx="12" cy="5" r="2.5"/><path d="M12 8v7M8 11h8M9 21l3-6 3 6"/>', 'brief': '<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M9 7V4h6v3M3 12h18"/>', 'bag': '<path d="M5 8h14l-1 13H6Z"/><path d="M9 8a3 3 0 0 1 6 0"/>', 'star': '<path d="m12 3 2.6 5.6 6.1.6-4.6 4.1 1.3 6L12 16.3 6.6 19.3l1.3-6L3.3 9.2l6.1-.6Z"/>'}


def ico(n):
    return f'<svg class="ico" viewBox="0 0 24 24" aria-hidden="true">{ICON[n]}</svg>'


def why(icon, title, text):
    return f'<article class="why"><span class="why-ico">{ico(icon)}</span><h3>{title}</h3><p>{text}</p></article>'


def sample(cat, name, line, city, featured=False):
    badge = '<span class="ad-badge">Featured</span>' if featured else ''
    return f'''<article class="ad{' ad-feat' if featured else ''}">
      <div class="ad-top"><span class="ad-cat">{cat}</span>{badge}</div>
      <h3>{name}</h3><p>{line}</p>
      <div class="ad-foot"><span class="ad-city">{city}</span><span class="ad-links"><span>Call</span><span>Website</span>{'<span>Directions</span>' if featured else ''}</span></div>
    </article>'''


form_on = bool(FORM_TO)
form_attrs = (f'action="https://formsubmit.co/{FORM_TO}" method="POST"' if form_on
              else 'onsubmit="event.preventDefault(); this.querySelector(\'.form-msg\').textContent = \'Thanks!  Online requests open very soon.\';"')
form_hidden = ('<input type="hidden" name="_subject" value="HBLiving: new advertiser request"><input type="hidden" name="_template" value="table">'
               '<input type="hidden" name="_next" value="https://hbliving.com/thanks.html"><input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off">') if form_on else ''

home = f'''{head('HBLiving | Local advertising in Huntington Beach', 'Advertise your business to Huntington Beach and nearby neighbors from $5 a month.  No contracts, cancel anytime.', '<link rel="stylesheet" href="assets/vendor/leaflet/leaflet.css">')}
<body>
{header()}
<main>
  <section class="hero">
    <div class="hero-in">
      <div class="hero-copy">
        <p class="kicker">Local advertising for Huntington Beach</p>
        <h1>Put your business <em>on the local map.</em></h1>
        <p class="lede">HBLiving connects Huntington Beach businesses with the neighbors who live, work and spend here.  Simple plans from $5 a month.  No contracts.</p>
        <div class="cta-row"><a class="btn btn-coral" href="#advertise">Start advertising</a><a class="btn btn-ghost" href="#plans">View plans</a></div>
        <ul class="proof"><li><b>From $5</b><span>per month</span></li><li><b>4 areas</b><span>across HB</span></li><li><b>No</b><span>contracts</span></li></ul>
      </div>
      <div class="preview" aria-hidden="true">
        <div class="pv-card">
          <div class="pv-top"><span class="pv-cat">Food and drink</span><span class="ad-badge">Featured</span></div>
          <b class="pv-name">Your Business Name</b>
          <span class="pv-line">Your offer, your hours and what makes you the local favorite.</span>
          <div class="pv-btns"><span>Call</span><span>Website</span><span>Directions</span></div>
        </div>
        <div class="pv-stats">
          <p>Example monthly report</p>
          <div><b>1,240</b><span>views</span></div><div><b>86</b><span>website taps</span></div><div><b>31</b><span>call taps</span></div>
        </div>
      </div>
    </div>
    {pier_scene()}
  </section>

  <section class="wrap" id="why">
    <div class="sec-head"><p class="kicker">Why HBLiving</p><h2>Advertising that's actually local.</h2></div>
    <div class="grid4">
      {why('pin', 'Only local eyes', 'Every ad is built for Huntington Beach and the towns around it, not shown to people three states away.')}
      {why('tag', 'Priced for small business', 'Less than the price of a coffee a week.  Big-name ad sites can cost many times as much.')}
      {why('shake', 'No contracts', 'Pay month to month and cancel anytime.  Stay because it works, not because you signed something.')}
      {why('chart', 'See your results', 'Advertisers on the $10 plan get a simple monthly report: how many people saw the ad and tapped to call, visit the website or get directions.')}
    </div>
  </section>

  <section class="wrap" id="communities">
    <div class="sec-head"><p class="kicker">Local communities</p><h2>Neighborhood sites, <em>powered by HBLiving.</em></h2><p class="sub">Each neighborhood gets its own free site for neighbors: a calendar, a bulletin board and neighbors helping neighbors.  Local businesses that advertise keep it free.</p></div>
    <div class="comms comms-2">
      <article class="comm"><span class="comm-status soon">Coming soon</span><h3>Meredith Gardens</h3><p>Across the Seaview ballfields.  Southeast HB.</p><span class="comm-note">Launching soon</span></article>
      <article class="comm comm-join"><span class="comm-status join">Your neighborhood</span><h3>Bring it to your street</h3><p>Want a free site for your tract or HOA?  We'll set it up.  Tell us about your neighborhood.</p><a class="btn btn-coral" href="#advertise" data-plan="Start">Start a community site</a></article>
    </div>
  </section>

  <section class="band" id="plans">
    <div class="wrap">
      <div class="sec-head center"><p class="kicker">Simple pricing</p><h2>Two plans.  <em>No surprises.</em></h2><p class="sub">Reach your neighborhood for $5, or your neighborhood and all of Huntington Beach for $10.  Pay monthly, or pay for the year and get two months free.</p></div>
      <div class="plans">
        <article class="plan">
          <h3>Community</h3>
          <p class="price"><b>$5</b><span>per month</span></p>
          <p class="yearly">or $50 a year, two months free</p>
          <ul>
            <li>Your ad on one community site's Local page</li>
            <li>Seen by the neighbors who live right around you</li>
            <li>Your pin on the HBLiving map</li>
            <li>Name, phone, website and a short description</li>
            <li>Tap to call and tap for your website</li>
            <li>Update your details anytime</li>
          </ul>
          <a class="btn btn-ghost btn-wide" href="#advertise" data-plan="Community">Choose Community</a>
        </article>
        <article class="plan plan-feat">
          <span class="plan-flag">Best value</span>
          <h3>Community plus HBLiving</h3>
          <p class="price"><b>$10</b><span>per month</span></p>
          <p class="yearly">or $100 a year, two months free</p>
          <ul>
            <li>Everything in Community</li>
            <li>Your ad on the HBLiving home page and in your area of the city</li>
            <li>Every community site in your area, including new ones as they launch</li>
            <li>Featured badge and a gold-ringed pin on the map</li>
            <li>Your photo or logo and a special offer line</li>
            <li>Monthly report of views and taps to call, visit or get directions</li>
          </ul>
          <a class="btn btn-coral btn-wide" href="#advertise" data-plan="Both">Choose Community plus HBLiving</a>
        </article>
      </div>
      <div class="founding"><b>Founding advertisers lock in their price.</b><span>Businesses that join in the first year keep their rate for as long as they stay with us, even if prices go up later.</span></div>
    </div>
  </section>

  <section class="wrap" id="how">
    <div class="sec-head"><p class="kicker">How it works</p><h2>Live in <em>three easy steps.</em></h2></div>
    <ol class="steps">
      <li><b>Tell us about your business</b><span>Fill in the short form below.  It takes about two minutes.</span></li>
      <li><b>We build your ad</b><span>We write it, add your details and send it to you to approve.  No design work on your end.</span></li>
      <li><b>Go live and get found</b><span>Once you approve and pay, your ad goes up.  Change it whenever you like.</span></li>
    </ol>
  </section>

  <section class="band band-sand" id="map">
    <div class="wrap">
      <div class="sec-head"><p class="kicker">The HBLiving map</p><h2>Every ad gets <em>a pin on the map.</em></h2><p class="sub">Huntington Beach in four areas.  Tap an area to zoom in, or tap an ad to find it on the map.  These are sample ads to show how it works.</p></div>
      <div class="chips" id="terrChips" role="group" aria-label="Areas"></div>
      <div class="map-wrap">
        <div class="map-box"><div id="hbMap" role="region" aria-label="Map of Huntington Beach areas and businesses"></div><p class="terr-info" id="terrInfo"></p></div>
        <ol class="mad-list" id="adList" aria-label="Ads in this area"></ol>
      </div>
      <p class="map-note">Area lines follow ZIP codes, so the edges are approximate.</p>
    </div>
  </section>

  <section class="wrap" id="categories">
    <div class="sec-head"><p class="kicker">Categories</p><h2>Room for <em>every kind of business.</em></h2></div>
    <ul class="cats">{''.join(f'<li>{ico(i)}{t}</li>' for i, t in CATS)}</ul>
  </section>

  <section class="band" id="faq">
    <div class="wrap faq-wrap">
      <div class="sec-head"><p class="kicker">Questions</p><h2>Good to <em>know.</em></h2></div>
      <div class="faq">
        <details><summary>How do I pay?</summary><p>After you approve your ad, we send you a secure link to pay by card, monthly or for the year.</p></details>
        <details><summary>Is there a contract?</summary><p>No.  Plans are month to month and you can cancel anytime.  Yearly plans are paid up front for two free months.</p></details>
        <details><summary>Can I change my ad later?</summary><p>Yes.  Send us new hours, a new offer or a new photo and we'll update it.</p></details>
        <details><summary>What is the difference between the plans?</summary><p>Community puts your ad on one neighborhood site, where the people right around you see it.  Community plus HBLiving adds the HBLiving home page, your area of the city and every community site near you, including new ones as they open.</p></details>
        <details><summary>What are the four areas?</summary><p>Downtown and the Pier, Harbour and Sunset Beach, North HB and Central Park, and Southeast HB.  They follow Huntington Beach's ZIP codes, so your ad shows in your own area and across the whole city.</p></details>
        <details><summary>Who sees my ad?</summary><p>People looking for local businesses in Huntington Beach and nearby towns: Fountain Valley, Seal Beach, Sunset Beach, Westminster, Costa Mesa and Newport Beach.</p></details>
        <details><summary>What do I need to get started?</summary><p>Just your business name, phone, website or social page, and a sentence or two about what you do.  A logo or photo helps for Featured ads.</p></details>
      </div>
    </div>
  </section>

  <section class="wrap" id="advertise">
    <div class="adv">
      <div><p class="kicker">Advertise with HBLiving</p><h2>Ready to get <em>found?</em></h2><p>Send us your details and we'll build your ad and send it over for you to approve.  You don't pay anything until you've seen it.</p></div>
      <form class="adv-form" {form_attrs}>
        {form_hidden}
        <div class="row"><label>Business name<input name="business" required maxlength="80"></label><label>Your name<input name="name" required maxlength="60"></label></div>
        <div class="row"><label>Email<input type="email" name="email" required></label><label>Phone<input type="tel" name="phone" maxlength="20"></label></div>
        <div class="row"><label>Website or social page <span class="opt">(optional)</span><input name="website" maxlength="120"></label><label>City<select name="city">{''.join(f'<option>{c}</option>' for c in CITIES)}<option>Other nearby</option></select></label></div>
        <div class="row"><label>Category<select name="category">{''.join(f'<option>{t}</option>' for _, t in CATS)}<option>Something else</option></select></label><label>Plan<select name="plan" id="planSel"><option>Community plus HBLiving, $10 a month</option><option>Community, $5 a month</option><option>Start a community site (free)</option><option>Not sure yet</option></select></label></div>
        <label>Community <select name="community"><option>Meredith Gardens (coming soon)</option><option>Not sure, help me pick</option><option>A new neighborhood</option></select></label>
        <label>Tell us about your business <span class="opt">(optional)</span><textarea name="about" rows="3" maxlength="600"></textarea></label>
        <button class="btn btn-coral" type="submit">Send my details</button>
        <p class="form-msg" role="status"></p>
        <p class="fine">We only use your details to set up and manage your ad.  We never sell or share them.</p>
      </form>
    </div>
  </section>
</main>
{footer()}
<script src="assets/vendor/leaflet/leaflet.js"></script>
<script src="assets/js/track.js?v={ver('assets/js/track.js')}"></script>
<script src="assets/js/map-data.js?v={ver('assets/js/map-data.js')}"></script>
<script src="assets/js/map.js?v={ver('assets/js/map.js')}"></script>
</body>
</html>
'''

thanks = f'''{head('Thanks | HBLiving', 'Thanks for your interest in advertising with HBLiving.', noindex=True)}
<body>
{header()}
<main class="wrap thanks"><p class="kicker">Got it</p><h1>Thanks!  <em>We'll be in touch.</em></h1><p class="body-lg">We'll build your ad and send it over for you to approve, usually within a couple of business days.</p><a class="btn btn-coral" href="index.html">Back to HBLiving</a></main>
{footer()}
</body>
</html>
'''

import re as _re2
def brandify(html):
    """Wrap HBLiving in page text as HB + italic Living.  Leaves tags, titles, scripts and styles alone."""
    out, skip = [], 0
    for part in _re2.split(r'(<[^>]+>)', html):
        if part.startswith('<'):
            tag = part[1:].split()[0].rstrip('>').lower() if len(part) > 2 else ''
            if tag in ('title', 'script', 'style', 'textarea', 'option'): skip += 1
            elif tag in ('/title', '/script', '/style', '/textarea', '/option'): skip = max(0, skip - 1)
            out.append(part)
        else:
            out.append(part if skip else part.replace('HBLiving', '<span class="nm">HB<em>Living</em></span>'))
    return ''.join(out)
report = f'''{head('Monthly report | HBLiving', 'HBLiving advertiser report.', noindex=True)}
<body>
{header()}
<main class="wrap thanks">
  <p class="kicker">For HBLiving only</p><h1>Monthly <em>report.</em></h1>
  <form id="repSignin" class="adv-form rep-form" hidden>
    <label>Admin email<input type="email" name="email" required></label>
    <button class="btn btn-coral" type="submit">Email me a sign-in link</button>
  </form>
  <div id="repMain" hidden><div class="rep-bar"><label>Month <input type="month" id="repMonth"></label><button type="button" class="btn btn-ghost" id="repOut">Sign out</button></div><div id="rep"></div></div>
  <p id="repMsg" class="form-msg" role="status"></p>
</main>
{footer()}
<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2.116.0/dist/umd/supabase.js"></script>
<script src="assets/js/track.js?v={ver('assets/js/track.js')}"></script>
<script src="assets/js/map-data.js?v={ver('assets/js/map-data.js')}"></script>
<script src="assets/js/report.js?v={ver('assets/js/report.js')}"></script>
</body>
</html>
'''
(ROOT / 'report.html').write_text(brandify(report))
home = brandify(home); thanks = brandify(thanks)
(ROOT / 'index.html').write_text(home)
(ROOT / 'thanks.html').write_text(thanks)
import re as _re
_h = hashlib.md5(b''.join((ROOT / f).read_bytes() for f in ['index.html', 'thanks.html', 'assets/css/site.css', 'assets/js/site.js', 'assets/js/map.js', 'assets/js/map-data.js', 'assets/js/track.js', 'assets/img/mark.svg'])).hexdigest()[:10]
_sw = (ROOT / 'sw.js').read_text(); (ROOT / 'sw.js').write_text(_re.sub(r'const CACHE = "[^"]*";', f'const CACHE = "hbl-{_h}";', _sw))
print('built index.html and thanks.html, cache', _h)
