import urllib.request, os

url = "https://raw.githubusercontent.com/aliyahx12-creator/thelevelupculture/main/index.html"
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "index.html")

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

print(f"Current file size: {len(content)} chars")

# Add principles-grid class to the principles card grid
old_grid = 'class="card-grid cols-3" style="margin-top:48px;max-width:900px;margin-inline:auto"'
new_grid = 'class="card-grid cols-3 principles-grid" style="margin-top:48px;max-width:900px;margin-inline:auto"'

if old_grid in content:
    content = content.replace(old_grid, new_grid)
    print("Step 1 done: Added principles-grid class")
elif 'principles-grid' in content:
    print("Step 1 already done")
else:
    print("ERROR: Could not find principles grid")

# Add mobile CSS fix
fix_css = '@media(max-width:768px){.principles-grid{grid-template-columns:1fr!important}}'
if fix_css not in content:
    last_style = content.rfind('</style>')
    content = content[:last_style] + '\n' + fix_css + '\n' + content[last_style:]
    print("Step 2 done: Added mobile CSS")
else:
    print("Step 2 already done")

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Fixed file size: {len(content)} chars")
print("SUCCESS - Now open GitHub Desktop, commit and push")
input("Press Enter to close...")
