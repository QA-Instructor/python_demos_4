import re
from datetime import date

print(date.today())
year = str(date.today())[:4]
print(year)

copyright_string = 'copyright 2005-2006'
print(re.sub(r'((19|20)[0-9]{2})-((19|20)[0-9]{2})', r'\1-' + year, copyright_string))

copyright_string2 = 'copyright 1996-2014'
print(re.sub(r'((19|20)[0-9]{2})-((19|20)[0-9]{2})', r'\1-' + year, copyright_string2))
