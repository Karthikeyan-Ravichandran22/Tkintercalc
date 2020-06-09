from tkinter import *
root=Tk()
root.geometry('250x400')
root.resizable(0,0)
root.title("Calculator")

val=""
operator=""
A=0
def click_1():
    global val
    val+="1"
    data.set(val)

def click_2():
    global val
    val+="2"
    data.set(val)

def click_3():
    global val
    val+="3"
    data.set(val)

def click_4():
    global val
    val+="4"
    data.set(val)

def click_5():
    global val
    val+="5"
    data.set(val)

def click_6():
    global val
    val+="6"
    data.set(val)

def click_7():
    global val
    val+="7"
    data.set(val)

def click_8():
    global val
    val+="8"
    data.set(val)

def click_9():
    global val
    val+="9"
    data.set(val)

def click_0():
    global val
    val+="0"
    data.set(val)

def click_pluse():
    global val
    global operator
    global A
    A=int(val)
    operator="+"
    val+="+"
    data.set(val)

def click_mul():
    global val
    global operator
    global A
    A = int(val)
    operator = "*"
    val+= "*"
    data.set(val)

def click_sub():
    global val
    global operator
    global A
    A = int(val)
    operator = "-"
    val+= "-"
    data.set(val)

def click_div():
    global val
    global operator
    global A
    A = int(val)
    operator = "/"
    val+= "/"
    data.set(val)

def click_reset():
    global A
    global val
    global operator
    val=""
    data.set(val)

def click_result():
    global A
    global val
    global operator
    val2=val
    if operator=="+":
        x=int(val2.split("+")[1])
        c=A+x
        data.set(c)
        val = str(c)
    elif operator=="-":
        x=int(val2.split("-")[1])
        c=A-x
        data.set(c)
        val = str(c)
    if operator=="*":
        x=int(val2.split("*")[1])
        c=A*x
        data.set(c)
        val = str(c)
    if operator=="/":
        x=int(val2.split("/")[1])
        c=A/x
        data.set(c)
        val=str(c)



data=StringVar()

label=Label(root,text='Label',anchor=SE,textvariable=data)
label.pack(expand=TRUE,fill=BOTH)


row1=Frame(root,bg='white')
row1.pack(expand=TRUE,fill=BOTH)
row2=Frame(root,bg='white')
row2.pack(expand=TRUE,fill=BOTH)
row3=Frame(root,bg='white')
row3.pack(expand=TRUE,fill=BOTH)
row4=Frame(root,bg='white')
row4.pack(expand=TRUE,fill=BOTH)

button1=Button(row1,text='1',font=('Italic',22),relief=FLAT,command=click_1)
button1.pack(side=LEFT,expand=TRUE,fill=BOTH)
button2=Button(row1,text='2 ',font=('Italic',22),relief=FLAT,command=click_2)
button2.pack(side=LEFT,expand=TRUE,fill=BOTH)
button3=Button(row1,text='3',font=('Italic',22),relief=FLAT,command=click_3)
button3.pack(side=LEFT,expand=TRUE,fill=BOTH)
button_pluse=Button(row1,text='+',font=('Italic',22),relief=FLAT,command=click_pluse)
button_pluse.pack(side=LEFT,expand=TRUE,fill=BOTH)

button4=Button(row2,text='4',font=('Italic',22),relief=FLAT,command=click_4)
button4.pack(side=LEFT,expand=TRUE,fill=BOTH)
button5=Button(row2,text='5 ',font=('Italic',22),relief=FLAT,command=click_5)
button5.pack(side=LEFT,expand=TRUE,fill=BOTH)
button6=Button(row2,text='6',font=('Italic',22),relief=FLAT,command=click_6)
button6.pack(side=LEFT,expand=TRUE,fill=BOTH)
button_sub=Button(row2,text='-',font=('Italic',22),relief=FLAT,command=click_sub)
button_sub.pack(side=LEFT,expand=TRUE,fill=BOTH)


button7=Button(row3,text='7',font=('Italic',22),relief=FLAT,command=click_7)
button7.pack(side=LEFT,expand=TRUE,fill=BOTH)
button8=Button(row3,text='8 ',font=('Italic',22),relief=FLAT,command=click_8)
button8.pack(side=LEFT,expand=TRUE,fill=BOTH)
button9=Button(row3,text='9',font=('Italic',22),relief=FLAT,command=click_9)
button9.pack(side=LEFT,expand=TRUE,fill=BOTH)
button_mul=Button(row3,text='*',font=('Italic',22),relief=FLAT,command=click_mul)
button_mul.pack(side=LEFT,expand=TRUE,fill=BOTH)


button_reset=Button(row4,text='C',font=('Italic',22),relief=FLAT,command=click_reset)
button_reset.pack(side=LEFT,expand=TRUE,fill=BOTH)
button0=Button(row4,text='0 ',font=('Italic',22),relief=FLAT,command=click_0)
button0.pack(side=LEFT,expand=TRUE,fill=BOTH)
button_equal=Button(row4,text='=',font=('Italic',22),relief=FLAT,command=click_result)
button_equal.pack(side=LEFT,expand=TRUE,fill=BOTH)
button_div=Button(row4,text='/',font=('Italic',22),relief=FLAT,command=click_div)
button_div.pack(side=LEFT,expand=TRUE,fill=BOTH)

root.mainloop()
