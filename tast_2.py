print('Меня зовут Svetlana,' 'Домашнее задание №2')

print('1 уровень')
print('1) Пользователь вводит число а и число b. Возвести а в степень b')
a = int(input("Ввести число 1: "))
b = int(input("Ввести число 2: "))
print(a ** b)

print('2) Пользователь вводит 2 числа. Вывести наибольшее из них')
a = int(input("Ввести число1: "))
b = int(input("Ввести число2: "))
print(max(a,b))

print('3) Пользователь вводит сумму в гривне и курс доллара. Нужно пересчитать сумму в долларе')
print('Сумма в гривне:', 25100)
print('Курс доллара:', 38.1)
a = 25100
b = 38.1
print(a//b)

print('4) Пользователь вводит цифру от 1 до 7, нужно вывести соотвествующий день недели')
user_input = int(input("Ввести число: "))
days = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
}
if user_input in days:
    print(days[user_input])
else:
    print("Invalid input. Please enter a number from 1 to 7.")

print('2 уровень')
print('1) Пользователь вводит число. Если оно четное, вывести "четное". Если оно нечетное, вывести "нечетное"')
number = int(input('Ввести число: '))
if number % 2 == 0:
    print('Четное число')
else:
    print('Нечентное число')

print('2) Пользователь вводит 3 числа. Вывести наименьшее из них')
a = int(input('Первое число  : '))
b = int(input('Второе число : '))
c = int(input('Третье число  : '))

smallest = 0

if a < b and a < c :
    smallest = a
if b < a and b < c :
    smallest = b
if c < a and c < b :
    smallest = c

print(smallest, "Это самое маленькое число")

print('3) Из Убудского чата Аня узнала,')
print('что рекомендуется спать хотя бы А часов в сутки,')
print('но пересыпать тоже вредно и не стоит спать более В часов.')
print('Сейчас Аня спит Н часов в сутки.Если режим сна Ани удовлетворяет рекомендациям Сергея,')
print('выведите "Это нормально". Если Аня спит менее А часов,/n выведите "Недосып", если же более В ')
print('то выведите "Пересып" Получаемое число А всегда меньше либо равно В (то есть это проверять не надо)')

A = int(input('Количество часов в сутки рекомендованые ко сну : '))
B = int(input('Не рекомендовано спать больше часов в сутки : '))
H = int(input('Сейчас спит Аня : '))
A <= B
if A <= H <=B:
    print('Это нормально')
elif H < A:
    print('Недосып')
elif H > B:
    print('Пересып')