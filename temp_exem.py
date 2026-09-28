transactions = [101, "ERROR", 102, 103, "ERROR", 104]

clean_tx = [transaction for transaction in transactions if transaction != "ERROR"]
print(clean_tx)

screws = 0
while screws < 10:
    screws += 1
    print(f"Гайка №{screws} закручена.")

    if screws == 7:
        print(f"Перегрев {screws}! Мгновенная остановка!")
        break


subscriptions = {
    "basic": 300,
    "premium": 700,
    "ultra": 1200
}
subscriptions["basic"] += 50
subscriptions["ultra"] = 1500

for key, value in subscriptions.items():
    print(f"{key}: {value}")


clients_db = {
    "Антон": 1200,
    "Мария": 7500,
    "Игорь": 4800,
    "Ольга": 9300,
    "Влад": 5000
}

promo_clients = [name for name, money in clients_db.items() if money >= 5000]
print(promo_clients)
