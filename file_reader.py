'''with open('my_file.txt', 'r') as file: #algoritma membuka dan membaca file
    for string in file: #looping berdasarkan baris
        string_list = string.split(' ') #membuat list
        for symbol in string_list: #melakukan iterasi dalam list
            print(int(symbol)+1) #nyetak data real '''

#taks 1
'''count = 0
with open('my_file.txt', 'r') as file:
    for string in file:
        string_list = string.split(' ')
        for symbol in string_list:
            if int(symbol) == 1:
                count = count+1
print(count) '''

#taks 2 (mengambil data dibaris ke 14 elemen ke 8)
'''with open('my_file.txt', 'r') as file:
    lines = file.readlines()
    second_line = lines[13].split(' ')
    item = int(second_line[7])
    print(item)'''

#taks 3 ()
'''count = 0
with open('my_file.txt', 'r') as file:
    line = file.readlines()
    for i in range(len(line)):
        string_list = line[i].split(' ')
        for j in range(len(string_list)):
            count = count + int(string_list[j])
print(count)'''

#taks 4
'''count = 0
with open('my_file.txt', 'r') as file:
    lines = file.readlines()
    for i in range(len(lines)):
        string_list = lines[i].split(' ')
        for j in range(len(string_list)):
            if i == 2 or i == 5 or i == 8 or i == 11:
                count = count + int(string_list[j])
print(count)'''

#taks 5
count = 0
max_elem = 0
with open('my_file.txt', 'r') as file:
    lines = file.readlines()
    for i in range(len(lines)):
        string_list = lines[i].split(' ')
        for j in range(len(string_list)):
            if int(string_list[j]) > max_elem:
                max_elem = int(string_list[j])
        count = count + max_elem
        max_elem = 0
print(count)