import math
from tkinter import *
from tkinter import messagebox
from math import pi,e,sin,cos,tan,log
window=Tk()
window.geometry("600x700")
window.resizable(1,1) # handles the resizing of the window this sets it to false meaning the window should not resize
window.title("Calculator by Festus")
#icon=PhotoImage(file="C:\\Users\\Administrator\\Downloads\\wall 5.jpeg")
#window.iconphoto(True,icon)
window.config(bg="#3b403e")# gives body the color
label1=Label(window,text="Made by Festu",fg="blue",bg="black",font=("arial",20,"bold"))
label1.config(relief=RAISED)
label1.pack()
#window.iconbitmap("C:\\Users\\Administrator\\Downloads\\cool.png")

def about(): # creating drop down menu
    license_text= """MIT LICENSE"""
    messagebox.showinfo("About", "made by Festus")

def clickbutton(item):
    global expression
    inputText.set(inputText.get()+(str(item)))


def clearbutton():
    global expression
    inputText.set(inputText.get()[0:-1])



def clearAll ():
    inputText.set("")

def exponent ():
    inputText.set(inputText.get()+'^')

def equalbutton():
    try:
        expression = inputText.get()
        if '^' in expression:
            base, exp = expression.split('^')
            result = float(base) ** float(exp)   # ✅ exponentiation
        else:
            result = eval(expression)
        inputText.set(result)
    except:
        inputText.set("Error")

# Constants


menubar=Menu(window,bg="#3b403e",fg="white")
filemenu=Menu(menubar,tearoff=0,bg="#3b403e",fg="white")
filemenu.add_command(label="Copy")
filemenu.add_command(label="Paste")
filemenu.add_separator()
filemenu.add_command(label="Exit",command=window.quit)
menubar.add_cascade(label="Edit",menu=filemenu)
helpmenu=Menu(menubar,bg="#3b403e",fg="white")
helpmenu.add_command(label="About",command=about)
menubar.add_cascade(label="Help",menu=helpmenu)

expression= " "
inputText=StringVar()
inputFrame=Frame(window,
                 width=312,
                 height=150,
                 bd=0,
                 highlightbackground="black",highlightcolor="gray",
                 highlightthickness=1)
inputFrame.pack(side=TOP)
inputFeild = Entry(inputFrame,
                font=("arial",20,"bold"),
                textvariable=inputText,
                width=50,fg="white",bg="#3b403e",bd=0,
                justify=RIGHT)
inputFeild.grid(row=0,column=0)
inputFeild.pack(ipady=43)
# finally the main frame nigga
mainFrame=Frame(window,width=312,
                height=272.5,
                bg="black")
mainFrame.pack()

ac = PhotoImage(file="C:\\Users\\Administrator\\Downloads\\icons\\ac.png")
acimage=ac.subsample(4,4)
ac_button = Button(mainFrame,text="AC",fg="black",image=acimage,bd=0,bg="#3b403e",
cursor="hand2",command=lambda: clearAll()).grid(row=0,column=0,padx=1,pady=1)

clear= PhotoImage(file="C:\\Users\\Administrator\\Downloads\\icons\\clear.png")
clearimage=clear.subsample(4,4)
clear_button = Button(mainFrame,text="AC",fg="black",image=clearimage,bd=0,bg="#3b403e",
cursor="hand2",command=lambda:clearbutton()).grid(row=0,column=1,padx=1,pady=1)

expan_btn = PhotoImage(file="C:\\Users\\Administrator\\Downloads\\icons\\exponent_btn.png")
expan_btn_image=expan_btn.subsample(4,4)
percantage = Button(mainFrame,fg="black",image=expan_btn_image,bd=0,bg="#3b403e",cursor="hand2",
                    command=lambda:exponent()).grid(row=0,column=2,padx=1,pady=1)
divide=PhotoImage(file="C:\\Users\\Administrator\\Downloads\\icons\\divide.png")
divide_image=divide.subsample(4,4)
divide_button= Button(mainFrame,text="/",fg="black",image=divide_image,bd=0,bg="#3b403e",cursor="hand2",
command=lambda:clickbutton("/")).grid(row=0,column=3,padx=1,pady=1)

seven=PhotoImage(file="C:\\Users\\Administrator\\Downloads\\icons\\seven.png")
seven_image=seven.subsample(4,4)
Seven_button=Button(mainFrame,text="7",fg="black",image=seven_image,bd=0,bg="#3b403e",cursor="hand2",
             command=lambda:clickbutton(7)).grid(row=1,column=0,padx=1,pady=1)

eight=PhotoImage(file="C:\\Users\\Administrator\\Downloads\\icons\\eight.png")
eight_image=eight.subsample(4,4)
eight=Button(mainFrame,text="8",fg="black",image=eight_image,bd=0,bg="#3b403e",cursor="hand2",
             command=lambda:clickbutton(8)).grid(row=1,column=1,padx=1,pady=1)

nine=PhotoImage(file="C:\\Users\\Administrator\\Downloads\\icons\\nine.png")
nine_image=nine.subsample(4,4)
nine_button=Button(mainFrame,text="9",fg="black",image=nine_image,bd=0,bg="#3b403e",cursor="hand2",
            command=lambda:clickbutton(9)).grid(row=1,column=2,padx=1,pady=1)

four=PhotoImage(file="C:\\Users\\Administrator\\Downloads\\icons\\four.png")
four_image=four.subsample(4,4)
four_button=Button(mainFrame,text="4",fg="black",image=four_image,bd=0,bg="#3b403e",cursor="hand2",
            command=lambda:clickbutton(4)).grid(row=2,column=0,padx=1,pady=1)

five=PhotoImage(file="C:\\Users\\Administrator\\Downloads\\icons\\five.png")
five_image=five.subsample(4,4)
five_button=Button(mainFrame,text="5",fg="black",image=five_image,bd=0,bg="#3b403e",cursor="hand2",
            command=lambda:clickbutton(5)).grid(row=2,column=1,padx=1,pady=1)

six=PhotoImage(file="C:\\Users\\Administrator\\Downloads\\icons\\six.png")
six_image=six.subsample(4,4)
six_button=Button(mainFrame,text="6",fg="black",image=six_image,bd=0,bg="#3b403e",cursor="hand2",
            command=lambda:clickbutton(6)).grid(row=2,column=2,padx=1,pady=1)


one=PhotoImage(file="C:\\Users\\Administrator\\Downloads\\icons\\one.png")
one_image=one.subsample(4,4)
one_button=Button(mainFrame,text="1",fg="black",image=one_image,bd=0,bg="#3b403e",cursor="hand2",
            command=lambda:clickbutton(1)).grid(row=3,column=0,padx=1,pady=1)


two=PhotoImage(file="C:\\Users\\Administrator\\Downloads\\icons\\two.png")
two_image=two.subsample(4,4)
two_button=Button(mainFrame,text="2",fg="black",image=two_image,bd=0,bg="#3b403e",cursor="hand2",
            command=lambda:clickbutton(2)).grid(row=3,column=1,padx=1,pady=1)

three=PhotoImage(file="C:\\Users\\Administrator\\Downloads\\icons\\three.png")
three_image=three.subsample(4,4)
three_button=Button(mainFrame,text="3",fg="black",image=three_image,bd=0,bg="#3b403e",cursor="hand2",
            command=lambda:clickbutton(3)).grid(row=3,column=2,padx=1,pady=1)

multi=PhotoImage(file="C:\\Users\\Administrator\\Downloads\\icons\\multi.png")
multi_image=multi.subsample(4,4)
multi_button=Button(mainFrame,text="*",fg="black",image=multi_image,bd=0,cursor="hand2",bg="#3b403e",
 command=lambda:clickbutton("*")).grid(row=1,column=3,padx=1,pady=1)

minus=PhotoImage(file="C:\\Users\\Administrator\\Downloads\\icons\\minus.png")
minus_image=minus.subsample(4,4)
minus_button=Button(mainFrame,text="-",fg="black",image=minus_image,bd=0,cursor="hand2",bg="#3b403e",
 command=lambda:clickbutton("-")).grid(row=2,column=3,padx=1,pady=1)


plus=PhotoImage(file="C:\\Users\\Administrator\\Downloads\\icons\\plus.png")
plus_image=plus.subsample(4,4)
plus_button=Button(mainFrame,text="+",fg="black",image=plus_image,bd=0,cursor="hand2",bg="#3b403e",
 command=lambda:clickbutton("+")).grid(row=3,column=3,padx=1,pady=1)


zero=PhotoImage(file="C:\\Users\\Administrator\\Downloads\\icons\\0.png")
zero_image=zero.subsample(4,4)
zero_button=Button(mainFrame,text="0",fg="black",image=zero_image,bd=0,cursor="hand2",bg="#3b403e",
 command=lambda:clickbutton(0)).grid(row=4,column=0,padx=0,pady=0,columnspan=2)

point=PhotoImage(file="C:\\Users\\Administrator\\Downloads\\icons\\point.png")
point_image=point.subsample(4,4)
point_button=Button(mainFrame,text=".",fg="black",image=point_image,bd=0,cursor="hand2",bg="#3b403e",
 command=lambda:clickbutton(".")).grid(row=4,column=2,padx=1,pady=1)

equal=PhotoImage(file="C:\\Users\\Administrator\\Downloads\\icons\\equal.png")
equal_image=equal.subsample(4,4)
equal=Button(mainFrame,text="=",fg="black",image=equal_image,bd=0,cursor="hand2",bg="#3b403e",
 command=lambda:equalbutton()).grid(row=4,column=3,padx=1,pady=1)


bracket1=PhotoImage(file="C:\\Users\\Administrator\\Downloads\\icons\\bracket1.png")
bracket1_image=bracket1.subsample(4,4)
bracket1_button=Button(mainFrame,text="(",fg="black",image=bracket1_image,bd=0,cursor="hand2",bg="#3b403e",
 command=lambda:clickbutton("(")).grid(row=5,column=0,padx=1,pady=1)


bracket2=PhotoImage(file="C:\\Users\\Administrator\\Downloads\\icons\\bracket2.png")
bracket2_image=bracket2.subsample(4,4)
bracket2_button=Button(mainFrame,text=")",fg="black",image=bracket2_image,bd=0,cursor="hand2",bg="#3b403e",
 command=lambda:clickbutton(")")).grid(row=5,column=1,padx=1,pady=1)


pie=PhotoImage(file="C:\\Users\\Administrator\\Downloads\\icons\\pi.png")
pie_image=pie.subsample(4,4)
pie_button=Button(mainFrame,text="pi",fg="black",image=pie_image,cursor="hand2",bg="#3b403e",
          command=lambda:clickbutton(pi)).grid(row=5,column=2,padx=1,pady=1)



ei=PhotoImage(file="C:\\Users\\Administrator\\Downloads\\icons\\eie.png")
ei_image=ei.subsample(4,4)
ei_button=Button(mainFrame,text="e",fg="black",image=ei_image,cursor="hand2",bg="#3b403e",
          command=lambda:clickbutton(e)).grid(row=5,column=3,padx=1,pady=1)



Sin_photo=PhotoImage(file="C:\\Users\\Administrator\\Downloads\\icons\\sin_btn.png")
sin_image=Sin_photo.subsample(4,4)
sin_button=Button(mainFrame,text="sin",fg="black",image=sin_image,cursor="hand2",bg="#3b403e",
          command=lambda:clickbutton("sin(")).grid(row=5,column=4,padx=1,pady=1)

cos_btn=PhotoImage(file="C:\\Users\\Administrator\\Downloads\\icons\\cos_btn.png")
cos_image=cos_btn.subsample(4,4)
cos_btn=Button(mainFrame,text="cos",fg="black",image=cos_image,cursor="hand2",bg="#3b403e",
          command=lambda:clickbutton("cos(")).grid(row=4,column=4,padx=1,pady=1)

tan_btn=PhotoImage(file="C:\\Users\\Administrator\\Downloads\\icons\\tan_btn.png")
tan_image=tan_btn.subsample(4,4)
tan_btn=Button(mainFrame,text="tan",fg="black",image=tan_image,cursor="hand2",bg="#3b403e",
          command=lambda:clickbutton("tan(")).grid(row=3,column=4,padx=1,pady=1)

log_btn=PhotoImage(file="C:\\Users\\Administrator\\Downloads\\icons\\log_btn.png")
log_image=log_btn.subsample(4,4)
log_btn=Button(mainFrame,text="log",fg="black",image=log_image,cursor="hand2",bg="#3b403e",
          command=lambda:clickbutton("log(")).grid(row=2,column=4,padx=1,pady=1)









window.mainloop()

