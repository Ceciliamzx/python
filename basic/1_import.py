

# 问答互动程序 input返回字符串如果要返回数字要加int or float;int不能和str拼接打印
user_age = int(input("请输入年龄: "))
user_age_after_10_year = user_age + 10
print("10年后你将会是: " + str(user_age_after_10_year) + "岁")

# 条件语句
user_question = input("Cecilia是不是宇宙第一美？")
if user_question == "是":
    print("你真是个聪明的孩子！")
else:
    print("你说错了，Cecilia就是宇宙第一美！")

user_age = int(input("请输入年龄: "))
print(user_age)

# 嵌套条件语句 多个取值范围时用elif
if user_age >= 18:
    print("你是成年人")
    if user_age < 6:
        print("你还是个小宝宝")
    elif 6 <= user_age < 12:
        print("你是个少年")
    elif 12 <= user_age <= 14:
        print("你是个青少年")

else:
    print("你是未成年人")

# 列表
shopping_list = ["apple" , "orange", "pear"]
shopping_list.append("banana")
shopping_list.remove("apple")
print(shopping_list)
print(shopping_list[0])
len(shopping_list)

price = [5, 3, 4]
max_price = max(price)
min_price = min(price)
sorted_price = sorted(price)
total_price = sum(sorted_price)
print(max_price, min_price, sorted_price, total_price)




