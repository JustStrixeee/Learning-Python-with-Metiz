"""
dictionary — это изменяемая структура данных, которая хранит
 элементы в формате пар «ключ: значение»
"""
from django.template.defaultfilters import lower

"""Создание пустого словаря"""

alien_0 = {}

"""Вносим значения по [ключу]"""
alien_0['color'] = 'green'
alien_0['points'] = 5
# alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color']) # green | Так выглядит обращение по ключу и вывод по значению
print(alien_0['points']) # 5

print(alien_0) # {'color': 'green', 'points': 5}

"""Обращение к значениям в словаре"""
new_points = alien_0['points']
print(f"You just earned {new_points} points!")


"""Изменение значений в словаре"""
alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")

alien_0 = {'color': 'yellow'}
print(f"The alien is now {alien_0['color']}.")

users = ["Иван", "Анна", "Сергей", "Иван", "Алексей"]
print(users)
users.remove("Иван")

delete_user = users.pop()
print(f"This user was added mistakes: {delete_user}.")

users.append("Мария")
print(len(users), users)

speeds = [1500, 4200, 3000, 800, 5000, 2300]
speeds.sort(reverse=True)
print(speeds, f"\nTop speed is {speeds[:3]}")
print(f"min speed is {min(speeds)}")

staff = {
    "иван": "Разработчик",
    "анна": "Дизайнер",
    "сергей": "Тестировщик"
}
name = input("What is your name?:").strip().lower()

position = staff.get(name, f"Access denied; user '{name}' not found in the system.")

print(position)

traffic = [1200, 4500, 3000, 5100, 2400]
fixed_traffic = []  # Сюда складываем результат

normal_speed_traffic = [] # Cool speed traffic

for _ in traffic:
    if _ >= 3000:
        fixed_traffic.append(_)
    elif _ <= 2999:
        normal_speed_traffic.append(_)
print(f"Ths traffic is over value: {fixed_traffic}, \nthis is pretty well{normal_speed_traffic}")

# Текущие скорости торрентов (в сумме тут 16 200 КБ/с — диск умрет!)
traffic = [1200, 4500, 3000, 5100, 2400]
MAX_TOTAL_LIMIT = 3000  # Больше стольки сервер суммарно выдать не должен

fixed_traffic = []
current_total = 0

for speed in traffic:
    # Сколько у нас осталось свободного места до общего лимита в 3000?
    remaining_space = MAX_TOTAL_LIMIT - current_total

    if remaining_space <= 0:
        # Место кончилось, все остальные торренты получают 0 (стоят в очереди)
        fixed_traffic.append(0)
    elif speed <= remaining_space:
        # Торрент пролазит целиком, отдаем ему всё, что он просит
        fixed_traffic.append(speed)
        current_total += speed
    else:
        # Торрент просит больше, чем осталось. Отдаем ему только остаток!
        fixed_traffic.append(remaining_space)
        current_total += remaining_space

print(f"Исходный трафик: {traffic}")
print(f"Реальное распределение: {fixed_traffic}")
print(f"Итоговая сумма: {sum(fixed_traffic)} КБ/с (Лимит не превышен!)")