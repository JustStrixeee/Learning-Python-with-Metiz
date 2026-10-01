# изучаем функции по принципу проектирования бетономешалки
from numpy.ma.core import append

from dictionary import current_total


def concrete_mixer(concrete): # Т.е. в теории мы должны как сделать: берем чертеж и думаем как реализовать задачу
    return f"We mixed {concrete}!" # внутрь помещаем наше содержимое и что-то с ним делаем, добавим песок и воду. Мешаем.

print(concrete_mixer("concrete"))

# Задача: «Калькулятор скидок»
# напишем простую функцию, которая принимает цену товара и размер скидки в процентах, а потом считает итоговую стоимость.

def calculator_price(price, discount):
    final_results = price * (1 - discount / 100)
    return f"Wr bye concerete with {discount}% sale, as {final_results}!"

print(calculator_price(1000, 10))
print(calculator_price(500, 5))


# «То, что произошло внутри бетономешалки, остаётся внутри бетономешалки»
def concrete_mixer2(cement, sand="песок", water="воду"):
    return f"We mixed {cement}, {sand} и {water}!"

print(concrete_mixer2("цемент"))

def build_wall(blocks_count):
    wall_status = "Стена построена"
    return f"{wall_status} из {blocks_count} блоков."

# Так не делай! Это для наглядности внутр. переменной, что находится в функции.
# print(wall_status)


flat_rooms = [20, 15, 12, 35]

def calculate_cement(rooms_list):
    cement_needed = [] # пустой список для результатов

    for room in rooms_list: # Запусти цикл for по полученному списку
        bags_cement = room * 2 #  каждом шаге умножай площадь комнаты на 2
        cement_needed.append(bags_cement) # добавляй результат в cement_needed через .append()

    return cement_needed

# Вызываем функцию и заземляем результат в новую переменную
total_cement = calculate_cement(flat_rooms)

print(f"Площади комнат: {flat_rooms}")
print(f"Необходимо мешков цемента по комнатам: {total_cement}")

print(calculate_cement(flat_rooms))

def calculate_cement_pro(rooms_list):
    # Фейсконтроль/генератор сразу возвращает собранный в воздухе список!
    return [room * 2 for room in rooms_list]

print(calculate_cement_pro(flat_rooms))

print([x for x in range(5) if x % 2])

def radius_info_cycle(radius, pi=3.14):
    s = pi * radius**2
    return s

print(radius_info_cycle(5))

users = ['asdf;', 'asd;fkew', 'S134rkdf', '43rt894']

def say_hello(names):
    for name in names:
        print(f"Hello {name.title()}")


print(say_hello(users))



# def print_machine(list_for_printer, completed):
#     for index, value in enumerate(list_for_printer):
#         print(f"{index}. {value} was printed.")
#         completed_list.append(value)
#         return completed_list
#
# def user_info_status_print(completed_list):
#     for i in completed_list:
#         result = completed_list.pop(i)
#         print(f"{i}: {result}")

print_list = ["phone case", "harry potter figure", "arduino case", "cat toy"]
completed_list = []


def printer_work(print_, completed_):
    while print_:
        current_design = print_.pop()
        completed_.append(current_design)

    return f"Program 3D printing was done!"

def user_output_info(completed_):
    for index, value in enumerate(completed_, start=1):
        print(f"{index}. Element was painted: {value.title()}")



print(printer_work(print_list[:], completed_list))
user_output_info(completed_list)


def make_pizza(*toppings):
    """Выводит описание пиццы с заказанными топингами."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

# Вызовы функции напрямую (без внешнего print(), чтобы не было None)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

def build_profile(first, last, **user_info):
    """Строит словарь, где имя и фамилия ВСЕГДА идут первыми."""
    # Сначала создаем базис с правильным порядком ключей
    profile = {
        'first_name': first,
        'last_name': last,
    }
    # Добавляем все остальные параметры из **user_info в конец
    profile.update(user_info)
    return profile

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)

