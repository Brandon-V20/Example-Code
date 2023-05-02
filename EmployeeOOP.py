# Python Object-Oriented programming
# Difference in class and an instance of a class
# Every time we use an instance of a class, it's their own unique or (DISTINCT)
#       instance of the class and their own location

# class variables should be the same for each instance
# Lets say our company gives annual raises every year, the amount can change every year So this is great for a class variable
class Employee:
    raise_amt = 1.04 # 4% raise
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@gmail.com'

        Employee.num_of_emps += 1

    def full_name(self):
        # No need to put first and last as arguments since they have been implemented in the previous function

        return '{} {}'.format(self.first, self.last)
        # Now we can label emp_x.full_name() for every x to find every full name instead of doing the code for each employee

    # Now we work with raises
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)  # putting raise_amount wont work because raise amount is not defined in the class itself
        # We must put (employee.) before the raise amount reference or (self.)

    # Decorator
    @classmethod
    def set_raise_amt(cls, amount):
        #pass
        cls.raise_amt = amount


emp_1 = Employee('Brandon', 'Villanueva', 57000)
emp_2 = Employee('Savannah', 'Janda', 62000)
# print(Employee.num_of_emps)

Employee.set_raise_amt(1.04)

emp_1.set_raise_amt(1.05)
emp_2.set_raise_amt(1.03)
# This even changes all the instances of the employees to the latest change so now all raise_amt = 1.03

# Lets say you have strings of new employees like 'Jacob-Newman-21942'
emp_str_1 = 'Jacob-Newman-21942'
emp_str_2 = 'Randall-Strikr-194281'
emp_str_3 = 'Jessie-James-305913'

 # We can create a new employee with this sample code
first, last, pay = emp_str_1.split('-')
new_emp_1 = Employee(first,last,pay)
first, last, pay = emp_str_2.split('-')
new_emp_2 = Employee(first,last,pay)
first,last,pay = emp_str_3.split('-')
new_emp_3 = Employee(first,last,pay)
# We set the arguments of new_emp_1 in the employee class since we labeled the variables first last and pay to the new employee.
# We can use the same variables over and over, yet they must be corresponding with the order of code

print(new_emp_1.email)
print(new_emp_2.email)
print(Employee.num_of_emps) 
print(new_emp_3.first)
# now we see that there are 3 employees

#     print('{} {}'.format(emp_1.first, emp_1.last))
    # this is a lot of code just to get a full name of an employee, so we created the def full_name in the class of employees

# __init__ method = initialize the class with arguments that you input above
# We can minimalize all the code below through the init method
# emp_1.first = 'Brandon'
# emp_1.email = 'brandonvillanueva@gmail.com'
# emp_1.pay = 56000
# emp_1.last = 'Villanueva'
# emp_2.first = 'Savannah'
# emp_2.pay = 62000

# we can run the class itself with just the name

# since emp_x = the class employee, then the instances and variables automatically go through the employee section variables

# emp_2.raise_amount = 1.05

# print(emp_2.raise_amount)
# print(Employee.raise_amount)
# emp_2.apply_raise()
# print(emp_2.pay)




