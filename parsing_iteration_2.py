import re

file_name = 'Factiva20240612PDL'
path_2 = rf"C:\Users\AVKochubey\Desktop\parsing\iter_1\{file_name}.txt"
path_3 = rf"C:\Users\AVKochubey\Desktop\parsing\iter_2\{file_name}.txt"
with open(path_2, 'r', encoding='utf-8') as file:
    current_line_read_file = file.read()
    #print(type(current_line_read_file))
    # print(current_line_read_file)

    new_text_http_with_bracket = re.findall(rf"\[https?://\S+", current_line_read_file)
    #print(new_text_http_with_bracket)
    print(f"len(new_text_http_without_bracket): {len(new_text_http_with_bracket)}")
    #print(type(new_text_http_with_bracket))



    # text_without_href = current_line_read_file.strip()
    for i in new_text_http_with_bracket:
        #print(i)
        #print(type(i))
        # print(new_text[i])
        # new_current_line_read_file = current_line_read_file.strip(i)
        # print(current_line_read_file.replace(i, ''))
        current_line_read_file = current_line_read_file.replace(i, '')
        # print(current_line_read_file)
        new_text_http_without_bracket = re.findall(f"https?://\S+", current_line_read_file)
        #print(new_text_http_without_bracket)
        print(f"len(new_text_http_without_bracket): {len(new_text_http_without_bracket)}")
        #print(type(new_text_http_without_bracket))

    print('-----------------new_text_http_without_bracket--------------')
    for i in new_text_http_without_bracket:
        print(i)
        print(type(i))
        # print(new_text[i])
        # new_current_line_read_file = current_line_read_file.strip(i)
        # print(current_line_read_file.replace(i, ''))
        current_line_read_file = current_line_read_file.replace(i, '')
# print(current_line_read_file)

with open(path_3, 'w+', encoding='utf-8') as file_3:
    file_3.writelines(current_line_read_file)
