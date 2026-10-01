import pizza # Открывает доступ программе ко всем функциям из модуля
# Чаще всего пишут обращение к конкретной функции модуля и синтаксис имеет вид
# from pizza import make_pizza - суть такова, что если у нас есть фун-ия make_pizza то вот ее и берем напрямую

# import pizza as p - даст возможность p.make_pizza(16, "pepperoni") как псевдоним
# p.make_pizza(16, "pepperoni")
# Вывод :
# Making pizza of size 16-inch with the following toppings:
# - pepperoni

# from pizza import * - для импортирования каждой фун-ии в модуле


pizza.make_pizza(16, "pepperoni")
pizza.make_pizza(12, "mushrooms", "green peppers", "extra cheese")

