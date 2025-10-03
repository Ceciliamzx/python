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
