# from kite tutorial
# https://www.youtube.com/watch?v=Zee665ssm8Y&t=12s

class Employee:

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name  # class variables
        self.last_name = last_name
        self.salary = salary
        self.email = self.first_name + '.' + self.last_name + '@company.com'

    def give_raise(self, new_salary):
        self.salary = new_salary


class developer(Employee):

    def __init__(self, first_name, last_name, salary, programming_languages):
        super().__init__(first_name, last_name, salary)
        self.programming_language = programming_languages

    def add_language(self, lang):
        self.programming_language.append(lang)


employee_a = Employee('george', 'will', 40000)

print(employee_a.salary)

employee_a.give_raise(100000
                      )
print(employee_a.salary)

dev_a = developer('steve', 'strange', 140000, ['python'])
print(dev_a.salary)

dev_a.give_raise(165000)
print(dev_a.salary)

print(dev_a.programming_language)

dev_a.add_language('javascript')

print(dev_a.programming_language)
