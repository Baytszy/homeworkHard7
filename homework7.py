grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]] #list
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
a = {}
a[list(students)[0]] = sum(grades[0]) / len(grades[0])
a[list(students)[1]] = sum(grades[1]) / len(grades[1])
a[list(students)[2]] = sum(grades[2]) / len(grades[2])
a[list(students)[3]] = sum(grades[3]) / len(grades[3])
a[list(students)[4]] = sum(grades[4]) / len(grades[4])
print(a)


#appdate добавялет несколько пар сразу phone_book.update({.....})
#get возвращает значение по указ ключу phone_bok.get('kay')
#pop - a = phone_book.pop('Anton') удаляет ключ и возвращает cоответствующее ему значение

#множества
#set_= {1,2,3,4,5}
#мжства хранят только уникальные значения
#set перевести список в множества - set(list)