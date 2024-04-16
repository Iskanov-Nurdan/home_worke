# #1 Задание
# dictionary_1 = {'a': 300, 'b': 400} 
# dictionary_2 = {'c': 500, 'd': 600}

# dictionary_1.update(dictionary_2)
# print(dictionary_1)
#2 Задание
# number = {'num_1' : 1, 'num_2' : 2, 'num_3' :3, 'num_100' : 100}
# print(number['num_1']*5)
# print(number['num_2']*5)
# print(number['num_3']*5)
# print(number['num_100']*5)
#3 Задание
# student = {'name' : 'Askhat', 'age' : 17}
# print(student['age']*2)
#4 Задание
# student = {'name' : 'Askhat', 'age' : 17, 'color' : 'White' }
# student['age'] = 16
# print(student)
#5 Задание
# student = {'name' : 'Askhat', 'age' : 17}
# student.pop('age')
# print(student)
#6 Задание
# student = {'name' : 'Askhat'}
# student['address'] = 'Западный Анар'
# print(student)
#7 Задание
# def funk():
#     text = input("Введите слова: ")
#     rozdel = text.split()
#     a = []
#     for word in rozdel:
#         a.append(word[0].upper())
#     b = "".join(a)
#     print(b)

# funk()
#8 Задание
# def count_words(song):
#     words = song.lower().split()
#     word_count = {}
#     for word in words:
#         if word in word_count:
    
#             word_count[word] += 1
#         else:
#             word_count[word] = 1
#     return word_count

# song = "Money, money, money, it's always sunny, in the richmen's world"
# word_count = count_words(song)
# for word, count in word_count.items():
#     print(f"слово  -  {word}: кол-во {count}\n")
#9 Задание
# def isoramm(word):
#     word_dick = list(word)
#     no_duble = set(word)
#     if len(word_dick) == len(no_duble):
#         print("True")
#     else:
#         print("False")

# isoramm(input("Введите слова: "))
#10 Задание
# a = input("Введите число:")
# b = ''
# for i in a:
#     b = i + b
# print(b)
#Доп дз
#11 Задание
# def bot(text):
#     text = input("Введите слова ")
#     if "?" in text:
#         print("Конечно")
#     elif "!" in text:
#         print("Успокойся")
#     elif text == "":
#         print("Как классно, когда ты молчишь. Продолжай в том же духе")
#     else:
#         print("ну и что")

# bot("text")

