# age = 18
# print('child' if age < 18 else 'old')


# def double_values(values):
#     for i in range(len(values)):
#         values[i] *= 2
#     return values
# data = (10, 20, 30, 40)
# print(double_values(data))

# for i in range(2, 8, 2):
#     print(i * 3)

# def positive_numbers(input_list):
#     output_list = []
#     for num in input_list:
#         if num > 0:
#             output_list.append(num)
#     return output_list
# data = [1, 2, -3, 4, -2]
# print(positive_numbers(data))


# def filter_successful_employees(sales_string: str, names_string: str) -> list[str]:
#     sales = sales_string.split(',')
#     names = names_string.split(',')
#     if len(sales) != len(names):
#         print('Списки не равны')
#         return []
#     for sale in sales:
#         if int(sale) < 0:
#             print('Отрицательные значения в продажах не допускаются')
#             return []
#     # result = [i[1] for i in zip(sales, names) if int(i[0]) >= 1000]
#     result = [name for sale, name in zip(sales, names) if int(sale) >= 1000]
#     return result
#
# sales_string = input()
# names_string = input()
# successful_employees = filter_successful_employees(sales_string, names_string)
#
# if successful_employees:
#     for employee in successful_employees:
#         print(employee)
# else:
#     print('Никто')


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



# def classify_triangle(input_string: str) -> str:
#     if not input_string:
#         return 'Error: Empty data'
#     try:
#         sides = list(map(float, input_string.split()))
#         if len(sides) != 3:
#             return 'Error: Triangle must have 3 sides'
#     except ValueError:
#         return 'Error: Enter digit means'
#     for side in sides:
#         if not (1 <= side <= 1000):
#             return f'Error: "{side}" must be from 1 to 1000'
#         if side <= 0:
#             return f'Error: "{side}" must be greater than 0'
#     sides.sort()
#     if sides[0] + sides[1] <= sides[2]:
#         return 'Не треугольник'
#     sides = [round(side, 6) for side in sides]
#     if len(set(sides)) == 1:
#         return 'Равносторонний'
#     elif len(set(sides)) == 2:
#         return 'Равнобедренный'
#     else:
#         return 'Обычный'
#
#
# input_data = input()
# result = classify_triangle(input_data)
# print(result)



# def classify_triangle(input_string: str) -> str:
#     lst = input_string.split()
#     try:
#         sides = [float(i) for i in lst]
#     except ValueError:
#         return "Ошибка: все значения должны быть числовыми."
#
#     for side in sides:
#         if side <= 0 or side >= 1000:
#             return "Ошибка: длины сторон должны быть больше 0 и меньше 1000."
#
#     summa = sum(sides)
#     max_side = max(sides)
#     summa_two_sides = summa - max_side
#
#     if summa_two_sides <= max_side:
#         return "Не треугольник"
#
#     if sides[0] == sides[1] == sides[2]:
#         return "Равносторонний"
#     elif sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2]:
#         return "Равнобедренный"
#     else:
#         return "Обычный"

# input_string = input()
# result = classify_triangle(input_string)
# print(result)



# def classify_triangle(input_string: str) -> str:
#     lst = input_string.strip().split()
#     if len(lst) != 3:
#         return 'Invalid input'
#     try:
#         sides = [float(i) for i in lst]
#     except ValueError:
#         return 'Ошибка: все значения должны быть числовыми'
#     for side in sides:
#         if not (1 <= side <= 1000):
#             return f'Ошибка: "{side}" => длина стороны от 1 до 1000 включительно'
#     sides.sort()
#     if sides[0] + sides[1] <= sides[2]:
#         return 'Не треугольник'
#     elif sides[0] == sides[1] == sides[2]:
#         return 'Равносторонний'
#     elif sides[0] == sides[1] or sides[1] == sides[2] or sides[2] == sides[0]:
#         return 'Равнобедренный'
#     else:
#         return 'Обычный'
#
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



# import re
#
#
# def check_password(password):
#     return (8 < len(password) < 100 and
#             re.search(r'[!@#$%*^&(),.?\":{}|<>]', password) and
#             re.search(r'\d', password) and
#             re.search(r'[A-Z]', password) and
#             re.search(r'[a-z]', password)
#             )
#
#
# input_data = input()
# print('Yes' if check_password(input_data) else 'No')