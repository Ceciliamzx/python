# class
print("========== class ==========")
class CuteCat:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

cat1 = CuteCat("mimi", 18, "red")
print(f'cat1 name is {cat1.name}, age is {cat1.age}, color is {cat1.color}')

class Student:
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID
        self.grades  = {"语文": 0, "数学": 0, "英语":0}

    def set_grades(self, subject, grade):
        if subject in self.grades:
            self.grades[subject] = grade
        else:
            print(f"科目{subject}不存在")

    def print(self):
        print(f'chen name is {self.name}, ID is {self.ID}, grades is {self.grades}')

chen = Student("小陈", "S12345")
chen.set_grades("语文", 85)
print(f'chen name is {chen.name}, ID is {chen.ID}, grades is {chen.grades}')

class Tv:
    def __init__(self, brand,size,color):
        self.brand = brand
        self.size = size
        self.color = color

    def set_name(self, name):
        self.name = name

    def print(self):
        print(f'Tv brand is {self.brand}, size is {self.size}, color is {self.color}, name is {self.name}')
tv1 = Tv("海信", 55, "black")
tv1.set_name("客厅电视")
tv1.print()

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def print(self, info):
        print(f'Employee name is {self.name}, id is {self.id} ')

class FullTimeEmployee(Employee):
    def __init__(self, name, id, monthly_salary):
        super().__init__(name,id)
        self.monthly_salary = monthly_salary

    def calculate_monthly_salary(self):
        return self.monthly_salary

class PartTimeEmployee(Employee):
    def __init__(self, name, id, daily_salary, work_days):
        super().__init__(name,id)
        self.daily_salary = daily_salary
        self.work_days = work_days
    def calculate_monthly_salary(self):
        return self.daily_salary * self.work_days

class people:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Name: {self.name}, Age: {self.age}")


class student(people):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def introduce(self):
        super().introduce()
        print(f"Student ID: {self.student_id}")


class teacher(people):
    def __init__(self, name, age, subject, icon="https://www.baidu.com/img/flexible/logo/pc/result.png"):
        super().__init__(name, age)
        self.subject = subject
        self.icon = icon

    def introduce(self):
        super().introduce()
        print(f"Subject: {self.subject}")
        print(f"icon: {self.icon}")



if __name__ == "__main__":
    p = people("Alice", 30)
    s = student("Bob", 20, "S12345")
    t = teacher("Charlie", 40, "Math")

    s.student_id = ""
    s.introduce()

    lst = [ p, s, t ]
    for person in lst:
        person.introduce()
        print("-----")