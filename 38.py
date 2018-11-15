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