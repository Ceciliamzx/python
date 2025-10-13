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




