my_dict = {
    'day': 'monday',
    'time': "Might",
    'year': 2026
}
print(type(my_dict), my_dict)
print()

runners = ["Алексей", "Мария", "Иван"]
final_results = runners[:]

final_results.append("Ольга")
final_results.insert(0, "Победитель")

print(runners, f"\n {final_results}")

