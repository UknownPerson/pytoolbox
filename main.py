from threading import *
from tkinter import *
from time import *

# 初始赋值
Time_Start = time()

window_width = "300"  # 窗口_宽
window_height = "500"  # 窗口_高

# 初始计算
window_geometry = window_width + "x" + window_height  # 窗口_形状


# 函数

# CPU名称

class cpu_name(Thread):

    def __init__(self, text):
        Thread.__init__(self)
        self.text = text

    def run(self):
        Time_Start1 = time()
        import wmi
        Cpu_Info = wmi.WMI()
        for cpu in Cpu_Info.Win32_Processor():
            print_log("CPU_名称: " + cpu.name, "信息")
        Time_End1 = time()
        print_log(self.text + ": " + str((Time_End1 - Time_Start1) * 1000) + "ms", "信息")


def mainloop(text):
    Time_End = time()
    print_log(text + str((Time_End - Time_Start) * 1000) + "ms", "信息")
    window.mainloop()


# 日志
def print_log(msg, log_type):
    log_a = strftime("%H:%M:%S ", localtime())
    log_b = "[%s] " % log_type
    log_c = msg
    log_All = log_a + log_b + log_c
    print(log_All)


# 初始窗口
window = Tk()
window.title("")
window.geometry(window_geometry)
window.resizable(False, False)

# 初始化
thread_1 = cpu_name("线程1_运行耗时", )
thread_1.start()
# 显示窗口
mainloop("窗口_启动耗时: ")
thread_1.join()
