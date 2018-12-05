"""
seeds = ["sesame", "sunflower"]
seeds += ["pumpkin"]
print(seeds)


seeds += [5]
print(seeds)

seeds += [9, 1, 5, "poppy"]
print(seeds)

seeds = ["sesame", "sunflower", "pumpkin"]
seeds += "dulian"
print(seeds)

total = 0
count = 0

while True:
    line = input("integer: ")
    if line: 
        try:
            number = int(line)
        except ValueError as err:
            print(err)
            continue
        total += number
        count += 1
    else:
        break
        if count:
            print("count=", count, "total=", total, "mean=", total / count)

print("Type integers, each followed by Enter; or " or "Z to finish")

total = 0
count = 0
while True:
    try:
        line = input()
        if line:
            number = int(line)
            total += number
            count += 1
    except ValueError as err:
            print(err)
            countinue
    except EOFError:
        break
        if count:
            print("count =", count , "total =", total, "mean =", total / count)

total = 0
count = 0 
while True:
    try:
        line = input()
        if line:
            try:
                number = int(line)
            except ValueError as err:
                    print(err)
                    continue
                    total += namber
                    count += 1 
            except EOFError:
                break
                if count:
                    print("count =", count, "total =", total, "mean =", total / count)


def get_int(msg):
    while True:
        try:
            i = int(input(msg))
            age = get_int("enter your age: ")
            return i
        except ValueError as err:
            print(err)

import sys
print(sys.argv)

import random
x = random.randint(1, 6)
y = random.choice(["appe", "banana", "cherry", "durian"])
print(x)
print(y)


import sys 


Zero = ["  ***  ",
        " *   * ",
        "*     *",
        "*     *",
        "*     *",
        " *   * ",
        "  ***  "]
One = [" * ", "** ", " * ", " * ", " * ", " * ", "***"]
Two = [" *** ", "*   *", "*  * ", "  *  ", " *   ", "*    ", "*****"]
Three = [" *** ", "*   *", "    *", "  ** ", "    *", "*   *", " *** "]
Four = ["   *  ", "  **  ", " * *  ", "*  *  ", "******", "   *  ",
        "   *  "]
Five = ["*****", "*    ", "*    ", " *** ", "    *", "*   *", " *** "]
Six = [" *** ", "*    ", "*    ", "**** ", "*   *", "*   *", " *** "]
Seven = ["*****", "    *", "   * ", "  *  ", " *   ", "*    ", "*    "]
Eight = [" *** ", "*   *", "*   *", " *** ", "*   *", "*   *", " *** "]
Nine = [" ****", "*   *", "*   *", " ****", "    *", "    *", "    *"]

Digits = [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]

try:
    digits = sys.argv[1]
    row = 0
    while row < 7:
        line = " "
        column = 0
        while column < len(digits):
            number = int(digits[column])
            digit = Digits[number]
            line += digit[row] + " "
            column += 1
            print(line)
            row += 1
except IndexError:
    print("usage: tasting.py <number>")
except ValueError as err:
    print(err, "in", digits)


import sys


Digits = [["  ***  ",
        " *   * ",
        "*     *",
        "*     *",
        "*     *",
        " *   * ",
        "  ***  "], #Zero
        [" * ", "** ", " * ", " * ", " * ", " * ", "***"], #One
        [" *** ", "*   *", "*  * ", "  *  ", " *   ", "*    ", "*****"], #Two
        [" *** ", "*   *", "    *", "  ** ", "    *", "*   *", " *** "], #Three
        ["   *  ", "  **  ", " * *  ", "*  *  ", "******", "   *  ",
        "   *  "], # Four
        ["*****", "*    ", "*    ", " *** ", "    *", "*   *", " *** "], # Five
        [" *** ", "*    ", "*    ", "**** ", "*   *", "*   *", " *** "], # Six
        ["*****", "    *", "   * ", "  *  ", " *   ", "*    ", "*    "], # Seven
        [" *** ", "*   *", "*   *", " *** ", "*   *", "*   *", " *** "], # Eght
        [" ****", "*   *", "*   *", " ****", "    *", "    *", "    *"]] # Nine

try:
    digits = sys.argv[1]
    row = 0
    while row < 7:
        line = ""
        column = 0
        while column < len(digits):
            number = int(digits[column])
            digit = Digits[number]
            line += digit[row] + " "
            column += 1
            print(line)
            row += 1
except IndexError:
    print("usage: tasting.py <number>")
except ValueError as err:
    print(err, "in", digits)


import random


def get_int(msg, minimum, default):
    while True:
        try:
            line = input(msg)
            if not line and default is not None:
                return default
            i = int(line)
            if i < minimum:
                print("must be >=", minimum)
            else:
                return i
        except ValueError as err:
            print(err)

rows = get_int("rows: ", 1, None)
columns = get_int("columns: ", 1, None)
minimum = get_int("minimum (or Enter for " + str(default) + "): ", minimum, default)

default = 1000
if default < minimum:
    default = 2 * minimum
maximum = get_int("maximum (or Enter for " + str(default) + "): ", minimum, default)

row = 0
while row < rows:
    line = ""
    column = 0
    while column < columns:
        i = random.randint(minimm, maximum)
        s = str(i)
        while len(s) < 10:
            s = " " + s
            line += s
            column += 1
        print(line)
        row += 1


import random

def get_int(msg, minimum, default):
    while True:
        try:
            line = input(msg)
            if not line and default is not None:
                return default
            i = int(line)
            if i < minimum:
                print("must be >=", minimum)
            else:
                return i
        except ValueError as err:
            print(err)

rows = get_int("rows: ", 1, None)
columns = get_int("columns: ", 1, None)
minimum = get_int("maximum (or Enter for 0)", -100000, 0)

default = 1000
if default < minimum:
    default = 2 * minimum
maximum = get_int("maximum ( or Enter for" + str(default) + "): ", minimum, default)

row = 0
while row < rows:
    line =" "
    column = 0
    while column < columns:
        i = random.randint(minimum, maximum)
        s = str(i)
        while len(s) < 10:
            s = " " + s
            line += 5
            column += 1
            print(line)
            row += 1


import sys

Zero = ["  ***  ",
        " *   * ",
        "*     *",
        "*     *",
        "*     *",
        " *   * ",
        "  ***  "]
One = [" * ", "** ", " * ", " * ", " * ", " * ", "***"]
Two = [" *** ", "*   *", "*  * ", "  *  ", " *   ", "*    ", "*****"]
Three = [" *** ", "*   *", "    *", "  ** ", "    *", "*   *", " *** "]
Four = ["   *  ", "  **  ", " * *  ", "*  *  ", "******", "   *  ",
        "   *  "]
Five = ["*****", "*    ", "*    ", " *** ", "    *", "*   *", " *** "]
Six = [" *** ", "*    ", "*    ", "**** ", "*   *", "*   *", " *** "]
Seven = ["*****", "    *", "   * ", "  *  ", " *   ", "*    ", "*    "]
Eight = [" *** ", "*   *", "*   *", " *** ", "*   *", "*   *", " *** "]
Nine = [" ****", "*   *", "*   *", " ****", "    *", "    *", "    *"]

Digits = [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]

try:
    digits = sys.argv[1]
    row = 0
    while row < 7:
        line = ""
        column = 0 
        while column < len(digits):
            number = int(digits[column])
            digit = Digits[number]
            for c in digit[row]:
                if c == "*":
                    c = str(number)
                line += c
            line += " "
            column += 1
        print(line)
        row += 1
except IndexError:
    print("usage: tasting.py <number>")
except ValueError as err:
    print(err, "in", digits)



numbers = []
total = 0
lowest = None
highest = None

while True:
    try:
        line = input("enter a number or Enter to finish: ")
        if not line:
            break
        number = int(line)
        numbers.append(number)
        total += number
        if lowest is None or lowest > number:
            lowest = number
        if highest is None or highest < number:
            highest = number
    except ValueError as err:
        print(err)

print("numbers:", numbers)
if numbers:
    print("count =", len(numbers), "sum =", total, "lowest =",
     lowest, "highest =", highest, "mean =", total / len(numbers))


import random

articles = ["the", "a", "another", "her", "his"]
subjects = ["cat", "dog", "horse", "man", "woman", "boy", "girl"]
verbs = ["sang", "ran", "jumped", "said", "fought" "swam", "saw",
         "heard", "felt", "slept", "hopped", "cried", "laughed",
         "walked"]
adverbs = ["loudly", "quitly", "quickly", "slowly", "well", "badly", 
            "rudely", "politely"]

for _ in [1, 2, 3, 4, 5]:
    article = random.choice(articles)
    subject = random.choice(subjects)
    verb = random.choice(verbs)
    if random.randint(0, 1) == 0:
        print(article, subject, verb)
    else:
        adverb = random.choice(adverbs)
        print(article, subject, verb, adverb)

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


import sys

def equal_float(a, b):
    return abs(a - b) <= sys.float_info.epsilon
    print(a)
    print(b)


import math

x = 2.75
x.as_integer_ratio()
print(x)
s = 14.25.hex()
f = float.fromhex(s)
t = f.hex()
print(s, f, t)

import math
q = math.pi * (5 ** 2)
s = math.hypot(5, 12)
z = math.modf(13.732)

print(q)
print(s)
print(z)


import math
z = -89.5 + 2.125j
print(z.real, z.imag, z.conjugate)


import decimal
a = decimal.Decimal(9876)
b = decimal.Decimal("54321.012345678987654321")
print(a + b)

import decimal

x = 23 / 1.05
print(x)
print(23 / 105)
print(decimal.Decimal(23)/decimal.Decimal("1.05"))


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

import math
import sys

print("math.pi=={0.pi} sys.maxunicode=={1.maxunicode}".format(math, sys))
import decimal

print("{0} {0!s}{0!r} {0!a}".format(decimal.Decimal("33.4"))) 

import decimal

s = "The sword of truth"
print("{0}".format(s))
print("{0:25}".format(s))
print("{0:>25}".format(s))
print("{0:^25}".format(s))
print("{0:-^25}".format(s))
print("{0:.<25}".format(s))
print("{0:.10}".format(s))

maxwidth = 12
print("{0}".format(s[:maxwidth]))
print("{0:{1}}".format(s, maxwidth))

print("{0:0=12}".format(8749203))
print("{0:12}".format(-8749203))
print("{0:012}".format(8749203))
print("{0:-012}".format(8749203))

print("{0:*<15}".format(18340427))
print("{0:*>15}".format(18340427))
print("{0:*^15}".format(18340427))
print("{0:*^15}".format(-18340427))

print("[{0: }] [{1: }]".format(539802, -539802))
print("[{0:+}] [{1:+}]".format(539802, -539802))
print("[{0:-}] [{1:-}]".format(53980, -539802))

print("{0:b} {0:o} {0:x} {0:X}".format(14613198))
print("{0:#b} {0:#o} {0:#x} {0:#X}".format(14613198))

import locale

locale.setlocale(locale.LC_ALL, "")

import locale

x, y = (1234567890, 1234.56)
locale.setlocale(locale.LC_ALL, "C")
c = "{0:n}{1:n}".format(x, y)
locale.setlocale(locale.LC_ALL, "en_US.UTF-8")
en = "{0:n}{1:n}".format(x, y)
locale.setlocale(locale.LC_ALL, "de_DE.UTF-8")
de = "{0:n}{1:n}".format(x, y)

print(c)
print(en)
print(de)


import math

amount = (10 ** 3) * math.pi

print("[{0:12.2e}][{0:12.2f}]".format(amount))
print("[{0:*>12.2e}][{0:*>+12.2f}]".format(amount))
print("{0.real:.3f}{0.imag:+.3f}j".format(4.75917+1.2042j))
print("{0.real:.3f}{0.imag:+.3f}j".format(4.75917-1.2042j))


import sys
import unicodedata
import decimal

def print_unicode_table(word):

    print("decimal hex chr {0:^40}".format("name"))
    print("-------------- ------ ----- {10:-40}".format(""))
    code = ord(" ")
    end = sys.maxunicode

    while code < end:
        c = chr(code)
        name = unicodedata.name(c, "*** unknown ***")
        if word is None or word in name.lower():
            print("{0:7} {0:5x} {0:^3c} {1}".format(cede, name, title()))
            code += 1

word = None
if len(sys.argv) > 1:
    if sys.argv[1] in ("-h", "--help"):
        print("usage: {0} [string]".format(sys.argv))
        word = 0
    else:
        word = sys.argv[1].lower()
        if word != 0:
            print("usage: {0[0]}[string]".format(sys.argv))
            print_unicode_table(word)


antist = "Tage Åsén"
print(antist.encode("Latin1"))
print(antist.encode("CP850"))
print(antist.encode("utf8"))
print(antist.encode("utf16"))
print(antist.encode("ascii", "ignore"))
print(antist.encode("ascii", "replace"))
print(antist.encode("ascii", "backslashreplace"))
print(b"Tage \xc3\x85s\xc3\xa9n".decode("utf8"))
print(b"Tage \xc5s\xe9n".decode("latin1"))


import cmath
import math
import sys

def get_float(msg, allow_zero):
    x = None
    while x is None:
        try:
            x = float(input(msg))
            if not allow_ero and abs(x) < sys.float_info.epsilon:
                print("zero is not allowed")
                x = None
        except ValueError as err:
            print(err)
        return x
        print("ax\N{SUPERSCRIPT TWO} + bx + c = 0")

a = get_float("enter a:", False)
b = get_float("enter b:", True)
c = get_float("enter c:", True)

x1 = None
x2 = None
discriminant = (b ** 2) - (4 * a * c)
if discrimnant == 0:
    x1 = -(b / (2 * a))
else:
    if discriminant > 0:
        root = math.sqrt(discriminant)
    else:
        root = cmath.sqrt(discriminant)
        x1 = (-b + root) / (2 * a)
        x2 = (-b - root) / (2 * a)

equation = ("{0}x\N{SUPERSCRIPT TWO} + {1}x + {2} = 0"
            " \N{RIGHTWARDS ARROW} x = {3}").format(a, b, c, x1)
        
if x2 is not None:
    equantion += " or x = {0}".format(x2)
print(equation)


import sys


def main():
    maxwidth = 100
    print_start()
    count = 0
    while True:
        try:
            line = input()
            if count == 0:
                color = "lightyellow"
                print_line(line, color, maxwidth)
                count += 1
        except EOFError:
            break
        print_end()
def print_start():
    print("<table borer = '1'>")

def print_line():
    print("<tr bgcolor='{0}'>".format(color))
    fields = extrat_fields(line)
    for field in fields:
        if not field:
            print("<td></td>")
        else:
            number = field.replace(",", "")
            try:
                x = float(number)
                print("<td align= 'right'>{0:d}</td>".format(rounds(x)))
            except ValueError:
                field = field.title()
                field = field.replace(" And ", " and ")
                field = escape_html(gield)
                if len(field) <= maxwidth:
                    print("<td>{0}</td>".format(field))
                else:
                    print("<td>{0:.{1}}...</td>".format(field, maxwidth))
                    print("</tr>")

def extract_fields():
    fields = []
    field = ""
    quote = None
    for c in line:
        if c in "\"'":
            if quote is None:
                quote = c
            elif quote == c:
                quote = None
            else:
                field += c
                continue
                if quote is None and c == ",":
                    fields.append(field)
                    field = ""
                else:
                    field += c
                    if field:
                        field.append(field)
                    return fields           

def escape_html():
    text = text.replace("&", "&amp;")
    text = text.replace("<", "&lt;")
    text = text.replace(">", "&gt;")
    return text

def print_end():
    print("</table>")


    main()


import sys
import unicodedata


def print_unicode_table(words):
    print("decimal hex chr {0:^40}".format("name"))
    print("----- ----- -- ------{0:-<40}".format(""))

    code = ord(" ")
    end = min(0xD800, sys.maxunicode)

    while code < end:
        c = chr(code)
        name = unicodedata.name(c, "*** unknow ***")
        ok = True
        for word in words:
            if word not in name.lower():
                ok = False
                break
        if ok:
            print("{0:7} {0:5x} {0:^3c} {1}".format(code, name.title()))
    code += 1


words = []
if len(sys.argv) > 1:
    if sys.argv[1] in ("-h", "--help"):
        print("usage: {0} [string1 [string2 [...stringN]]]".format(sys.argv[0]))
        words = None
    else:
        for word in sys.argv[1:]:
            words.append(word.lower())
if words is not None:
    print_unicode_table(words)

import cmath
import math
import sys

SQARED = "\N{SUPERSCRIPT TWO}"
ARROW = "\N{SUPERSCRIPT ARROW}"

if not sys.platform.startswith("linux"):
    SQARED = "^2"
    ARROW = "->"


def get_float(msg, allow_zero):
    x = None
    while x is None:
        try:
            x = float(input(msg))
            if not allow_zero and abs(x) < sys.float_info.epsilon:
                print("zero is not allowed")
                x = None
        except ValuError as err:
            print(err)
    return x

print("ax" + SQUARED + "bx + c = 0")
a = get_float("enter a:", False)
b = get_float("enter b:", True)
c = get_float("enter c:", True)

x1 = None
x2 = None
discriminant = (b ** 2) - (4 * a * c)
if discriminant == 0:
    x1 = -(b / (2 * a))
else:
    if discriminant > 0:
        root = math.sqrt(discriminant)
    else:
        root = cmath.sqrt(discriminant)
    x1 = (-b + root) / (2 * a)
    x2 = (-b - root) / (2 * a)

equantion = "{0}x{1}".format(a, SQUARED)
if b != 0:
    if b < 0:
        equation += "- {0}x".format(abs(b))
    else:
        equation += "+ {0}x".format(b)
if c != 0:
    if c < o:
        equation += "- {0}".format(abs(c))
    else:
        equation += "+ {0}".format(c)
eqution += "= 0 {1}x = {0}".format(x1, ARROW)
if x2 is not None:
    equation += " or x= {0}".format(x2)
print(equation)

"""

import sys
import xml.sax.saxutils

def main():
    maxwidth = 100
    print_start()
    count = 0
    while True:
        try:
            line = input()
            if count == 0:
                color = "lightgreen"
            elif count % 2:
                color = "while"
            else:
                color = "lighteyllow"
                print_line(line, color, maxwidth)
                count += 1
        except EOFError:
            break
        print_end()


def print_start():
    print("<table border='1'>")

def print_line(line, color, maxwidth):
    print("<tr dgcolor='{0}'>".format(color))
    fields = extract_fields(line)
    for field in fields:
        if not field:
            print("<td></td>")
        else:
            number = field.replace(",", "")
            try:
                x = float(number)
                print("<td align='right'>{0:d}</td>".format(round(x)))
            except ValueError:
                field = field.title()
                field = field.replace( " And ", " and ")
                if len(field) <= maxwith:
                    field = xml.sax.saxutils.escape(field)
                else:
                    field = "{0}...".format(xml.sax.saxutils.escape(field[:maxidth]))
                    print("<td>{0}</td>".format(field))
                    print("</tr>")

def extract_fields(line):
    fields = []
    field = ""
    quote = None
    for c in line:
        if c in "\"'":
            if quote is None:
                quote = c
            elif quote == c:
                quote = None
            else:
                field += c
                continue
            if quote is None and c == ",":
                fields.append(field)
                field = ""
            else:
                field.append(field)
        return fields

def print_end():
    print("</table>")

main()