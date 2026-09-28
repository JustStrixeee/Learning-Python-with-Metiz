input_chars = input("some characters: ")

def replace_vowels(input_chars):

    old_vowels = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]
    new_vowels = ["о", "и", "e", "e", "а", "ы", "у", "e", "я", "ю"]

    # Переводим строку в список букв
    chars_list = list(input_chars.strip())

    # Бежим ОДНИМ циклом по индексам нашего слова
    for index in range(0, len(chars_list)):
        current_char = chars_list[index]

        # Если буква есть в списке старых гласных
        if current_char in old_vowels:
            # Находим её позицию в таблице шифров
            vowel_index = old_vowels.index(current_char)
            # Меняем СТРОГО эту одну ячейку в нашем списке
            chars_list[index] = new_vowels[vowel_index]

    # Собираем список букв обратно в целую строку
    return f" Changed word: {''.join(chars_list)}"

print(replace_vowels(input_chars))


#text_ = input("Enter some text: ")

# def change_text(text_):
#     return text_.replace("а", "о")
#
# print(change_text(text_))

# def change_master_slave(text_):
#     return text_.replace("а", "о").replace("м", "н")
# print(change_master_slave(text_))

"""Задачи на сортировку в фун-ии"""


# sort()   → изменил список → None
# sorted() → создал новый   → список


# # 1
# numbers = [3, 7, 2, 9, 4]
# def process_numbers(numbers):
#     numbers.append(10)
#     return sorted(numbers)
#
# print(process_numbers(numbers))
#
#
# # 2
# numbers = [5, 2, 8, 1]
# def process_numbers2(numbers):
#     numbers.append(10)
#     result = numbers.sort()
#
#
# print(process_numbers2(numbers))