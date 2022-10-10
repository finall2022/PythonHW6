""" Напишите программу, удаляющую из текста все слова, 
содержащие ""абв"".
Входные и выходные данные хранятся в отдельных текстовых файлах. 



не смог победить ошибку с кодировкой, поэтому строка на латинице"""

# path1 = 'task1file_in.txt'
# path2 = 'task1file_out.txt'
# data_in = open(path1, 'r')
# data_out = open(path2, 'w')
# newline = []
# fragment = 'abc'
# for line in data_in:
#     print(line)
#     oldline = line.split(' ')
#     # print(oldline)
#     for word in oldline:
#         if fragment not in word:
#             newline.append(word)
# line1 = ' '.join(newline)
# data_out.write(line1)
# print(line1)
# data_in.close()
# data_out.close()

path1 = 'task3file_in.txt'
path2 = 'task3file_out.txt'
data_in = open(path1, 'r')
data_out = open(path2, 'w')
newline = []
fragment = 'abc'
for line in data_in:
    list1 = line.split()
    list2 = [i for i in list1 if fragment not in i]
newline = ' '.join(list2)
data_out.write(newline)

data_in.close()
data_out.close()
