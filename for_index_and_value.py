"""Пример 1: Вернет список из фруктов"""
fruits = ["яблоко", "банан", "груша"]

for item in fruits:
    # В переменную item на каждом круге падает само ЗНАЧЕНИЕ
    print(item) #яблоко, банан, груша


"""Пример 2: Вернет список из значений"""
fruits = ["яблоко", "банан", "груша"]

# len(fruits) равен 3. range(3) дает числа 0, 1, 2
for i in range(len(fruits)):
    # В переменную i падает ИНДЕКС (число)
    # Чтобы достать само значение, мы пишем fruits[i]
    print(f"Индекс: {i}, Значение: {fruits[i]}")
"""
Индекс: 0, Значение: яблоко
Индекс: 1, Значение: банан
Индекс: 2, Значение: груша
"""


"""Пример 3: Перебор через enumerate(items)"""

fruits = ["яблоко", "банан", "груша"]
# enumerate выдает сразу две переменные: i (индекс) и item (значение)
for i, item in enumerate(fruits):
    print(f"Порядковый номер: {i}, Фрукт на этом месте: {item}")

"""
Порядковый номер: 0, Фрукт на этом месте: яблоко
Порядковый номер: 1, Фрукт на этом месте: банан
Порядковый номер: 2, Фрукт на этом месте: груша
"""

"""Сравнение"""

"""
Способ записи      |    Что лежит в переменных цикла?  |     Как достучаться до значения?
___________________|___________________________________|________________________________
for item in items: |    item — это само значение.      |     Сразу готово: item

for i in           |    i — это только индекс          |     Нужно вытаскивать: items[i]  
range(len(items)): |    (число 0, 1, 2...).            |

for i, item in     |    i — индекс,                    |     Сразу готово: item 
 enumerate(items): |    item — значение.               |     (а i используем для индекса)
"""


nums = [2, 7, 11, 15]
target = 9

# for i in range(len(nums)):
#     for j in range(i+1, len(nums)):
#         if nums[i] + nums[j] == target:
#             print(f"index {i}, index {j} | value {nums[i]} value {nums[j]}")

for index, value in enumerate(nums):
    for index2, value2 in enumerate(nums[index+1:]):
        if value + value2 == target:
            real_index = index + index2 + 1
            print(f"{value} {value2}")


# Найти индексы двух чисел из nums, которые в сумме дают target (ровно 1 решение, без повтора элементов).
# nums = [2, 7, 11, 15]
# target = 9
# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         # Внешний цикл по всему списку
#         for index, value in enumerate(nums):
#             # Внутренний цикл по отрезанному куску списка
#             for index2, value2 in enumerate(nums[index + 1:]):
#
#                 # Если нашли нужную сумму
#                 if value + value2 == target:
#                     # Вычисляем оригинальный индекс второго числа
#                     real_index2 = index2 + index + 1
#
#                     # Возвращаем результат в виде списка индексов
#                     return [index, real_index2]

print(f"*" * 80)

sessions = [101, 102, 103, 104, 105]
sessions.pop(0)
sessions.remove(104)
sessions.append(106)
print(sessions)