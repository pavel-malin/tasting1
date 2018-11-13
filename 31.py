import random
import sys

articles = ["the", "a", "another", "her", "his"]
subjects = ["cat", "dog", "horse", "man", "woman", "boy", "girl"]
verbs = ["sang", "ran", "jumped", "said", "fought" "swam", "saw",
         "heard", "felt", "slept", "hopped", "cried", "laughed",
         "walked"]
adverbs = ["loudly", "quitly", "quickly", "slowly", "well", "badly", 
            "rudely", "politely"]

lines = 5
if len(sys.argv) > 1:
    try:
        temp = int(sys.argv[1])
        if 1 <= temp <= 10:
            lines = temp 
        else:
            print("lines must be 1-10 inclusive")
    except ValueError:
        print("usage: tasting.py [lines] ")

while lines:
    article = random.choice(articles)
    subject = random.choice(subjects)
    verb = random.choice(verbs)
    if random.randint(0, 1) == 0:
        print(article, subject, verb)
    else:
        adverb = random.choice(adverbs)
        print(article, subject, verb, adverb)
    lines -= 1



numbers = []
indexes = []
total = 0
lowest = None
highest = None


while True:
    try:
        line = input("enter a number or Enter to finish: ")
        if not line:
            break
        indexes.append(len(numbers))
        number = int(line)
        numbers.append(number)
        total += number
        if lowest is None or lowest > number:
            lowest = number
        if highest is None or highest < number:
            highest = number
    except ValueError as err:
        print(err)

swapped = True
while swapped:
    swapped = False
    for index in indexes:
        if index + 1 == len(numbers):
            break
        if numbers[index] > numbers[index + 1]:
            temp = numbers[index]
            numbers[index] = numbers[index + 1]
            numbers[index + 1] = temp
            swapped = True
if numbers:
    index = int(len(numbers) / 2)
    median = numbers[index]
    if index and index * 2 == len(numbers):
        median = (median + numbers[index - 1]) / 2

print("numbers:", numbers)
if numbers:
    print("count =", len(numbers), "total =", total,
        "lowest =", lowest, "highest =", highest, "mean =", total / len(numbers),
        "median =", median)


for _ in (0, 1, 2, 3, 4, 5):
    print("hello")
