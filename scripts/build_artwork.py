"""Generate original SVG panels with static fallbacks and reduced-motion support."""
from pathlib import Path
from xml.etree import ElementTree

ROOT = Path(__file__).resolve().parents[1]
THEMES = {
    "dark": ("#080f10", "#101c1b", "#263f39", "#eff8f2", "#9bb9ac", "#59efa5", "#edc775"),
    "light": ("#f4f8f3", "#e6eee5", "#c8d6ca", "#152b23", "#526c5d", "#137a4b", "#896215"),
}


def save(name, title, height, body, width=1000):
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title">
<title id="title">{title}</title>
<defs>
<pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse"><path d="M32 0H0V32" fill="none" stroke="{line}" stroke-width=".6"/></pattern>
<radialGradient id="halo"><stop stop-color="{green}" stop-opacity=".18"/><stop offset="1" stop-color="{bg}" stop-opacity="0"/></radialGradient>
<linearGradient id="trace"><stop stop-color="{green}" stop-opacity="0"/><stop offset=".5" stop-color="{green}"/><stop offset="1" stop-color="{amber}" stop-opacity=".2"/></linearGradient>
</defs>
<style>
text {{ font-family:ui-monospace,'Liberation Mono',Consolas,monospace; fill:{text}; }}
.label {{ fill:{muted}; font-size:14px; letter-spacing:2px; }}
.orbit {{ transform-origin:790px 180px; animation:rotate 48s linear infinite; }}
.reverse {{ animation-direction:reverse; animation-duration:65s; }}
.signal {{ animation:pulse 5s ease-in-out infinite; }}
.flow {{ stroke-dasharray:8 28; animation:flow 14s linear infinite; }}
.cursor {{ animation:blink 1.4s step-end infinite; }}
@keyframes rotate {{ to {{ transform:rotate(360deg); }} }}
@keyframes pulse {{ 50% {{ opacity:.35; }} }}
@keyframes flow {{ to {{ stroke-dashoffset:-360; }} }}
@keyframes blink {{ 50% {{ opacity:0; }} }}
@media(prefers-reduced-motion:reduce) {{ .orbit,.signal,.flow,.cursor {{ animation:none; }} }}
</style>
<rect x="1" y="1" width="{width-2}" height="{height-2}" rx="18" fill="{bg}" stroke="{line}"/>
{body}
</svg>
'''
    ElementTree.fromstring(svg)
    (ROOT / "assets" / f"{name}-{theme}.svg").write_text(svg)


for theme, colors in THEMES.items():
    bg, panel, line, text, muted, green, amber = colors
    save("header", "Adam ZS · Cybersecurity Engineer", 360, f'''
<rect x="18" y="18" width="964" height="324" rx="10" fill="url(#grid)"/>
<circle cx="790" cy="180" r="172" fill="url(#halo)"/>
<path d="M40 74V40H74 M926 40H960V74 M40 286V320H74 M926 320H960V286" fill="none" stroke="{green}" stroke-width="2"/>
<text x="64" y="77" class="label">/ HOME / ADAM-ZS</text>
<text x="58" y="188" font-size="102" font-weight="700" letter-spacing="-7">ADAM ZS<tspan style="fill:{green}">.</tspan></text>
<text x="64" y="240" style="fill:{green}" font-size="22" letter-spacing="3">CYBERSECURITY ENGINEER</text>
<path d="M64 274H584" stroke="{line}"/>
<path d="M64 274H584" stroke="url(#trace)" class="flow" stroke-width="2"/>
<text x="64" y="308" class="label">PERSONAL LAB</text>
<circle cx="555" cy="302" r="4" fill="{amber}" class="signal"/>
<circle cx="790" cy="180" r="122" stroke="{line}" fill="none"/>
<g class="orbit"><circle cx="790" cy="180" r="104" stroke="{green}" stroke-dasharray="2 13" fill="none"/><circle cx="894" cy="180" r="5" fill="{amber}"/></g>
<circle cx="790" cy="180" r="137" stroke="{muted}" stroke-dasharray="64 180 12 100" fill="none" class="orbit reverse"/>
<path d="M790 109L852 144V216L790 251L728 216V144Z" fill="{panel}" stroke="{green}" stroke-width="1.5"/>
<path d="M753 206L773 156L793 206M761 190H785M805 157H830L803 204H830" fill="none" stroke="{text}" stroke-width="5"/>
<path d="M637 180H660M920 180H943M790 26V48M790 313V334" stroke="{green}"/>
''')
    chips = ""
    for row, labels in enumerate([
        ["PYTHON", "C++", "JAVASCRIPT", "REACT"],
        ["LINUX", "DOCKER", "GIT", "ARDUINO"],
    ]):
        for col, label in enumerate(labels):
            x, y = 290 + col * 166, 76 + row * 70
            chips += f'<rect x="{x}" y="{y}" width="150" height="50" rx="8" fill="{panel}" stroke="{line}"/><circle cx="{x+17}" cy="{y+25}" r="3" fill="{amber if row else green}"/><text x="{x+85}" y="{y+31}" text-anchor="middle" font-size="16">{label}</text>'
    save("signals", "Toolbox · Python, C++, JavaScript, React, Linux, Docker, Git, Arduino", 242, f'''
<text x="32" y="39" class="label">01 / TOOLBOX</text>
<path d="M62 117H100M62 155H100M214 117H252M214 155H270V100H290M130 68V92M168 68V92M130 180V214M168 180V214" fill="none" stroke="{line}" stroke-width="2"/>
<path d="M214 155H270V100H290" fill="none" stroke="{green}" class="flow" stroke-width="2"/>
<rect x="100" y="92" width="114" height="88" rx="14" fill="{panel}" stroke="{green}"/>
<path d="M141 118L124 136L141 154M173 118L190 136L173 154M163 112L151 160" fill="none" stroke="{text}" stroke-width="3"/>
{chips}
''')
    honeycomb = ""
    for x, y in [(794, 109), (850, 141), (794, 173), (738, 141), (850, 77), (738, 77)]:
        honeycomb += f'<path d="M{x} {y-30}l26 15v30l-26 15-26-15v-30Z" fill="{panel}" stroke="{amber}" stroke-opacity=".55"/>'
    save("project", "HoneySentinel AI · collaborative capstone · open development fork", 242, f'''
<rect x="18" y="18" width="964" height="206" rx="10" fill="url(#grid)" opacity=".5"/>
<text x="32" y="40" class="label">02 / CAPSTONE</text>
<text x="40" y="111" font-size="44" font-weight="700" letter-spacing="-2">HoneySentinel<tspan style="fill:{amber}"> AI</tspan></text>
<text x="42" y="151" class="label">HONEYPOT / THREAT INTELLIGENCE</text>
<rect x="40" y="181" width="226" height="34" rx="17" fill="{panel}" stroke="{line}"/>
<text x="58" y="203" font-size="14">OPEN DEVELOPMENT FORK</text>
{honeycomb}
<circle cx="794" cy="109" r="8" fill="{amber}" class="signal"/>
<path d="M925 197H955V167M953 169L920 202" fill="none" stroke="{green}" stroke-width="2"/>
''')
    save("terminal", "adam@lab · build, break, repeat", 142, f'''
<circle cx="32" cy="28" r="4" fill="{amber}"/><circle cx="49" cy="28" r="4" fill="{muted}"/><circle cx="66" cy="28" r="4" fill="{green}"/>
<path d="M24 47H976" stroke="{line}"/>
<text x="32" y="97" font-size="24"><tspan style="fill:{green}">adam@lab</tspan><tspan style="fill:{muted}">:~$ </tspan>build. break. repeat.</text>
<rect x="505" y="77" width="12" height="25" fill="{green}" class="cursor"/>
<path d="M738 96H780L792 74L810 113L830 61L852 105L867 96H955" fill="none" stroke="{line}" stroke-width="2"/>
<path d="M738 96H780L792 74L810 113L830 61L852 105L867 96H955" fill="none" stroke="{green}" stroke-width="2" class="flow"/>
''')
    for name, label, icon in [
        ("portfolio", "PORTFOLIO", "M24 27H48V49H24ZM24 34H48M30 30H31M35 30H36"),
        ("repos", "REPOS", "M29 26V49M29 32H40Q46 32 46 38V49M25 26H33M25 49H33M42 49H50"),
        ("connect", "CONNECT", "M25 32L36 25L47 32V45L36 52L25 45ZM25 32L47 45M47 32L25 45"),
        ("coffee", "COFFEE", "M25 31H44V44Q44 52 35 52Q25 52 25 44ZM44 34H49Q56 40 44 44M29 25V20M36 25V20"),
    ]:
        save(f"nav-{name}", label, 76, f'<path d="{icon}" fill="none" stroke="{green}" stroke-width="2" stroke-linejoin="round"/><text x="68" y="44" font-size="17" letter-spacing="1">{label}</text><path d="M213 30L221 38L213 46" fill="none" stroke="{amber}" stroke-width="2"/>', width=240)

print("Built and XML-validated 16 themed SVG assets.")
