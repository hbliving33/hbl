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
    pil = ''.join(f'<path d="M{x} 236 V{268 + (x % 3) * 2}"/>' for x in range(470, 1300, 34))
    birds = ''.join(f'<path d="M{x} {y} q6 -6 12 0 q6 -6 12 0"/>' for x, y in [(300, 120), (336, 104), (380, 132), (1120, 90)])
    return f'''<svg class="scene" viewBox="0 0 1440 360" preserveAspectRatio="xMidYMax slice" aria-hidden="true">
  <defs>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffe9a0"/><stop offset=".5" stop-color="#ffc14d"/><stop offset=".85" stop-color="#f5873a"/><stop offset="1" stop-color="#e0522b"/></linearGradient>
    <linearGradient id="sea" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1f7fa6"/><stop offset="1" stop-color="#0d4f6e"/></linearGradient>
    <radialGradient id="sun" r=".5"><stop offset="0" stop-color="#fff4d6"/><stop offset=".6" stop-color="#ffd27a"/><stop offset="1" stop-color="#ffb35a"/></radialGradient>
  </defs>
  <rect width="1440" height="360" fill="url(#sky)"/>
  <circle class="sunglow" cx="880" cy="214" r="120" fill="#ffe28a" opacity=".45"/>
  <clipPath id="sunc"><circle cx="880" cy="214" r="62"/></clipPath>
  <g clip-path="url(#sunc)"><rect x="810" y="150" width="140" height="30" fill="#d62b1f"/><rect x="810" y="180" width="140" height="24" fill="#f8b800"/><rect x="810" y="204" width="140" height="30" fill="#138a43"/></g>
  <g class="birds" fill="none" stroke="{INK}" stroke-width="2.2" stroke-linecap="round" opacity=".55">{birds}</g>
  <rect y="226" width="1440" height="134" fill="url(#sea)"/>
  <path d="M760 240 H1000 M790 254 H970 M820 268 H940" stroke="#ffe07a" stroke-width="4" stroke-linecap="round" opacity=".6"/>
  <!-- pier on pilings -->
  <g class="pier" stroke="{INK}" stroke-width="5" stroke-linecap="round">{pil}</g>
  <path d="M440 232 H1300" stroke="{INK}" stroke-width="9" stroke-linecap="round"/>
  <path d="M440 222 H1300" stroke="{INK}" stroke-width="2" opacity=".7"/>
  <path d="M1214 232 V204 H1290 V232Z" fill="{INK}"/><path d="M1208 205 L1252 184 L1296 205Z" fill="#d62b1f"/><rect x="1238" y="212" width="12" height="10" fill="#f8b800"/><rect x="1258" y="212" width="12" height="10" fill="#f8b800"/>
  <!-- beach and palms -->
  <path d="M0 262 C 160 250 300 252 470 270 L 470 360 H0Z" fill="#f0d3a4"/>
  <path d="M0 290 C 180 278 330 284 520 306 L 560 360 H0Z" fill="#f6e2bf"/>
  <g fill="none" stroke="{INK}" stroke-linecap="round">
    <path d="M150 300 C 146 250 150 210 164 170" stroke-width="7"/>
    <path d="M232 300 C 236 262 232 232 222 204" stroke-width="6"/>
  </g>
  <g fill="#1b7a3c">
    <path d="M164 170 c-22 -10 -48 -4 -60 12 c18 -8 40 -8 60 -6 c-16 -14 -38 -22 -56 -14 c22 0 42 6 56 14 c2 -20 -10 -38 -26 -44 c12 12 22 28 26 40 c12 -18 36 -26 58 -18 c-22 4 -40 12 -52 24 c24 -6 44 2 56 18 c-18 -12 -40 -14 -62 -8z"/>
    <path transform="translate(90.8 68) scale(.8)" d="M164 170 c-22 -10 -48 -4 -60 12 c18 -8 40 -8 60 -6 c-16 -14 -38 -22 -56 -14 c22 0 42 6 56 14 c2 -20 -10 -38 -26 -44 c12 12 22 28 26 40 c12 -18 36 -26 58 -18 c-22 4 -40 12 -52 24 c24 -6 44 2 56 18 c-18 -12 -40 -14 -62 -8z"/>
  </g>
  <!-- surfer on a small wave -->
  <path class="swell" d="M520 318 C 600 296 660 296 700 318 C 720 330 760 330 800 316" fill="none" stroke="#e9fbff" stroke-width="5" stroke-linecap="round" opacity=".9"/>
  <g class="surfer" transform="translate(640 296)"><path d="M-22 4 Q0 10 24 2" stroke="#d62b1f" stroke-width="3" fill="none" stroke-linecap="round"/><path d="M-22 6.5 Q0 12.5 24 4.5" stroke="#f8b800" stroke-width="2.6" fill="none" stroke-linecap="round"/><path d="M-21 9 Q0 15 23 7" stroke="#138a43" stroke-width="2.6" fill="none" stroke-linecap="round"/><path d="M-4 4 L0 -10 L5 4 M0 -10 L1 -22 M1 -18 L-10 -14 M1 -18 L12 -22" stroke="{INK}" stroke-width="3" fill="none" stroke-linecap="round"/><circle cx="2" cy="-27" r="4.4" fill="{INK}"/></g>
  <path d="M0 326 C 240 314 520 322 760 334 S 1200 328 1440 320" fill="none" stroke="#d62b1f" stroke-width="6"/>
  <path d="M0 332 C 240 320 520 328 760 340 S 1200 334 1440 326" fill="none" stroke="#f8b800" stroke-width="6"/>
  <path d="M0 338 C 240 326 520 334 760 346 S 1200 340 1440 332" fill="none" stroke="#138a43" stroke-width="6"/>
  <path d="M0 342 C 240 330 520 338 760 350 S 1200 344 1440 336 V360 H0Z" fill="{FOAM}"/>
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

NAV = [('#why', 'Why HBLiving'), ('#map', 'Map'), ('#plans', 'Plans'), ('#how', 'How it works'), ('#categories', 'Categories'), ('#faq', 'Questions')]
CITIES = ['Huntington Beach', 'Fountain Valley', 'Seal Beach', 'Sunset Beach', 'Westminster', 'Costa Mesa', 'Newport Beach']
CATS = [('🌮', 'Food and drink'), ('🔧', 'Home services'), ('🏄', 'Surf and outdoor'), ('💪', 'Health and fitness'), ('✂️', 'Beauty and spa'),
        ('🐾', 'Pets'), ('🏡', 'Real estate'), ('🚗', 'Auto'), ('🎨', 'Kids and family'), ('💼', 'Professional services'), ('🛍️', 'Shops and boutiques'), ('🎉', 'Events and entertainment')]


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


def why(icon, title, text):
    return f'<article class="why"><span class="why-ico" aria-hidden="true">{icon}</span><h3>{title}</h3><p>{text}</p></article>'


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
    <div class="hero-copy">
      <p class="kicker">Local advertising for Huntington Beach</p>
      <h1>Get your business seen <em>in Surf City.</em></h1>
      <p class="lede">HBLiving puts local businesses in front of the people who live, work and play here.  Plans start at $5 a month, with no contracts and nothing to install.</p>
      <div class="cta-row"><a class="btn btn-coral" href="#plans">See the plans</a><a class="btn btn-ghost" href="#advertise">Start advertising</a></div>
      <ul class="cities" aria-label="Areas we cover">{''.join(f'<li>{c}</li>' for c in CITIES)}</ul>
    </div>
    {pier_scene()}
  </section>

  <section class="wrap" id="why">
    <div class="sec-head"><p class="kicker">Why HBLiving</p><h2>Advertising that's <em>actually local.</em></h2></div>
    <div class="grid4">
      {why('📍', 'Only local eyes', 'Every ad is built for Huntington Beach and the towns around it, not shown to people three states away.')}
      {why('💵', 'Priced for small business', 'Less than the price of a coffee a week.  Big-name ad sites can cost many times as much.')}
      {why('🤝', 'No contracts', 'Pay month to month and cancel anytime.  Stay because it works, not because you signed something.')}
      {why('📊', 'See your results', 'Featured advertisers get a simple monthly report: how many people saw the ad, called and clicked.')}
    </div>
  </section>

  <section class="band" id="plans">
    <div class="wrap">
      <div class="sec-head center"><p class="kicker">Simple pricing</p><h2>Two plans.  <em>No surprises.</em></h2><p class="sub">Pay monthly, or pay for the year and get two months free.</p></div>
      <div class="plans">
        <article class="plan">
          <h3>Local Listing</h3>
          <p class="price"><b>$5</b><span>per month</span></p>
          <p class="yearly">or $50 a year, two months free</p>
          <ul>
            <li>Your business in its category</li>
            <li>Name, phone, website and city</li>
            <li>A short description of what you do</li>
            <li>Your own pin on the HBLiving map</li>
            <li>Tap to call and tap for your website</li>
            <li>Update your details anytime</li>
          </ul>
          <a class="btn btn-ghost btn-wide" href="#advertise" data-plan="Local Listing">Choose Local Listing</a>
        </article>
        <article class="plan plan-feat">
          <span class="plan-flag">Most popular</span>
          <h3>Featured</h3>
          <p class="price"><b>$10</b><span>per month</span></p>
          <p class="yearly">or $100 a year, two months free</p>
          <ul>
            <li>Everything in Local Listing</li>
            <li>Top of your category and your area, with a Featured badge</li>
            <li>A bigger, gold-ringed pin on the map</li>
            <li>Your photo or logo on the ad</li>
            <li>Rotating spot on the home page</li>
            <li>Directions button and a special offer line</li>
            <li>Monthly report of views, calls and clicks</li>
          </ul>
          <a class="btn btn-coral btn-wide" href="#advertise" data-plan="Featured">Choose Featured</a>
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
    <ul class="cats">{''.join(f'<li><span aria-hidden="true">{i}</span>{t}</li>' for i, t in CATS)}</ul>
  </section>

  <section class="band" id="faq">
    <div class="wrap faq-wrap">
      <div class="sec-head"><p class="kicker">Questions</p><h2>Good to <em>know.</em></h2></div>
      <div class="faq">
        <details><summary>How do I pay?</summary><p>After you approve your ad, we send you a secure link to pay by card, monthly or for the year.</p></details>
        <details><summary>Is there a contract?</summary><p>No.  Plans are month to month and you can cancel anytime.  Yearly plans are paid up front for two free months.</p></details>
        <details><summary>Can I change my ad later?</summary><p>Yes.  Send us new hours, a new offer or a new photo and we'll update it.</p></details>
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
        <div class="row"><label>Category<select name="category">{''.join(f'<option>{t}</option>' for _, t in CATS)}<option>Something else</option></select></label><label>Plan<select name="plan" id="planSel"><option>Featured, $10 a month</option><option>Local Listing, $5 a month</option><option>Not sure yet</option></select></label></div>
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

(ROOT / 'index.html').write_text(home)
(ROOT / 'thanks.html').write_text(thanks)
import re as _re
_h = hashlib.md5(b''.join((ROOT / f).read_bytes() for f in ['index.html', 'thanks.html', 'assets/css/site.css', 'assets/js/site.js', 'assets/js/map.js', 'assets/js/map-data.js', 'assets/img/mark.svg'])).hexdigest()[:10]
_sw = (ROOT / 'sw.js').read_text(); (ROOT / 'sw.js').write_text(_re.sub(r'const CACHE = "[^"]*";', f'const CACHE = "hbl-{_h}";', _sw))
print('built index.html and thanks.html, cache', _h)
