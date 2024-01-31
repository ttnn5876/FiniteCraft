import pickle
import re

line = "Rain = Water + Cloud | False"

# Define a regular expression pattern to match the desired elements
pattern = r'(\w+)\s*=\s*(\w+)\s*\+\s*(\w+)\s*\|\s*(True|False)'

with open("log", "r") as fd:
    for line in fd.readlines():
        match = re.match(pattern, line)
        used = list()
        seen = list()
        if match:
            new_element = match.group(1)
            element1 = match.group(2)
            element2 = match.group(3)
            boolean_value = match.group(4)
            used.append(element1 + element2)
            seen.append(new_element)

with open("used", 'wb') as fd:
    pickle.dump(used, fd)

with open("seen", 'wb') as fd:
    pickle.dump(seen, fd)

