import re

test_string = 'The quick brown fox jumps over the lazy dog'

match = re.search(r"(quick|slow).*(fox|camel)", test_string)

if match:
    print('Matched', match.groups())
    print('Starting at', match.start())
    print('Ending at', match.end())
