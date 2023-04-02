# калькулятор
number1 = int(input("Введите первое число: "))
number2 = int(input("Введите второе число: "))
operations = input("Выберите операцию (+,-,*,/): ")
c = ["+", "-", "*", "/"]
if operations in "+":
    result1 = number1 + number2
    print("Результат: ", result1)
if operations in "-":
    result2 = number1 - number2
    print("Результат: ", result2)
if operations in "*":
    result3 = number1 * number2
    print("Результат: ", result3)
if operations in "/":
    result4 = number1 / number2
    print("Результат: ", result4)
for i in c:
    j = input("Хотите продолжить? (yes/no): ")
    if j in "no":
        print("Спасибо!")
        break
    if j in "yes":
        number1 = int(input("Введите первое число: "))
        number2 = int(input("Введите второе число: "))
        operations = input("Выберите операцию (+,-,*,/): ")
        if operations in "+":
            result1 = number1 + number2
            print("Результат: ", result1)
        if operations in "-":
            result2 = number1 - number2
            print("Результат: ", result2)
        if operations in "*":
            result3 = number1 * number2
            print("Результат: ", result3)
        if operations in "/":
            result4 = number1 / number2
            print("Результат: ", result4)

