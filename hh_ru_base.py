# def filter_successful_employees(sales_string: str, names_string: str) -> list[str]:
#     sales = sales_string.split(',')
#     names = names_string.split(',')
#     if len(sales) != len(names):
#         print('Списки не равны')
#         return []
#     result = []
#     for sale, name in zip(sales, names):
#         try:
#             if int(sale) < 0:
#                 print(f'Ошибка: "{sale}" => не может быть отрицательных продаж')
#             elif int(sale) >= 1000:
#                 result.append(name.strip())
#         except ValueError:
#             print(f'Ошибка: "{sale}" => введите целое число')
#     return result
#
#
# sales_string = input()
# names_string = input()
# successful_employees = filter_successful_employees(sales_string, names_string)
# if successful_employees:
#     for employee in successful_employees:
#         print(employee)
# else:
#     print('Никто')



# def filter_passed_students(score_string: str, name_string: str) -> list[str]:
#     score = score_string.strip().split(',')
#     name = name_string.strip().split(',')
#     if len(score) != len(name):
#         print('Списки не равны')
#         return []
#     passed_students = []
#
#     for i in score:
#         try:
#             score_value = int(i)
#             if score_value < 0 or score_value > 55:
#                 print(f'Не корректные значения: {score_value}. Введите оценки от 0 до 55.')
#                 return []
#         except ValueError:
#             print('Введите целые числа только в оценках')
#             return []
#
#     for score_i, name_i in zip(score, name):
#         if int(score_i) >= 35:
#             passed_students.append(name_i)
#     if not passed_students:
#         print('Никто')
#     return passed_students
#
# score_string = input()
# name_string = input()
# passed_students = filter_passed_students(score_string, name_string)
# for student in passed_students:
#     print(student)


#
# def classify_triangle(input_string: str) -> str:
#     lst = input_string.strip().split()
#     if len(lst) != 3:
#         return 'Ошибка: необходимо ввести ровно 3 значения'
#     try:
#         sides = [float(i) for i in lst]
#     except ValueError:
#         return 'Ошибка: все значения должны быть числовыми'
#
#     for side in sides:
#         if side <= 0 or side > 1000:
#             return 'Ошибка: длины сторон должны быть от 1 до 1000 включительно'
#
#     if sides[0] + sides[1] <= sides[2] or sides[1] + sides[2] <= sides[0] or sides[0] + sides[2] <= sides[1]:
#         return 'Не треугольник'
#     if sides[0] == sides[1] == sides[2]:
#         return 'Равносторонний'
#     elif sides[0] == sides[1] or sides[1] == sides[2] or sides[2] == sides[0]:
#         return 'Равнобедренный'
#     else:
#         return 'Обычный'
#
# input_string = input()
# result = classify_triangle(input_string)
# print(result)



# def check_password(password):
#     spec_symbols = '[!@#$%*^&(),.?\":{}|<>]'
#     if len(password) < 8 or len(password) > 100:
#         print('Не подходит')
#         return ''
#     if not any(i in spec_symbols for i in password):
#         print('Не подходит')
#         return ''
#     if not any(i.isdigit() for i in password):
#         print('Не подходит')
#         return ''
#     if not any(i.islower() for i in password):
#         print('Не подходит')
#         return ''
#     if not any(i.isupper() for i in password):
#         print('Не подходит')
#         return ''
#     return 'Подходит'
#
#
# password = input()
# result = check_password(password)
# print(result)



# def solve(input_string: str) -> str:
#     punctuation = "!-,.?"
#     if not input_string:
#         return 'Invalid input'
#     lower_str = input_string.lower()
#     clean_string = lower_str.translate(str.maketrans('', '', punctuation))
#     unique_words = set(clean_string.split())
#     length = len(unique_words)
#     return str(length)
#
# input_string = input()
# result = solve(input_string)
# print(result)


# def check_candidates(names_input, scores_input):
#     names = names_input.strip().split(',')
#     blocks_scores = scores_input.split('|')
#     if len(names) != len(blocks_scores):
#         return 'Ошибка: Длины списков не равны'
#     mid_summa = []
#     try:
#         for block in blocks_scores:
#             scores = [int(num) for num in block.split(',')]
#             if len(scores) != 4:
#                 return 'Ошибка: Каждая группа оценок должна содержать ровно 4 оценки'
#             if not all(0 <= score <= 100 for score in scores):
#                 return 'Ошибка: Вводимые оценки должны быть от 0 до 100 включительно'
#             average_summa = sum(scores) / len(scores)
#             mid_summa.append(average_summa)
#     except ValueError as e:
#         return f'Ошибка: Введите целые числа. {str(e)}'
#
#     res = [name for name, score in zip(names, mid_summa) if score >= 50]
#     if res:
#         return '\n'.join(res)
#     else:
#         return 'Никто'
#
#
# names_input = input()
# scores_input = input()
# result = check_candidates(names_input, scores_input)
# print(result)





# def is_right_triangle(side_string: str) -> bool:
#     sides = side_string.split()
#     if len(sides) != 3:
#         print('Ошибка: Надо ввести ровно 3 стороны')
#         return False
#     try:
#         sides = [int(side) for side in sides]
#         if not all(1 <= side <= 1000 for side in sides):
#             print('Ошибка: Все стороны должны быть от 1 до 1000 включительно')
#             return False
#     except ValueError:
#         print('Ошибка: Все стороны должны быть целыми числами')
#         return False
#     side_1, side_2, side_3 = sorted(sides)
#     return side_1 ** 2 + side_2 ** 2 == side_3 ** 2
#
#
# side_string = input().strip()
# if is_right_triangle(side_string):
#     print('Да')
# else:
#     print('Нет')




# def solve(input_string1: str, input_string2: str) -> str:
#     try:
#         string1 = list(map(int, input_string1.split()))
#         string2 = list(map(int, input_string2.split()))
#         if len(string1) != len(string2):
#             return 'Ошибка: Длина списков должна быть одинакова'
#         if len(string1) > 100:
#             return 'Ошибка: Длина списка не более 100 элементов'
#         count1 = {}
#         count2 = {}
#         for num in string1:
#             if num in count1:
#                 count1[num] += 1
#             else:
#                 count1[num] = 1
#         for num in string2:
#             if num in count2:
#                 count2[num] += 1
#             else:
#                 count2[num] = 1
#         if count1 == count2:
#             return 'Да'
#         else:
#             return 'Нет'
#     except ValueError:
#         return 'Ошибка: Введите целые числа'
#
#
# input_string1 = input()
# input_string2 = input()
# result = solve(input_string1, input_string2)
# print(result)


# def triangle_perimeter(input_string: str) -> str:
#     try:
#         sides = [float(side) for side in input_string.split()]
#     except ValueError:
#         return 'Введите целые или дробные числа'
#     if len(sides) != 3:
#         return 'Введите 3 стороны'
#     for side in sides:
#         if side <= 0 or side > 1000:
#             return 'Длины сторон от 1 до 1000 включительно'
#     sort_sides = sorted(sides)
#     if sort_sides[0] + sort_sides[1] <= sort_sides[2]:
#         return 'Не существует'
#     perimeter = sum(sort_sides)
#     return f'{perimeter}'
#
#
# input_string = input()
# result = triangle_perimeter(input_string)
# print(result)


# def mask(string_to_mask: str) -> str:
#     data = string_to_mask
#     if not data:
#         return 'Invalid input'
#     if ' ' in data:
#         return 'Строка должна быть без пробелов'
#     if len(data) > 100:
#         return 'В строке не больше 100 символов'
#     if len(data) < 4:
#         return data
#     return '#' * (len(data) - 4) + data[-4:]
#
#
# string_to_mask = input()
# result = mask(string_to_mask)
# print(result)


# def generate_shortcut(full_name: str) -> str:
#     if len(full_name) < 3 or len(full_name) > 50:
#         return 'Invalid input'
#     names = full_name.split()
#     first_name = names[0]
#     last_name = names[1]
#     first_initial = first_name[0].upper() + '.'
#     last_initial = last_name[0].upper() + '.'
#     return first_initial + ' ' + last_initial
#
#
# full_name = input()
# result = generate_shortcut(full_name)
# print(result)
