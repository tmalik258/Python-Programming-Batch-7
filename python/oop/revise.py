# exit(1)
name = 'xyz'

class Employee:
    def __init__(self, n, e): # magic methods are used to override built-in methods
        self.name = n
        self.email = e

    def work(self):
        self.name
        print('im working')
    
    def display_name(self):
        print(f'Name is {name}')
    
    def display_email(self):
        print(f'Email is {self.email}')

# object or instance
talha = Employee('talha', 'talha@xample.com')

talha.work()
talha.display_name()
talha.display_email()


# umer = Employee('umer', 'umer@xample.com')

# umer.display_name()
# umer.display_email()