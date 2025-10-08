# list
from fileinput import close

from sqlalchemy.util.preloaded import import_prefix

print("========== list ==========")
a = [1, 2, 3]
print(a[:-1])

a[0] = 100
print(a)

a.append(4)
print(a)

a.insert(0, 200)
print(a)

# dict
print("========== json dict 对象object 结构体 ==========")
allen = {"name":"allen", 'age':18, 'height': 1.75, "icon": "https://www.baidu.com/img/flexible/logo/pc/result.png"}
print(allen['name'])
print(allen.get('age'))

student_newcastle = [
    allen,
    {"name": "bob", 'age':20, 'height': 1.85},
    {"name": 'cindy', "age":19, 'height': 1.65, 'color': "red"}
]

# 对象object vs 实例
# 电视=对象，海信电视=实例

# stack
print("========== stack ==========")
stack = [1, 2, 3]
print(stack)
print(stack.pop())
print(stack)
print(stack.pop())
print(stack.pop())
print(stack)

# queue: 异步(提高响应速度)，削峰()，解耦
print("========== queue ==========")
from collections import deque
queue = deque([1, 2, 3])
print(queue)
queue.insert(0, 4)
print(queue)
queue.pop()
print(queue)
queue.pop()
print(queue)

# 对字符串求长度
print("========== string ==========")
s = "hello, world"
print(len(s))
print(s[0])
print(s[11])
print(s[len(s) -1])
print(s[5:7])
print(s[-7:])
print(s[:5])
print(s[:])

# 布尔值
b1 = True
b2 = False
# 空值类型
n = None
#小数
f = 3.14
# type函数
print(type(s))
print(type(True))
print(type(b2))
print(type(n))
print(type(f))
print(type(n))
# for 循环 range(start, end, step)
print("========== for ==========")
for i in range(1,10,2):
    print(i)
total = 0
for i in range(1, 101):
    total = total + i
print(total)
# while 循环
print("========== while ==========")
count = 0
while count < 5:
    print(count)
    count = count + 1
# format
print("========== format ==========")
name = "allen"
age = 18
message_content = "hello, my name is {0}, i am {1} years old".format(name, age)
print(message_content)
message_content = f"hello, my name is {name}, i am {age} years old"
print(message_content)
gpa_dict = {"allen": 3.8, "bob": 3.5, "cindy": 3.9}
for student, gpa in gpa_dict.items():
    print(f"{student} has a GPA of {gpa:.2f}")
# def
print("========== def ==========")
def colculate_BMI(height, weight):
    bmi = weight / (height * height)
    if bmi < 18.5:
        category = "underweight"
    elif 18.5 <= bmi < 24:
        category = "normal weight"
    elif 24 <= bmi < 28:
        category = "overweight"
    else:
        category = "obesity"
    print(f"您的bmi值为: {bmi:.2f}", f"您当前的体重状态为: {category}")
    return bmi
colculate_BMI(1.75, 70)


# format
print("========== format ==========")
name = "allen"
age = 18
message_content = "hello, my name is {0}, i am {1} years old".format(name, age)
print(message_content)
message_content = f"hello, my name is {name}, i am {age} years old"
print(message_content)
gpa_dict = {"allen": 3.8, "bob": 3.5, "cindy": 3.9}
for student, gpa in gpa_dict.items():
    print(f"{student} has a GPA of {gpa:.2f}")
# def
print("========== def ==========")
def colculate_BMI(height, weight):
    bmi = weight / (height * height)
    if bmi < 18.5:
        category = "underweight"
    elif 18.5 <= bmi < 24:
        category = "normal weight"
    elif 24 <= bmi < 28:
        category = "overweight"
    else:
        category = "obesity"
    print(f"您的bmi值为: {bmi:.2f}", f"您当前的体重状态为: {category}")
    return bmi
colculate_BMI(1.75, 70)

# 引入模块
print("========== import ==========")
import statistics
print(statistics.median([1, 2, 3]))
from statistics import median
print(median([1, 2, 3]))

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


ft_emp = FullTimeEmployee("小张", "E12345", 8000)
pt_emp = PartTimeEmployee("小李", "E54321", 300, 20)
print(f'Full-time Employee: {ft_emp.name}, Monthly Salary: {ft_emp.calculate_monthly_salary()}')
print(f'Part-time Employee: {pt_emp.name}, Monthly Salary: {pt_emp.calculate_monthly_salary()}')
print(ft_emp.calculate_monthly_salary())

# 读取文件
print("========== file ==========")
f = open(".\data.txt", "r", encoding="utf-8")
content = f.read()
print(content)
f.close()
with open(".\data.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)
with open(".\data.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        print(line)