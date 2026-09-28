from itertools import count
from nt import remove

user_logs = [101, 102, 101, 103, 102, 104, 101]

move_set = set(user_logs)
print(move_set)
get_back_list = list(move_set)
print(get_back_list)

#Допустим у нас есть список, в нем будут повторы, но в этом чаще всего есть cat, другие
pets = ["dog", "cat", "snack", "cat", "parrot", "rat", "tortilla", "cat"]
# print(pets.count("cat"))
#
# while True:
#      counter_ = pets.count("cat")
#      if counter_ == 1:
#          break
#      else:
#          pets.remove("cat")
#
# print(pets)

# clean_pet = [pet.remove('rat') for pet in pets]
# print(clean_pet)
clean_pet = [pet for pet in pets if pet != "rat"]
print(clean_pet)

text = "Linux is good"

text.replace("good", "great")

print(text)


text = "кот"
numbers = [1, 2]

a = text.upper()
b = numbers

numbers.append(3)
b.append(4)

print(text)
print(a)
print(numbers)
print(b)