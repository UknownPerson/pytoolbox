import base64
import os
from threading import *
from tkinter import *
from time import *


# 日志
def print_log(msg, log_type):
    log_a = strftime("%H:%M:%S ", localtime())
    log_b = "[%s] " % log_type
    log_c = msg
    log_All = log_a + log_b + log_c
    print(log_All)


print_log("主线程_窗口_启动", "信息")
# 初始赋值
Time_Start = time()

window_width = "300"  # 窗口_宽
window_height = "500"  # 窗口_高

icon_img = b'AAABAAEAICAAAAEAIACoEAAAFgAAACgAAAAgAAAAQAAAAAEAIAAAAAAAABAAABILAAASCwAAAAAAAAAAAAAeKUr/HChI/x0oSP8fKkf' \
           b'/IS1W/yUvZP8hKmH/Iyxk/zU+df8zPXv/HSdv/yIraf9HU2z/QktU/05WYf9bYW3/TVRj/1lfav9ZYGv/MDpK/zI7SP8zO0j/TFFc' \
           b'/29tef9panX/Sk9c/zpEVf83QVP/PEhh/yk4W/8tOk3/N0dh/wsUYP8KFFX/CRRP/wkUU/8TG3v/GRyY/xkZn/8aGp//Ghmf' \
           b'/xUXkv8UFpT/LTOW/295jf9OU1//bHJ+/5KYof9RV2X/b3R+/2dsd/86Q1P/NDxL/zxEUP9UWGP/enWA/29rd/9scHr/V2Fx/1Neb' \
           b'/9SXHT/Hi5S/zRHaP84TXH/Dhhq/wwWXf8LFVv/DBZh/xAYef8WGJD/GRma/xcZlf8WGJD/FRiN/x4dnv9hbJL/Ymhx/19kdv9YX2z' \
           b'/mp+m/1RaZP9+g43/io+Y/zpCUv83P1L/P0dU/1ZaZP96doH/e3WA/1ZaZf80Pk//O0db/0VSZ/83Sm3/RVl//1NnjP8SG3n/EBl2' \
           b'/w4Yb/8MF2f/ERl7/xYaj/8XGZD/FBmF/xcZkf8gGqj/ISWE/zlEUf8+RVL/UFZh/09WYf9cYW3/T1Re/1ZcZf9SWWT/LDVF/zxEV' \
           b'/9FTlr/XmBq/4F7h/+Df4n/TlNh/y88Tv8/TGP/VGWC/1hrkP9VZ4z/UmWK/xQaiP8VGon/EhmA/w0YaP8SGnv/Fh2C/xMZgv8YGJX' \
           b'/Hhqh/yYnnf8hLFH/Iy05/zhAT/9JUFn/TVRe/0xSX/9OVF3/S1Jb/0dNVv8uN0b/PkZY/0pRXv9raXT/ioaQ/4yKk/9WW2j/NUBT' \
           b'/0ZUa/9WaIT/Wm2R/2qBo/9uh6b/ERp6/xMagf8UHXz/Eh1w/xUeeP8UHHz/GRyP/x4aov8kI53/bXeh/zpFTP8XIS7/Ii03/ygyO' \
           b'/8rNT7/LjdA/y02P/8sNT7/JzE5/yw1Qf9DS1v/TlRi/4GAiv+dnaP/n5+m/2BndP86Q1X/T1xy/1Jjfv9PYYH/a4Cd/2J4m/8UHXn' \
           b'/GCF5/xYgc/8THnD/FR90/xQbhP8gIpf/IR2e/1RZoP+yt7f/bHR+/x4oMf8kLjb/Hyoy/x4pMf8fKTH/ICoy/yEqM/8gKjP/MDhB' \
           b'/0ZNWv9PVWT/jIyU/7K0uP+3t7z/cXR+/z9JWf9SYHT/YHCK/3mKqf9qe6T/U2iM/xkhgP8cJXj/HSZ4/xojd/8ZIIP/GyGP' \
           b'/yMllv8iJZX/fYag/7G1t/97g4//JC44/yYxOf8kLzf/JC83/yUvN/8kLjf/JS84/ygxOf8wN0L/SE9d/1RaaP+RkZj/vr7A' \
           b'/8HAwf91d4H/RExc/1lldv9qfJb/VmSY/05ekP9XZ5f/ISiE/yApfv8hKnr/ISl8/yAmif8jJZX/Jyed/x4na/9qc33/qrG5/2Bnc' \
           b'/8jLTb/JjI5/yUwOP8mMTn/JjE5/ygyOv8qMjv/KzE6/zE5Q/9MVGH/W19r/5STmv++vsD/wMDB/3V5g/9JUmH/YWt7/2V0j/9qeZf' \
           b'/ZHWY/1Nhlv8mMnL/Ii9a/x0rTf8fLF7/Iyt9/yYrj/8rLaD/HipM/09XYP+NlqP/RExa/ycxO/8nMTn/KDI6/ykyOv8oMTr/KzI7' \
           b'/y01Pf8sNDz/MztH/09XZP9hZG//l5if/7y8vf++vb7/eHuG/0tXZv9ocX//iZKh/6+3wP+Kma//Z3mh/yk0S/8nMUD/LjpL' \
           b'/yg4Wf8mMnT/LDKS/y4xo/8kLXj/LzlK/1phbP9AR1b/Jy88/yw0P/8rMj7/KzM+/yw0P/8vNkD/MDdB/zA4Qv83P07/Ulpp/2Zqdf' \
           b'+dnqT/wsLD/8TDxf97f4n/T1tp/295iP+JkZv/q7W+/3OEn/91jbD/QExd/1Ffd/9gco//RFh+/zZEfP88Qpf/Njmh/zQ4pP8wOnv' \
           b'/UFto/11lc/8rMzz/MTlD/y02Qf8uN0H/MDdB/y83QP8xOkL/ND1G/zxEUf9YYG3/am14/6Ggpv/Gxsf/x8bJ/3yAiv9XYW3/eICR' \
           b'/4yWo/+AjK//bny0/3eHxP9xgJn/gJGr/3OHpf9abJH/TF6B/0tdgP9JU5L/Rkyf/0ZLp/9VYZv/fIug/z5HUP8xOUb/MDhF' \
           b'/y84Qv8wOEX/MTpH/zQ9Sf80PEn/RExY/2Jqdf9vcX3/paSp/8jHyP/JyMv/goWO/2Fodf+Ci5n/kZ24/3Z9zf9xds3/Yma9/4yctv' \
           b'+Sobj/gZKr/3CBoP9gcpP/UmWC/09iiP9dap3/ZGqy/1ZZt/9zf67/a3eK/zE6SP84RFn/Tl11/1tsh/9YaYb/XG2K/1Nie/9RXXH' \
           b'/anF9/3R3g/+oqa7/y8rL/8vKzP+IipP/aG99/4mUpP+bp9L/g4zQ/3aFvv93jbr/ssDP/6Cww/+Upbv/jp61/4WVrv98jqf/fI+p' \
           b'/3yOq/9pep7/a3eo/2Nwo/9PYIj/R1h4/1drjP9ab5L/Y3aY/2V6mv9tgqL/cIWl/2l5k/91fIn/fn6J/6+vsv/MzM3/y8vM/4' \
           b'+Rmv9xdoT/kJqm/5yoxP+LpcP/lr7X/6jS5//f5+7/vMjV/6S1yv+ltsr/pLTI/6Szx/+iscj/o7TL/6S0yv+ywtD/vs3c' \
           b'/6S0yP9pfZ3/UWWI/1JkhP9WaIf/Wm6O/2F1lf9ugqD/cIKc/4SMmf+Ljpf/srK2/87N0P/OztH/l5yk/4SKlv+jr7r/nbPF/5S40P' \
           b'+lzuj/qtPq/+Xs8//X4Of/tMLU/6270P+tvND/rbzQ/6O0y/+ZqsP/rLvQ/7zK3P/N2+j/ucjZ/11wj/9MXnn/TF16/09gfP9XaIX' \
           b'/W22M/2Z4lf+Ck6r/qbS8/6u0uf/b3d//8/X1//L09f+3v8T/oKuy/7jG0/+rzeH/mMDa/5vC3v+bw9//7PL4/+rx9v/Z4+z/x9Lh' \
           b'/7fE1f+tvM//na3C/4WUrP+ot8r/tsTW/6Gxxv99jqn/cYSg/3KEn/9vf5r/ZXaR/19xi/9ecI3/XnGO/4masv+zv8r/p7G2/9vg4v/6' \
           b'/P3/+Pv7/73Fyv+st77/sMLR/5y90v+bv9b/ncXe/5/G3f/y+P3/8vj9//T6/v/z+P3/5ezy/8vW4v+2w9L/qbjM/6u6zP+gr8T/gpSu' \
           b'/5Ciu/+lts3/p7jO/6i2zf+aqsL/jZ63/4aXr/99jqj/fIym/5yrvf+otL7/xMfK/+nr7P/i5Ob/rbW6/664wP+1wsv/t9LX/7TP1P' \
           b'+qwdD/n7LF//L4/f/y+f3/9Pr+//T7/v/z+v7/7PP5/9vk7P/M2OT/tMPV/6KzyP+er8b/n7HJ/6S0yv+ot83/rLrQ/6a4zv+ktsz' \
           b'/oLLJ/5uqwf+PnrX/ipis/6Wwu//LztH/8vT0/+bn6f+uuL3/wMjP/9Pb4P++yM3/o6yx/6Gss/+Voq7/9Pr+//b7///3/f//+P7' \
           b'///X7/v/u9Pr/5+7z/9ji6v+ywc//o7bK/6W2zf+Vpr7/lKO7/5qqwf+erMP/orLJ/6a4zv+qutD/qLjO/6Cwxf+aqbz/oq++/73Ey' \
           b'//g5Of/1dja/7a/xv/V3uT/4erv/97l6v/P197/wczT/8PM0//2/P//9/3///f////4////9/7///D2+//m7vT/1+Hp/7K/zP+gscj' \
           b'/nKvD/4GQqP+isMb/ssDV/6e1y/+Tobr/n67E/6270f+ruc//qbfL/6a2yP+ls8T/prLA/8rT2//b4uf/2uLo/97m6//e5+v/3ebr' \
           b'/93m6//d5ev/3+Tp//b9///4//7/+f/+//n//v/3/v//8vj9/+jw9v/Y4un/s8DO/5yuxf+bqsL/i5qy/4qZsf+bqsH/kZ+3/5Shuv' \
           b'+jscf/q7nP/6y60P+rus3/qrnL/6m0wf+qtMH/0Nng/+Hp7f/e5er/2+To/9vj6P/a4OX/19/k/9bd5P/U3OP/9/7///n//v/5//7/+f' \
           b'/+//j////0+v3/6vD3/9fh6f+3w9D/qrrQ/6Ozyv+brMT/k6O7/5Gft/+cq8L/qbfM/6i1y/+xvtP/tcPX/6+90f+vvM//qLG7/77Gzf' \
           b'/Y3+b/1dzi/9Tb4v/T2+L/09rh/9La4P/R2eD/0dng/9DY3//3////+f/+//n//v/5//7/+f/+//X7/v/q8ff/2OLp/77J1v+xv9T' \
           b'/q7vT/5usxP+Qnrb/lqO6/5Wiuf+jscb/rLvP/7jG2f+5x9n/tcPY/7fD0/+qsrj/vMPJ/9Ha4v/Q2N//0Njg/9HZ4P/R2eD/0dnh' \
           b'/9HZ4P/S2uH/0tng//n//v/5//7/+f/+//n//v/5//7/9vz+/+vy+P/Y4ur/w87Z/6m4y/+gssj/oLLI/6W0yv+puMz/o7PI/6W1yP' \
           b'+puMv/sb/U/7fF2f+7yNn/vMfQ/6yxtf+/x83/0tvi/9HZ4P/U2+L/1Nzi/9Xc4//W3eP/1N3k/9bd4//W3eP/+f/+//n//v/5//7/+f' \
           b'/+//n//v/3/f//6/L5/9fh6v/H0dv/o7LA/5Ojtv+RoLX/nK3D/6K1yP+gssb/nq7B/52rvf+ptcT/rbvM/7jD0P+yu8T/q7C0/8PL0f' \
           b'/W3uX/193j/9fe5P/Z4OX/3OPn/9zj5//b5On/3eXp/93k6P/5//7/+f/+//n//v/5//7/+f/+//b8///r8vj/1uDp/8zW3/+ntMP' \
           b'/lqa5/5urvP+gsMP/p7fJ/6i2yf+ls8X/o7LC/6e0w/+ptsT/sLrG/62zu/+xs7f/z9Xb/9jg5v/b4eb/2+Pn/9/m6f/i6Oz/4+nt' \
           b'/+Xr7v/m7O//5uzu//n//v/5//7/+f/+//n//v/5//7/9vz//+vx9v/W4Oj/z9ji/7bAzf+Wpbj/mai7/6Oyxf+rusz/q7rN/6i2x' \
           b'/+jssH/prPD/6y5x/+vucT/q66y/8DAxP/c4+j/3OPn/9/m6v/j6e3/5evu/+nt8f/q7/L/6+/z/+3w9P/s8fT/+f/+//n//v/5//7' \
           b'/+f/+//n//v/3/f//6vH3/9Xg6P/Q2uT/v8rV/5mot/+gssb/qLjK/6q5zP+su83/rr3P/627zv+tvM//rrrI/6qwtv+0tbj/1Nre' \
           b'/97m6//g6Oz/5eru/+jt8P/r8PT/8vX4//b5+//2+/z/+Pz9//j9/v/5//7/+f/+//n//v/5//7/+f/+//f9///q8fj/1uDp/8/a5P' \
           b'/M2OP/oq68/5aktf+nt8r/qrrN/6y6zf+uvdD/rr3O/6y4w/+orrX/r7S4/8/W2v/f5+z/4uju/+fs8P/r7/P/7vL3//X5+//6/v7' \
           b'/+/////v////+/////P////n//v/5//7/+f/+//n//v/5//7/9/3//+rw9//Y4ur/z9rk/8/b5v/Ez9r/mKCr/42Ypv+YpLP/nqm1' \
           b'/6Ktt/+gqrX/oaet/7W4vP/T2d3/4Oft/+Lq7//o7vT/6/D1/+/z+P/1+vz/+f////v////8/////v' \
           b'//////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA' \
           b'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA= '

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
            print_log("线程1_结果_CPU名称: " + cpu.name, "信息")
        Time_End1 = time()
        print_log(self.text + ": " + str((Time_End1 - Time_Start1) * 1000) + "ms", "信息")


# 初始窗口
print_log("主线程_窗口_初始化_启动", "信息")
Time_Start2 = time()
window = Tk()
window.title("ToolBox")
window.geometry(window_geometry)
window.resizable(False, False)
Time_End2 = time()
print_log("主线程_窗口_初始化_耗时: " + str((Time_End2 - Time_Start2) * 1000) + "ms", "信息")

print_log("主线程_窗口_设置图标_启动", "信息")
Time_Start3 = time()
tmp_img = open('icon.ico', 'wb+')
tmp_img.write(base64.b64decode(icon_img))
tmp_img.close()
window.iconbitmap('icon.ico')
os.remove('icon.ico')
Time_End3 = time()
print_log("主线程_窗口_设置图标_耗时: " + str((Time_End3 - Time_Start3) * 1000) + "ms", "信息")

# 初始化
print_log("主线程_线程1_运行_启动", "信息")
thread_1 = cpu_name("线程1_运行_耗时", )
thread_1.start()

# 显示窗口
Time_End = time()
print_log("主线程_窗口_启动_耗时: " + str((Time_End - Time_Start) * 1000) + "ms", "信息")
print_log("主线程_窗口_mainloop", "信息")
window.mainloop()
