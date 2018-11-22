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