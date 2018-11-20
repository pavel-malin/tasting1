import sys

if len(sys.argv) > 3:
    print("usage: tasting.py word infile1 [infile2 [... infileN]]")
    sys.exit()

    word = sys.argv[1]
for filename in sys.argv[2:]:
    with open(filename) as file:
        for lino, line in enumerate(file, start=1):
            if word in line:
                print("{0}:{1}:{2:.40}".format(filename, lino, line.rstrip()))

print(list(range(5)), list(range(9, 14)), tuple(range(10, -11, -5)))


for i in range(len(x)):
    x[i] = abs(x[i])

i = 0
while i < len(x):
    x[i] = abs(x[i])
    i += 1

#?????

calculate(1, 2, 3, 4)
t = (1, 2, 3, 4)
calculate(*t)
calculate(*range(1,5))

# return bug
def get_forenames_and_surnames():
    forenames = []
    surnames = []

for names, filename in ((forenames, "data/forenames.txt"), (surnames, "data/surnames.txt")):
    for name in open(filename, encoding="utf8"):
        names.append(name.rstrip())
    return forenames, surnames
