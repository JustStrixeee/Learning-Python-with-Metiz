"""Перебор всего списка"""

"""Тело цикла for может содержать сколько угодно строк кода. 
На практике часто требуется выполнить в цикле for несколько 
разных операций для каждого элемента списка."""

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

print() # Просто строка разграничитель

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

print("Thanks you, everyone. That was a great magic show!")

"""Создание числовых списков"""

"""Фун-ия range() - упрощает создание числовых последовательностей """
for value in range(1,5):
    print(value)

# Использование фу-ии range для создания числового списка

""" Если нужно создать числовой список, нужно преобразовать результаты range() в список 
при помощи фу-ии list() следующим образом -> Заключить вызов range() в фу-ию list(), 
результат будет представлять собой список с числовыми элементами."""

numbers = list(range(1, 6))
print(numbers) # [1, 2, 3, 4, 5]

"""Для генерации числовой посл-ти в заданном диапазоне можно задать range(1, 6)
в случае если нам нужен определенный шаг, то добавляем 3-е значение, range(1, 6, 2)
"""
even_numbers = list(range(2, 11, 2))
print(even_numbers) # [2, 4, 6, 8, 10]

# создание списка из чисел возведенных в квадрат

squares = []  # создали пустйо список
for value in range(1, 11): # перебрали все значения от 1 до 10 при помощи range()
    square = value**2 # берем текущее значение value и возводим в квадрат
    squares.append(square) # результат степени сохраненный в square добавляем в список squares при помощи метода append()

print(squares) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

"""Более емкий вариант записи кода
squares = []
for value in range(1, 11)
    squares.append(value**2)

print(squares)
"""

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

print(f"min is:", min(digits))
print(f"max is:", max(digits))

"""Генератор списков"""
# Данная вещь хоть и кажется простой и красивой, но вызывает у меня сложности при взаимодействии
squares_ = [value**2 for value in range(1, 11)]
print(squares_) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

"""Работа с частью списка slices позволяет работать с конкретным подмножеством элементов списка
и может содержать любую выбранную часть, начало, середину или конец"""
contacts = ["charles", "martina", "michael", "florence", "eli"]
print(contacts[0:3]) # ['charles', 'martina', 'michael']
print(contacts[:3]) # Эквивалент без 0 - ['charles', 'martina', 'michael']
print(contacts[-3:]) # Эквивалент reverse, выведет - ['michael', 'florence', 'eli']
print(contacts)

"""Перебор содержимого среза """
contacts = ["charles", "martina", "michael", "florence", "eli"]
