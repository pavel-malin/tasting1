import encodings

fin = open(Filename, encoding="utf-8")
fout = open(Filename, "w", encoding="utf-8")
for line in open(Filename, encoding="utf-8"):
    process(line)
