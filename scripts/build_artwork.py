"""Build self-contained GitHub profile artwork, with light/dark and reduced-motion support."""
from pathlib import Path
from xml.etree import ElementTree

ROOT = Path(__file__).resolve().parents[1]


def frame(title, description, height, colors, content):
    bg, panel, line, text, muted, green, amber = colors
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="{height}" viewBox="0 0 1000 {height}" role="img" aria-labelledby="title desc">
<title id="title">{title}</title><desc id="desc">{description}</desc>
<defs>
<pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse"><path d="M32 0H0V32" fill="none" stroke="{line}" stroke-width=".6"/></pattern>
<radialGradient id="halo"><stop stop-color="{green}" stop-opacity=".12"/><stop offset="1" stop-color="{bg}" stop-opacity="0"/></radialGradient>
</defs>
<style>
text {{ font-family: ui-monospace, 'Liberation Mono', Consolas, monospace; }}
.label {{ fill:{muted}; font-size:12px; letter-spacing:2px; }}
.orbit {{ transform-origin:800px 174px; animation:rotate 40s linear infinite; }}
.signal {{ animation:signal 5s ease-in-out infinite; }}
.cursor {{ animation:blink 1.4s step-end infinite; }}
@keyframes rotate {{ to {{ transform:rotate(360deg); }} }}
@keyframes signal {{ 50% {{ opacity:.35; }} }}
@keyframes blink {{ 50% {{ opacity:0; }} }}
@media (prefers-reduced-motion: reduce) {{ .orbit,.signal,.cursor {{ animation:none; }} }}
</style>
<rect x="1" y="1" width="998" height="{height-2}" rx="18" fill="{bg}" stroke="{line}"/>
{content}
</svg>'''


for theme, colors in {
    'dark': ('#080f10', '#101c1b', '#263f39', '#eff8f2', '#9bb9ac', '#59efa5', '#edc775'),
    'light': ('#f4f8f3', '#e6eee5', '#c8d6ca', '#152b23', '#526c5d', '#137a4b', '#896215'),
}.items():
    bg, panel, line, text, muted, green, amber = colors
    header = f'''
<rect x="18" y="18" width="964" height="324" rx="10" fill="url(#grid)" opacity=".6"/>
<circle cx="800" cy="174" r="168" fill="url(#halo)"/>
<path d="M40 70V40H70 M930 40H960V70 M40 290V320H70 M930 320H960V290" fill="none" stroke="{green}" stroke-width="2"/>
<text x="64" y="72" class="label">ADAM-ZS / PERSONAL LAB</text>
<circle cx="627" cy="67" r="4" fill="{amber}" class="signal"/>
<text x="60" y="166" fill="{text}" font-size="82" font-weight="700" letter-spacing="-5">ADAM ZS<tspan fill="{green}">.</tspan></text>
<text x="64" y="212" fill="{green}" font-size="23">Security research. Thoughtful engineering.</text>
<text x="64" y="250" fill="{muted}" font-size="17">Understand the system. Build something better.</text>
<path d="M64 277H618" stroke="{line}"/>
<text x="64" y="304" class="label">01 / SOFTWARE</text><text x="254" y="304" class="label">02 / SYSTEMS</text><text x="439" y="304" class="label">03 / HARDWARE</text>
<circle cx="800" cy="174" r="108" stroke="{line}" fill="none"/>
<circle cx="800" cy="174" r="91" stroke="{green}" stroke-width="1.5" stroke-dasharray="3 12" fill="none" class="orbit"/>
<path d="M800 103L862 138V210L800 245L738 210V138Z" fill="{panel}" stroke="{green}" stroke-width="1.5"/>
<path d="M763 200L783 150L803 200M771 184H795M815 151H840L813 198H840" fill="none" stroke="{text}" stroke-width="5" stroke-linecap="square" stroke-linejoin="miter"/>
<path d="M691 174H661M908 174H938M800 65V45M800 283V303" stroke="{green}"/>
<circle cx="692" cy="174" r="4" fill="{amber}"/><circle cx="908" cy="174" r="4" fill="{green}" class="signal"/>
<text x="800" y="326" text-anchor="middle" class="label">RESEARCH / BUILD / REFINE</text>'''
    terminal = f'''
<path d="M18 1H982Q999 1 999 18V47H1V18Q1 1 18 1" fill="{panel}"/>
<circle cx="28" cy="24" r="5" fill="{amber}"/><circle cx="48" cy="24" r="5" fill="{muted}"/><circle cx="68" cy="24" r="5" fill="{green}"/>
<text x="500" y="29" text-anchor="middle" class="label">adam@lab: ~/workspace</text>
<g font-size="19">
<text x="32" y="88" fill="{green}">adam@lab<tspan fill="{muted}">:~$ </tspan><tspan fill="{text}">cat focus.txt</tspan></text>
<text x="32" y="123" fill="{muted}">Security research / developer tools / hardware curiosity</text>
<text x="32" y="177" fill="{green}">adam@lab<tspan fill="{muted}">:~$ </tspan><tspan fill="{text}">ls projects/</tspan></text>
<text x="32" y="212" fill="{amber}">honeysentinel/</text><text x="276" y="212" fill="{muted}">capture - investigate - share</text>
<text x="32" y="266" fill="{green}">adam@lab<tspan fill="{muted}">:~$ </tspan><tspan fill="{text}">printf 'Stay curious. Keep building.'</tspan></text>
<text x="32" y="301" fill="{text}">Stay curious. Keep building.</text>
<text x="32" y="356" fill="{green}">adam@lab<tspan fill="{muted}">:~$</tspan></text>
<rect x="188" y="339" width="11" height="21" fill="{green}" class="cursor"/>
</g>
<text x="966" y="357" text-anchor="end" class="label">A PERSONAL WORKSPACE, ALWAYS EVOLVING</text>'''
    signals = f'''
<text x="32" y="40" class="label">HOW I LIKE TO WORK</text>
<path d="M80 98H920" fill="none" stroke="{line}" stroke-width="2"/>
<path d="M80 98H920" fill="none" stroke="{green}" stroke-dasharray="8 18" opacity=".55"/>
<g font-size="23" fill="{text}">
<circle cx="80" cy="98" r="9" fill="{green}"/><text x="80" y="149">Explore</text>
<circle cx="360" cy="98" r="9" fill="{amber}"/><text x="360" y="149">Build</text>
<circle cx="680" cy="98" r="9" fill="{green}" class="signal"/><text x="680" y="149">Refine</text>
</g>
<g font-size="15" fill="{muted}"><text x="80" y="181">Ask better questions.</text><text x="360" y="181">Turn ideas into tools.</text><text x="680" y="181">Test. Document. Repeat.</text></g>'''
    for name, title, description, height, body in [
        ('header', 'Adam ZS — security research and engineering', 'A green and amber circuit-inspired personal banner with an AZ monogram. Software, systems, and hardware.', 360, header),
        ('terminal', "Inside Adam's workspace", 'Security research, developer tools, and hardware curiosity. Current project: HoneySentinel. Stay curious. Keep building.', 390, terminal),
        ('signals', 'Explore. Build. Refine.', 'Ask better questions, turn ideas into tools, and test, document, and repeat. Decorative workflow, not live statistics.', 216, signals),
    ]:
        svg = frame(title, description, height, colors, body)
        ElementTree.fromstring(svg)
        (ROOT / 'assets' / f'{name}-{theme}.svg').write_text(svg)
print('Built and XML-validated six self-contained SVGs.')
