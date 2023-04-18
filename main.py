
voc = {('a', 'e', 'i', 'o', 'u', 'l', 'n', 's', 't', 'r'): 1, ('d', 'g'): 2, ('b', 'c', 'm', 'p'): 3, ('f', 'h', 'v', 'w', 'y'): 4,
       'k': 5, ('j', 'x'): 8, ('q', 'z'): 10, ('а', 'в', 'е', 'и', 'н', 'о', 'р', 'с', 'т'): 1, ('д', 'к', 'л', 'м', 'п', 'у'): 2,
       ('б', 'г', 'ё', 'ь', 'я'): 3, ('й', 'ы'): 4, ('ж', 'з', 'х', 'ц', 'ч'): 5, ('ш', 'э', 'ю'): 8, ('ф', 'щ', 'ъ'): 10}


str_input = input("Введите какое-нибудь слово: ")
count = 0
for i in range(len(str_input)):
    for state in voc.keys():
        if str_input[i] in list(state):
            count = count + int(voc.get(state))

print(count)
