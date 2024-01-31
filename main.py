import requests
from collections import deque
import pickle

PAIR_REQUEST_FORMAT = "https://neal.fun/api/infinite-craft/pair?first={}&second={}"


elements = ["Water", "Fire", "Wind", "Earth"]

with open("seen", 'rb') as file:
    seen_pickle = pickle.load(file)

if seen_pickle:
    seen = set(seen_pickle)
else:
    seen  = set(elements)

queue = deque(seen)

with open("used", 'rb') as file:
    used_pickle = pickle.load(file)

if used_pickle:
    used = set(used_pickle)
else:
    used  = set(elements)

used = []
while queue:
    current_element = queue.popleft()
    
    for other_element in elements:
        if current_element + other_element in used:
            continue
        
        try:
            resp = requests.get(PAIR_REQUEST_FORMAT.format(current_element, other_element)).json()
            combined_element = resp["result"]
            if combined_element not in seen:
                entry = "{} = {} + {} | {}\n".format(combined_element, current_element, other_element, resp["isNew"])
                fd = open("log", "a")
                fd.write(entry)
                print(entry)
                fd.close()
                seen.add(combined_element)
                queue.append(combined_element)
                elements.append(combined_element)
        except Exception as e:
            print(e)
            continue
