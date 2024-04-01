# -*- coding: utf-8 -*-
"""Processing1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rc1xlENGzqNy6QzNZLsgm6G2RUebAc-Z
"""

#Adelaide Call
#3/8/24
#1. The difference between an if decision and an if-else decision is that if-else structures can run code based on a False result when the if statement can only run for a True result
#2. A condition is the expression that results as a True or False state. It allows us to control the outcome by starting the flow of execution.
#3. A while loop is condition controlled it repeats until the condition is met where the for loop is count controlled it repeats a specific number of times.

#Problem 1
x = input("Enter integer for X")
y = input("Enter integer for Y")
if x>y:
  print('X is larger than Y')

#Problem 2
x = input("Enter integer for X")
y = input("Enter integer for Y")
if x>y:
  print('X is larger than Y')
else:
  print("Y is Larger than X")

#Problem 3
x = input("Enter integer for X")
y = input("Enter integer for Y")
if x>y:
  print('X is larger than Y')
elif x==y:
  print("X and Y are equal")
else:
  print("Y is Larger than X")

#Problem 4
x = 1
while x < 101:
  print(x)
  x = x + 1
while x > 0:
  print(x)
  x = x - 1

#Problem 5
for x in (range(1, 101)):
  print(x)
for x in (range(100, 0, -1)):
  print(x)

#Problem 6
for x in (range(10, 101)):
  print(x)

#Problem 7
for x in (range(10, 101, 10)):
  print(x)

#Problem 8
lst = ["Bob","Smith","1234 Noplace Street","Nowhere", "UT", "84999"]
for n in lst:
    print(n)

#Problem 9
while True:
  age = input ("Enter age: ")
  try:
    age = int(age)
  except:
    print("Erorr not a numeric value.")
    continue
  if age < 1 or age > 125:
    print("Error invalid age.")
    continue
  break
print("Your age is:", age)