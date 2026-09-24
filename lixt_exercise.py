# Very stupid exercise when you research func min|max
shit_list = [24, 3, 56, -12, 0, 8]
min = None
max = None

for i in shit_list:
    if max is None or i > max:
        max = i
    if min is None or i < min:
        min = i

print(f"Max value in shit_list", {max})
print(f"Min value in shit_list", {min})


do_rev_list = [24, 3, 56, -12, 0, 8, 5, 99]
clear_list = []

revd_list = do_rev_list[::-1]
print(do_rev_list, revd_list)

while do_rev_list:
    i = do_rev_list.pop()
    clear_list.append(i)

print(clear_list, sorted(clear_list))
