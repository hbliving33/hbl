"""Builds the HB Living site: index.html (home) and logos.html (logo options, not linked, noindex)."""
import pathlib, math, hashlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
YEAR = 2026

# Palette: deep Pacific, sea glass, warm sand, sunset coral, golden hour
INK, SEA, GLASS, SAND, CORAL, GOLD, FOAM = '#0f2a3a', '#0e6e8c', '#8fd0cf', '#f3e4c8', '#f2765a', '#f6b94a', '#fbf7ef'

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,600;9..144,700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">'


def ver(path):
    return hashlib.md5((ROOT / path).read_bytes()).hexdigest()[:8]


# ---------- Hero illustration: golden hour at the pier ----------
def pier_scene():
    pil = ''.join(f'<path d="M{x} 236 V{268 + (x % 3) * 2}"/>' for x in range(470, 1300, 34))
    birds = ''.join(f'<path d="M{x} {y} q6 -6 12 0 q6 -6 12 0"/>' for x, y in [(300, 120), (336, 104), (380, 132), (1120, 90)])
    return f'''<svg class="scene" viewBox="0 0 1440 360" preserveAspectRatio="xMidYMax slice" aria-hidden="true">
  <defs>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffd9a8"/><stop offset=".55" stop-color="#ffc39a"/><stop offset="1" stop-color="#ffb08f"/></linearGradient>
    <linearGradient id="sea" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2c8fa8"/><stop offset="1" stop-color="#0e5f7a"/></linearGradient>
    <radialGradient id="sun" r=".5"><stop offset="0" stop-color="#fff4d6"/><stop offset=".6" stop-color="#ffd27a"/><stop offset="1" stop-color="#ffb35a"/></radialGradient>
  </defs>
  <rect width="1440" height="360" fill="url(#sky)"/>
  <circle class="sunglow" cx="880" cy="214" r="120" fill="#ffe3a6" opacity=".45"/>
  <circle cx="880" cy="214" r="62" fill="url(#sun)"/>
  <g class="birds" fill="none" stroke="{INK}" stroke-width="2.2" stroke-linecap="round" opacity=".55">{birds}</g>
  <rect y="226" width="1440" height="134" fill="url(#sea)"/>
  <path d="M760 240 H1000 M790 254 H970 M820 268 H940" stroke="#ffd98f" stroke-width="4" stroke-linecap="round" opacity=".6"/>
  <!-- pier on pilings -->
  <g class="pier" stroke="{INK}" stroke-width="5" stroke-linecap="round">{pil}</g>
  <path d="M440 232 H1300" stroke="{INK}" stroke-width="9" stroke-linecap="round"/>
  <path d="M440 222 H1300" stroke="{INK}" stroke-width="2" opacity=".7"/>
  <path d="M1214 232 V204 H1290 V232 M1210 204 L1252 186 L1294 204" fill="{INK}" stroke="{INK}" stroke-width="2" stroke-linejoin="round"/>
  <!-- beach and palms -->
  <path d="M0 262 C 160 250 300 252 470 270 L 470 360 H0Z" fill="#f0d3a4"/>
  <path d="M0 290 C 180 278 330 284 520 306 L 560 360 H0Z" fill="#f6e2bf"/>
  <g fill="none" stroke="{INK}" stroke-linecap="round">
    <path d="M150 300 C 146 250 150 210 164 170" stroke-width="7"/>
    <path d="M232 300 C 236 262 232 232 222 204" stroke-width="6"/>
  </g>
  <g fill="{INK}">
    <path d="M164 170 c-22 -10 -48 -4 -60 12 c18 -8 40 -8 60 -6 c-16 -14 -38 -22 -56 -14 c22 0 42 6 56 14 c2 -20 -10 -38 -26 -44 c12 12 22 28 26 40 c12 -18 36 -26 58 -18 c-22 4 -40 12 -52 24 c24 -6 44 2 56 18 c-18 -12 -40 -14 -62 -8z"/>
    <path transform="translate(90.8 68) scale(.8)" d="M164 170 c-22 -10 -48 -4 -60 12 c18 -8 40 -8 60 -6 c-16 -14 -38 -22 -56 -14 c22 0 42 6 56 14 c2 -20 -10 -38 -26 -44 c12 12 22 28 26 40 c12 -18 36 -26 58 -18 c-22 4 -40 12 -52 24 c24 -6 44 2 56 18 c-18 -12 -40 -14 -62 -8z"/>
  </g>
  <!-- surfer on a small wave -->
  <path class="swell" d="M520 318 C 600 296 660 296 700 318 C 720 330 760 330 800 316" fill="none" stroke="#e9fbff" stroke-width="5" stroke-linecap="round" opacity=".9"/>
  <g class="surfer" transform="translate(640 296)"><path d="M-22 6 Q0 12 24 4" stroke="{CORAL}" stroke-width="5" fill="none" stroke-linecap="round"/><path d="M-4 4 L0 -10 L5 4 M0 -10 L1 -22 M1 -18 L-10 -14 M1 -18 L12 -22" stroke="{INK}" stroke-width="3" fill="none" stroke-linecap="round"/><circle cx="2" cy="-27" r="4.4" fill="{INK}"/></g>
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
{FONTS}
<link rel="stylesheet" href="assets/css/site.css?v={ver('assets/css/site.css')}">
{extra}
</head>'''


NAV = [('#beaches', 'Beaches'), ('#outside', 'Get outside'), ('#eat', 'Eat and drink'), ('#events', 'Events'), ('#neighborhoods', 'Neighborhoods')]


def header():
    links = ''.join(f'<a href="{h}">{t}</a>' for h, t in NAV)
    return f'''<header class="top">
  <div class="top-in">
    <a class="brand" href="index.html"><img src="assets/img/mark.svg" alt="" width="40" height="40"><span>HB <em>Living</em></span></a>
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="nav">Menu</button>
    <nav id="nav" class="nav" aria-label="Main">{links}<a class="nav-cta" href="#letter">Get the letter</a></nav>
  </div>
</header>'''


def footer():
    return f'''<footer class="foot">
  <div class="foot-in">
    <div><a class="brand brand-foot" href="index.html"><img src="assets/img/mark.svg" alt="" width="36" height="36"><span>HB <em>Living</em></span></a>
    <p>The good life in Huntington Beach, California.  An independent local guide, not an official City of Huntington Beach website.</p></div>
    <nav aria-label="Footer">{''.join(f'<a href="{h}">{t}</a>' for h, t in NAV)}</nav>
    <small>&copy; {YEAR} HB Living.</small>
  </div>
</footer>
<script src="assets/js/site.js?v={ver('assets/js/site.js')}"></script>'''


def card(tag, title, text):
    return f'<article class="card"><span class="card-tag">{tag}</span><h3>{title}</h3><p>{text}</p></article>'


home = f'''{head('HB Living | The good life in Huntington Beach', 'HB Living: a local guide to life in Huntington Beach, California.  Beaches, the outdoors, places to eat, events and neighborhoods.')}
<body>
{header()}
<main>
  <section class="hero">
    <div class="hero-copy">
      <p class="kicker">Huntington Beach, California</p>
      <h1>Life is better <em>at the beach.</em></h1>
      <p class="lede">HB Living is a local's guide to Huntington Beach.  The best stretches of sand, sunset spots, places to eat, things to do this weekend and the neighborhoods that make it home.</p>
      <div class="cta-row"><a class="btn btn-coral" href="#beaches">Explore HB</a><a class="btn btn-ghost" href="#letter">Get the weekly letter</a></div>
    </div>
    {pier_scene()}
  </section>

  <section class="wrap" id="beaches">
    <div class="sec-head"><p class="kicker">Miles of coastline</p><h2>The <em>beaches</em></h2></div>
    <div class="grid4">
      {card('Downtown', 'The Pier and Main Street', 'The heart of town.  Walk the pier, watch the surfers, then head up Main Street for food and shops.')}
      {card('North', 'Bolsa Chica State Beach', 'Wide, open sand along Pacific Coast Highway, with fire rings and a long bike path.')}
      {card('Dogs welcome', 'Huntington Dog Beach', 'A stretch of shoreline where dogs can run off leash and make friends.')}
      {card('South', 'Huntington State Beach', 'Quieter sand running south to the Santa Ana River, with room to spread out.')}
    </div>
  </section>

  <section class="band" id="outside">
    <div class="wrap split">
      <div>
        <div class="sec-head"><p class="kicker">Beyond the sand</p><h2>Get <em>outside</em></h2></div>
        <p class="body-lg">Huntington Beach is more than the waves.  There are trails, wetlands and a huge city park, all a short ride from the coast.</p>
      </div>
      <ul class="list">
        <li><b>Huntington Central Park</b><span>Lakes, trails, a library and plenty of shade.</span></li>
        <li><b>Bolsa Chica Ecological Reserve</b><span>Wetland walks and some of the best bird watching on the coast.</span></li>
        <li><b>The beach bike path</b><span>Miles of flat riding along the sand, sunrise to sunset.</span></li>
        <li><b>Santa Ana River Trail</b><span>Ride inland from the river mouth along the water.</span></li>
      </ul>
    </div>
  </section>

  <section class="wrap" id="eat">
    <div class="sec-head"><p class="kicker">Coming soon</p><h2>Eat and <em>drink</em></h2></div>
    <div class="grid3">
      {card('Mornings', 'Coffee and breakfast', 'Where locals start the day before a surf or a walk on the sand.')}
      {card('Casual', 'Tacos and takeout', 'Fish tacos, burritos and beach-day food worth the drive.')}
      {card('Evenings', 'Sunset tables', 'Spots with a view for when the sky turns orange.')}
    </div>
    <p class="note">We're putting together our list now, with real picks from people who live here.</p>
  </section>

  <section class="wrap split" id="events">
    <div><div class="sec-head"><p class="kicker">On the calendar</p><h2>This <em>week</em> in HB</h2></div>
    <p class="body-lg">Farmers markets, surf contests, concerts in the park and the big events that bring the whole town out.  Our weekly roundup is coming soon.</p></div>
    <div class="soon-box"><b>Weekly events, coming soon</b><span>Sign up for the letter and we'll send the first one your way.</span></div>
  </section>

  <section class="band band-sand" id="neighborhoods">
    <div class="wrap">
      <div class="sec-head"><p class="kicker">Finding home</p><h2>The <em>neighborhoods</em></h2></div>
      <div class="grid3">
        {card('Close to the sand', 'Downtown and the coast', 'Walk to the pier, the beach and Main Street.  Lively, sunny and always something going on.')}
        {card('Room to grow', 'Family neighborhoods', 'Quiet streets, parks and schools, a short bike ride from the beach.')}
        {card('On the water', 'Harbor living', 'Homes along the channels, with docks out back and boats at the door.')}
      </div>
    </div>
  </section>

  <section class="wrap" id="letter">
    <div class="letter">
      <div><p class="kicker">The HB Living letter</p><h2>The best of the week, <em>once a week.</em></h2><p>Events, new spots and the little things that make Huntington Beach home.  Short, local and free.</p></div>
      <form class="letter-form" onsubmit="event.preventDefault(); this.querySelector('.form-msg').textContent = 'Thanks!  Sign-ups open soon.';">
        <label for="em">Email address</label>
        <div class="row"><input id="em" type="email" required placeholder="you@example.com"><button class="btn btn-coral" type="submit">Sign me up</button></div>
        <p class="form-msg" role="status"></p>
      </form>
    </div>
  </section>
</main>
{footer()}
</body>
</html>
'''

(ROOT / 'index.html').write_text(home)
print('built index.html')
