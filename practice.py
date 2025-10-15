# 1.打印9个*一共9行，第一行1个*，第二行2个*，依次类推
print("打印9个*一共9行，第一行1个*，第二行2个*，依次类推")
for i in range (1,10):
    print("*" * i)
# 2.打印9个*一共9行，第5行开始递减
print ("打印9个*一共9行，第5行开始递减")
for i in range (1,10):
    if i < 5:
        print("*" * i)
    else:
        print("*" * (10 - i))
# 3.打印99乘法表
print("打印99乘法表")
for i in range (1,10):
    for j in range (1,i+1):
        print(f"{j}*{i}={i*j}", end= '\t') # end= '\t'表示不换行，使用制表符分隔
    print()
# 4.将一个列表排序
print("将一个列表排序")
lst = [100, 1, 7, 3, 9]
lst.sort()
print(lst)
# 5.合并两个列表并排序
print("合并两个列表并排序")
lst1 = [100, 1, 7, 3, 9]
lst2 = [200, 50, 300, 20, 400]
lst3 = lst1 + lst2
lst3.sort()
print(lst3)

# 6.control()
class HomeAppliance:
    def control(self):
        pass
class Tv(HomeAppliance):
    def control(self):
        print("切换视频至中央一台")
class AirConditioner(HomeAppliance):
    def control(self):
        print("空调温度调至26度")
class Light(HomeAppliance):
    def control(self):
        print("切换为暖光模式")

def operate_appliance(appliance: HomeAppliance):
    appliance.control()

tv = Tv()
ac = AirConditioner()
light = Light()
operate_appliance(tv)
operate_appliance(ac)
operate_appliance(light)

# 7.yieling()
class Animal:
    def yieling(self):
        pass
class Dog(Animal):
    def yieling(self):
        print("wow")
class Cat(Animal):
    def yieling(self):
        print("meow")
def make_animal_sound (animal:Animal):
    animal.yieling()

dog1 = Dog()
cat1 = Cat()
make_animal_sound(dog1)
make_animal_sound(cat1)

 # 8.两数之和
number1 = 1
number2 = 2
sum = number1 + number2
print(sum)
print(f"{number1}+{number2}={sum}")

# 9.数字的阶乘
def get_jiecheng(number):
    result = 1
    while number > 0:
        result *= number
        number -=1
    return result
print("jiecheng 6=",get_jiecheng(6))

# 10.计算圆的面积
import math
print(math.pi)

import math
def compute_area_of_circle(r):
    return round(math.pi * r * r,2)
print("area of 2 is:",compute_area_of_circle(2))

# 11.区间内的所有素数
def is_primes(number):
    if number in (1,2):
        return True
    for idx in range (2,number):
        if number % idx == 0 :
            return False
        return True

def print_primes(begin, end):
    for number in range(begin,end+1):
        if is_primes(number):
            print(f"{number}is a primes")

begin = 11
end = 25
print_primes(begin,end)

# 12.求前n个数字的平方和
def sum_of_square(n):
    result = 0
    for number in range (1,n+1):
        result += number * number
    return result
print(sum_of_square(5))

# 13.计算列表所有数字的和
def sum (param_list):
    total = 0
    for item in param_list:
        total += item
    return total
list1 = [1,2,3,4]
print(f"sum of {list1},",sum(list1))
print(sum(list1))

# 14.数字范围中所有的偶数(列表代表式）
data =[item for item in range(begin,end) if item % 2 == 0]
begin = 4
end = 15
print(f"begin={begin},end={end},even numbers :",data)

# 15.移除列表中的多个元素
list1 = [3,5,7,9,11,13]
list2 = [7,11]
data = [item for item in list1 if item not in list2]
print(f"from{list1} remove{list2},result:",data)

# 16.怎样对列表元素去重(set集合不会包含重复元素）
list1 = [10,20,30,10,20]
print(f"source list{list1},unique list:",list(set(list1)))

# 17.怎么对简单列表元素进行排序
list1 = [20,40,30,50]
# list1.sort()原地排序
list2 = sorted(list1)
print(list1)
print(list2)

list1 = [20,40,30,50]
list1.sort(reverse=True)
print(list1)



