from employee import Employee

emp1 = Employee('Tino', 'von Stegmann', 50000)
emp2 = Employee('Jonny', 'Doe', 50001)

print("The company's {} current employees are: \n {} \n {}".format(Employee.num_of_emps, emp1.full_name(), emp2.full_name()))

print('Original Salary: {}'.format(emp1.salary))
emp1.apply_raise()
print('Raised Salary: {}'.format(emp1.salary))