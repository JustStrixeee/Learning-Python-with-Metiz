user_profile = {
    "name": "Иван",
    "balance": 3000,
    "is_admin": True,
    "city": "Москва",
    "status": "Active"
}


# 1. Достань имя (можно по обычному ключу в квадратных скобках)
name = user_profile["name"]

# 2. ТВОЙ ХОД: Достань телефон через .get(), чтобы код не упал
phone = user_profile.get("phone", "Не указан")

print(f"Имя: {name}")
print(f"Телефон: {phone}")

for key, value in user_profile.items():
    print(f"Ключ: {key} | Значение:  {value}")



stock = {
    "яблоки": 50,
    "бананы": 0,
    "апельсины": 12,
    "груши": 0
}

for key, value in stock.items():
    if value > 0:
        print(f"{key.title()} кол-во {value} шт.")
    else:
        print(f"[ВНИМАНИЕ] {key.title()} закончился!")

banned_dict = {
    "круассаны": "SA-101",
    "кортадо": "SA-102",
    "макбук": "SA-103"
}

truck_items = ["яблоки", "кортадо", "картошка", "макбук"]

for item in truck_items:
    if item in banned_dict.keys():
        print(f"[КОНФИСКАТ] {item} запрещен к ввозу!")
    else:
        print(f"{item} проверен, пропускаем")



