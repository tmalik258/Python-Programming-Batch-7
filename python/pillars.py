# 4 pillars
# inheritance
# encapsulation
# polymorphism
# abstration

# Inheritance

class Person: # parent class
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def intro(self):
        print(f'My name is {self.name} and age is {self.age}')
    

class Student(Person): # child class of Person
    def __init__(self, name, age, st_id, marks):
        # Person.__init__(name, age)
        super().__init__(name, age)
        self.st_id = st_id
        self.marks = marks

    def study(self):
        print('im studying')
    
    def intro(self):
        # Person.intro(self)
        super().intro()
        print(f'and my roll no is {self.st_id} and my marks are {self.marks}')
    
    # override intro method


class Employee(Person): # child class of Person
    def work(self):
        print('im working')
        

p1 = Person('talha', 22)

p1.intro()
# p1.study()    # error

s1 = Student('Abdul Raheem', 22, 878242, 90)
s1.intro()
s1.study()

print(s1.st_id, s1.marks)

# polymorphism - overloading, overriding
