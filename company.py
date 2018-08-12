from employee import Employee

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

# Using a classmethod as an alternative constructor 

print("\n Creating employee instance using classmethod: ")
emp3_str = 'Steve-Smith-120000'
print("String being passed: {}".format(emp3_str))
emp3 = Employee.from_string(emp3_str)
print(f'New employee full name: {emp3.full_name()}')

# Looking at static methods
print("\n Using static method to check weekday: ")
import datetime
today = datetime.datetime.now()
print(f'Today\'s date: {today}')
print(f'Is today a weekday?  Computer says: {Employee.is_workday(today)}')