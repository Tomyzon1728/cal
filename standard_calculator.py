import tkinter as t
#import math
#-----------------------------GlobalVariables------------------------------------------------------
screen = ''
operator = ''
fval = ''
all_clear = False
#screen_OnOff = True

#---------------------------------WindowAttributes----------------------------------------
window = t.Tk()
window.title("CALCULATOR")
window.resizable(width=False,height=False)
window.geometry("474x312+0+0")




#------------------------CalulatorFunctions------------------------------------
def on_screen(display):
    global screen,all_clear
    if all_clear == True:
        screen.delete(0,"end")
        all_clear = False
    if screen.get() == "0" and display != ".":
        screen.delete(0,'end')
        screen.insert(0,display)
    else:
        s_length = len(screen.get())
        screen.insert(s_length,display)
        return
def clear_screen():
    global screen
    screen.delete(0,"end")
    screen.insert(0,'0')
    return

def pocket(cal):
    global screen, operator, fval
    fval = float(screen.get())
    screen.delete(0,"end")
    operator = cal

def equalto():
    global screen, operator, fval,all_clear
    all_clear = True
    if(operator == "+"):
        sval = float(screen.get())
        result = fval + sval
        screen.delete(0,"end")
        screen.insert('end', result)
    elif(operator == "-"):
        sval = float(screen.get())
        result = fval - sval
        screen.delete(0,"end")
        screen.insert('end',result)
    elif(operator == "*"):
        sval = float(screen.get())
        result = fval * sval
        screen.delete(0,"end")
        screen.insert('end',result)
    elif(operator == "/"):
        sval = float(screen.get())
        result = fval / sval
        screen.delete(0,"end")
        screen.insert('end',result)






#----------------------------Screen  Column<0 - 4>------------------------------------------------
screen = t.Entry(window, text="0",width = 28,font = ('serif 15', 20, 'bold'), bd =3, bg = 'powder blue', justify = 'right')
screen.grid(row=0, column=0, columnspan = 4)
screen.insert(0,'0')



#---------FirstRow  Column<0 - 4>--------------------------------------------------------------
btn_clear = t.Button(window, text=" c  ", padx= 16, bd = 2, fg='black', font =('courier',20, 'bold'), bg = '#00ffff',command = clear_screen)
btn_clear.grid(row=1, column=0,)
btn_allclear = t.Button(window, text="  ~ ", padx= 16, bd = 2, fg='black', font =('courier',20, 'bold'),bg = '#00ffff',command = clear_screen)
btn_allclear.grid(row=1, column=1,)
btn_del = t.Button(window, text=" d ",padx= 16, bd = 2, fg='black', font =('courier',20, 'bold'),bg = '#00ffff',command = clear_screen)
btn_del.grid(row=1, column=2,)
btn_sqrt = btn_del = t.Button(window, text="  s  ",padx= 16, bd = 2, fg='black', font =('courier',20, 'bold'),bg = '#00ffff',command =  clear_screen)
btn_sqrt.grid(row=1, column=3,)

                  #----------SecondRow  Column<0 - 4>----------------------
btn7 = t.Button(window, text=" 7  ",padx= 16, bd = 2, fg='black', font =('courier',20, 'bold'),bg = 'powder blue', command = lambda: on_screen('7'))
btn7.grid(row=2, column=0)
btn8 = t.Button(window, text="  8 ",padx= 16, bd = 2, fg='black', font =('courier',20, 'bold'),bg = 'powder blue', command = lambda: on_screen('8'))
btn8.grid(row=2, column=1)
btn9 = t.Button(window, text =' 9 ',padx= 16, bd = 2, fg='black', font =('courier',20, 'bold'),bg = 'powder blue',command = lambda: on_screen('9'))
btn9.grid(row=2, column=2)
btn_add = t.Button(window, text="  +  ", padx= 16, bd = 2, fg='black', font =('courier',20, 'bold'),bg = '#073278',command = lambda: pocket('+'))
btn_add.grid(row=2, column=3)


                        #----------ThirdRow  Column<0 - 4>---------------
btn4 = t.Button(window, text=" 4  ",  padx= 16, bd = 2,fg='black', font =('courier',20, 'bold'),bg = 'powder blue',command = lambda: on_screen(4))
btn4.grid(row=3, column=0)
btn5 = t.Button(window, text="  5 ",padx= 16, bd = 2, fg='black', font =('courier',20, 'bold'),bg = 'powder blue',command = lambda: on_screen(5))
btn5.grid(row=3, column=1)
btn6 = t.Button(window, text=" 6 ", padx= 16, bd = 2, fg='black', font =('courier',20, 'bold'),bg = 'powder blue',command = lambda: on_screen(6))
btn6.grid(row=3, column=2)
btn_sub = t.Button(window, text="  -  " ,padx= 16, bd = 2, fg='black', font =('courier',20, 'bold'),bg = '#073278',command = lambda: pocket('-'))
btn_sub.grid(row=3, column=3)


#                -----------FourthRow  Column<0 - 4> ----------------------
btn1 = t.Button(window, text=" 1  ", padx= 16, bd = 2, fg='black', font =('courier',20, 'bold'),bg = 'powder blue',command = lambda: on_screen(1))
btn1.grid(row=4, column=0)
btn2 = t.Button(window, text="  2 ", padx= 16, bd = 2, fg='black', font =('courier',20, 'bold'),bg = 'powder blue',command = lambda: on_screen(2))
btn2.grid(row=4, column=1)
btn3 = t.Button(window, text=" 3 ", padx= 16, bd = 2, fg='black', font =('courier',20, 'bold'),bg = 'powder blue',command = lambda: on_screen(3))
btn3.grid(row=4, column=2)
btn_mul = t.Button(window, text="  *  ", padx= 16, bd = 2, fg='black', font =('courier',20, 'bold'),bg = '#073278',command = lambda: pocket('*'))
btn_mul.grid(row=4, column=3)

#          -----------FifthRow-------------
btn_zero = t.Button(window, text="  0 ", padx= 16, bd = 2, fg='black', font =('courier',20, 'bold'),bg = 'powder blue',command = lambda: on_screen(0))
btn_zero.grid(row=5, column=0)
btn_point = t.Button(window, text=" .  ", padx= 16, bd = 2, fg='black', font =('courier',20, 'bold'),bg = 'powder blue',command = lambda: on_screen("."))
btn_point.grid(row=5, column=1)
btn_equal = t.Button(window, text=" = ",  padx= 16, bd = 2, fg='black', font =('courier',20, 'bold'),bg = '#00ffff',command = lambda:equalto())
btn_equal.grid(row=5, column=2)
btn_div = t.Button(window, text="  /  ",  padx= 16, bd = 2, fg='black', font =('courier',20, 'bold'),bg = '#073278',command = lambda: pocket('/'))
btn_div.grid(row=5, column=3)


window.mainloop()