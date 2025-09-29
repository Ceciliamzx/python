# list
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

