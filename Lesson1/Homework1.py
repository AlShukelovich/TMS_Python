# Part 1
# Program in PyCharm
print('Hello world!')

# Part 2
# Task 1
a = 17/2*3+2
a1 = (17/2*3)+2
a2 = (17/2*3+2)
print("a:", a, ",", a1, ",", a2)
b = 2+17/2*3
b1 = 2+(17/2)*3
b2 = (2+17/2*3)
print("b:", b, ",", b1, ",", b2)
c = 19%4+15/2*3
c1 = 19%4+(15/2)*3
c2 = (19%4+15/2*3)
print("c:", c, ",", c1, ",", c2)
d = (15+6)-10*4
d1 = (15+6)-(10*4)
d2 = ((15+6)-10*4)
print("d:", d, ",", d1, ",", d2)
e = 17/2%2*3**3
e1 = 17/2%2*(3**3)
e2 = (17/2)%2*3**3
e3 = (17/2%2)*(3**3)
e4 = ((17/2%2)*(3**3))
e5 = (17/2%2*3**3)
print("e:", e, ",", e1, ",", e2, ",", e3, ",", e4, ",", e5)
# Task 2
string = "abcdefghi"
# 1
print("1.1.", string.capitalize())
print("1.2.", string.title())
print("1.3.", string.replace("a","A"))
# 2
print("2.", string[0:3])
# 3
print("3.", string[1::2])
# 4
print("4.", string.upper())