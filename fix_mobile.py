
# Run this script to fix the mobile principles grid issue
# Double-click this file or run: python fix_mobile.py

import re

path = r"C:\Users\LemurLee\Claude\Projects\🎮 The Level Up Culture\thelevelupculture\index.html"

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Step 1: Add class to principles grid
old_grid = 'class="card-grid cols-3" style="margin-top:48px;max-width:900px;margin-inline:auto"'
new_grid = 'class="card-grid cols-3 principles-grid" style="margin-top:48px;max-width:900px;margin-inline:auto"'
content = content.replace(old_grid, new_grid)

# Step 2: Add targeted mobile CSS
fix_css = '\n@media(max-width:768px){.principles-grid{grid-template-columns:1fr!important}}\n'
last_style = content.rfind('</style>')
content = content[:last_style] + fix_css + content[last_style:]

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Done! Now commit and push in GitHub Desktop.")
input("Press Enter to close...")
