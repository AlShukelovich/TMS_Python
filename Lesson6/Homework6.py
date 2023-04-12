# Functions, task 1
def same_value(x, y):
    c = []
    for i in x:
        for j in y:
            if i == j:
                c.append(i)
            else:
                pass
    return print(c)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
same_value(a, b)

# task 9
def new_dict(x, y):
    d = {}
    for i in x:
        for j in y:
            if x.index(i) == y.index(j):
                d[i] = d.get(0, j)
    return print(d)

a = [1, 2, 3]
b = ["q", "w", "e"]
new_dict(a, b)

# Wrappers, task 3
def check_values(func):
    def inner_func(x, y):
        if x > 0 and y > 0:
            func(x, y)
        else:
            print("Error")
    return inner_func

@check_values
def func(a, b):
    print(a/b)
func(1,0)

# task 8, method 1
def single_values(func):
    def inner_func(*args):
        t = []
        func(*args)
        for i in args:
            if i not in t:
                t.append(i)
        print(t)
    return inner_func

@single_values
def func(*args):
    print(args)  # после добавления декоратора ожидается что func выведет ("string", 1, 2, 3)
func("string", 1, 2, 3, 2, "string")

# method 2
def single_values2(func):
    def inner_func(*args):
        t = []
        func(*args)
        for i in args:
            t.append(i)
            e = set(t)
        print(e)
    return inner_func

@single_values2
def func(*args):
    print(args)  # после добавления декоратора ожидается что func выведет ("string", 1, 2, 3)
func("string", 1, 2, 3, 2, "string")

