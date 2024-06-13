import io
import re

path = rf"C:\Users\AVKochubey\Desktop\parsing\Factiva-20240612-PACA.txt"
path_2 = rf"C:\Users\AVKochubey\Desktop\parsing\iter_1\Factiva-20240612-PACA.txt"
with open(path, 'r', encoding='utf-8') as file:
    # parsing_file = file.open(file.decode('utf-8')))
    current_line_read_file = file.read().splitlines()
    # what_found = 'Document'
    # for what_found in current_line_read_file:
    # print(current_line_read_file[0:5:])
    print()
    print()
    # print(type(current_line_read_file))
    # print(current_line_read_file)
    # sorted(i.findall() for i in )
    current_line_read_file_and_space = [rec + ' ' for rec in current_line_read_file]
    print(current_line_read_file_and_space)

print('Document')
what_found = 'Document'
what_found_2 = ' mots'
print('mots')

str_new_line = rf'\n'
str_space = ' '

#numbers_and_str_2 = [(current_line_read_file_and_space.index(h), h) for h in current_line_read_file_and_space if (what_found_2 in h and len(h)<10)]
#print(numbers_and_str_2)
#print(f"len(numbers_and_str_2): {len(numbers_and_str_2)}")

numbers_and_str = [(current_line_read_file_and_space.index(i), i) for i in current_line_read_file_and_space if what_found in i]
# print(numbers_and_str)
print(f" count numbers_of_str= {len(numbers_and_str)}")
numbers_and_str.insert(0, (0, ''))
# print(numbers_and_str)
print(f" count numbers_of_str= {len(numbers_and_str)}")
# print(numbers_and_str[0])
# print(numbers_and_str[100])
changed_numbers_and_str = []

len_list = 1
while len_list < 101:
    turple_1 = numbers_and_str[len_list - 1]
    turple_2 = numbers_and_str[len_list]
    # print(f"turple_1: {turple_1}")
    # print(f"turple_2: {turple_2}")
    print(f"turple_1[0]: {turple_1[0]}")
    print(f"type(turple_1[0]): {type(turple_1[0])}")
    # print(f"turple_2[0]: {turple_2[0]}")
    # print(f"turple_1[1]: {turple_1[1]}")
    print(f"turple_2[1]: {turple_2[1] + '\n'}")
    print(f"type(turple_2[1]): {type(turple_2[1])}")
    print()
    triple_3 = (turple_1[0], turple_2[1])
    changed_numbers_and_str.append(triple_3)
    print(f"triple_3: {triple_3}")

    # numbers_and_str[len_list-1] =
    current_line_read_file_and_space[turple_1[0]] = '**** *id_' + turple_2[1] + '*reg_' + '\n'
    len_list += 1

# print(changed_numbers_and_str)
print('--------------------------')
print(type(current_line_read_file_and_space))
# print(current_line_read_file)


with open(path_2, 'w+', encoding='utf-8') as file_2:
    file_2.writelines(current_line_read_file_and_space)

# f.writelines(["cat\n", "dog\n"])

# with open(file) as f:
# lines = f.readlines()

# lines[1] = " Новое Предложение\n"

# with open(file, "w") as f:
# f.writelines(lines)

# with open ('test.txt', 'w') as f:
# f.write(new_data)

# numbers_of_str.
# number_find = next((i for i, s in enumerate(current_line_read_file) if what_found in s), None)
# print(number_find)
# print(type(number_find))


# with open(path_2, 'w', encoding='utf-8') as file_2:
# list_strings[1] = 'строка55\n'  # Вместо 1 номер строки, которую нужно заменить
# f.writelines(list_strings)
# f.close()
#   current_line_read_file_2 = file_2.readlines()
#   print(current_line_read_file_2)


# print(current_line_read_file)
