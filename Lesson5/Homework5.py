# part 1, task 1
a = ["books", "flowers", 12, 2, "city", "snow"]
print(list(filter(lambda x: isinstance(x,str), a)))
print(list(filter(lambda  x: type(x) == str, a)))
# task 2
from functools import  reduce
list_ = [10, 20, 30, 40]
a = reduce(lambda x,y: (x + y), list_,0)
b = reduce(lambda x,y: len(list_),list_,1)
print(a/b)
# task 3
persons = [{"name":"Vasya", "birth_year":1999},{"name":"Valentin", "birth_year":1934},
           {"name":"Petr", "birth_year":2005}]
n = list(map(lambda x: x.update({"age": 2023 - x["birth_year"]}), persons))
print(persons)
# part 2 task 1
def change_name(func):
    def name():
        p = func()
        print(p.capitalize())
    return name()
@change_name
def func():
    return input("Введите имя: ")
#part 3 пробовала сделать
def calculate(func):
    def check(x, y):
        if x and y in check.cache:
            print("From cache: ", check.cache)
        else:
            c = mul(x, y)
            check.cache[x, y] = c
            print(c)
        check.cache = {}
        return check()
@calculate
def mul(a, b):
    a = 2
    b = 3
    return a * b





