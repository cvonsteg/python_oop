
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


    @classmethod
    def from_string(cls, emp_str):
        first, last, salary = emp_str.split('-')
        return cls(first, last, salary)

    
    @staticmethod
    def is_workday(day):
        if day.weekday() >= 5:
            return False
        return True







