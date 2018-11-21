t = "venus", -28, "green", "21", 19.74
print(t[-5])
print(t[-4])
print(t[-3])
print(t[-2])
print(t[-1])
print(t[0])
print(t[1])
print(t[2])
print(t[3])
print(t[4])
print(t.count("venus"), 1)
print(t.count(-28), 2)
print(t.count("green"), 3)
print(t.count("21"), 4)
print(t.count(19.74), 5)
print(t.index("venus"), 1)
print(t.index(-28), 2)
print(t.index("green"), 3)
print(t.index("21"), 4)
print(t.index(19.74), 5)
hair = "black", "brown", "blonde", "red"
print(hair[2])
print(hair[-3:])
print(hair[:2], "gray", hair[2:])
print(hair[:2] + ("gray",) + hair[2:])

a, b = (1, 2)
def f(x):
    return x, x ** 2

for x, y in ((1, 1), (2,4), (3, 9)):
    print(x, y)

eyes = ("brown", "hazel", "amber", "green", "blue", "gray")
colors = (hair, eyes)
print(colors[1][3:-1])
