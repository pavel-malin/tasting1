import re
phone1 = re.compile("^((?:[(]\\d+[)])?\\S*\\d+(?:-\\d+)?)$")
phone2 = re.compile(r"^((?:[(]\d+[)])?\S*\d+(?:-\d+)?)$")
print(phone1) 
print(phone2)

euros = "\N{euro sign} \u20AC \U0000020AC"
print(ord(euros[0]))
print(hex(ord(euros[0])))
print(euros)

s = "anarchists are "+ chr(8734) +chr(0x23B7)
print(s)
print(ascii(s))
u = "hello, word!"
s = "The waxwork man"
print(s[:7])
print(s[4:11])
print(s[7:])
print(s[-3:])
print(s[:12] + s[7:9] + s[12:])
s = s[:12] + "wo" +s[12:]
print(s)

s[::-2] == 'do ea th'
print(s)
s[::3] == 'ha m o'
print(s)
print(s[::-2])
print(s[::3])
print(s, s[::-1])

s[-1:2:-2] == s[:2:-2] =='do ea t'
print(s)
s[0:-5:3] == s[:-5:3] == 'ha m'
print(s)
trearises = ["Arithmetica", "Conics", "Elements"]
print(" ".join(trearises))
print("-<>-".join(trearises))
print("".join(trearises))
print("".join(reversed(s)))
print(str.isupper(s))
print(str.isupper(s))
print(str.islower(s))
print(str.isnumeric(s))
print(str.isspace(s))
print(str.isdigit(s))
print(str.isdecimal(s))
print(str.istitle(s))
print(str.title(s))
print(str.capitalize(s))
print(str.expandtabs(s))
print(str.format(s))
print(str.isalnum(s))
print(str.lower(s))
print(str.split(s))
print(str.splitlines(s))
print(str.strip(s))
print(str.upper(s))

s = "=" * 5
print(s)

s *= 10
print(s)

def extract_from_tage(tag, line):
    opener = "<" + tag +">"
    closer = "</" + tag + ">"
    try:
        i = line.index(opener)
        start = i + len(opener)
        j = line.index(closer, start)
        return line[start:j]
    except ValueError:
        return None

def extract_from_tag(tag, line):
    opener = "<" + tag + ">"
    closer = "</" + tag + ">"
    i = line.find(opener)
    if i != -1:
        start = i + len(opener)
        j = line.find(closer, start)
        if j != -1:
            return line[start:j]
            return None

s.count("m", 6) == s[6:].count("m")
s.count("m", 5, -3) == s[5:-3].count("m")
result = s.rfind("/")
i = s.rfind("/")
if i == -1:
    result = s, ", "
else:
    result = s[:i], s[i], s[i + 1:]

if filename.lower().endswith((".jpg", "jpeg"))
print(filename, "is a JPEG image")

print("917.5".isdigit(), "".isdigit(), "-2".isdigit(), "203".isdigit())

s = "/t no parking"
print(s.lstrip(), s.rstrip(), s.strip())
print("<unbracketed>".strip("[](){}<>"))

record = "Leo Tolstoy*1828-8-28*1910-11-20"
fields = record.split("*")
print(fields)
born = fields[1].split("-")
print(born)
died = fields[2].split("-")
print(died)
print("lived about", int(died[0]) - int(born[0]), "yers")
year_born = int(fields[1].split("-")[0])
print(year_born)

table = "".maketrans("\N{bengali digit zero}",
 "\N{bengali digit one}\N{bengali digit two}",
 "\N{bengali digit three}\N{bengali digit four}",
 "\N{bengali digit five}\N{bengali digit six}",
 "\N{bengali digit seven}\N{bengali digit eight}",
 "\N{bengali digit nine}", "0123456789")
print("20749".translate(table))
print("\N{bengali digit two}07\N{bengali digit four}",
 "\N{bengali digit nine}".translate(table))

print("The novel '{0}'was published in {1}".format("Hard Times", 1854))

print("{{{0}}} {1};-}}".format("I'm in braces", "i'm not"))

print("{0}{1}".format("The amount ue is $", 200))

x = "three"
s = "{0} {1} {2}"
s = s.format("The", x, "tops")
print(s)
print("{who} turned {age} this year".format(who="She", age=88))
print("The {who} was {0} last week".format(12, who="boy"))

stock = ["paper", "envelopes", "notepads", "pens", "paper clips"]
print("We have {0[1]} and {0[2]} in stock".format(stock))
d = dict(animal = "elephant", weight=12000)
print("The {0[animal]} weighs {0[weight]}kg".format(d))
