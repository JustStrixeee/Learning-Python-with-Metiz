"""
Список (list) в Python — это изменяемая, упорядоченная коллекция,
представляющая собой «всеядный» динамический контейнер, куда можно
одновременно положить данные абсолютно любых типов — от простых чисел,
строк и логических значений (True/False) до других списков и сложных
объектов — при этом каждый элемент получает свой строгий порядковый
номер (индекс), что позволяет легко менять их местами, удалять или
добавлять новые прямо на ходу.
"""

# Простой пример

bicycles = ['trek', 'cannondle', 'redline', 'specialized']
print(bicycles)

#Обращение к элементам списка
print(bicycles[0]) # trek

#Отформатировать содержание списка можно при помощи строковых методов
print(bicycles[0].title())  # Trek

print(bicycles[1]) # cannondle
print(bicycles[3]) # specialized
print(bicycles[-1]) # specialized - выведет последний эл. в списке, соотв. и -2 и т.д

"""Исп. отдельных эл. из списка. f-строки"""

message = f"My first bicycle was {bicycles[0].title()}." # My first bicycle was [0].
print(message) # My first bicycle was Trek.

"""Изменение, добавление  и удаление элементов"""

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles) #['honda', 'yamaha', 'suzuki']

motorcycles[0] = 'ducati' # изменим нулевое значение элемента в списке
print(motorcycles) # выведет ['ducati', 'yamaha', 'suzuki']

"""Добавление элементов в список"""

motorcycles.append('ducati') # тут автор непонятно зачем решил вернуть хонду, но я продолжу как есть
print(motorcycles) # метод append() добавляет строку в конец списка ['ducati', 'yamaha', 'suzuki', 'ducati']

"""Вставка элементов в список"""
# данный метод позволяет произвести вставку нового элемента в произвольную позицию списка по заданному индексу
# допустим у нас есть наш список состоящий из ['ducati', 'yamaha', 'suzuki', 'ducati']
# нам нужно добавить 'honda'.

motorcycles.insert(0, 'honda')
print(motorcycles) # ['honda', 'ducati', 'yamaha', 'suzuki', 'ducati'] - где 'honda' стала нулевым индексом списка
# сместив весь список на одну позицию вправо

"""Удаление элементов из списка"""

del motorcycles[0] # ['honda', 'ducati', 'yamaha', 'suzuki', 'ducati'] Удаление при помощи оператора del при его известной позиции
print(motorcycles)

"""Удаление элем. при помощи pop()"""



