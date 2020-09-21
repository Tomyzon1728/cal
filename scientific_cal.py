
from tkinter import *
import math
import parser
import tkinter as t
#=============================================================================================================
screen = ''
operator = ''
fval = ''
style = ''
new = ''
#================================================================================================================
window = t.Tk()
window.title("ShugarCalculator")
window.wm_iconbitmap('cal.ico')
window.resizable(width=False,height=False)
#=============================================================================================================
screen = t.Entry(window, text="0",width = 32,font = ('serif 15', 20, 'bold'), bd =3, insertwidth =20, bg = 'powder blue', justify = 'right')
screen.grid(row=0, column=0, columnspan = 4)
#===============================================================================================================
def on_screen(display):
    global screen
    s_length = len(screen.get())
    screen.insert(s_length,display)
    return
def clear_screen():
    global screen
    screen.delete(0,"end")
    return
def pocket(cal):
    global screen, operator, fval
    fval = float(screen.get())
    screen.delete(0,"end")
    operator = cal
def equalto():
    global screen, operator, fval
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
def cos(self):
    self.result = False
    self.new = math.cos(math.radians(float(screen.get())))
    self.on_screen(self.new)
#---------first row--------------------------------------------------------------------------------------------
btn_log = t.Button(window, text="log ",padx= 16, bd = 2, fg='black', font =('courier',20, 'bold'),bg = '#073278',command = clear_screen)
btn_log.grid(row=1, column=0,)
btn_Sin = t.Button(window, text="Sin ",padx= 16, bd = 2, fg='black', font =('courier',20, 'bold'),bg = '#073278',command = clear_screen)
btn_Sin.grid(row=1, column=1,)
btn_Cos = t.Button(window, text=" Cos ",padx= 16, bd = 2, fg='black', font =('courier',20, 'bold'),bg = '#073278',command = cos)
btn_Cos.grid(row=1, column=2,)
btn_Tan = t.Button(window, text=" Tan ", padx= 16, bd = 2, fg='black', font =('courier',20, 'bold'),bg = '#073278',command = clear_screen)
btn_Tan.grid(row=1, column=3,)
#===============================================
btn_clear = t.Button(window, text=" c  ",padx= 16, bd = 2, fg='black', font =('courier',20, 'bold'),bg = '#073278', command = clear_screen)
btn_clear.grid(row=2, column=0)
btn_exp = t.Button(window, text="exp ",padx= 16, bd = 2, fg='black', font =('courier',20, 'bold'),bg = '#073278', command = lambda: on_screen())
btn_exp.grid(row=2, column=1)
btn_factorial = t.Button(window, text ='   ! ',padx= 16, bd = 2, fg='black', font =('courier',20, 'bold'),bg = '#073278',command = lambda: on_screen())
btn_factorial.grid(row=2, column=2)
btn_sqrt = t.Button(window, text="sqrt ", padx= 16, bd = 2, fg='black', font =('courier',20, 'bold'),bg = '#073278',command = lambda: pocket('+'))
btn_sqrt.grid(row=2, column=3)
#----------third row----------
btn4 = t.Button(window, text=" 7  ",  padx= 16, bd = 2,fg='black', font =('courier',20, 'bold'),bg = 'powder blue',command = lambda: on_screen(7))
btn4.grid(row=3, column=0)
btn5 = t.Button(window, text="  8 ",padx= 16, bd = 2, fg='black', font =('courier',20, 'bold'),bg = 'powder blue',command = lambda: on_screen(8))
btn5.grid(row=3, column=1)
btn6 = t.Button(window, text="   9 ", padx= 16, bd = 2, fg='black', font =('courier',20, 'bold'),bg = 'powder blue',command = lambda: on_screen(9))
btn6.grid(row=3, column=2)
btn_sub = t.Button(window, text="  +  " ,padx= 16, bd = 2, fg='black', font =('courier',20, 'bold'),bg = '#00ffff',command = lambda: pocket('+'))
btn_sub.grid(row=3, column=3)
#                -----------fourth row ------------
btn1 = t.Button(window, text=" 4  ", padx= 16, bd = 2, fg='black', font =('courier',20, 'bold'),bg = 'powder blue',command = lambda: on_screen(4))
btn1.grid(row=4, column=0)
btn2 = t.Button(window, text="  5 ", padx= 16, bd = 2, fg='black', font =('courier',20, 'bold'),bg = 'powder blue',command = lambda: on_screen(5))
btn2.grid(row=4, column=1)
btn3 = t.Button(window, text="   6 ", padx= 16, bd = 2, fg='black', font =('courier',20, 'bold'),bg = 'powder blue',command = lambda: on_screen(6))
btn3.grid(row=4, column=2)
btn_mul = t.Button(window, text="  -  ", padx= 16, bd = 2, fg='black', font =('courier',20, 'bold'),bg = '#00ffff',command = lambda: pocket('-'))
btn_mul.grid(row=4, column=3)
#          -----------fifth row-------------
btn_zero = t.Button(window, text="  1 ", padx= 16, bd = 2, fg='black', font =('courier',20, 'bold'),bg = 'powder blue',command = lambda: on_screen(1))
btn_zero.grid(row=5, column=0)
btn_point = t.Button(window, text=" 2  ", padx= 16, bd = 2, fg='black', font =('courier',20, 'bold'),bg = 'powder blue',command = lambda: on_screen(2))
btn_point.grid(row=5, column=1)
btn_equal = t.Button(window, text="   3 ",  padx= 16, bd = 2, fg='black', font =('courier',20, 'bold'),bg = 'powder blue',command = lambda:on_screen(3))
btn_equal.grid(row=5, column=2)
btn_div = t.Button(window, text="  *  ",  padx= 14, bd = 2, fg='black', font =('courier',20, 'bold'),bg = '#00ffff',command = lambda: pocket('*'))
btn_div.grid(row=5, column=3)
#-------------------------------------------
btn_log = t.Button(window, text=" 0  ",padx= 16, bd = 2, fg='black', font =('courier',20, 'bold'),bg = 'powder blue',command = lambda: on_screen(0))
btn_log.grid(row=6, column=0)
btn_tan = t.Button(window, text="  . ",padx= 16, bd = 2, fg='black', font =('courier',20, 'bold'),bg = 'powder blue',command = lambda: on_screen('.'))
btn_tan.grid(row=6, column=1)
btn_cos = t.Button(window, text="  =  ",padx= 16, bd = 2, fg='black', font =('courier',20, 'bold'),bg = '#00ffff',command = lambda: equalto())
btn_cos.grid(row=6, column=2)
btn_sin = t.Button(window, text="  /  ",padx= 16, bd = 2, fg='black', font =('courier',20, 'bold'),bg = '#00ffff',command = lambda: pocket('/'))
btn_sin.grid(row=6, column=3)
#------------------------------------
window.mainloop()