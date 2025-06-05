# x = 6
# y = "20"
# print('x' + 'y')  # 'x' и 'y' здесь просто строковые значения


# def slice(data):
#     return data[1:-1] #TypeError: 'int' object is not subscriptable
#
#
# numbers = 15963 #целое число, не  список, строка, кортеж или другой объект, поддерживающий индексацию
# sorted_numbers = int(''.join(str(numbers))) #белиберда!
# print(slice(numbers))


# num = -3
# print('ноль' if num == 0 else 'положительное' if num > 0 else 'отрицательное')


# numbers = [1, 2, 5, 7, 8, 10]  # не правильное удаление положительных
# for i in range(len(numbers)):  # чисел из списка
#     if numbers[i] % 2 == 0:    # Ошибка: IndexError: list index out of range
#         numbers.remove(numbers[i])


# numbers = [1, 2, 5, 7, 8, 10]
# new_numbers = []
# for number in numbers:
#     if number % 2 != 0:
#         new_numbers.append(number)
# numbers = new_numbers
# print(numbers)


# numbers = [1, 2, 5, 7, 8, 10]
# new_numbers = [number for number in numbers if number % 2 != 0]
# print(new_numbers)


# def calculate(items):
#     #total = 0 #переменная 'total' не объявлена внутри функции
#     for price, num in items:
#         total += price * num
#     return total
#
#
# items_list = [(100, 2), (120, 3), (140, 1)]
# calculate(items_list)


# def calculate(items):
#     total = 0
#     for price, num in items:
#         total += price * num
#     print(total)
#
#
# items_list = [(100, 2), (120, 3), (140, 1)]
# calculate(items_list)


# class MyClass:
#     def __init__(self, value):
#         self.value = value
#
# obj = MyClass(10)  # Создание объекта статическим способом
# print(obj.value)


# class Dog:
#     def __init__(self, name, breed):
#         self.name = name
#         self.breed = breed
#
#     @staticmethod
#     def bark():
#         print('Haf-haf')
#
#
# my_dog = Dog('Shradick', 'sausage dog')
# your_dog = Dog('Listick', 'badger-dog')
# print(my_dog.name, my_dog.breed)
# Dog.bark()


# class Dog:
#     def __init__(self, name, breed):
#         self.name = name
#         self.breed = breed
#
#     def bark(self):
#         print('Haf-haf')
#
#
# my_dog = Dog('Shradick', 'sausage dog')
# your_dog = Dog('Listick', 'badger-dog')
# print(my_dog.name, my_dog.breed)
# your_dog.bark()



# class Car:
#     def __init__(self, make, model, year=2023):  #'year' по умолчанию
#         self.make = make
#         self.model = model
#         self.year = year
#
#
# my_car = Car('Toyota', 'Camry')
# your_car = Car('Honda', 'Civic', 2021)
# print(my_car.make, my_car.model, my_car.year)
# print(your_car.year)


# class Person:
#     def __init__(self, name, *args, **kwargs):
#         self.name = name
#         self.additional_info = args
#         self.keyword_info = kwargs
#
#
# person1 = Person('cubinez85', 'Programmer', 60, city='Moscow', country='Russia')
# person2 = Person('Bob', occupation='Software Developer', city='London')
# print(person1.additional_info)
# print(person2.name)
# print(person2.keyword_info['city'])


# class Point:  #класс представляет собой просто контейнер для данных или логики
#     pass
#
#
# p = Point()
# p.x = 10
# p.y = 20
# print(p.x, p.y)


# class Config:
#     pass
#
#
# config = Config()
# config.api_key = 'YOUR_API_KEY'
# config.server_url = 'https://flask.cubinez.ru'
# print(config.server_url)


# class Shape:
#     pass
#
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#
#
# circle = Circle(5)
# print(circle.radius)