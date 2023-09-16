import string

init_string = "Сыр — это молочный продукт, получаемый путём свертывания молока и последующего отделения сыворотки. " \
         "Он является важной частью диеты во многих культурах по всему миру и имеет богатую историю " \
         "и разнообразие видов и вкусов. История сыра История производства сыра насчитывает тысячелетия. " \
         "Первые упоминания о сыре встречаются в древних рукописях и документах разных культур, таких как египетская и"\
         "сумерийская. В разные эпохи сыр служил источником питания и средством его хранения. , , , , , , , , , , , , , , , , , , , , , , ,"

init_string.lower()
intermediate_string = "".join(char for char in init_string if char not in string.punctuation)
words = intermediate_string.split()

max = 0
most_frequent_word = None

for word in words:
    if words.count(word) > max:
        max = words.count(word)
        most_frequent_word = word

print(f"Наиболее часто встречается слово {most_frequent_word}. Оно упоминается в тексте {max} раз")
