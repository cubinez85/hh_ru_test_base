# def test(value):
#     result = int(2 * value)# при вводе '1.0' - это строка
#     return result # возвращает строку "1.01.0"
#
#
# data = input()
# print(test(data))


# def test(value):
#     result = int(2 * float(value)) # переводим строку в число
#     return result
#
#
# data = input()
# print(test(data))


# result = 2 * [2] + [2]
# print(result)


# def f():
#     pass
#
#
# def g():
#     count = 0
#     call_count = 0  # добавляем счетчик вызовов f()
#     for i in range(10):
#         count += i
#         for j in range(i):
#             f()  # вызываем и считаем количество вызовов f()
#             call_count += 1
#     return call_count
#
#
# print(g())


# def inverse_list(my_list):
#     ans = []
#     for i in range(len(my_list) - 1, -1, -1):  # 0 не корр => elem 10 pass
#         ans.append(my_list[i])
#     return ans
#
#
# data = [10, 9, 8]
# print(inverse_list(data))
# print(data)


# class MyClass:
#     static_var = 0
#
# instance1 = MyClass()
# instance2 = MyClass()
#
# print(MyClass.static_var)  # Output: 0
# print(instance1.static_var) # Output: 0
# print(instance2.static_var) # Output: 0
#
# MyClass.static_var = 10  # Изменяем через класс
#
# print(MyClass.static_var)  # Output: 10
# print(instance1.static_var) # Output: 10
# print(instance2.static_var) # Output: 10
#
# instance1.static_var = 20  # Изменяем через экземпляр (создает теневую переменную)
#
# print(MyClass.static_var)  # Output: 10 (не изменилось)
# print(instance1.static_var) # Output: 20 (теневая переменная)
# print(instance2.static_var) # Output: 10 (не изменилось)


# numbers = [1, 2, 3, 4, 5]
# squares = [x**2 for x in numbers]  # генератор списка
# print(squares)  # Output: [1, 4, 9, 16, 25]

# words = ["apple", "banana", "cherry"]
# uppercase_words = [word.upper() for word in words]
# print(uppercase_words)  # Output: ['APPLE', 'BANANA', 'CHERRY']


# my_dict = {"a": 1, "b": 2, "c": 3}
# keys_list = [key for key in my_dict]
# print(keys_list)  # Output: ['a', 'b', 'c']

# my_dict = {"a": 1, "b": 2, "c": 3}
# items_list = [(key, value) for key, value in my_dict.items()]
# print(items_list)  # Output: [('a', 1), ('b', 2), ('c', 3)]