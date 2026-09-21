"""
Кортеж (tuple) в Python — это неизменяемая структура данных,
которая очень похожа на список, но её нельзя изменить после
создания. Он используется для хранения упорядоченных коллекций
 элементов.
"""

demensions = (200, 50)

print(demensions[0]) # 200
print(demensions[1]) # 50

# Допустим мы хотим попробовать изменить занчение demensions индекса 0 на demensions[0] = 250
# Получим TypeError: 'tuple' object does not support item assignment
print()

"""Перебор всех значений в кортеже"""
for _ in demensions:
    print(_)

print()

"""Элементы кортежа не могут изменятся но им можно присвоить новое значение переменной"""
print(f"Original demensions: {demensions}")
for demension in demensions:
    print(demension)

print()

demensions = (400, 100)
print(f"Extended demensions: {demensions}")
for demension in demensions:
    print(demension)

