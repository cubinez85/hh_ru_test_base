# orders = [
#     {'order_id': 101, 'product': 'Ноутбук'},
#     {'order_id': 102, 'product': 'Смартфон'}
# ]
# for order in orders:
#     print(f'Заказ №{order["order_id"]}: {order["product"]}')
# else:
#     print('В списке заказов нет данных')


# orders = [
#     {'order_id': 101, 'product': 'Ноутбук'},
#     {'order_id': 102, 'product': 'Смартфон'}
# ]
#
# if orders:
#     for order in orders:
#         print(f"Заказ №{order['order_id']}: {order['product']}")
# else:
#     print('В списке заказов нет данных')


# def check_candidates(names_input, scores_input):
#     names = names_input.split(',')
#     blocks_scores = scores_input.split('|')
#     if len(names) != len(blocks_scores):
#         return 'Ошибка: Списки не равны'
#     average_scores = []
#     for block in blocks_scores:
#         try:
#             scores = list(map(int, block.split(',')))
#             if len(scores) != 4:
#                 return 'Ошибка: Каждая группа оценок должна содержать ровно 4 оценки'
#             if not all(0 <= score <= 100 for score in scores):
#                 return 'Ошибка: Введите значения от 0 до 100 включительно'
#             average_sum = sum(scores) / len(scores)
#             average_scores.append(average_sum)
#         except ValueError as e:
#             return f'Ошибка: Введите целые числа. {str(e)}'
#
#     passing_candidates = [name for name, score in zip(names, average_scores) if score >= 50]
#     if passing_candidates:
#         return '\n'.join(passing_candidates)
#     else:
#         return 'Никто'
#
#
# data_names = input()
# data_scors = input()
# result = check_candidates(data_names, data_scors)
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


# def is_right_triangle(side_string: str) -> bool:
#     try:
#         sides = list(map(int, side_string.split()))
#         if len(sides) != 3:
#             raise ValueError('Ошибка: Введите 3 стороны треугольника')
#         if not all(1 <= side <= 1000 for side in sides):
#             raise ValueError('Ошибка: Введите значения от 1 до 1000 включительно')
#     except ValueError as e:
#         print(e)
#         return False
#     side1, side2, side3 = sorted(sides)
#     return side1 ** 2 + side2 ** 2 == side3 ** 2
#
#
# side_string = input()
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



# def solve(input_string1: str, input_string2: str) -> str:
#     try:
#         lst1 = [int(i) for i in input_string1.split()]
#         lst2 = list(map(int, input_string2.split()))
#         if len(lst1) != len(lst2):
#             return 'Ошибка: списки не равны'
#         elif len(lst1) > 100:
#             return 'Ошибка: длины списков не больше 100 элементов'
#     except ValueError:
#         return 'Ошибка: введите целые числа'
#
#     from collections import Counter
#     count1 = Counter(lst1)
#     count2 = Counter(lst2)
#     if count1 == count2:
#         return 'Yes'
#     else:
#         return 'No'
#
#
# data1_input = input()
# data2_input = input()
# result = solve(data1_input, data2_input)
# print(result)