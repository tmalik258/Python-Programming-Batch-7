class Circle:
    PI = 3.1416
    
    def __init__(self, r): # constructor
        # initialization
        self.radius = r
    
    def area(self):
        result = self.PI * self.radius

        print('area is calculated: ', result)
    
    def __add__(self, obj):
        result = self.radius + obj.radius
        print('this is the sum of plus operator', result)

    


c1 = Circle(5)

c1.area()

c2 = Circle(8)
c2.area()

# print(c1 + c2) # operand
# c1.__add__(c2)

# c1.__add__(c2)


# Constructor - magic methods


# student class
# properties: name, age, st_id, marks, class/subject
# methods: study(), attend_school(), intro()