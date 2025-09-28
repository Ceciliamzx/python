

def sum(a, b):
    return a + b
print(sum(1,2))


def test(a):
    result = 0
    for i in range(1, a+1):
        print(i)
        result += i
    return result

sum = test(10)
print(sum)

# 双线程异步打印
print("============ 多线程打印 ============")
import threading
import time
def task(name):
    for i in range(100):
        print(f'Task {name} - iteration {i}\n')

thread1 = threading.Thread(target=task, args=('A',))
thread2 = threading.Thread(target=task, args=('B',))
thread1.start()
thread2.start()
# thread1.join()
# thread2.join()
print('All tasks completed')




