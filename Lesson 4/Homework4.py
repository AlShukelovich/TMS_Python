# Part 1
# Task 1
m = "заказ"
n = list(m)
c = []
def check(p):
 for i in reversed(p):
  c.append(i)
 if c == n:
  print("Палиндром")
 else:
     print("Не палиндром")
g = check(n)

# Task 2
# сделать результат в словаре не получилось.
def new_a(x, y):
   dict = {}
   x = dict.values()
   y = dict.keys()
   print(dict)

a ="тетрадь"
b = list(a)
j = 0
for i in b:
    j = b.count(i)
    print(j, i)
#new_a(i, c)

#Task 3
#Вариант 1
def new_list(a, b):
    c = []
    c = a + b
    print(c)

a = [1, 2, 3]
b = [4, 5, 6]
#Вариант 2
#если количество списков неизвестно
listm_ = []
while True:
    list_ = input("Введите строку: ")
    listn_ = list(list_)
    listm_.extend(list_)
    print(listm_)

#Task 4
#значения в функции поменялись. но не получилось изменить это в самом словаре dict1
def new_dict(dict1):
    for key, value in dict1.items():
            key, value = value, key
            print(key,value)
    print(dict1)

dict = {"a":1, "b":2}
new_dict(dict)

#Task 5
a = 10
b = 2
abc = lambda a, b: a % b
print(abc(a,b))
if abc(a,b) == 0:
        print("Число четное")
if abc(a,b) != 0:
        print("Число нечетное")

















