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
