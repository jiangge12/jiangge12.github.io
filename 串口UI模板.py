import serial,time   # 需要安装库 pip install pyserial
import serial.tools.list_ports as listport
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg

#************* 获取串口列表 **************************************

port_list = list(sorted(listport.comports()))       # 获得带有描述的串口列表
for i in range(len(port_list)):                     # 遍历列表
    port_list[i] = port_list[i][0]                  # 只保留串口号供 ser 语句调用，如 COM1    
    
#************* 按钮函数 *****************************************

def btn0():#打开串口
    global ser, port                                # 全局变量，方便其他函数调用
    port = combo.get()                              # combo控件里的当前值
    try:                                            # 串口这样容易失败的操作用 try + except 组合方便出错处理
        ser = serial.Serial(port, 115200)
        print("\n串口 "+port+" 连接成功")
    except:
        print("\n串口已经连接或打开失败!")
        msg.showwarning(title="警告", message="串口已经连接或打开失败！")
        
def btn1():
    print("\n向串口 "+port+" 发送字符串 Hello 和结束符")
    ser.write(('Hello\r\n').encode('utf-8'))        # \r\n 是单片机需要的结束符
    time.sleep(0.1)                                 # 等待下位机处理完数据并返回接收到的参数
    re = ser.read_all()                             # 读出串口缓冲区全部内容（接收并未严格要求\r\n）
    if len(re) ==0 : print("下位机无应答：")
    else : print("串口设备 "+port+" 返回：",re)

def btn2():
    msg.showwarning(title="警告", message="按下了按钮2")
              
#*************** 构建UI *****************************************  
  
win = tk.Tk()
win.geometry('400x300+600+400')
    
# 串口选择combo
combo = ttk.Combobox(win,width=8,values=port_list)  
combo.place(x=10,y=12) 
combo.current(0)

# 三个按钮
B0 = ttk.Button(win, text="打开串口", command=btn0).place(x=100,y=10)
B1 = ttk.Button(win, text="按钮1", command=btn1).place(x=100,y=200)
B2 = ttk.Button(win, text="按钮2", command=btn2).place(x=200,y=200)
