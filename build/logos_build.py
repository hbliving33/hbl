"""25 logo concepts for HBLiving, written to logos.html (not linked, noindex).  Concept 1 is the temporary site mark."""
import pathlib, math

ROOT = pathlib.Path(__file__).resolve().parent.parent
INK, SEA, GLASS, SAND, CORAL, GOLD, FOAM, PALMG = '#161310', '#138a43', '#9bd8a4', '#f3e4c8', '#d62b1f', '#f8b800', '#fbf7ef', '#2f8a63'
SERIF, SANS = "Fraunces, Georgia, serif", "Inter, system-ui, sans-serif"


def wave(y, x0=14, x1=106, amp=5, n=3, color=SEA, w=5):
    step = (x1 - x0) / n
    d = f'M{x0} {y}' + ''.join(f' q{step/4:.1f} {-amp} {step/2:.1f} 0 t{step/2:.1f} 0' for _ in range(n))
    return f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{w}" stroke-linecap="round"/>'


def rays(cx, cy, r1, r2, n=9, color=GOLD, w=4, start=0, span=180):
    out = ''
    for i in range(n):
        a = math.radians(start + span * i / (n - 1))
        out += f'<line x1="{cx + r1*math.cos(a):.1f}" y1="{cy - r1*math.sin(a):.1f}" x2="{cx + r2*math.cos(a):.1f}" y2="{cy - r2*math.sin(a):.1f}" stroke="{color}" stroke-width="{w}" stroke-linecap="round"/>'
    return out


def pier(y=70, x0=14, x1=106, color=INK, legs=6, w=4):
    gap = (x1 - x0) / (legs - 1)
    return (f'<path d="M{x0} {y} H{x1}" stroke="{color}" stroke-width="{w + 1}" stroke-linecap="round"/>' +
            ''.join(f'<path d="M{x0 + i*gap:.1f} {y} V{y + 18}" stroke="{color}" stroke-width="{w - 1}" stroke-linecap="round"/>' for i in range(legs)))


def palm(x, y, s=1, color=INK):
    return (f'<g transform="translate({x} {y}) scale({s})"><path d="M0 0 C -2 -20 0 -36 8 -52" fill="none" stroke="{color}" stroke-width="5" stroke-linecap="round"/>'
            f'<path d="M8 -52 c-12 -6 -26 -2 -32 8 c10 -6 22 -6 32 -4 c-8 -8 -20 -12 -30 -8 c12 0 22 4 30 8 c0 -12 -6 -22 -14 -26 c6 6 12 16 14 24 c6 -10 20 -14 32 -10 c-12 2 -22 6 -28 14 c14 -2 24 2 30 10 c-10 -6 -22 -8 -34 -4z" fill="{color}"/></g>')


def text(x, y, s, size, fill=INK, font=SERIF, weight=700, ls=0, anchor='middle', style=''):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="{font}" font-weight="{weight}" font-size="{size}" letter-spacing="{ls}" fill="{fill}"{style}>{s}</text>'


def star(cx, cy, r, color):
    pts = [f'{cx + (r if k % 2 == 0 else r*.42)*math.cos(math.radians(-90 + 36*k)):.1f},{cy + (r if k % 2 == 0 else r*.42)*math.sin(math.radians(-90 + 36*k)):.1f}' for k in range(10)]
    return f'<polygon points="{" ".join(pts)}" fill="{color}"/>'


SUN_PIER = f'<path d="M24 66 A36 36 0 0 1 96 66Z" fill="{GOLD}"/>{rays(60, 66, 42, 52, 9, CORAL, 4)}{pier(70, 10, 110)}{wave(100, 14, 106, 4, 3, SEA, 5)}'

LOGOS = [
 ('Golden Hour Pier', 'The pier on its pilings against a setting sun.  The classic HB view.', SUN_PIER),
 ('Sunset Stripes', 'A retro sun striped like a 1960s surf shop sign, sinking into the sea.',
  f'<defs><clipPath id="ss"><circle cx="60" cy="58" r="40"/></clipPath></defs><g clip-path="url(#ss)"><rect x="10" y="10" width="100" height="100" fill="{GOLD}"/>' +
  ''.join(f'<rect x="10" y="{50 + i*10}" width="100" height="{3 + i}" fill="{FOAM}"/>' for i in range(5)) + f'<rect x="10" y="62" width="100" height="48" fill="{CORAL}" opacity=".85"/></g>' + wave(100, 18, 102, 4, 3, SEA, 5)),
 ('HB Wave Monogram', 'A lowercase h and b joined by a breaking wave.',
  text(46, 82, 'h', 64, INK) + text(78, 82, 'b', 64, SEA) + f'<path d="M18 96 C 40 86 60 86 72 96 C 80 102 92 100 102 92" fill="none" stroke="{CORAL}" stroke-width="6" stroke-linecap="round"/>'),
 ('Palm and Sun', 'One tall palm leaning into the afternoon sun.',
  f'<circle cx="74" cy="48" r="22" fill="{GOLD}"/>{palm(44, 100, 1.05)}{wave(100, 18, 104, 4, 3, SEA, 5)}'),
 ('Lifeguard Tower', 'The lifeguard tower that dots the sand all along the coast.',
  f'<path d="M30 36 H90 L84 28 H36Z" fill="{CORAL}"/><rect x="34" y="36" width="52" height="28" rx="3" fill="{SEA}"/><rect x="42" y="42" width="36" height="12" rx="2" fill="{GLASS}"/><path d="M38 64 L30 102 M82 64 L90 102 M34 84 H86 M86 70 L104 98" stroke="{INK}" stroke-width="4" stroke-linecap="round"/><path d="M14 104 H106" stroke="{SAND}" stroke-width="6" stroke-linecap="round"/>'),
 ('Surfboard HB', 'A longboard standing on end, with HB down the stringer.',
  f'<path d="M60 10 C 80 30 82 84 60 112 C 38 84 40 30 60 10Z" fill="{FOAM}" stroke="{INK}" stroke-width="4"/><path d="M60 16 V106" stroke="{CORAL}" stroke-width="2"/>' + text(60, 58, 'H', 20, SEA, SANS, 800) + text(60, 82, 'B', 20, SEA, SANS, 800)),
 ('Badge', 'A round badge, like a beach permit sticker, with the pier in the middle.',
  f'<circle cx="60" cy="60" r="52" fill="{FOAM}" stroke="{INK}" stroke-width="4"/><circle cx="60" cy="60" r="40" fill="{GLASS}"/><path d="M30 58 A30 30 0 0 1 90 58Z" fill="{GOLD}"/>{pier(62, 24, 96, INK, 5, 3)}{wave(84, 30, 90, 3, 3, SEA, 4)}' +
  f'<path id="bt" d="M16 60 A44 44 0 0 1 104 60" fill="none"/><text font-family="{SANS}" font-weight="800" font-size="10" letter-spacing="2.4" fill="{INK}"><textPath href="#bt" startOffset="50%" text-anchor="middle">HBLIVING</textPath></text>'),
 ('Script Sunset', 'A flowing script wordmark over a low sun.  Easygoing and warm.',
  f'<path d="M20 84 A40 40 0 0 1 100 84Z" fill="{GOLD}" opacity=".9"/>' + text(60, 78, 'HB', 46, INK, SERIF, 700, 0, 'middle', ' font-style="italic"') + wave(98, 18, 102, 3, 3, CORAL, 4)),
 ('Compass Rose', 'A compass pointing west to the water.  Find your way to the coast.',
  f'<circle cx="60" cy="60" r="44" fill="none" stroke="{INK}" stroke-width="3"/><path d="M60 18 L68 60 L60 102 L52 60Z" fill="{INK}"/><path d="M18 60 L60 52 L102 60 L60 68Z" fill="{SEA}"/><path d="M18 60 L60 52 L60 68Z" fill="{CORAL}"/><circle cx="60" cy="60" r="6" fill="{GOLD}"/>' + text(10, 64, 'W', 11, CORAL, SANS, 800, 0, 'start')),
 ('Home by the Sea', 'A simple house with a wave rolling through the door.  Living, right at the beach.',
  f'<path d="M20 58 L60 22 L100 58" fill="none" stroke="{INK}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/><path d="M30 54 V100 H90 V54" fill="none" stroke="{INK}" stroke-width="7" stroke-linejoin="round"/><path d="M40 92 C 44 70 64 62 76 72 C 82 78 78 86 72 84" fill="none" stroke="{SEA}" stroke-width="7" stroke-linecap="round"/>'),
 ('Tricolor Pier', 'The pier crossing a sunset in red, gold and green bands.',
  f'<defs><clipPath id="tp"><circle cx="60" cy="58" r="44"/></clipPath></defs><g clip-path="url(#tp)"><rect x="10" y="10" width="100" height="32" fill="{CORAL}"/><rect x="10" y="42" width="100" height="22" fill="{GOLD}"/><rect x="10" y="64" width="100" height="50" fill="{SEA}"/></g>{pier(62, 18, 102, INK, 6, 3.4)}<circle cx="60" cy="58" r="44" fill="none" stroke="{INK}" stroke-width="4"/>'), ('Pier Lines', 'The pier drawn in clean, simple lines, the way it looks from the sand.',
  f'<path d="M10 54 H110" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>' + ''.join(f'<path d="M{x} 54 V{80 + (x % 20) / 4}" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>' for x in range(16, 110, 12)) + f'<path d="M84 54 V40 H104 V54 M82 40 L94 32 L106 40" fill="none" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/>{wave(92, 10, 110, 4, 4, SEA, 4)}{wave(104, 22, 98, 3, 3, GLASS, 3)}'),
 ('Rasta Wave', 'One curling wave drawn in three bands of red, gold and green.',
  ''.join(f'<path d="M{16 + k*4} {92 - k*8} C {28 + k*4} {56 - k*8} {58 + k*2} {40 - k*6} {82 - k*2} {46 - k*4} C {98 - k*2} {50 - k*4} {96 - k*2} {70 - k*6} {82 - k*2} {70 - k*6}" fill="none" stroke="{c}" stroke-width="8" stroke-linecap="round"/>' for k, c in enumerate([SEA, GOLD, CORAL])) + f'<path d="M14 102 H106" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>'), ('Beach Cruiser', 'A beach cruiser bike, the way most of HB gets to the sand.',
  f'<circle cx="34" cy="78" r="18" fill="none" stroke="{INK}" stroke-width="5"/><circle cx="88" cy="78" r="18" fill="none" stroke="{INK}" stroke-width="5"/><path d="M34 78 L52 52 L82 52 L88 78 M52 52 L60 78 L34 78 M82 52 L78 40 L90 38 M52 52 L48 44 H58" fill="none" stroke="{CORAL}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/><circle cx="60" cy="78" r="3" fill="{INK}"/>'),
 ('Bird of the Coast', 'A pelican gliding over the waves, a familiar sight off the pier.',
  f'<circle cx="86" cy="36" r="12" fill="{GOLD}"/><path d="M14 64 C 30 50 46 48 58 58 C 70 46 88 44 104 54 C 90 54 76 58 66 66 L 58 70 C 50 64 32 60 14 64Z" fill="{INK}"/><path d="M58 58 C 56 52 60 46 66 46 C 72 46 74 52 70 56 L 92 60 L 70 62Z" fill="{INK}"/><path d="M70 60 L92 60 L72 64Z" fill="{CORAL}"/>{wave(92, 14, 106, 5, 4, SEA, 6)}'),
 ('Stacked Wordmark', 'HB in a big, warm serif with LIVING spaced out underneath.  Clean and classic.',
  text(60, 70, 'HB', 56, INK) + f'<path d="M22 80 H98" stroke="{CORAL}" stroke-width="3"/>' + text(60, 98, 'LIVING', 13, SEA, SANS, 700, 5)),
 ('Postcard Stamp', 'A vintage postage stamp with a sunset over the water.',
  f'<rect x="18" y="14" width="84" height="92" fill="{FOAM}" stroke="{INK}" stroke-width="3" stroke-dasharray="5 3"/><rect x="26" y="22" width="68" height="62" fill="#ffd9a8"/><circle cx="60" cy="66" r="16" fill="{CORAL}"/><rect x="26" y="66" width="68" height="18" fill="{SEA}"/>{pier(66, 30, 90, INK, 5, 2.4)}' + text(60, 100, 'HB', 12, INK, SANS, 800, 3)),
 ('Tide Circle', 'A circle split by the tide line: sky above, sea below.',
  f'<defs><clipPath id="tc"><circle cx="60" cy="60" r="46"/></clipPath></defs><g clip-path="url(#tc)"><rect x="10" y="10" width="100" height="56" fill="#ffd9a8"/><circle cx="60" cy="66" r="18" fill="{GOLD}"/><path d="M10 64 q12.5 -7 25 0 t25 0 t25 0 t25 0 V110 H10Z" fill="{SEA}"/><path d="M10 80 q12.5 -6 25 0 t25 0 t25 0 t25 0" fill="none" stroke="{GLASS}" stroke-width="3"/></g><circle cx="60" cy="60" r="46" fill="none" stroke="{INK}" stroke-width="4"/>'),
 ('Flip Flops', 'A pair of flip flops in the sand.  Shoes optional.',
  f'<path d="M30 20 C 46 20 50 40 48 64 C 46 90 42 104 32 104 C 22 104 18 90 18 64 C 16 40 18 20 30 20Z" fill="{CORAL}"/><path d="M72 26 C 88 26 92 46 90 70 C 88 96 84 108 74 108 C 64 108 60 96 60 70 C 58 46 60 26 72 26Z" fill="{SEA}"/><path d="M22 52 L33 34 L44 52 M64 58 L75 40 L86 58" fill="none" stroke="{FOAM}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>'),
 ('Sun Rays HB', 'HB set inside a rising sun, with rays fanning out.',
  rays(60, 86, 46, 58, 11, GOLD, 5) + f'<path d="M18 86 A42 42 0 0 1 102 86Z" fill="{CORAL}"/>' + text(60, 80, 'HB', 30, FOAM, SANS, 800, 1) + f'<path d="M12 92 H108" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>'),
 ('Lion Sun', 'A lion whose mane is a sunburst of red, gold and green dreadlocks.',
  ''.join(f'<path d="M{60 + 26*math.cos(math.radians(a)):.1f} {58 - 26*math.sin(math.radians(a)):.1f} L{60 + 50*math.cos(math.radians(a)):.1f} {58 - 50*math.sin(math.radians(a)):.1f}" stroke="{[CORAL, GOLD, SEA][i % 3]}" stroke-width="8" stroke-linecap="round"/>' for i, a in enumerate(range(0, 360, 20))) +
  f'<circle cx="60" cy="58" r="26" fill="#d9952f"/><path d="M48 64 C 50 76 70 76 72 64 C 70 70 50 70 48 64Z" fill="#f3d9a6"/><circle cx="51" cy="52" r="3" fill="{INK}"/><circle cx="69" cy="52" r="3" fill="{INK}"/><path d="M55 60 H65 L60 66Z" fill="{INK}"/>'), ('Coastline Map', 'The curve of the HB coastline with a pin dropped on the beach.',
  f'<path d="M14 24 C 34 40 46 52 60 70 C 72 86 90 96 108 102" fill="none" stroke="{SEA}" stroke-width="7" stroke-linecap="round"/><path d="M14 36 C 32 52 44 62 56 78 C 68 94 86 104 104 110" fill="none" stroke="{GLASS}" stroke-width="4" stroke-linecap="round" opacity=".8"/><path d="M60 62 C 48 62 42 52 42 44 C 42 32 50 24 60 24 C 70 24 78 32 78 44 C 78 52 72 62 60 62Z M60 62 L60 74" fill="{CORAL}" stroke="{CORAL}" stroke-width="3" stroke-linecap="round"/><circle cx="60" cy="43" r="7" fill="{FOAM}"/>'),
 ('Wave Seal', 'A modern seal with a single curling wave, made for a phone icon.',
  f'<rect x="12" y="12" width="96" height="96" rx="26" fill="{SEA}"/><path d="M26 84 C 30 54 52 36 74 40 C 92 44 92 66 78 68 C 68 70 66 60 72 56" fill="none" stroke="{FOAM}" stroke-width="9" stroke-linecap="round"/><path d="M22 92 H98" stroke="{GOLD}" stroke-width="5" stroke-linecap="round"/>'),
 ('Lowercase Living', 'A relaxed, all-lowercase wordmark with living set in italic underneath.',
  text(60, 72, 'hb', 50, INK, SERIF, 600) + text(60, 98, 'living', 22, SEA, SERIF, 400, 1, 'middle', ' font-style="italic"')),
 ('Pier at Night', 'The pier lit up against the night sky, with a crescent moon and stars.',
  f'<rect x="10" y="10" width="100" height="100" rx="24" fill="{INK}"/><path d="M80 26 a12 12 0 1 0 10 20 a10 10 0 1 1 -10 -20Z" fill="{GOLD}"/>' + star(34, 30, 3.4, FOAM) + star(52, 22, 2.4, FOAM) + star(64, 38, 2, FOAM) +
  pier(70, 18, 102, GLASS, 6, 3) + ''.join(f'<circle cx="{x}" cy="64" r="2" fill="{GOLD}"/>' for x in range(26, 100, 14)) + wave(96, 20, 100, 3, 3, SEA, 4)),
]


def mark(svg, size=120):
    return f'<svg viewBox="0 0 120 120" width="{size}" height="{size}" role="img" aria-hidden="true">{svg}</svg>'


cards = ''
for i, (name, desc, svg) in enumerate(LOGOS, 1):
    cards += f'''
  <article class="lc" id="logo-{i}">
    <div class="lc-main">{mark(svg, 92)}<div class="lc-word"><b>HB<em>Living</em></b><small>Huntington Beach, California</small></div></div>
    <div class="lc-alt">
      <div class="lc-dark">{mark(svg, 54)}<span>HBLiving</span></div>
      <div class="lc-icon" title="Phone app icon">{mark(svg, 46)}</div>
    </div>
    <h2><span class="lc-num">{i}</span>{name}</h2>
    <p>{desc}</p>
  </article>'''

html = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Logo Options | HBLiving</title>
<meta name="robots" content="noindex">
<link rel="icon" href="assets/img/mark.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,600;9..144,700&family=Inter:wght@400;600;700;800&display=swap" rel="stylesheet">
<style>
  :root {{ --ink: {INK}; --sea: {SEA}; --coral: {CORAL}; --muted: #4f6573; --line: #e4d8c2; }}
  * {{ box-sizing: border-box; }}
  body {{ margin: 0; font-family: Inter, system-ui, sans-serif; color: var(--ink); background: linear-gradient(180deg, #ffe9b0, #fbf7ef 340px); }}
  header {{ max-width: 1180px; margin: 0 auto; padding: 44px 20px 8px; }}
  .kicker {{ font-size: 13px; font-weight: 700; letter-spacing: .14em; text-transform: uppercase; color: var(--sea); }}
  h1 {{ font-family: Fraunces, Georgia, serif; font-size: clamp(36px, 6vw, 58px); margin: 6px 0 10px; }}
  h1 em, .lc-word em {{ color: var(--coral); }}
  header p {{ max-width: 700px; color: var(--muted); font-size: 17px; }}
  .grid {{ max-width: 1180px; margin: 24px auto 60px; padding: 0 20px; display: grid; grid-template-columns: repeat(auto-fill, minmax(330px, 1fr)); gap: 18px; }}
  .lc {{ background: #fffdf8; border: 1px solid var(--line); border-radius: 22px; padding: 22px; box-shadow: 0 12px 28px rgba(22, 19, 16, .08); }}
  .lc-main {{ display: flex; align-items: center; gap: 14px; }}
  .lc-word b {{ display: block; font-family: Fraunces, Georgia, serif; font-size: 28px; line-height: 1; }}
  .lc-word em {{ font-weight: 400; }}
  .lc-word small {{ color: var(--muted); font-size: 13px; }}
  .lc-alt {{ display: flex; gap: 12px; margin-top: 16px; align-items: center; }}
  .lc-dark {{ flex: 1; display: flex; align-items: center; gap: 8px; background: var(--ink); border-radius: 14px; padding: 6px 10px; }}
  .lc-dark svg {{ background: #fbf7ef; border-radius: 50%; padding: 3px; }}
  .lc-dark span {{ font-family: Fraunces, Georgia, serif; font-weight: 700; color: #fff; font-size: 18px; }}
  .lc-icon {{ width: 62px; height: 62px; border-radius: 15px; background: #fff; border: 1px solid var(--line); box-shadow: 0 4px 10px rgba(22, 19, 16, .12); display: grid; place-items: center; }}
  .lc h2 {{ display: flex; align-items: center; gap: 8px; font-family: Fraunces, Georgia, serif; font-size: 22px; margin: 18px 0 4px; }}
  .lc-num {{ width: 28px; height: 28px; flex: none; border-radius: 50%; background: var(--ink); color: #fff; display: grid; place-items: center; font-family: Inter, sans-serif; font-size: 14px; font-weight: 800; }}
  .lc p {{ margin: 0; color: var(--muted); font-size: 15px; }}
</style>
</head>
<body>
<header>
  <div class="kicker">Logo options</div>
  <h1>Pick a <em>favorite</em>.</h1>
  <p>Twenty-five ideas for the HBLiving logo, in red, gold and green.  Each card shows the logo with the name, on a dark background, and as a phone app icon.  Tell us the number you like, or mix and match.</p>
</header>
<main class="grid">{cards}
</main>
</body>
</html>
'''
(ROOT / 'logos.html').write_text(html)
(ROOT / 'assets' / 'img' / 'mark.svg').write_text(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120">{SUN_PIER}</svg>\n')
print('logos', len(LOGOS))
