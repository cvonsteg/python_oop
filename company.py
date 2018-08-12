from employee import Employee, Developer, Manager

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

# Create developer
dev1 = Developer('Childish', 'Gambino', '1000000', 'fortran')
print("\n New dev has joined the dev team: ")
print(f'Name: {dev1.full_name()}')
print(f'Email: {dev1.email}')
print(f'Salary: {dev1.salary}')
print(f'Language: {dev1.language}')
print(f'Employee Count: {Developer.num_of_emps}')
print(f'Number of Devs: {Developer.num_of_devs}')

dev2 = Developer('Paul', 'Kalkbrenner', '150000', 'C++')
print("\n New dev has joined the dev team: ")
print(f'Name: {dev2.full_name()}')
print(f'Email: {dev2.email}')
print(f'Salary: {dev2.salary}')
print(f'Language: {dev2.language}')
print(f'Employee Count: {Developer.num_of_emps}')
print(f'Number of Devs: {Developer.num_of_devs}')

# Create Manager
man1 = Manager('Jurgen', 'Klopp', '1000001', [dev1])
print('\nNew Senior Manager: {}'.format(man1.full_name()))
print(f'{man1.first} manages: ')
man1.print_emps()
print(f'{man1.first} now also manages {dev2.full_name()}')
man1.add_employee(dev2)
print(f'{man1.first} now manages: ')
man1.print_emps()
print(f'{dev1.full_name()} is being moved to a different manager.')
man1.remove_employee(dev1)
print(f'{man1.first}\'s new team is: ')
man1.print_emps()