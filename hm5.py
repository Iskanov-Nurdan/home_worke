# Dict задачи
# student = {'name':"Nurdan", 'age': "15", 'color': "blek"}
# print(student["name"])
# print(student["age"])
# print(student["color"])
# 2
# student = {'name':"Nurdan", 'age': "15", 'color': "blek"}
# student['hobbe'] = "horse racing"
# print(student)
# 3
# student = {'name':"Nurdan", 'age': "15", 'color': "blek"}
# print(student['age'])
# 4
# student = {'name':"Nurdan", 'age': "15", 'color': "blek"}
# student['color'] = "red"
# print(student)
# 5
# student.pop('hobbe')
# print(student)
# 6
# Set
# 1
# fail = {"red", "blek", "green", "wite",}
# fail1 = set(fail)
# print(fail1)
# 2
# a = {1,2,3,4,5}
# b = {4,5,6,7,8,9}
# result = a.union(b)
# print(result)
# 3
# a = [5, [1, 2], 2, 'r', 4, 'ee']
# b = [4, 'we', 'ee', 3, [1, 2]]
 
# c = []
 
# for i in a:
#     for j in b:
#         if i == j:
#             c.append(i)
#             break
 
# print(c)
# 4
# name1 = input("Введите списак: ")
# name2 = set(name1)
# print(name2)
# 5
# fail = {"red", "blek", "green", "wite",}
# fail = {"red", "blek", "green", "wite",}
# print()

# solar_system = {'Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'}
# first_three_planets = {'Mercury', 'Venus', 'Earth'}
# poor_small_guy = {'Pluto'}
# emptyness = set()
# print(first_three_planets.issubset(solar_system))

# num1 = frozenset(1,2,3,4,5,6,7,8,9)
# num2.add(10)
# print(num1)

# num1 = frozenset([1,2,3,4,5])
# num2 = frozenset([6,7,8,9,10])
# num3 = num1 & num2
# print(num3)

# num1 = frozenset([1,2,3,4,5 ,6,7,8,9])
# num2 = frozenset([10,11,12,13,14,15,16,17,18,19])
# print(num1==num2)


# num1 = frozenset([1,2,3,4,5,6,7,8,9])
# num2 = frozenset([1,2,3,4,5,6,7,8,9])
# print(num1==num2)

# user = frozenset(["Nurdan", "Sabrina", "Nuradil", "Marsel"])
# print(list(user))

# user = frozenset.union(frozenset(["Sabrina","Nurdan","Marsel","Aisezim"]),frozenset(["Nurbolot","Nurai","Islam"]))
# print(user)

# sport = ["foodbol","basketbol","tenis","run","lung jump"]
# num = int(input("Введите число от 1:5: "))
# print(sport[num])

# string_input = input("введите строку: ")
# if string_input.isdigit():
#     number = int(string_input)
#     print("Введеное число:",number)
# else:
#     print("Ошибка")

# month = {"Январь":1,"Февраль":2,"Март":3,"Апрель":4,"Май":5,"Июнь":6,"Июль":7,"Август":8,"Сентябрь":9,"Октябрь":10,"Ноябрь":11,"Декабрь":12}
# user_month = input("Введите месяц: ")
# try:
#     number = month[user_month]
#     print("Порядковый номер месяца '{}' : {}".format(user_month,month))
# except KeyError:
#     print("Месяц не найден '{}'в словаре.".format(user_month))