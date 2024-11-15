# class Student():
#     def __init__(self, name, age, subject, grade):
#         self.name = name
#         self.age = age
#         self.subject = subject
#         self.grade = grade

#     def show_details(self):
#         print(f"Student Details: {self.name}, {self.age}, {self.subject}, {self.grade}")
    
#     def set_grade(self, new_grade):
#         self.grade = new_grade


# colin = Student("Colin", 21, "Software", 93)
# tahfia = Student("Tahfia", 21, "Data", 93)

# colin.show_details()
# colin.set_grade(100)

# print(colin.name)
# print(colin.age)
# print(colin.subject)
# print(colin.grade)

class Employee():
    def __init__(self, name, age, role, employee_id, salary):
        self.name = name
        self.age = age
        self.role = role
        self.employee_id = employee_id
        self.salary = salary
    
    def show_details(self):
        print(f"Employee details: {self.name}, {self.age}, {self.role}, {self.employee_id}, {self.salary}")

colin = Employee("Colin", 21, "Software Engineer", "EMPID203", 100000)

colin.show_details()

print(colin.name)
print(colin.age)
print(colin.role)
print(colin.employee_id)
print(colin.salary)

