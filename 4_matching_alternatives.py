import re

# This example can match 3 alternatives
drink = 'A glass of Coors'
if re.search(r'Bud|Miller|Coors', drink):
    print("It's a beer!")

# This example can match 9 combinations
pattern = r'A (glass|bottle|barrel) of (Bud|Miller|Coors)'

if re.search(pattern, drink):
    print("This drink is suitable for Americans")
