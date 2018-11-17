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
