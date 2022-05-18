# a list
fruits = ['Banana', 'orange', 'apple']
commodities = ["soap", 13, 37.90]
integers = 23
decimals = 23.90
full_name = 'Fred Bebeni'
# this is a string, enclosed by quotation marks
name = 'Fred'
# integer
age = 30
name, age = 'Fred', 30
print(name)
# upper()
# lower()
print(name.upper())
print(name.lower())

# this is an integer
num = -87
print(fruits)
print(type(fruits))
print(type(integers))
print(type(decimals))
print(type(full_name))
# if and else statement
num = 100
var = 28
# if statement, gives alternatives
if num:
    print("This is a true expression value")
    print(num)
# else gives an optional
else:
    print(var)
    print("That was awesome")
# elif statement, to check if true
num = 200
if num == 300:
    print("This is False")
    print(num)
elif num == 150:
    print("This is False")
    print(num)
elif num == 1000:
    print("This is False")
    print(num)
elif num == 200:
    print("This is True")
    print(num)
else:
    print(num)

# the for loop, to iterate statements
fruits = ["mango", "oranges", "grapes"]
for fruit in fruits:
    print(fruit)

for letter in 'fruits':
    print(letter)
# % modulator divisibility
# * multiplication
# + concatenate
# using else statement with a FOR loop
num = []
for num in range(10, 20):
    for i in range(2, num):
        if num % i == 0:
            x = num / i
            print(num, i, x)
            break
        else:
            print(num)
            break

# indexing and slicing([])
# slicing an item from its position
fruits = ["orange", "apple", "grapes", "banana"]
print(fruits[0])
print(fruits[1])
print(fruits[-1])
print(fruits[-2])

# indexing, used to identify item position value
print(fruits.index('orange'))
print(fruits.index('grapes'))

# tuples()
# tuples are just like lists but immutable, once written cannot be changed
fruits = ("oranges", "grapes", "apples")
print(fruits)
# type 2 tuple
list = ("chair", "table", "shelf", "23", "1990")
print(list)
# type 3 tuple
items = "bank", "school", "bus"
print(items)

# accessing values in a tuple
list = ("chair", "table", "shelf", "23", "1990")
print(list[3])
print(list[2])

# Not update, not changing tuples but assigning new tuples
list = ("chair", "table", "shelf", "23", "1990")
items = "bank", "school", "bus"
items_total = items + list
print(items_total)

fruits = ("oranges", "grapes", "apples")  # this is a tuple
fruits = ["oranges", "grapes", "apples"]  # this is a list
fruits[0] = "mangoes"
print(fruits)

# deleting a tuple
# commodities = ("chair", "table", "shelf", "23", "1990")
# print(commodities)
# del commodities
# print(commodities)

# python dictionaries
# use curly braces{}
person = {"name": "Fred", "age": 25, "shop": "pen"}

# accessing values in dictionaries
print(person)
print(person["age"])
print("The age of Fred is:", person["age"])

# updating a dictionary
person = {"name": "Fred", "age": 25, "shop": "pen"}
person['age'] = 30
person['shop'] = 'soap'
print(person)

# deleting a dictionary element
person = {"name": "Fred", "age": 25, "shop": "pen"}
# remove a single element first
del person['shop']
print(person)
# del person
# print(person)

# Adding items in a dictionary
# person = {"name": "Fred", "age": 25, "shop": "pen"}
# person['household'] = 'chair'
# print(person)
# print(type(person))
# For loop in a dictionary
# for key, value in person.items():
#    print("{} is {}". format(key,value))

# write a file in python
# f = open('Sessionfred2.text', "w")
# f.write('Hello Class \n')
# f.writelines('This is a python class')

# read data in a txt file
# f = open('Sessionfred2.txt', 'r')
# print(f.readlines())
# f.seek(0)
# print(f.read(10))

# append texts in the file
# f = open('sessionfred2.txt', 'a')
# f.write('This is added text \n')
# f.close()

# while loop statement
# count = 0
# while count < 20:
#    print(count)
#    count +=1
# num = 0
# while num < 10:
#   print(num) # infinite loop, happens when the condition id false
#   num+=1
# using else statement with the while loop
count = 0


# while count < 20:
#    print(count, 'is less than 20')
#   count+=1
# else:
#    print(count, 'It is not less than 20')

# run time complexity
# array
# name = "fred"
# print(name.capitalize())
# print(len(name))

# name = 'schooling'
# print(len(name))

# append, add item at the end of the list
# commodities = ["chair", "table", "shelf", "23", "1990"]
# commodities.append('apples')
# print(commodities)
# boolean, for checking true or false
# print(10>9)
# print(10==9)
# a = "class"
# print(bool(a))

# a = 100
# b = 22
# if b > a:
#    print('b is greater than a')
# else:
#    print('b is not greater than a')

# creating a function
# def function(apple):
#    print(apple)
#    return;
# function('This is a first function')

# defining a function
# def items(list):
#    list = [1, 2, 3, 4, 5]
#    print('Values are inside the function', list)
#    return;
# list =[54, 67, 86]
# items(list)# function call
# print('Values outside the list', list)
# dafault argument
# def function(name):
#    print(name)
#    return;
# function('Fred')


# Args and kwargs used for multiple arguments
# def function(*args, **kwargs):
#    a = 1
#    b = hello
#    print("Hello")


# python classes
# fruits = ['orange', 'mango', 'apple']
# integers = 1, 2, 2, 4
# def function(hello):
#    print('hello')
#   print(type(function))

# classes
# class ClassName():
#    a = 10

# a1 = ClassName()
# print(a1.a)
# print(a1)

class Cat:
    def meow(self):
        print('meow')


# c = Cat
# print(c)


# __init__() Function# assign class values to object
# class Population:
#   def __init__(self, names, age):
#        self.names = names
#       self.age = age

# person1 = Population('John', 28)
# person2 = Population('Fred', 20)
# print(person1.names)
# print(person1.age)

# class Person:
#    def __init__(self,name, age):
#        self.name = name
#        self.age = age

#   def get_name(self):
#        print('This is a code:' + self.name)

#       def get_age(self):
#            return self.age
# p1 = Person('Mary', 27)
# print(p1.get_name())
# p1.get_age


# parent class
#class School:
#    def __init__(self, name, age, grade):
#       self.name = name
#        self.age = age
#        self.grade = grade

 #   def get_grade(self):
 #       return self.grade


# child class
#class Course:
#    def __init__(self, name, max_students):
#        self.name = name
 #       self.max_students = max_students
 #       self.students = []
#
  #  def sum_student(self, student):
  #3      if len(self.students) < self.max_students:
 #           self.students.append(student)
 #           return True
 #       return False

 #   def get_average(self):
 #       value = 0
 #       for student in self.students:
#            value += student.get_grade()
 #       return value / len(self.students)


#st1 = School('Ann', 20, 80)
#st2 = School('Kelvin', 30, 70)
#st3 = School('Mark', 29, 40)

#course = Course('Maths', 3)
#course.sum_student(st1)
#course.sum_student(st2)
#print(course.students[1].name)
#args and kwargs nonkeyword and keyword
#def function(self): (* args, **kwargs)
#    print('Hello')
result = 0 # this is a global variable
#def add(a, b):
 #   result = a + b # this is a local variable
  #  print(result)
   # return result
#add (10, 20)
#print(result)


#assert statements
# they state or assert facts/ commands in a program
#to check whether statement is true or false
#debugs the program as soon as an error occurs and displays it

#def get_average(scores):
#    assert len(scores) !=0 "List is empty"
#    return sum(scores) / len(scores)
#score1 = []
#print("Average of score:", get_average(score1))

#score2 = [24, 34, 10, 122]
#print("Average of score:", get_average(score2))