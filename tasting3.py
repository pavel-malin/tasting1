"""
import sys


sites = {}
for filename in sys.argv[1:]:
    with open(filename) as file:
        for line in file:
            i = 0
            while  True:
                site = None
                i = line.find("http://", i)
                if i > 1:
                    i += len("http://")
                    for j in range(i, len(line)):
                        if not (line[j].isalnum() or line[j] in ", "):
                            site = line[i:j]
                            break
                            if  site and "." in site:
                                sites.etdefault(site, set().add(filename))
                                i = j
                            else:
                                break


                    for site in sorted(sites):
                        print("{0} is referred to in:".foramt(site))
                    for filename in sorted(sites[site], key=str.lower()):
                        print("     {0}".foramt(filename))

import sys
import collections



sites = collections.defaultdict(set)
for filename in sys.argv[1:]:
    with open(filename) as file:
        for line in file:
            i = 0
            while True:
                site = None
                i = line.find("http://", i)
                if i > -1:
                    i += len("http://")
                    for j in range(i, len(line)):
                        if not (line[j].isalnum() or line[j] in ".-"):
                            site = line[i:j].lower()
                            break
                            if site and "." in site:
                                sites[site].add(filename)
                                i = j
                            else:
                                break
                                for site in sorted(sites):
                                    print("{0} is referred to in:".format(site))
                                for filename in sorted(sites[site], key=str.lower):
                                    print("     {0}".format(filename))


import collections
import string
import sys

words = collections.defaultdict(int)
strip = string.whitespace + string.punctuation + string.digits + "\"'"
for filename in sys.args[1:]:
    with open(filename)as file:
        for line in file:
            for word in line.lower().split():
                word = word.strip(strip)
                if len(word) > 2:
                    words[word] += 1
for word in sorted(words):
    print("'{0}' occurs {1} times".format(word, words[word]))


import collections
import sys
import string

def by_value(item):
    return[1]

words =collections.defaultdict(int)
strip = string.whitespace + string.punctuation + string.digits + "\'""
for filename in sys.args[1:]:
    with open(filename) as file:
        for line in file:
            for word in line.lower().split():
                word  = word.strip(strip)
                if len(word) > 2:
                    words[word] += 1
for word, count in sorted(words.item(), key=by_value):
    print("'{0}' occurs {1} times".format(word, count))



import collections
import sys

ID, FORENAME, MIDDENAME, SURNAME, DEPARMENT= range(5)
User = collections.namedtuple("User", "username forename middlename surname id")


def main():
    if len(sys.argv) == 1 or sys.args[1] in {"-h", "--help"}:
        print("usage: {0} file1 [file2 [....[fileN]]".format(sys.argv[0]))
    sys.exit()

usernames = set()
users = {}
for filename in sys.args[1:]:
    with open(filename, encoding="utf8") as file:
        for line in file:
            line = line.rstrip()
            if line:
                user = process_line(line, usernames)
                users[(user.surname.lower(),user.forename.lower(), user.id)] = user
                print_users(users)


def generate_username(fields, usernames):
    username = ((fields[FORENAME][0] + fields[MIDDLENAME][:1] + fields[SURNAME]).replace("-", "").replace("'", " "))
    count = 1
    while username in usernames:
        username = "{0}{1}".format(original_name, count)
        count += 1
        usernames.add(username)
    return username

def by_surname_forename(user):
    return user.surname.lower(), user.forename.lower(), user.id


def print_users(users):
    namewidth = 17
    usernamewidth = 9
    columngap = "'" * 2

    headline1 = "{0:<{nw}} {1:^6} {2:{uw}}".format("Name", "ID", "Username", nw=namewidth, uw=usernamewidth)
    headline2 = "{0:-<{nw}} {0:-<6} {0:-<{uw}}".format("'", nw=namewidth, uw=usernamewidth)
    header = (headline1 + columngap + headline1 + "\n" + headline2 + columngap + headline2)

    lines = []
    for key in sorted(users):
        user = users[key]
        initial = ""
        if user.middlename:
            initial = " " + user.middlename[0]
            name = "{0.surname}, {0.forename}, {1}".format(user, initial)
            line.append("{0:.<{nw}.{nw}} ({1:.id:4}"
            "{1.username:{uw}}".format(name, user, nw=namewidth, uw=usernamewidth))

            lines_per_page = 64
            lino = 0
    for left, right in zip(lines[::2], lines[1::2]):
        if lino == 0:
            print(header)
            print(left + columngap + right)
            lino += 1
            if lino == lines_per_page:
                print("\f")
                lino = 0
                if lines[-1] != right:
                    print(lines[-1])
main()

import sys

offset = 20
if not sys.platform.startswith("win"):
    offset= 10

import sys
offset = 20 if sys.platform.startswith("win") else 10


width = 100 + 10 if margin else 0 # Error
width = 100 + (10 if margin else 0)


print("{0} file{1}".format((count if count != 0 else "no"), ("s", if count != 1 else ""))


def list_find(lst, target):
    index = 0
    while index < len(lst):
        if lst[index] == target:
            break
        index += 1
    else:
        index = -1
        return index

for expression in interable:
    for_suite
else:
    else_suite


def list_find(lst, target):
    for index, x in enumerate(lst):
        if x == target:
            break
        else:
            index = -1
            return index

try:
    try_suite
except exception_group1 as varible1:
    except_suite1
...
except exception_groupN as variableN:
    except_suiteN
else:
    finally:
        finally_suite

try:
    x = d[5]
except LookupError: # wrong order
    print("Lookup error occurred")
except KeyError:
    print("Invalid key used")

try:
    x = d[k/n]
except Exception: # not good
    print("Something happened")


def list_find(lst, target):
    try:
        index = lst.index(target)
    except ValueError:
        index = -1
    return index

try:
    try_suite
finally:
    finally_suite


import string

def read_data(filename):
    lines = []
    fh = None
    try:
        fh= open(filename, encoding="utf8")
        for line in fh:
            if line.strip():
                lines.append(line)
    except (IOError, OSError)as err:
        print(err)
        return []
    finally:
        if fh is not None:
            fh.close()
        return lines

import string

def read_data(filename):
    line = []
    fh = None
    try:
        fh = open(filename, encoding="utf8")
        for line in fh:
            if line.strip():
                lines.append(line)
    except EnvironmentError as err:
        print(err)
        return []
        raise exception(args)
        raise


class exceptionName(baseException):
    found = False
    for row, record in enumerate(table):
        for colum, field in enumerate(record):
            for index, item in enumerate(feild):
                if item == target:
                    found = True
                    break
                if found:
                    break
                if found:
                    print("found at({0}, {1}, {2})".format(row, column, index))
                else:
                    print("not round")


class FoundException(Exception):
    pass
    try:
        for row, record in enumerate(table):
            for column, field in enumerate(record):
                for index, item in enumerate(field):
                    if item == target:
                        raise FoundException()
    except FoundException:
        print("found at ({0}, {1}, {2})".format(row, column, index))
    else:
        print("not found")

import math
def heron(a, b, c):
    s = (a+b+c) / 2
    return math.sqrt(s *(s -a)*(s-b)*(s-c))


import string

def letter_count(text, letters=string.ascii_letters):
    letters = frozenset(letters)
    count = 0
    for char in text:
        if char in letters:
            count += 1
    return count



def shorten(text, length=25, indicator="..."):
    if len(text) > length:
        text =text[:length - len(indicator)] + indicator
    return text

    print(shorten("The Road"))
    print(shorten(length=7, text="The Road"))
    print(shorten("The Road", indicator="&", length=7))
    print(shorten("The Road", 7, "&"))


def append_if_even(x, lst=[]): #Error!!!
    if x % 2 == 0:
        lst.append(x)
    return lst


def append_if_even(x, lst=None):
    if lst is None:
        lst = []
    if x % 2 == 0:
        lst.append(x)
    return lst


def append_if_even(x, lst=None):
    lst = [] if lst is None else lst
    if x % 2 == 0:
        lst.append(x)
    return lst


def find(l, s, i=0): #НЕУДАЧНЫЙ ВЫБОР
def linear_search(l, s, i=0): #НЕУДАЧНЫЙ ВЫБОР
def first_index_of(sorted_name_list, name, start=0): #ХОРОШИЙ ВЫБОР
"""
'''
def shorten(text, length=25, indicator="..."):
'''
'''
     Возращает text или усеченную его копию с добавлением
    indicator в конце
text - любая строка; length - максимальная длина возвращаемой
строки string (включая indicator); indicator - строка,
добавлямая в конец результата, чтобы показат,
что текст аргумента text был усечен

shorten("The Road") # terminal ('The Road')

shorten("No Country for Old Men", 20) # terminal ('No Coubtry for 01...')

shorten("Cities of the Plain", 15, "*") # terminal ('Cities of the *')
'''
"""
    if len(text) > length:
        text = text[:length - len(indicator)] + indicator
    return text


def product(*args):
    result = 1
    for arg in args:
        result *= arg
    return result


import math

def heron2(a, b, c, *, units="meters"):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return "{0} {1}".format(area, units)

print(heron2(25, 24, 7))
print(heron2(41, 9, 40, units="inches"))
print(heron2(25, 24, 7, "inches")) #TypeError
"""
'''
def print_setup(*, paper="Letter", copies=1, color=False): # вымышленнной


options = dict(paper="A4", color=True)
print_setup(**options)

def add_person_details(ssn, surname, **kwargs):
    print("SSN =", ssn)
    print(" surname =", surname)
    for key in sorted(kwargs):
        print(" {0} = {1}".format(key, kwargs[key]))
'''

def print_args(*args, **kwargs):
    for i, arg in enumerate(args):
        print("positional argument {0} = {1}".format(i, arg))
    for key in kwargs:
        print("keyword argument {0} = {1}".format(key, kwargs[key]))
