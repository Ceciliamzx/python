from langchain_community.chat_models.litellm_router import get_llm_output
print("hello, world")
# 出现多个双引号
print("hello, \"world\"")
# 换行
print("hello,\nworld")
# 跨行
print('''你是我小时候掰着脚丫萌生的最初梦想，
背着书包想要放飞的翅膀，
扑哧扑哧地撞击着心墙，
一页一页为你写下的诗行，
腼腆、羞涩、稚嫩，迷茫''')
# 下划线命名法（字母全部小写，单词之间用下划线分隔）  greet_chinese
# 驼峰命名法（每个单词的首字母大写，单词之间不使用下划线分隔） GreetChinese
# 变量
greet = "你好"
greet_chinese = greet
greet_english = "hello"
greet = greet_english
print(greet +":zhang")
print(greet_chinese + ":zhang")
# 数学运算
import math
math.sin(1)
result = math.sin(1)
print(result)
# 一元二次方程求解
import math
a = -1
b = -2
c = 3
delta = b**2 - 4*a*c
(-b + math.sqrt(delta)) / (2*a)
(-b - math.sqrt(delta)) / (2*a)
print((-b + math.sqrt(delta)) / (2*a))
print((-b - math.sqrt(delta)) / (2*a))




