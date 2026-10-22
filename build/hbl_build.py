"""Builds the HBLiving site: index.html (home) and logos.html (logo options, not linked, noindex)."""
import pathlib, math, hashlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
YEAR = 2026

# ---------- Which site is public at hbliving.com ----------
#   "holding"  = the plain HBLiving one-pager is the home page.  The business site is kept at business.html (unlinked, noindex) for preview.
#   "business" = the full advertising site is the home page.
MODE = "holding"

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
    <linearGradient id="dusk" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff1cf" stop-opacity="0"/><stop offset=".45" stop-color="#ffdca0"/><stop offset=".8" stop-color="#ffb867"/><stop offset="1" stop-color="#ff9a4d"/></linearGradient>
    <linearGradient id="deep" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1fb3a6"/><stop offset="1" stop-color="#0c7d76"/></linearGradient>
    <radialGradient id="sunr" r=".5"><stop offset="0" stop-color="#ffe7a1"/><stop offset=".7" stop-color="#f8b800"/><stop offset="1" stop-color="#e88a12"/></radialGradient>
  </defs>
  <rect width="1440" height="320" fill="url(#dusk)"/>
  <circle cx="980" cy="246" r="120" fill="#fff3c4" opacity=".55"/>
  <circle cx="980" cy="246" r="54" fill="url(#sunr)"/>
  <rect y="244" width="1440" height="76" fill="url(#deep)"/>
  <path d="M900 256 H1060 M930 268 H1030 M955 280 H1005" stroke="#fff6d8" stroke-width="3" stroke-linecap="round" opacity=".85"/>
  <g stroke="#1d3b40" stroke-width="5" stroke-linecap="round">{pil}</g>
  <path d="M540 247 H1390" stroke="#1d3b40" stroke-width="8" stroke-linecap="round"/>
  <path d="M1300 247 V224 H1372 V247Z M1294 225 L1336 208 L1378 225Z" fill="#1d3b40"/>
  <path d="M0 270 C 200 258 360 260 560 282 L 600 320 H0Z" fill="#f3d9a4"/>
  <g fill="none" stroke="#1d3b40" stroke-linecap="round"><path d="M180 286 C 176 240 180 204 194 168" stroke-width="7"/><path d="M262 286 C 266 250 262 224 252 198" stroke-width="6"/></g>
  <g fill="#1d3b40">
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

NAV = [('#why', 'Why HBLiving'), ('#map', 'Map'), ('#plans', 'Pricing'), ('#neighborhood', 'Your neighborhood'), ('#how', 'How it works'), ('#categories', 'Categories'), ('#faq', 'Questions')]
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
    <p>Local advertising for Huntington Beach businesses and the towns next door.  Independently owned.</p></div>
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

home = f'''{head('HBLiving | Local advertising in Huntington Beach', 'Advertise your business to Huntington Beach and nearby neighbors for $10 a month.  No contracts, cancel anytime.', '<link rel="stylesheet" href="assets/vendor/leaflet/leaflet.css">')}
<body>
{header()}
<main>
  <section class="hero">
    <div class="hero-in">
      <div class="hero-copy">
        <p class="kicker">Local advertising for Huntington Beach</p>
        <h1>Put your business <em>on the local map.</em></h1>
        <p class="lede">HBLiving connects Huntington Beach businesses with the neighbors who live, work and spend here.  One simple price: $10 a month.  No contracts.</p>
        <div class="cta-row"><a class="btn btn-coral" href="#advertise">Start advertising</a><a class="btn btn-ghost" href="#plans">View plans</a></div>
        <ul class="proof"><li><b>$10</b><span>a month</span></li><li><b>4 areas</b><span>across HB</span></li><li><b>No</b><span>contracts</span></li></ul>
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
      {why('chart', 'See your results', 'Every advertiser gets a simple monthly report: how many people saw the ad and tapped to call, visit the website or get directions.')}
    </div>
  </section>

  <section class="band" id="plans">
    <div class="wrap">
      <div class="sec-head center"><p class="kicker">Simple pricing</p><h2>One plan.  <em>Everything included.</em></h2><p class="sub">$10 a month, no contract.  Pay for the year and get two months free.</p></div>
      <div class="plans">
        <article class="plan plan-feat">
          <span class="plan-flag">Everything included</span>
          <h3>HBLiving Featured</h3>
          <p class="price"><b>$10</b><span>per month</span></p>
          <p class="yearly">or $100 a year, two months free</p>
          <ul>
            <li>Your ad on the HBLiving home page and in your area of the city</li>
            <li>Featured badge and a gold-ringed pin on the map</li>
            <li>Your photo or logo and a special offer line</li>
            <li>Tap to call, tap for your website and tap for directions</li>
            <li>Monthly report of views and taps</li>
            <li>Update your details anytime</li>
          </ul>
          <a class="btn btn-coral btn-wide" href="#advertise" data-plan="Monthly">Start for $10 a month</a>
          <a class="btn btn-ghost btn-wide" href="#advertise" data-plan="Yearly">Go yearly for $100</a>
        </article>
        <article class="plan plan-ref">
          <span class="plan-flag plan-flag-alt">Referral program</span>
          <h3>Refer a business, <em>get two months free</em></h3>
          <p class="ref-big"><b>2</b><span>free months for you</span></p>
          <ul>
            <li>Know a local business that should be on HBLiving?  Send them our way.</li>
            <li>When they sign up for a year, you get two free months.</li>
            <li>No limit.  Refer six businesses on yearly plans and your whole year is free.</li>
            <li>They just put your business name in the "Referred by" box when they sign up.</li>
          </ul>
          <a class="btn btn-ghost btn-wide" href="#advertise">Refer a business</a>
        </article>
      </div>
      <div class="founding"><b>Founding advertisers lock in their price.</b><span>Businesses that join in the first year keep their rate for as long as they stay with us, even if prices go up later.</span></div>
    </div>
  </section>

  <section class="wrap" id="neighborhood">
    <div class="sec-head"><p class="kicker">Bring it to your neighborhood</p><h2>Bring five businesses.  <em>Get your neighborhood site free.</em></h2><p class="sub">Want a site for your street, tract or HOA, with a neighborhood calendar, a bulletin board and neighbors helping neighbors?  Sign up five local businesses to advertise with HBLiving and we'll build it for free.</p></div>
    <ol class="steps">
      <li><b>Tell us about your neighborhood</b><span>Your street, tract or HOA and what your neighbors would use.</span></li>
      <li><b>Bring five advertisers</b><span>The coffee shop, the plumber, the realtor you already know.  When five sign up, you're in.</span></li>
      <li><b>We build your site, free</b><span>Your own neighborhood site, set up for you and kept free for your neighbors.</span></li>
    </ol>
    <div class="cta-row"><a class="btn btn-coral" href="#advertise" data-plan="Neighborhood">Start my neighborhood</a></div>
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
        <details><summary>Is there a contract?</summary><p>No.  Monthly is $10 a month and you can cancel anytime.  Yearly is $100 paid up front, which works out to two free months.</p></details>
        <details><summary>Can I change my ad later?</summary><p>Yes.  Send us new hours, a new offer or a new photo and we'll update it.</p></details>
        <details><summary>How does the referral program work?</summary><p>Refer a business.  When they sign up for a yearly plan and put your business name in the "Referred by" box, you get two free months added to your plan.  There's no limit.</p></details>
        <details><summary>How do I get a free neighborhood site?</summary><p>Tell us about your neighborhood, then sign up five local businesses to advertise with HBLiving.  Once all five are live, we build your neighborhood site at no cost.</p></details>
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
        <div class="row"><label>Category<select name="category">{''.join(f'<option>{t}</option>' for _, t in CATS)}<option>Something else</option></select></label><label>Plan<select name="plan" id="planSel"><option>Monthly, $10 a month</option><option>Yearly, $100 (two months free)</option><option>Bring HBLiving to my neighborhood</option><option>Not sure yet</option></select></label></div>
        <div class="row"><label>Referred by <span class="opt">(optional)</span><input name="referred_by" maxlength="80" placeholder="Business that sent you"></label><label>Your neighborhood <span class="opt">(optional)</span><input name="neighborhood" maxlength="80" placeholder="Street, tract or HOA"></label></div>
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
home = brandify(home); thanks = brandify(thanks)

holding = brandify(f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>HBLiving | Surf City vibes</title>
<meta name="description" content="HBLiving: one love from Huntington Beach, Surf City USA.">
<meta name="theme-color" content="#0b0b0b">
<link rel="icon" href="assets/img/mark.svg" type="image/svg+xml">
<link rel="manifest" href="manifest.webmanifest">
<link rel="apple-touch-icon" href="assets/img/icon-180.png">
{FONTS}
<link rel="stylesheet" href="assets/css/hold.css?v={ver('assets/css/hold.css')}">
</head>
<body>
<div class="rays" aria-hidden="true"></div>
<div class="music"><p class="hint" id="hint">Tap for music</p><button class="play" id="play" type="button" aria-pressed="false" title="Music"><span class="eq" aria-hidden="true"><i></i><i></i><i></i><i></i></span><span class="pl-txt">Play the vibes</span></button></div>
<main class="vibe">
  <h1 class="logo">HB<em>Living</em></h1>
  <div class="flagbar" aria-hidden="true"><i></i><i></i><i></i></div>
  <p class="kick">Huntington Beach, California</p>
  <p class="now" id="now" aria-live="polite"><span class="dot"></span><span id="nowTxt"></span></p>
  <figure class="cam">
    <figcaption><span class="live">Live</span> From the pier</figcaption>
    <div class="cam-frame"><iframe src="https://www.youtube-nocookie.com/embed/mhQjsLBfOoY?autoplay=1&amp;mute=1&amp;rel=0&amp;playsinline=1&amp;controls=0&amp;disablekb=1&amp;fs=0&amp;iv_load_policy=3" title="Live camera on the Huntington Beach Pier" loading="lazy" referrerpolicy="strict-origin-when-cross-origin" allow="autoplay; encrypted-media; picture-in-picture; fullscreen" allowfullscreen></iframe></div>
    <a class="cam-credit" href="https://www.youtube.com/watch?v=mhQjsLBfOoY" rel="noopener" target="_blank">Live camera by the City of Huntington Beach</a>
  </figure>
  <div class="onelove"><p class="ol-s">One Love</p><svg viewBox="0 0 420 40" aria-hidden="true"><path d="M10 26 C 120 6 300 6 410 22" stroke="#d62b1f" stroke-width="7" fill="none" stroke-linecap="round"/><path d="M20 32 C 130 14 300 14 400 30" stroke="#f8b800" stroke-width="6" fill="none" stroke-linecap="round"/><path d="M34 38 C 140 22 300 22 388 37" stroke="#138a43" stroke-width="5" fill="none" stroke-linecap="round"/></svg><p class="ol-from">from Surf City</p></div>
</main>
<svg class="shore" viewBox="0 96 1440 204" preserveAspectRatio="xMidYMax slice" aria-hidden="true">
  <circle class="sun" cx="980" cy="210" r="96"/>
  <g class="glints" stroke="#fff3c4" stroke-linecap="round" stroke-width="3"><path d="M920 236 H1040"/><path d="M945 246 H1015"/></g>
  <g class="gulls" fill="none" stroke="#0b0b0b" stroke-width="3" stroke-linecap="round"><path d="M300 128 q10 -10 20 0 q10 -10 20 0"/><path d="M360 146 q8 -8 16 0 q8 -8 16 0"/><path d="M250 156 q7 -7 14 0 q7 -7 14 0"/></g>

  <g class="waves" transform="translate(-40 0) scale(1.08 1)"><path d="M0 230 C 120 214 240 246 360 230 S 600 214 720 230 S 960 246 1080 230 S 1320 214 1440 230 V300 H0Z" fill="#d62b1f"/>
  <path d="M0 250 C 120 236 240 264 360 250 S 600 236 720 250 S 960 264 1080 250 S 1320 236 1440 250 V300 H0Z" fill="#f8b800"/>
  <path d="M0 270 C 120 258 240 282 360 270 S 600 258 720 270 S 960 282 1080 270 S 1320 258 1440 270 V300 H0Z" fill="#138a43"/></g>
  <g fill="#0b0b0b"><path d="M560 214 H1390 V222 H560Z"/>{''.join(f'<rect x="{x}" y="214" width="6" height="40"/>' for x in range(570, 1390, 32))}<path d="M1300 214 V192 H1372 V214Z M1294 193 L1336 176 L1378 193Z"/></g>
  <g fill="none" stroke="#0b0b0b" stroke-linecap="round"><path d="M180 262 C 176 216 180 180 194 144" stroke-width="7"/><path d="M262 262 C 266 226 262 200 252 174" stroke-width="6"/></g>
  <g fill="#0b0b0b" class="fronds"><path d="M194 144 c-22 -10 -48 -4 -60 12 c18 -8 40 -8 60 -6 c-16 -14 -38 -22 -56 -14 c22 0 42 6 56 14 c2 -20 -10 -38 -26 -44 c12 12 22 28 26 40 c12 -18 36 -26 58 -18 c-22 4 -40 12 -52 24 c24 -6 44 2 56 18 c-18 -12 -40 -14 -62 -8z"/><path transform="translate(96.8 39.6) scale(.8)" d="M194 168 c-22 -10 -48 -4 -60 12 c18 -8 40 -8 60 -6 c-16 -14 -38 -22 -56 -14 c22 0 42 6 56 14 c2 -20 -10 -38 -26 -44 c12 12 22 28 26 40 c12 -18 36 -26 58 -18 c-22 4 -40 12 -52 24 c24 -6 44 2 56 18 c-18 -12 -40 -14 -62 -8z"/></g>
  <g class="surfer"><path d="M-40 0 C -20 6 20 6 40 0 C 20 -4 -20 -4 -40 0Z" fill="#f8b800" stroke="#0b0b0b" stroke-width="2"/><g fill="#0b0b0b"><circle cx="2" cy="-40" r="6"/><path d="M-2 -33 L 6 -33 L 8 -16 L 16 -2 L 10 0 L 2 -14 L -6 0 L -12 -2 L -4 -16Z"/><path d="M4 -30 L 22 -24 L 21 -21 L 4 -25Z M0 -30 L -18 -34 L -18 -31 L 0 -26Z"/></g></g>
</svg>
<div class="ticker" aria-hidden="true"><div class="tk">{''.join(f'<span>{t}</span>' for t in [f'{e} <i>{m}</i>' for e, m in [('Surf City Marathon', 'Feb'), ('Irish Fest', 'Mar'), ('Taste of Huntington Beach', 'Apr'), ('AVP Huntington Beach Open', 'May'), ('Fourth of July', 'Jul'), ('US Open of Surfing', 'Jul to Aug'), ('Oktoberfest', 'Sep to Nov'), ('Pacific Airshow', 'Oct'), ('Corgi Beach Day', 'Apr and Oct'), ('Magic on Main Street', 'Nov'), ('Cruise of Lights', 'Dec')]]*2)}</div></div>
<footer class="hfoot">&copy; {YEAR} HBLiving.  Independently owned.  <a href="https://open-meteo.com/" rel="noopener" target="_blank">Weather by Open-Meteo</a>.  Music: <a href="https://pixabay.com/music/reggae-reggae-island-vibes-537451/" rel="noopener" target="_blank">Reggae Island Vibes by alex-morgan</a></footer>
<script src="assets/js/hold.js?v={ver('assets/js/hold.js')}"></script>
</body>
</html>
''')

if MODE == "holding":
    # Only the one-pager is published.  The business pages are not written at all.
    (ROOT / 'index.html').write_text(holding)
    for p in ['business.html', 'thanks.html', 'report.html', 'logos.html']:
        (ROOT / p).unlink(missing_ok=True)
else:
    (ROOT / 'index.html').write_text(home)
    (ROOT / 'thanks.html').write_text(thanks)
    (ROOT / 'report.html').write_text(brandify(report))
import re as _re
_h = hashlib.md5(b''.join((ROOT / f).read_bytes() for f in ['index.html', 'assets/css/site.css', 'assets/js/site.js', 'assets/js/map.js', 'assets/js/map-data.js', 'assets/js/track.js', 'assets/js/hold.js', 'assets/css/hold.css', 'assets/img/mark.svg'])).hexdigest()[:10]
_sw = (ROOT / 'sw.js').read_text(); (ROOT / 'sw.js').write_text(_re.sub(r'const CACHE = "[^"]*";', f'const CACHE = "hbl-{_h}";', _sw))
print('mode', MODE, '- built index.html' + (' (one-pager only)' if MODE == 'holding' else ' (business site)') + ', cache', _h)
