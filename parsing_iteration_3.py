import re

file_name = 'Factiva20240612ARA'
path_3 = rf"C:\Users\AVKochubey\Desktop\parsing\iter_2\{file_name}.txt"
path_4 = rf"C:\Users\AVKochubey\Desktop\parsing\iter_3\{file_name}.txt"
with open(path_3, 'r', encoding='utf-8') as file:
    current_line_read_file = file.read()
    print(type(current_line_read_file))
    #print(current_line_read_file)

    new_text = re.findall(rf"[0-9]+ mots.+ *eserved", current_line_read_file)
    print(new_text)
    print(len(new_text))
    print(type(new_text))

    for i in new_text:
        print(i)
        print(type(i))
        #print(new_text[i])
        #new_current_line_read_file = current_line_read_file.strip(i)
        #print(current_line_read_file.replace(i, ''))
        current_line_read_file = current_line_read_file.replace(i, '')

with open(path_4, 'w+', encoding='utf-8') as file_4:
    file_4.writelines(current_line_read_file)