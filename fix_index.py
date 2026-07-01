
import urllib.request, os

url = "https://raw.githubusercontent.com/aliyahx12-creator/thelevelupculture/8052601eaf1b9634f4e9bb991a19c18379569ed8/index.html"
here = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(here, "index.html")

print("Fetching good version from GitHub history...")
with urllib.request.urlopen(url) as r:
    content = r.read().decode('utf-8')
print(f"Got {len(content)} chars")

# Add principles-grid class
content = content.replace(
    'class="card-grid cols-3" style="margin-top:48px;max-width:900px;margin-inline:auto"',
    'class="card-grid cols-3 principles-grid" style="margin-top:48px;max-width:900px;margin-inline:auto"'
)

# Add mobile CSS fix
fix_css = '\n/* PRINCIPLES GRID MOBILE FIX */\n@media(max-width:768px){.principles-grid{grid-template-columns:1fr!important}.principles-grid .card{grid-column:span 1!important}}\n'
content = content.replace('<style>\n@keyframes marquee', '<style>' + fix_css + '@keyframes marquee')

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"SUCCESS! Wrote {len(content)} chars to index.html")
print("Now open GitHub Desktop, commit and push.")
input("Press Enter to close...")
