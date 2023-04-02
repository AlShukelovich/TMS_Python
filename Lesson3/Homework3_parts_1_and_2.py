# Part 1
# Task 1
a = int(input("Введите число: "))
if a % 2 == 0:
     print(f"Число", a, f"четное")
else:
     print(f"Число", a, f"нечетное")
# Task 2
b = int(input("Введите угол: "))
if b >= 0 and b <= 90:
    print("Угол 1 четверти")
elif b >= 91 and b <= 180:
    print("Угол 2 четверти")
elif b >= 181 and b <= 270:
    print("Угол 3 четверти")
else:
    b >= 271 and b <= 360
    print("Угол 4 четверти")
# Task 3
age = int(input("Ваш возраст: "))
experience = int(input("Ваш опыт: "))
if (age >= 20 and age < 80) and experience >= 3:
    print("Вы подходите!")
elif experience < 3:
    print("Вы не подходите")
# Task 4
month = int(input("Your month: "))
if month in [3, 4, 5]:
    print("Spring")
elif month in [6, 7, 8]:
    print("Summer")
elif month in [9, 10, 11]:
    print("Autumn")
elif month in [12, 1, 2]:
    print("Winter")
# Part 2
# Task 1
# 1
a = 0
for i in range(0, 101, 4):
    a = i
    print(a)
#2
a = 0
for i in range(0, 101):
    if i % 4 == 0:
        a = i
        print(a)
# Task 2
dict_ = {"name": "Kirill", "age": 44}
d = []
c = dict_.keys()
d.extend(c)
for i in d:
    e = dict_[i]
    print(i, ":", e)
# Task 3
sum = 0
f = int(input("Введите число: "))
for i in range(1, f+1):
 sum += i
 if i == f:
  print(sum)









