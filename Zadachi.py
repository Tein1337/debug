# 1
# class Point3D():
#
#     def __init__(self, x = 0, y = 0, z = 0):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def info(self):
#         print(f'x = {self.x}, y = {self.y}, z = {self.z}')
#
#     def distance(self, a, b):
#         return b - a
#
#     def distance2(self):
#         return f'Расстояние от x до y: {self.distance(self.x, self.y)}.\nРасстояние между y и z: {self.distance(self.y, self.z)}.'
#
# first = Point3D(2, 5, 8)
# second = Point3D(5, 8, 7)
# third = Point3D(8, 7, 3)
# first.info()
# print(first.distance2())

# 2
'''class Square():

    def __init__(self, a = 0):
        self.a = a

    def s(self, a):
        return a ** 2

    def p(self, a):
        return 4 * a

    def s_and_p(self):
        return f'Сторона квадрата: {self.a}.\nПлощадь: {self.s(self.a)}.\nПериметр: {self.p(self.a)}'
side1 = Square(4)
side2 = Square(8)
side3 = Square(12)
print(side1.s_and_p())'''

# 3
# class Triangle():
#
#     def __init__(self, a = 0, b = 0, c = 0):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def s(self, a, b):
#         return 2 * a + b
#
#     def p(self, a, b, c):
#         return a + b + c
#
#     def s_and_p(self):
#         return f'Стороны треугольника: {self.a}, {self.b}, {self.c}.\nПлощадь: {self.s(self.a, self.b)}.\nПериметр: {self.p(self.a, self.b, self.c)}.'
#
# side1 = Triangle(3, 5)
# side2 = Triangle(4, 5, 6)
# side3 = Triangle(7, 8, 9)
# print(side1.s_and_p())

# 4
class distanceTriangle():

    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3


    def distance(self, a, b):
            return b - a

    def distance2(self):
            return f'Расстояние от x до y: {self.distance(self.x, self.y)}.\nРасстояние между y и z: {self.distance(self.y, self.z)}.'

    def p(self, a, b, c):
        return a + b + c


x = float(input())
y = float(input())
z = float(input())
user_nums = distanceTriangle(x, y, z)
print(user_nums.distance2())
print(user_nums.p(x, y, z))

# 5
# class CPerson():
#
#     def __init__(self, name, lastname, surname, birthday, gender):
#         self.name = name
#         self.lastname = lastname
#         self.surname = surname
#         self.birthday = birthday
#         self.gender = gender
#
#     def user_info_rename(self, new_name, new_lastname, new_surname, new_birthday, new_gender):
#         self.name = new_name
#         self.lastname = new_lastname
#         self.surname = new_surname
#         self.birthday = new_birthday
#         self.gender = new_gender
#
#     def user_info(self):
#         print(f'Ф.И.О: {self.lastname} {self.name} {self.surname}.\nДата рождения: {self.birthday}.\nПол: {self.gender}')
#
#     def __del__(self):
#         print('Данные стерты')
#
# people = CPerson('Matthew', 'Young', 'Vladimirovich ', '16.02.2000', 'male')
# new_name = input('Введите новое имя:')
# new_lastname = input('Введите новую фамилию:')
# new_surname = input('Введите новое отчество:')
# new_birthday = input('Введите новую дату рождения в формате "день.месяц.год":')
# new_gender = input('Введите новый пол:')
# people.user_info_rename(new_name, new_lastname, new_surname, new_birthday, new_gender)
# people.user_info()

# 6
# class Phone():
#
#     def __init__(self, number, model, weight, name):
#         self.number = number
#         self.model = model
#         self.weight = weight
#         self.name = name
#
#     def info(self):
#         print(self.number)
#         print(self.model)
#         print(self.weight)
#
#     def receiveCall(self):
#         print(f'Звонит {self.name}')
#
#     def getNumber(self):
#         return self.number
#
# user_phone = Phone('+777', 'ApplePhone', '1.5kg', 'Oleg')
# user_phone.info()
# user_phone.receiveCall()
# print(user_phone.getNumber())

# 7
# class Reader():
#     def __init__(self, name = None, lastname = None, surname = None, num_token = None, faculty = None, birthday = None, user_phone = None, count_books = None):
#         self.name = name
#         self.lastname = lastname
#         self.surname = surname
#         self.num_token = num_token
#         self.faculty = faculty
#         self.birthday = birthday
#         self.user_phone = user_phone
#         self.count_books = count_books
#
#     def takeBook(self):
#         return f'{self.lastname} {self.name} {self.surname} взял {self.count_books} книг'
#
#     def returnBook(self):
#         return f'{self.lastname} {self.name} {self.surname} вернул {self.count_books} книги'
#
#
#
# user_info = Reader('Matthew', 'Young', 'Petrovich', '3', 'history', '16.02.2000', '+79178716665', '3')
# print(user_info.takeBook())
# print(user_info.returnBook())
