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

numbers = list(range(1,6))
print(numbers) # [1, 2, 3, 4, 5]



