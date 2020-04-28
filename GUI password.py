from tkinter import *
obj = Tk()
obj.geometry('600x600')
import random
num = ['1','2','3','4','5','6','7','8','9','0']
upper=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lower=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
specialchar=list('`~!@#$%^&*()_+-=[]{}|/;:,<.>?')
allchar = num+upper+lower+specialchar
password = []
a = IntVar()
L = Label(text = 'Length of the password').place(x = 20, y = 20)
E = Text(height = 1,width = 40)
E.place(x = 160,y = 120)
T =  Text(width = 65, height = 25)
T.place(x = 30,y = 120)
def call(password):
    T.delete('1.0',END)
    T.insert(END,password)
def simple(n,password):
    print(n)
    n = int(n)
    B.config(state="disabled")
    for i in range(0, n):
        password.append(random.choice(upper + lower + num))
    password = ''.join(password)
    call(password)

def complx(n, password):
    B.config(state="disabled")
    n = int(n)
    for i in range(0, n):
        password.append(random.choice(upper + lower + num + specialchar))
    password = ''.join(password)
    call(password)
B = Button(obj, text = 'simple', command = lambda:simple(E.get('1.0','end-1c'),password))
B.grid(row =1,columns = 1)
B.place(x = 200, y = 80)
B2 = Button(obj, text = 'complex', command = lambda:simple(E.get('1.0','end-1c'),password))
B2.grid(row = 1, columns = 1)
B2.place(x = 350, y = 80)
print(password)
obj.mainloop()