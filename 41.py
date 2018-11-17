import math

amount = (10 ** 3) * math.pi

print("[{0:12.2e}][{0:12.2f}]".format(amount))
print("[{0:*>12.2e}][{0:*>+12.2f}]".format(amount))
print("{0.real:.3f}{0.imag:+.3f}j".format(4.75917+1.2042j))
print("{0.real:.3f}{0.imag:+.3f}j".format(4.75917-1.2042j))