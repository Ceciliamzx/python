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



