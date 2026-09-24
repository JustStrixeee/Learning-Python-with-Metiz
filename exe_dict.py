menu = {
    "капучино": 150,
    "латте": 180,
    "эспрессо": 100
}

orders = ["капучино", "эспрессо", "капучино", "латте", "капучино"]

total = 0

for order in orders:
    total += menu[order]
    print(menu.get(order))
print(f"Finally sum of order: {total}")
