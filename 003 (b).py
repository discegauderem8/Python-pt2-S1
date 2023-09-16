my_items = {"ключик": 2, "книга": 10, "фонарик": 7, "музыкальная колонка": 30}

backpack_size = 40
things_weight = 0
sorted_values = sorted(my_items.values(), reverse=True)

values_visited = []

final_items = {}

for k in my_items.keys():  # Самый большой предмет должен быть первым в списке финальных предметов
    if my_items[k] == sorted_values[0]:
        final_items[k] = my_items[k]
        values_visited.append(sorted_values[0])
        things_weight += sorted_values[0]

while len(values_visited) < len(my_items):  # Перебираем по одному предметы, помимо самого большого
    for item in sorted_values:
        if item not in values_visited and things_weight + item <= backpack_size:
            values_visited.append(item)
            for k in my_items.keys():
                if my_items[k] == item:
                    final_items[k] = my_items[k]
                    things_weight += item
    print(final_items)

    things_weight = sorted_values[0]  # Обнуляем значения до начальных и добавялем
    final_items = {}                  # в финальный список самый большой предмет
    for k in my_items.keys():
        if my_items[k] == sorted_values[0]:
            final_items[k] = my_items[k]
