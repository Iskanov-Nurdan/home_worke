# 1 Задание 
# Исключения нужны, чтобы сообщить программисту об ошибках. И предотвратить их моментально.

# 2 Задание 

# try:
#     print(undefined_variable)
# except NameError:
#     print("Произошла ошибка NameError: такая переменная не определена.")

# try:
#     # Вызываем ошибку IndexError - обращаемся к элементу списка по несуществующему индексу
#     my_list = [1, 2, 3]
#     print(my_list[10])
# except IndexError:
#     print("Произошла ошибка IndexError: индекс выходит за пределы списка.")

# 3 Задание 
# number =input("Введите 4 числа, через запятю: ")
# numbers_list = number.split(',')
# s_num = set(numbers_list)
# print(s_num)

# Доп. задание

# while True:
#     try:
#         num1 = float(input("Введите первое число: "))
#         num2 = float(input("Введите второе число: "))
        
#         sum = num1 + num2
#         raznost = num1 - num2
#         mult = num1 * num2
        
#         if num2 != 0:
#             dev = num1 / num2
#         else:
#             raise ZeroDivisionError("Делить на 0 нельзя! ")

#         print(f"Сумма Ваших чисел: {sum}")
#         print(f"Разность Ваших чисел: {raznost}")
#         print(f"Произведение Ваших чисел: {mult}")
#         print(f"Частное Ваших чисел: {dev}")
        
#         if sum % 2 == 0:
#             print("Сумма четная")
#         else:
#             print("Сумма нечетная")
        
#         break
        
#     except ValueError:
#         print("Ошибка: Введите числа корректно.")
#     except ZeroDivisionError as i:
#         print(f"Ошибка: {i}. Попробуйте ввести другое число.")



# while True:
#       try:
        
#         number_1 = float(input("Введите первое число: "))
#         number_2 = float(input("Введите второе число: "))
        
#         print(f"Сумма: {number_1+number_2}")
#         print(f"Разность: {number_1-number_2}")
#         print(f"Произведение:{number_1*number_2}")
#         print(f"Частное: {number_1/number_2}")
        
#         if number_2 != 0:
#              dev = number_1 / number_2
#         else:
#             raise ZeroDivisionError('На 0 делить нельзяяя!!!')
        
#         break
#       except ZeroDivisionError as i:
#          print(f"Ошибка: {i}. Попробуйте ввести другое число.")


 