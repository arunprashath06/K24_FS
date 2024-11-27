"""
f=open("abc.txt","r")
print(f.read(3))
print(f.readline())
print(f.read(4))
print("Remaining Data")
print(f.read())
"""
'''with open("abc.txt","w") as f:
    f.write("Durga\n")
    f.write("Software\n")
    f.write("Solutions\n")
    print("is file closed:",f.closed)
print("is file closed:",f.closed)
'''

'''
f=open("abc.txt","r")
print(f.tell())
print(f.read(2))
print(f.tell())
print(f.read(3))
print(f.tell())
'''

'''
data="All students are idiots"
f=open("abc.txt","w")
f.write(data)
with open("abc.txt","r+") as f:
    text=f.read()
    print(text)
    print("the current cursor position: ",f.tell())
    f.seek(17)
    print("the current cursor position: ",f.tell())
    f.write("GEMS!!!")
    f.seek(0)
    text=f.read()
    print("Data after Modification:")
    print(text)
'''

'''
def CheckNegative(num):
    if (num < 0):
        print("negative")
    else:
        print("positive")
num=int(input())

import CheckNegative
n = int(input("x: "))
checkNegative.checkNegativeNumber(n)
'''
'''
def arithoperations(num1,num2):
    print('addition:',num1 + num2)
    print('substraction:',num1 - num2)
    print('multiplication:',num1 * num2)
    print('division:', num1 / num2)

import Module_Imp1 as mi1
import Module_Imp2 as mi2
a = int(input("num1: "))
b = int(input("num2: "))
mi1.checkNegativeNumber(a)
mi1.checkNegativeNumber(b)
mi2.arithoperations(a,b)
'''

def calculatediameter(r):
    print("diameter:", 2 *r)
def calculatearea(s):
    print("area:",s*s)

from Module_Imp3 import calculatearea, calculate


from Module_Imp3 import calculatearea as area
from Module_Imp3 import calculatevolume as vol
len = int(input("length: "))
breadth= int(input("breadth: "))
area(len,breadth)
side = int(input("side: "))
vol(side)




