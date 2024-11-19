import re

test_string = 'Perl for Perl Programmers'
# sub

new_string = re.sub('Perl', 'Python', test_string)
print(new_string)

# subn
new_string, number = re.subn('Perl', 'Python', test_string)
if number:
    print(new_string)
    print(number)

# subn with only 1 substitution
new_string, number = re.subn('Perl', 'Python', test_string, 1)
if number:
    print(new_string)
    print(number)
