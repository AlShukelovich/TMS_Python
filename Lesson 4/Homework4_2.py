# task 2
def new_a(x):
   dict = {}
   for i in x:
    dict[i] = dict.get(i,0) + 1
   return dict
   print(dict)
a ="тетрадь"
b = list(a)
print(new_a(b))
# 2 вариант
def new_q(y):
    dict1 = {}
    for j in y:
        if dict1.get(j,0):
         dict1[j] += 1
        else:
         dict1[j] = 1
    return dict1
    print(dict1)
q = "books"
w = list(q)
print(new_q(w))
# task 3
def new_list(*args):
    c = []
    for i in args:
        c.append(i)
    return c
    print(c)
a = [1, 2, 3]
b = [4, 5, 6]
a1 = [7, 8]
b1 = [21,22]
print(new_list(a, b, a1, b1))
# task4
def new_dict(dict1):
    for key, value in dict1.items():
            key, value = value, key
            print(key,value)
    return dict1
    print(dict1)
dict = {"a":1, "b":2}
r = new_dict(dict)
print(r)
