my_string = input(str('Введите предложение: '))
my_string1 = my_string.replace(' ','')
"""назначаем новую переменную my_string1, в нее заносим значение из my_string,
но уже без пробелов, функцией .replace() вырезаем пробелы"""
print(my_string1)
if my_string1 != my_string1[::-1]:#здесь сравниваем наши переменные my_string & my_string1
    #my_string с начала, my_string1 c конца(для этого на мужен первый символ с конца, т.е -1)
    print('не является палиндромом')
else:
    print('является палиндромом')