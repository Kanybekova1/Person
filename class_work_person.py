class Person:
    #constructor
    def __init__(self,name,surname,age=None,gender=None):
        self.name=name
        self.surname=surname
        self.age=age
        self.gender=gender
#methods
    def walk(self):
        print("Person",self.name, "is walking")

    def info(self):
        print("Person name:", self.name,"\n" "Surname:", self.surname,"\n" "Age:", self.age,"\n" "Gender:", self.gender)
