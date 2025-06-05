# total_seconds = 10
# start_time = 0
# current_tick = 0
# while start_time < total_seconds:
#     if start_time % 2 == 0:
#         current_tick = (current_tick % 4) + 1
#         print(f'Такт: {current_tick}')
#     start_time += 1


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


# def solve(input_string: str) -> str:
#     punctuation = "!-,.?"
#     if not input_string:
#         return 'Invalid input'
#     lower_str = input_string.lower()
#     clean_str = ''.join(i for i in lower_str if i not in punctuation)
#     unique_words = set(clean_str.split())
#     return str(len(unique_words))
#
#
# def main():
#     data_input = input()
#     result = solve(data_input)
#     print(result)
#
#
# if __name__ == '__main__':
#     main()


# import re
#
# def solve(input_string: str) -> str:
#     punctuation = r"[!-,.?]"
#     if not input_string:
#         return 'Invalid input'
#     clean_str = re.sub(punctuation, '', input_string.lower())
#     print(clean_str)
#     unique_words = set(clean_str.split())
#     return str(len(unique_words))
#
#
# data_input = input()
# print(solve(data_input))

