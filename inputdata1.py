# -*- coding: utf-8 -*-
"""InputData1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_KPg6vxAF5p0BFJHeFS6EDjmhQgjas5w
"""

#Adelaide Call
#1/22/24
#1. Quantitive data is numerical data that can be measured and compared ex. the number of students in a class. Qualitative data is descriptive data that cannot be measured ex. the ethnicity of students in a class.
#2. Casting is the process of converting a vlaue from one data type to another. You would neet to use it when converting user input into integers that can be multiplied.
#3. Precision is the total number of significant digits and scale is the number of digits after the decimal point. For the number 3.1415 the precision is 5 and the scale is 4.

#Problem 1
print("Bob Smith", "\nbobsmith@email.com")

#Problem 2
x=100
y=15
print(x)
print(y)
print(x*y)
print(type(x*y))
print(x/y)
print (type(x/y))

x=input("Enter an integer")
print(x)
y=input("Enter another integer")
print(y)
x=int(x)
y=int(y)
print(type(x))
print(type(y))
print(x*y)
print(type(x*y))
print(x/y)
print(type(x/y))

"""1. True
2.False
3.True
"""

u="University of Utah"
print(type(u))
print(u[14]+u[8]+u[4]+u[6], end="!")

b="To be, or not to be, that is the question: Whether 'tis nobler in the mind to suffer The slings and arrows of outrageous fortune, Or to take arms against a sea of troubles And by opposing end them."
print(b)
print(len(b))
print(b[172]+b[2]+b[8]+b[4]+b[3:5]+b[90]+b[51]+b[36]+b[2]+b[21:23]+b[7:9]+b[10]+b[196])
d=(b[172]+b[2]+b[8]+b[4]+b[3:5]+b[90]+b[51]+b[36]+b[2]+b[21:23]+b[7:9]+b[10]+b[196])
print(d)