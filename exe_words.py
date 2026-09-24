city_redneck_words = ["купи", "Тесла", "Пилатес", "Кортадо", "Вай-фай", "Макбук", "Лабрудель"]

city_redneck_comment = ["привет", "как", "дела", "купи", "нашу", "Макбук"]

censored_comment = []
censore = '[ЦЕНЗУРА]'

for i in city_redneck_comment:
    if i in city_redneck_words:
        i = censore
    censored_comment.append(i)

print(censored_comment)
