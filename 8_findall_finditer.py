import re

test_string = '/dev/sd3d 135398 69683 52176 57% /home/stuff'

# findall returns a list
numbers = re.findall(r'\b\d+\b', test_string)
print(numbers)

# finditer returns an iterator
for match in re.finditer(r'\b(\d+)\b', test_string):
    print(match.groups())

