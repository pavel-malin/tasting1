import os

file_sizes = {name: os.path.getsize(name) for name in os.listdir(".") if os.path.isfile(name)}       

inverted_d = {v: k for k, v in d.items()}

words[word] = words.set(word, 0) +1

import collections

words = collections.defaultdict(int)
x = words["xyz"]
words[word] += 1

#1
product = 1
for i in [1, 2, 4, 8]:
    product *= i
    print(product)

#2
product = 1
i = iter([1, 2, 4, 8])
while True:
    try:
        product *= next(i)
    except StopIteration:
        break
        print(product)

x = [-2, 9, 7, -4, 3]
# print(all(x), any(x), len(x), min(x), max(x), sum(x))
x.append(0)
print(all(x), any(x), len(x), min(x), max(x), sum(x))