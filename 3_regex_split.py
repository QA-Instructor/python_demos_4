import re

line = 'root:;0.0:superuser,/root;/bin/sh'

# default is no limit to the number of splits
elements = re.split('[:;.,]', line)
print(elements)

# limit the number of splits to 3
elements = re.split('[:;.,]', line, 3)
print(elements)
