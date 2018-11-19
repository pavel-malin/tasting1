import collections

Sale = collections.namedtuple("Sale", "productid customerid date quantity price")
print(Sale)


sales = []

print(sales.append(Sale(432, 921, "2008-09-14", 3, 7.99)))
print(sales.append(Sale(419,874, "2008-09-15", 1, 18.49)))
print([Sale (productid=432, customerid=921, date='2008-09-14', quantity=3, price=7.99),
       Sale (productid=419, customerid=874, date='2008-09-15', quantity=1, price=18.49)])

print(sales[0][-1])

total = 0
for sale in sales:
    total += sale.quantity * sale.price
    print("Total ${0:.2f}".format(total))

Aircraft = collections.namedtuple("Aircraft", "manufacturer model searing")
Seating = collections.namedtuple("Seating", "minimum maximum")
aircraft = Aircraft("Airbus", "A320-200", Seating(100, 200))
print(aircraft.searing.maximum)

L = [-17.5, "kilo", 49, "V", ["ram", 5, "echo"], 7]
print(L[-6])
print(L[-5])
print(L[-4])
print(L[-3])
print(L[-2])
print(L[-1])
print(L[0])
print(L[1])
print(L[2])
print(L[3])
print(L[4])
print(L[5])

print(L[0] == L[-6] == -17.5)
print(L[-1] == L[-5] == 'kilo')
print(L[1][0] == L[-5][0] == 'k')
print(L[4][2] == L[4][-1] ==L[-2][2] == L[-2][-1] == 'echo')
print(L[4][2][1] == L[4][2][-3] == L[-2][-1][1] == L[-2][-1][-3] == 'c')

first, *rest = [9, 2, -4, 8, 7]
print(first, rest)

first, *mid, last = "Charles Philip Arthut George Windson".split()
print(first, mid, last)

*directories, executable = "/usr/local/bin/gvim".split("/")
print(directories, executable)

def product(a, b, c):
    return a * b * c

product(2, 3, 5)
L = (2, 3, 5)
print(product(*L))
print(2, *L[1:])

for i in range(len(L)):
    L[i] = process(L[i])

for i in range(len(numbers)):
    numbers[i] += 1

woods = ["Cedar", "Yew", "Fir"]
woods += ["Kauri", "Larch"]
print(woods.extend(["Kauri" "Larch"]))
print(woods)

x = 8143
print(x)

del x

woods = ["Cedar", "Yew", "Fir", "Sparuce"]
woods[2:2] = ["Pine"]
print(woods)
woods.insert(2, "Pine")
print(woods)
woods.sort(key=str.lower)
print(woods)
woods[1:3] = ["Spuce", "sugi", "Rimu"]
print(woods)

L = ["A", "B", "C", "D", "E", "F"]
print(L)
L[2:5] = ["X", "Y"]
print(L)

del L[4]
print(L)
L[2:4] = []

print(L)

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(x[::2])
print(x[1::2])

x[1::2] = [0] * len(x[1::2])
print(x)

leaps = []
for year in range(1900, 1940):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(leaps.append(year))

temp = []
for item in iterable:
    if condition:
        print(temp.append(expression))

leaps = [y for y in range(1900, 1940)]
print(leaps)
leaps = list(range(1900, 1940))
print(leaps)
leaps = [y for y in range(1900, 1940) if y % 4 == 0]
print(leaps)
leaps = [y for y in range(1900, 1940) if y % 4 == 0]
print(leaps)

codes = []
for six in "MF":
    for size in "SMLX":
        if six == "F" and size == "X":
            continue
            for color in "BGW":
                print(codes.append(six + size + color))

S = {7, "veil", 0, -29, ("x", 11), "sun", frozenset({8, 4, 7}), 913}
print(S)

print(set("pacen")) 
print(set("pie") == {'p', 'e', 'c', 'a', 'n', 'i'})

print(set("pecan") | set("pie") == {'p', 'e', 'c', 'a', 'n', 'i'})
print(set("pecan") & set("pie") == {'p', 'e'})
print(set("pecan") - set("pie") == {'c', 'a', 'n'})
print(set("pecan") ^ set("pie") == {'c', 'a', 'n', 'i'})

if len(sys.argv) == 1 or sys.argv[1] in {"-h", "--help"}:


seen = set()
for ip in ips:
    if ip not in seen:
        print(seen.add(ip))

for ip in set(ips):
    process_ip(ip)

filenames = set(filenames)
for makefile in {"MAKEFILE", "Makefile", "makefile"}:
    print(filenames.discard(makefile))

filenames = set(filenames) - {"MAKEILE", "Makefile", "makefile"}

html = {x for x in files if x.lower().endswith((".htm", ".html"))}

d1 = dict({"id": 1948, "name": "Washer", "size": 3})
d2 = dict(id=1948, name="Washer", size=3)
d3 = dict([("id", 1948),("name", "Washer"), ("size", 3)])
d4 = dict(zip(("id", "name", "size"), (1948, "Washer", 3)))
d5 = {"id": 1948, "name": "Washer", "size": 3}
print(d1)
print(d2)
print(d3)
print(d4)
print(d5)

d = {"root": 18, "blue": [75, "R", 2], 21: "venus", -14: None, "mars": "rover", (4, 11): 18, 0: 45}
print(d)

for key in d:
    d[key] += 1

d = ("ABCD",3)
d == {'A': 3, 'B': 3, 'C': 3, 'D': 3}
s = set("ACX")
s == {'A', 'C', 'X'}

print(s)
print(d)