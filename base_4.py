# def sum(data):
#     sum = 0
#     for i in data:
#         sum += i
#     return sum
# data = [10, 20, 30]
# print(sum(data))


# def remove_duplicates(input_string):
#     output_string = ''
#     for char in input_string:
#         if char not in output_string:
#             output_string += char
#     return output_string
#
# print(remove_duplicates("hello world"))

# def remove_duplicates(input_string):
#     output_string = ''
#     seen = set()
#     for char in input_string:
#         if char not in seen:
#             seen.add(char)
#             output_string += char
#     return output_string
#
#
# print(remove_duplicates('hello world'))

# def remove_duplicates(input_string):
#     seen = set()
#     output_string = ''.join(char for char in input_string if not (char in seen or seen.add(char)))
#     return output_string
#
# print(remove_duplicates('hello world'))


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


# def triangle_perimeter(input_string: str) -> str:
#     try:
#         sides = list(map(float, input_string.split()))
#     except ValueError:
#         return 'Ошибка: введите числа'
#     if len(sides) != 3:
#         return 'Ошибка: введите 3 стороны треугольника'
#     if any(side < 1 or side > 1000 for side in sides):
#         return 'Invalid input'
#     sides.sort()
#     if sides[0] + sides[1] <= sides[2]:
#         return 'Не существует'
#     else:
#         return str(sum(sides))
#
#
# data_input = input()
# print(triangle_perimeter(data_input))


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