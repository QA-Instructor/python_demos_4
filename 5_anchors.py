import re
import sys
import os

name, old, new = sys.argv[1:]

new_name = re.sub(fr"\.{old}$", f".{new}", name)
print(f"Renaming {name} to {new_name}")
os.rename(name, new_name)

# project:
# create a file called sales.xlsx
# terminal:
# python 5_anchors.py sales.xlsx xlsx csv
