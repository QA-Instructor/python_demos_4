import re

# \b matches a word boundary, beginning or end of a word
txt = 'Stranger in a strange land'
m = re.search(r'range\b', txt)
print(m.start())

# \B matches NOT a word boundary, embedded within a word
txt = 'Stranger in a strange land'
m = re.search(r'range\B', txt)
print(m.start())
