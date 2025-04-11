import tkinter as tk
import math
win=tk.Tk()
win.title('Калькулятор')
win.geometry('820x700+360+50')
win.resizable(False,False)
win.config(bg='blue')
# поле ввода
calc=tk.Entry(win,justify=tk.RIGHT,font=('Arial',30))
calc.grid(row=0,column=0,columnspan=10,stick='wesn',padx=5)
calc.insert(0,0)
win.grid_columnconfigure(0,minsize=200)
win.grid_columnconfigure(1,minsize=200)
win.grid_columnconfigure(2,minsize=200)
win.grid_columnconfigure(3,minsize=200)
win.grid_rowconfigure(0,minsize=60)
# создание кнопок 
per=0
def add_digit(digit):
    global per
    if per==0:
        value=calc.get()
        if len(value)==1 and value[0]=='0':
            value=value[1:]
        value=value+str(digit)
        calc.delete(0,tk.END)
        calc.insert(0,value)
    else:
        per=0
        calc.delete(0,tk.END)
        value=calc.get()
        if len(value)==1 and value[0]=='0':
            value=value[1:]
        value=value+str(digit)
        calc.delete(0,tk.END)
        calc.insert(0,value)
def add_operation(operation):
    value=calc.get()
    if len(value)==1 and value[-1]=='0':
        value=value[1:]
    if value[-1] in '-+*/.':
        value=value[:-1]
    calc.delete(0,tk.END)
    calc.insert(0,value+operation)
    global per
    if per==1:
        per=0
def make_digit_button(digit):
    if digit[-1]=='(' and len(digit)>1:
        digit_1=digit[:-1]
    else:
        digit_1=digit
    return tk.Button(text=digit_1,bd=5,font=('Arial',23),command=lambda:add_digit(digit))
def make_operation_button(operation):
    return tk.Button(text=operation,bd=5,font=('Arial',23),command=lambda:add_operation(operation))
k=1
for i in range(1,4):
    for j in range(3):
        make_digit_button(str(k)).grid(row=i,column=j,padx=5,pady=5,stick='wesn')
        k+=1
mas=['+','-','*','/','^']
for i in range(1,5):
    make_operation_button(mas[i-1]).grid(row=i,column=3,padx=5,pady=5,stick='wesn')
make_digit_button('(').grid(row=5,column=0,padx=5,pady=5,stick='wesn')
make_digit_button(')').grid(row=5,column=1,padx=5,pady=5,stick='wesn')
make_digit_button('^').grid(row=6,column=0,padx=5,pady=5,stick='wesn')
make_digit_button('e').grid(row=6,column=1,padx=5,pady=5,stick='wesn')
make_digit_button('π').grid(row=6,column=2,padx=5,pady=5,stick='wesn')
make_digit_button('ln').grid(row=6,column=3,padx=5,pady=5,stick='wesn')
make_digit_button('sin(').grid(row=7,column=0,padx=5,pady=5,stick='wesn')
make_digit_button('cos(').grid(row=7,column=1,padx=5,pady=5,stick='wesn')
make_digit_button('tg(').grid(row=7,column=2,padx=5,pady=5,stick='wesn')
make_digit_button('ctg(').grid(row=7,column=3,padx=5,pady=5,stick='wesn')
def clear_0():
    calc.delete(0,tk.END)
    calc.insert(0,0)
def delete_0():
    value=calc.get()
    if len(value)==1:
        calc.delete(0,tk.END)
        calc.insert(0,0)
    else:
        value=value[:-1]
        calc.delete(0,tk.END)
        calc.insert(0,value)
tk.Button(text='delete',bd=5,font=('Arial',23),command=lambda:delete_0()).grid(row=4,column=1,padx=5,pady=5,stick='wesn')
tk.Button(text='clear',bd=5,font=('Arial',23),command=lambda:clear_0()).grid(row=4,column=2,padx=5,pady=5,stick='wesn')
def calculation0(value):
    new_value=expression_2(value)
    if new_value!='error':
        new_value=expression_3(new_value)
        return new_value[0]
    else:
        return 'error'
def calculation1(value,v):
    value=float(value)
    if v=='(':
        return value
    elif v=='sin(':
        print(value)
        return math.sin(value)
    elif v=='cos(':
        return math.cos(value)
    elif v=='tg(':
        return math.tan(value)
    elif v=='ctg(':
        return 1/math.tan(value)
    elif v=='ln(':
        return math.ln(value)
def equal():
    global per
    per=1
    value_0=calc.get()
    value_0=expression_1(value_0)
    while  set(mas4).intersection(set(value_0))!=set():
        s=0
        for i in range(len(value_0)):
            if value_0[i] in mas4:
                s=i
                v=value_0[i]
            if value_0[i]==')':
                if value_0[s] in mas4:
                    value=value_0[s+1:i]
                    if len(value)==2:
                        if (value[0]=='-' or value[0]=='+') and type(value[1])==float:
                            r=float(value[0]+str(value[1]))
                            value_0[s]=float(r)
                            value_0.pop(s+1)
                            value_0.pop(s+1)
                            value_0.pop(s+1)
                            break
                    number=calculation0(value)
                    if number=='error':
                        calc.delete(0,tk.END)
                    value_0[s]=calculation1(number,v)                
                    for k in range(i-s):
                        value_0.pop(s+1)
                break
    calc.delete(0,tk.END)
    calc.insert(0,calculation0(value_0))
mas1=['sin(','cos(','tg(','ctg(','ln(']
mas2=[')','(']
mas3=['sin','cos','tg','ctg','ln']
mas4=['sin(','cos(','tg(','ctg(','ln(','(']
mas5=['1','2','3','4','5','6','7','8','9']
mas6=['sin(','cos(','tg(','ctg(','ln(',')','(',]
def expression_1(value_0):  
    k=0
    value=[]
    value_1=[]
    for i in range(len(value_0)):
        if value_0[i] in mas or value_0[i] in mas1 or value_0[i] in mas2:
            value.append(value_0[k:i])
            value.append(value_0[i])
            k=i+1
    value.append(value_0[k:])
    while '' in value:
        value.remove('')
    per=0
    for i in range(len(value)):
        if per==1:
            per=0
            continue
        if value[i] in mas3:
            value_1.append(value[i]+'(')
            per=1
        else:
            value_1.append(value[i])
    for i in range(len(value_1)):
        if value_1[i] not in mas6 and value_1[i] not in mas:
            value_1[i]=float(value_1[i])
        elif value_1[i]=='e':
            value_1[i]=math.e
        elif value_1[i]=='π':
            value_1[i]=math.pi
    return value_1
def expression_2(value):
    while '^' in value :
        for i in range(len(value)):
            if value[i]=='^':
                n=float(value[i-1])**float(value[i+1])
                value[i-1]=n
                value.pop(i)
                value.pop(i)
                break 
    while '*' in value or '/' in value:
        for i in range(len(value)):
            if value[i]=='*':
                n=value[i-1]*value[i+1]
                value[i-1]=n
                value.pop(i)
                value.pop(i)
                break
            if value[i]=='/':
                if value[i+1]==0:
                    print("ошибка деления на ноль")
                    return 'error'
                else:
                    n=value[i-1]/value[i+1]
                    value[i-1]=n
                    value.pop(i)
                    value.pop(i)
                break
    return value
def expression_3(value):
    while '+' in value or '-' in value:
        for i in range(len(value)):
            if value[i]=='+':
                n=value[i-1]+value[i+1]
                value[i-1]=n
                value.pop(i)
                value.pop(i)
                break
            if value[i]=='-':
                n=value[i-1]-value[i+1]
                value[i-1]=n
                value.pop(i)
                value.pop(i)
                break
    value[0]=round(value[0],6)
    return value
def add_point():
    value=calc.get()
    if value[-1]!='.':
        value=value+'.'
        calc.delete(0,tk.END)
        calc.insert(0,value)    
tk.Button(text='.',bd=5,font=('Arial',23),command=lambda:add_point()).grid(row=5,column=2,padx=5,pady=5,stick='wesn',)
tk.Button(text='=',bd=5,font=('Arial',23),command=lambda:equal()).grid(row=5,column=3,padx=5,pady=5,stick='wesn',)
make_digit_button('0').grid(row=4,column=0,padx=5,pady=5,stick='wesn')
win.mainloop()
