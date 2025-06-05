# a = 2
# b = 6
# print('result: ', a + b)
# result = a > b




# class Parent:
#     def method_name(self, arg1):
#         print(f'{arg1}')
#
# class Child(Parent):
#     def method_name_2(self, arg1, arg2):
#         super().method_name(arg1)
#         print(f'{arg2}')
# child_obj = Child()
# child_obj.method_name_2('Hello', 'world')


# class Parent:
#     def method_name(self, arg1):
#         print(f'{arg1}')
#
#
# class Child(Parent):
#     def method_name(self, arg1, arg2=None):
#         super().method_name(arg1)
#         if arg2 is not None:
#             print(f'{arg2}')
#
#
# child_obj = Child()
# child_obj.method_name('Hello', 'world')



# class Parent:
#     def method_name(self, arg1):
#         print(f"{arg1}")
#
# class Child(Parent):
#     def child_method(self, arg1, arg2):
#         super().method_name(arg1)
#         print(f"{arg2}")
#
# # Пример использования
# child_object = Child()
# child_object.child_method("Hello", "World")


# class Parent:
#     @staticmethod
#     def method_name(arg1):
#         print(f"{arg1}")
#
#
# class Child(Parent):
#     @staticmethod
#     def child_method(arg1, arg2):
#         Parent.method_name(arg1)
#         print(f"{arg2}")
#
#
# Child.child_method("Hello", "World")


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



# def generate_shortcut(full_name: str) -> str:
#     if not full_name:
#         return 'Error: Empty data'
#     if not (3 <= len(full_name) <= 50):
#         return 'Error: Length input string must be from 3 to 50'
#     data_names = full_name.split()
#     if len(data_names) != 2:
#         return 'Error: Input must contain exactly two names separated by a space'
#     first_name = data_names[0]
#     last_name = data_names[1]
#     first_initial = first_name[0].upper()
#     last_initial = last_name[0].upper()
#     return f'{first_initial}. {last_initial}.'
#
#
# full_name_data = input()
# result = generate_shortcut(full_name_data)
# print(result)