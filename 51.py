import sys

sites = {}
for filename in sys.argv[1:]:
    for line in open(filename):
        i = 0
        while True:
            site = None
            i = line.find("http://", i)
            if i > -1:
                i += len("http://", i)
                for j in range(i, line(line)):
                    if not (line[j].isalnum() or line[j] in ".-"):
                        site = line[i:j].lower()
                        break
                    if site and "." in site:
                        sites.setdefault(site, set()).add(filename)
                        i = j
                    else:
                        break 
                    if site not in sites:
                        sites[site] = set()
                        sites[site].add[filename]
                    for filename in sorted(sites[site], key=str.lower()):
                         print("  {0}".format(filename))
