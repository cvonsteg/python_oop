
class Employee:

    # Class variables
    num_of_emps : int = 0
    raise_amount : float = 1.04

    # Initialise
    def __init__(self, first : str, last : str, salary : int):
        self.first = first
        self.last = last
        self.salary = salary
        
        Employee.num_of_emps += 1

    # Anything that derives from the fundamental attributes of the class
    # should have a @property decorator.  This makes it into a method which
    # is updated if the init attributes are changed.  
    @property
    def email(self):
        return '{}.{}@company.com'.format(self.first, self.last)

    @property
    def full_name(self):
        return('{} {}'.format(self.first, self.last))

    # Setters allow you to set the __init__ attribute it's inheritors
    @full_name.setter
    def full_name(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @full_name.deleter
    def full_name(self):
        print('{} is gone.'.format(self.full_name))
        self.first = None
        self.last = None

    def apply_raise(self):
        self.salary = (self.salary * self.raise_amount)


    def __repr__(self):
        return f'Employee("{self.first}", "{self.last}", "{self.salary}")'

    def __str__(self):
        return f'{self.full_name}-{self.email}'

    @classmethod
    def set_raise_amount(cls, amount : float):
        cls.raise_amount = amount


    @classmethod
    def from_string(cls, emp_str : str):
        first, last, salary = emp_str.split('-')
        return cls(first, last, salary)

    
    @staticmethod
    def is_workday(day):
        if day.weekday() >= 5:
            return False
        return True


class Developer(Employee):
    """
    By passing parent class as argument to new class, it inherits
    all parent class attributes.  However if we want to add extra 
    arguments, we re-initialise the class.
    """
    num_of_devs = 0

    def __init__(self, first : str, last : str, salary : int, language : str):
        # super().__init__() passes the arguments which are initialised in the 
        # parent class to the sub class, so you only have to explicitly define
        # additional attributes.
        super().__init__(first, last, salary)
        self.language = language
        
        Developer.num_of_devs += 1

class Manager(Employee):
    
    def __init__(self, first, last, salary, employees=None):
        super().__init__(first, last, salary)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('---', emp.full_name)






