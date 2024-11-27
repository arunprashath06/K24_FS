#object oriented programming(OOPs)
#documenttation string represents description of th class.within the class doc string is always optional.
#to ways to print documenttation string
# 1)is print(classname,_doc_)
# 2)is help(classname)
#for ex:
""" class classname:
    "documenttation string"
print(classname.__doc__)
help(classname)"""
#self variable is the default variable which is always pointing to current object 
"""
class test:
    def __init__(self):
        print("dfsd dfefe")
    def m1(self):
        print("jcbduuf")

t1=test()
t2=test()
t3=test()
t1.m1()"""
#object is the physical existence of the class.
# polymorphism:same object with different behaviour
#for instance variable  method using self is important 
"""class P:
    def Hyname(self):
        print("working..")
class C(P):
# C(P) is C is the child and P is the parent,now we are inheriting the information from parent to child that is C(P)(child has no information defaultly now ,its only using parent information)
    pass
C=C()
print(C)
C.Hyname()"""
"""
#create a class called book that has a constructor to initialize the title and author of the book.add a method to display the book
details.
class Book:
    def __init__(self,author,title):
        self.title=title
        self.author=author
     def details(self):
        print(self.author)
        print(self.title)
        #didnt finish this quest
"""
"""
#define a class called circle with a constructor that accepts the radius as an arguement.implement methods to calculate the area and
circumeference of the circle

class Circle:
    def __init__(self,radius):
        self.radius=radius
        self.area=self.calc_area()
        self.circumference=self.calc_circumference()
    def calc_area(self):
        import math
        return math.pi*self.radius**2
    def calc_circumference(self):
        import math
        return math.pi*2*self.radius
    def show(self):
        print(self.radius)
        print(self.calc_area)
        print(self.calc_circumference)
circle=Circle(5)
print(circle)"""
class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
stud_1=student(name,age)
name=input(": ")
age=int(input(": ")) 

stud_2=student(name,age)
name=input(": ")
age=int(input(": "))

print("stud_1",stud_1.name)
print("stud_2",stud_2.name)


        


    
        
    


        