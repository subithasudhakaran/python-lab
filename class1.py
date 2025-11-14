"""class Car:
    def start_engine(self):
        print("Engine started")
my_car=Car()
my_car.start_engine()"""


"""class Car:
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color
    def  display(self):
        print("My car is a ",self.color,self.brand)
c1=Car("Toyota","red")
c2=Car("Honda","blue")
c1.display()
c2.display()"""

class Student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
    def grade(self):
        if self.marks>=90:
            print(self.name,self.age,"old got an A grade")
        elif self.marks>=75:
             print(self.name,self.age,"old got an B grade")
        else:
            print(self.name,self.age,"old got an B grade")
            
s1=Student("Anu",21,92)
s2=Student("Rahul",22,80)
s3=Student("Meera",24,60)
s1.grade()
s2.grade()
s3.grade()
        
