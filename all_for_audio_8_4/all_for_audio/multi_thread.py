import threading
import time


# 定义函数A和B
def A(event):
    while not event.is_set():
        print("执行了函数A")
        time.sleep(1)  # 模拟执行一段时间


def B(event):
    while not event.is_set():
        print("执行了函数B")
        time.sleep(1)  # 模拟执行一段时间


# 全局事件，用于控制函数执行
execution_event = threading.Event()

# 当前执行的函数
current_function = None


# 函数执行线程
def execute_function(func, event):
    global current_function
    current_function = func.__name__
    func(event)
    current_function = None


# 启动函数执行线程
def start_execution(func, event):
    global execution_thread
    execution_thread = threading.Thread(target=execute_function, args=(func, event))
    execution_thread.start()


# 停止当前执行的函数
def stop_execution():
    global execution_event, execution_thread, current_function
    if current_function == 'A':
        execution_event.set()
        execution_thread.join()
        execution_event.clear()
    elif current_function == 'B':
        execution_event.set()
        execution_thread.join()
        execution_event.clear()


# 主线程用来接收指令
while True:
    command = input("请输入指令 (a 或 b)，输入 q 退出: ")

    if command == 'a':
        stop_execution()
        start_execution(A, execution_event)
    elif command == 'b':
        stop_execution()
        start_execution(B, execution_event)
    elif command == 'q':
        print("退出程序")
        stop_execution()
        break  # 退出循环
    else:
        print("无效指令，请输入有效指令 (a 或 b)")
