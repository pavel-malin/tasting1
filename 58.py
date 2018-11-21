import random

def get_forenames_and_surnames():
    forenames = []
    surnames = []
    for names, filename in ((foreame, "data/forenames.txt"), (surname, "data/surnames.txt")):
        with open(filename, encoding="utf8") as file:
            for name in file:
                names.append(name.rstrip())
    return forenames, surnames

forenames, surnames = get_forenames_and_surnames()
with open("text-names2.txt", "w", encoding="utf8") as file:
    limit = 100
    years = list(range(1970, 2013)) * 3
    for year, forename, surname in zip(random.sample(years, limit), random.sample(forenames, limit), random.sample(surnames, limit)):
        name = "{0} {1}".format(name, year)

print(list(range(6)))
print(list(reversed(range(6))))

x = []
for t in zip(range(-10, 0, 1), range(0, 10,2), range(1, 10, 2)):
    x += t
    print(x)

print(sorted(x))
print(sorted(x, reverse=True))
print(sorted(x, key=abs))
