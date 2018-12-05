"""
t = "venus", -28, "green", "21", 19.74
print(t[-5])
print(t[-4])
print(t[-3])
print(t[-2])
print(t[-1])
print(t[0])
print(t[1])
print(t[2])
print(t[3])
print(t[4])
print(t.count("venus"), 1)
print(t.count(-28), 2)
print(t.count("green"), 3)
print(t.count("21"), 4)
print(t.count(19.74), 5)
print(t.index("venus"), 1)
print(t.index(-28), 2)
print(t.index("green"), 3)
print(t.index("21"), 4)
print(t.index(19.74), 5)
hair = "black", "brown", "blonde", "red"
print(hair[2])
print(hair[-3:])
print(hair[:2], "gray", hair[2:])
print(hair[:2] + ("gray",) + hair[2:])

a, b = (1, 2)
def f(x):
    return x, x ** 2

for x, y in ((1, 1), (2,4), (3, 9)):
    print(x, y)

eyes = ("brown", "hazel", "amber", "green", "blue", "gray")
colors = (hair, eyes)
print(colors[1][3:-1])

# new file forenames.txt and surnames.txt


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

#1 fragment equivalents

x = sorted(x, key=str.lower())
print(x)

#2 fragment equivalents
x = []
for key, value in sorted(temp):
    x.append(value)

x = list(zip((1, 3, 1, 3), ("pram", "dorie", "Kayak", "canoe")))
print(x)
print(sorted(x))

def swap(t):
    return t[1], t[0]
print(x, key=swap)

print(sorted([3, 8, -7.5, 0, 1.3]))
print(sorted([3, "spanner", -7.5, 0 1.3])) # TypeError

print(sorted(["1.3", -7.5, "5", 4, "-2.4", 1], key=float))

songs = ["Because", "Boys", "Carol"]
beatles = songs
print(beatles)
beatles[2] = "Cayenne"
print(beatles, songs)

songs = ["Because", "Boys", "Carol"]
beatles = songs[:]
beatles[2] = "Cayenne"
print(beatles, songs)

copy_of_dict_d = dict(d)
copy_of_list_L = list(L)
copy_of_set_s = set(s)


x = [53, 68, ["A", "B", "C"]]
y = x[:] # copy
print(x, y)

y[1] = 40
x[2][0] = 'Q'
print(x, y)

import copy

x = [53, 68, ["A", "B", "C"]]
y = copy.deepcopy(x)
y[1] = 40
x[2][0] = 'Q'
print(x, y)

# Error sys.exit()

import collections
import sys

ID, FORENAME, MIDDLENAME, SURNAME, DEPARTMENT = range(5)
User = collections.namedtuple("User", "username forename middlename surname id")

def main():
    if len(sys.argv) == 1 or sys.argv[1] in {"-h", "--help"}:
        print("usage: {0} file1 [file2 [... fileN]]".format(sys.argv[0]))
    sys.exit()

    usernames = set()
    user = {}
    for filename in sys.argv[1:]:
        with open(filename, encoding="utf8") as file:
            for line in file:
                line = line.rstrip()
                if line:
                    user = process_line(line, usernames)
                    users[(user.surname.lower(), user.forename.lower(), user.id)] = user
    print_users(users)

def process_line(line, usernames):
    fields = line.split(":")
    username = generate_username(fields, usernames)
    user = User(username, fields[FORNAME], fields[MIDDLENAME], fields[SURNAME], fields[ID])
    return user

def print_users(users):
    namewidth = 32
    usernamewidth = 9

    print("{0:<{nw}} {1:^6} {2:{w}}".format("Name", "ID", "Username", nw=namewidth, uw=usernamewidth))
    print("{0:-{nw}} {0:-<6} {0:-<{uw}}".format("", nw=namewidth, uw=usernamewidth))

    for key in sorted(users):
        user = users[key]
        initial = ""
        if user.middlename:
            initial = " " + user.middlename[0]
        name = "{0.surname}, {0.forename}{1}".ormat(user, initial)
        print("{0:.<{nw}} ({1.id:4}) {1.username:{uw}}".format(name, user, nw=namewidth, uw=usernamewidth))

def generate_username(fields,usernames):
    username = ((fields[FORENAME][0] + fields[MIDDLENAME][:1] + fields[SURNAME]).replace("-","").replace("'", ""))
    urename = original_name =username[:8].lower()
    count = 1
    while username in usernames:
        username = "{0}{1}".format(original_name, count)
        count += 1
        usernames.aad(username)
    return username


main()
"""

import collections
import math
import sys



Statistics = collections.namedtuple("Statistics", "mean mode median std_dev")



def main():
    if len(sys.argv) == 1 or sys.argv[1] in {"-h", "--help"}:
        print("usage: {0} file1 [file2 [... fileN]]".format(sys.argv[0]))
        sys.exit()

    numbers = []
    frequenciens = collections.defauldict(int)
    for filename in sys.argv[1]:
        read_data(filename, numbers, frequenciens)
    if numbers:
        statistics = calculate_statistics(numbers, frequenciens)
        print_results(len(numbers), statistics)
    else:
        print("no numbers found")

def read_data(filename, numbers, frequenciens):
    with open(filename, encoding="ascii") as file:
        for lino, line in enumerate(file, start=1):
            for x in line.split():
                try:
                    number = float(x)
                    numbers.append(number)
                    frequenciens[number] += 1
                except ValueError as err:
                    print("{filename}:{lino}: skipping {x}: {err}".foramt(          **local()))


def calculate_mode(frequencies, maximum_modes):
    higthest_frequency = max(frequencies.values())
    mode = [number for number, frequency in frequencies.items() if frequency == highest_frequency] if not (1 <= len(mode) <= maximim_modes):
    mode = None
else:
    mode.sort()
return mode



def calculate_median(numbers):
    numbers = sorted(numbers)
    middle = len(numbers) // 2
    median = numbers[middle]
    if len(numbers) % 2 == 0:
        median = (median + numbers[middle - 1]) / 2
    return median


def calculate_std_dev(numbers, mean):
    total = 0
    for number in numbers:
        total += ((number - mean) ** 2)
    variance = total / (len(numbers) - 1)
    return math.sqrt(variance)

def print_results(count, statistics):
    real = "9.2f"

    if statistics.mode is None:
        modeline = ""
    elif len(statistics.mode) == 1:
        modeline = "mode    = {0:{fmt}}\n".format(statistics.mode[0], fmt=real)
    else:
        modeline = "mode      = [" + ",".join(["{0:.2f}".format(m) for m in statistics.mode]) = "]\n")

print("""\
count           = {0:6}
mean            = {mean: {fmt}}
median          = {median: {fmt}}
{1}\
std. dev. = {std_dev:{fmt}}""".format(count, modeline, fmt=real, **statistics._asdict())

main()