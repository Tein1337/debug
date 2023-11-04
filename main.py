class Person:
    age = 5
    kind = 'men'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self, message):
        print(message)

    def say_hello(self):
        self.say(f'Hello, My name is {self.name}. \nI\'m {self.age} years old.')

    def __del__(self):
        print('Объект уничтожен', self.name)

tom = Person("Tom", 15)
bob = Person('Bob', 25)
# # print(tom.age, tom.kind)
# # print(bob.kind)
# # bob.say_hello()
# # bob.say("pqpqpqpqpqpqpq")
# # tom.say('DDDDDD')
# print(bob.name)
# print(tom.name)
# tom.say_hello()
# bob.say_hello()
# bob.age = 26
# bob.say_hello()
# tom.height = 1.80
# bob.weight = 50
# print(tom.height)
# print(bob.weight)
del bob
jim = Person('Jim', 18)
print(tom.name)
print(jim.name)
