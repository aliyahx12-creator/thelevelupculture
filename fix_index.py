"""
Fix script for The Level Up Culture - index.html mobile bug
Run from inside the thelevelupculture folder:
  python fix_index.py
"""
import os, sys

# Get the directory this script lives in
here = os.path.dirname(os.path.abspath(__file__))
index_path = os.path.join(here, "index.html")

print(f"Reading: {index_path}")

with open(index_path, 'r', encoding='utf-8') as f:
    content = f.read()

print(f"File size: {len(content)} chars")

if len(content) < 1000:
    print("ERROR: File is too small - it's been overwritten with a stub.")
    print("Please restore index.html from GitHub history first.")
    input("Press Enter to close...")
    sys.exit(1)

changed = False

# Fix 1: Add principles-grid class
old1 = 'class="card-grid cols-3" style="margin-top:48px;max-width:900px;margin-inline:auto"'
new1 = 'class="card-grid cols-3 principles-grid" style="margin-top:48px;max-width:900px;margin-inline:auto"'
if old1 in content:
    content = content.replace(old1, new1)
    print("Fix 1 applied: principles-grid class added")
    changed = True
elif 'principles-grid' in content:
    print("Fix 1 already applied")
else:
    print("WARNING: Could not find principles grid element")

# Fix 2: Add mobile CSS
fix_css = '@media(max-width:768px){.principles-grid{grid-template-columns:1fr!important}}'
if fix_css not in content:
    last_style = content.rfind('</style>')
    if last_style != -1:
        content = content[:last_style] + '\n' + fix_css + '\n' + content[last_style:]
        print("Fix 2 applied: mobile CSS added")
        changed = True
    else:
        print("ERROR: Could not find </style> tag")
else:
    print("Fix 2 already applied")

if changed:
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"\nSUCCESS! File saved ({len(content)} chars)")
    print("Now open GitHub Desktop, commit and push.")
else:
    print("\nNo changes needed.")

input("Press Enter to close...")
