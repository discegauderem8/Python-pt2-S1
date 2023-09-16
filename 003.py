
my_items = {"ключик": 2, "книга": 10, "фонарик": 7, "музыкальная колонка": 30}

backpack_size = 39
things_weight = 0
sorted_values = sorted(my_items.values(), reverse=True)

final_items = {}

for i in sorted_values:
    for k in my_items.keys():
        if my_items[k] == i:
            if things_weight + i > backpack_size:
                break
            else:
                final_items[k] = my_items[k]
                things_weight += i



print(final_items)

