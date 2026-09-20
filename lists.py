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

popped_motorcycles = motorcycles.pop()
print(popped_motorcycles)
print(motorcycles)

last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")
print(motorcycles)

"""Удаление элементов из произвольной позиции списка"""

first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}")

"""Если собираешься удалить элемент из списка полностью без эксплуатации, то нужно del. 
Если нужно использовать элемент далее то pop()"""

"""Удаление элемента по значению"""
# возьмем отдельный список для наглядности c _

motorcycles_ = ['honda', 'ducati', 'yamaha', 'suzuki', 'ducati']
print(motorcycles_)
motorcycles_.remove('ducati')
print(motorcycles_) # обратим внимание на то, что отсчет шел слева направо и был удален один ducati а еще один остался
"""проверим еще раз - если улучшить вариант по удалению всех эл. то нужно использовать циклы"""
motorcycles_.remove('ducati')
print(motorcycles_) # ['honda', 'yamaha', 'suzuki']

too_expensive = 'yamaha'
motorcycles_.remove(too_expensive)
print(motorcycles_)
print(f"\nA {too_expensive.title()} is too expensive for me.")

"""Упорядочение списка - Python представляет несколько способов упорядочения в зависимости от необходимости"""

"""Метод sort() позволяет изменить список навсегда"""

cars = ["bmw", "audi", "toyota", "subaru"]
cars.sort()
print(cars) # ['audi', 'bmw', 'subaru', 'toyota']
cars.sort(reverse=True)
print(cars) # ['toyota', 'subaru', 'bmw', 'audi']

"""Метод sorted() позволяет выполнить временную сортировку"""
cars_ = ["bmw", "audi", "toyota", "subaru"]
print(f"Here is the original list: {cars_}")
print(f"Here is the sorted list: {sorted(cars_)}")
print(f"Here is reverse the sorted list: {sorted(cars_, reverse=True)}")

"""Вывод списка в обратном порядке"""
# Метод reverse не сортирует в обратном порядке, он меняет порядок списка на обратный (индексы)
print(cars_) # ['bmw', 'audi', 'toyota', 'subaru']

cars_.reverse()
print(cars_)

"""Определение длины списка """

print(len(cars_)) # 4


