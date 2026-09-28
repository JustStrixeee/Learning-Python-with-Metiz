balance = 500

while balance > 0:
    balance -= 100
    print(balance)


details = 0
while details < 5:
    details += 1
    print(details)
    if details == 3:
        print(f"Деталь {details} бракованная, пропускаем!")
        continue
    if details == 4:
        print(f"Деталь {details} не до нее, дымится конвеер!")
        break
    """а до 5 мы и не дойдем"""

"""Задача на подбор пароля"""

correct_password = "admin"
attempts = 3

while attempts > 0:
    user_input = input("Enter your password: ")

    if user_input == correct_password:
        print(f"Welcome back!")
        break

    else:
        attempts -= 1
        print(f"You have attempts remaining {attempts}")

else:
    print(f"Account was baned! Call your administrator!")

user_profile = {"name": "Иван",
                "balance": 2500,
                "is_admin": False}

user_profile ["balance"] += 500
user_profile ["is_admin"] = True

print(user_profile)


