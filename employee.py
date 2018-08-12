
class Employee:

    # Class variables
    num_of_emps = 0
    raise_amount = 1.04

    # Initialise
    def __init__(self, first : str, last : str, salary : int):
        self.first = first
        self.last = last
        self.salary = salary
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    
    def full_name(self):
        return('{} {}'.format(self.first, self.last))


    def apply_raise(self):
        self.salary : int = (self.salary * self.raise_amount)

    
    @classmethod
    def set_raise_amount(cls, amount : float):
        cls.raise_amount : float = amount


# Creating instances    
emp1 = Employee('Tino', 'von Stegmann', 50000)
emp2 = Employee('Jonny', 'Doe', 50001)

# printing variables/methods
print("The company's {} current employees are: \n {} \n {}".format(Employee.num_of_emps, emp1.full_name(), emp2.full_name()))

# Class methods: functions associated with the class.  In this case apply_raise (must include (), just like a normal function)
print('\n Applying class method to salary: ')
print('Original Salary: {}'.format(emp1.salary))
emp1.apply_raise()
print('Raised Salary: {}'.format(emp1.salary))

# If we want to override variables for all instances (i.e. at class level): Class methods
print('\n Setting class variable (raise amount) to 1.06: ')
Employee.set_raise_amount(1.06)

print('Class methods: ')
print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)


# If we want to override at instance level only, we can also do that
print('\n Changing raise amount only for 1 instance (emp1): ')
emp1.raise_amount = 1.05

print('Class vs instance variables: ')
print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)






