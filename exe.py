from enum import unique

from PyInstaller.building.datastruct import unique_name

values = [5, 3, 2, 4, 2, 5, 3]
clear_list = []

while values:
    i = values.pop()
    if i != 2:
        clear_list.append(i)
    else:
        continue

print(f"Новый список{clear_list}.")
# for value in values:


uszvers = ["Иван", "Аня", "Иван", "Петр", "Аня", "Ольга"]
unique_name = []

for uzver in uszvers:
    if uzver not in unique_name:
        unique_name.append(uzver)

print(unique_name)

products = [500, 1200, 3000, 800, 1000]
sales_products = []

sale_percent = 10

for product in products:
    if product <= 1000:
        sales_products.append(product)
    else:
        calculate_ = (product * sale_percent) / 100
        result_ = product - calculate_
        sales_products.append(int(result_))

print(sales_products)

def order_(sales_products):
    return print(sum(sales_products), max(sales_products), min(sales_products))

order_(sales_products)



"""
for product in products:
    if product > 1000:
        calculate_ = (product * sale_percent) / 100
        result_ = product - calculate_
        sales_products.append(int(result_))
    else:
"""