print('1) Створити простий калькулятор, який зчитує три рядки введених користувачем даних:')
print('перше число, друге число та операцію. Після цього калькулятор застосовує операцію до')
print('введених чисел ("перше число" "операція" "друге число") і виводить результат на екран.')
print('Підтримувані операції: +, -, /, *, mod, pow, div, де:')
print('mod - це отримання залишку від ділення,')
print('pow - піднесення до степеня,')
print('div - цілочисельне ділення.')
def calculate(A, operator, B):
    if operator == "+":
        return A + B
    elif operator == "-":
        return A - B
    elif operator == "/":
        return A / B
    elif operator == "*":
        return A * B
    elif operator == "mod":
        return A % B
    elif operator == "pow":
        return A ** B
    elif operator == "div":
        return A // B
    elif operator == "de":
        return A / 100 * B
    else:
        return "Invalid operator"
A = int(input("Введите первое число: "))
operator = input("Виберите операцию (+, -, /, *, mod, pow, div, de): ")
B = int(input("Введите второе число: "))
result = calculate(A, operator, B)
print("Результат:", result)


print('2) Маємо 2 числа a і b. Визначте, чи ділиться a на b націло. Чи ділиться b на a?')
a = int(input("Ввести перше число : "))
b = int(input("Ввести друге число: "))
if b % a == 0:
    print(b, "рівномірно ділиться на", a)
else:
    print(b, "не ділиться рівномірно на", a)
if a % b == 0:
    print(a, 'рівномірно ділиться на', b)
else:
    print(a, "не ділиться рівномірно на", b)

print('3) Дано трицифрове число. Визначте, чи є серед його цифр однакові.')
number = int(input("Введіть трицифрове число: "))
digit_1 = number // 100  # extract first digit
digit_2 = (number // 10) % 10  # extract second digit
digit_3 = number % 10  # extract third digit
if digit_1 == digit_2 or digit_1 == digit_3 or digit_2 == digit_3:
    print("Число має хоча б одну повторювану цифру.")
else:
    print("Число не містить однакових цифр.")