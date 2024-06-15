import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *

def put_digit(digit):
    global operands, cur_operand_nr, started
    if started:
        operands[cur_operand_nr] = operands[cur_operand_nr] * 10 + digit
        print(operands[cur_operand_nr])
        operand_to_scoreboard()

def put_digit_9():
    global operands, cur_operand_nr
    operands[cur_operand_nr] = operands[cur_operand_nr] * 10 + 9
    operand_to_scoreboard()

def always_on_top_():
    global win_on_top
    if win_on_top:
        window.attributes('-topmost', False)
        win_on_top = False
    else:
        window.attributes('-topmost', True)
        win_on_top = True

def operand_to_scoreboard():
    global operands, cur_operand_nr, scoreboard
    scoreboard.forget
    print(str(operands[cur_operand_nr]))
    scoreboard = tk.Label(frame, text=str(operands[cur_operand_nr]), font='Arial 25', borderwidth=5, relief="flat", \
    width=15, anchor=tk.E)
    scoreboard.pack(anchor="nw")

def clear_all():
    operands = [0, 0]
    cur_operand_nr = 0
    scoreboard['text'] = '0'

# def menu_vis_swicher():
#     global menu_visible
#     global window
#     print('in func',window.geometry(), menu_visible)
#     if menu_visible:
#         menu_visible = False
#
#         #main_menu.tk_popup(1,1)
#     else:
#         menu_visible = True
#         main_menu.tk_popup(100,  100)
#         #main_menu

# КОНФИГУРАЦИЯ ОКНА
window = tk.Tk()
window.geometry("324x500")
window.resizable(False,False)
window.title ('My calculator')
window.iconbitmap(default="my_calc.ico")

# ПЕРЕМЕННЫЕ
operands = [0, 0]
cur_operand_nr = 0
scoreboard_text = '0'
started = False


# МЕНЮ
# main_menu = Menu(window)
# #the_menu = Menu()
# menu_visible =False
# window.option_add("*tearOff", False)
# main_menu.add_command(label="Обычный")
# main_menu.add_command(label="Инженерный", state=DISABLED)
# main_menu.add_command(label="Программист", state=DISABLED)
# window.config(menu=main_menu)
# menu_visible = False

# ВЫБОР ТИПА КАЛЬКУЛЯТОРА
pic_menu = PhotoImage(file = "menu.png")
button_menu = tk.Button(window, width=20, image = pic_menu)#, command = menu_vis_swicher())
button_menu.place(x=10, y=10)
# ТЕКУЩИЙ ТИП КАЛЬКУЛЯТОРА
calc_type = tk.Label(window, text = 'Обычный', font='Arial 15', borderwidth=0, relief="flat")
calc_type.place(x = 45, y = 12)

# КНОПКА Always On Top
win_on_top = False
pic_top = PhotoImage(file = "top.png")
button_ontop = tk.Button(window, width=20, image = pic_top, command = always_on_top_)
button_ontop.place(x=165, y=10)

# ТАБЛО
frame = ttk.Frame(borderwidth=5, relief="solid")
#frame.place(x=5, y=50)
frame.pack(expand=None, anchor=tk.W)
scoreboard = tk.Label(frame, text = scoreboard_text, font='Arial 25', borderwidth=5, relief="flat", width = 15, height = 1 ,anchor=tk.E)
scoreboard.pack(expand=None, anchor=tk.W)

# КНОПКИ МАНИПУЛЯЦИЙ С ПАМЯТЬЮ
button_mc = tk.Button(window, width = 6, text = 'MC')
button_mc.place(x=4, y=120)
button_mr = tk.Button(window, width = 6, text = 'MR')
button_mr.place(x=56, y=120)
button_mplus = tk.Button(window, width = 6, text = 'M+')
button_mplus.place(x=108, y=120)
button_mminus = tk.Button(window, width = 6, text = 'M-')
button_mminus.place(x=160, y=120)
button_ms = tk.Button(window, width = 6, text = 'MS')
button_ms.place(x=212, y=120)
button_mj = tk.Button(window, width = 6, text = 'M' + chr(8744))
button_mj.place(x=264, y=120)

# КНОПКИ ОПЕРАЦИЙ
button_proc = tk.Button(window, width = 9, height = 2, text = '%')
button_proc.place(x=4, y=150)
button_ce = tk.Button(window, width = 9, height = 2, text = 'CE')
button_ce.place(x=83, y=150)
button_c = tk.Button(window, width = 9, height = 2, text = 'C', command=clear_all())
button_c.place(x=162, y=150)
pic_back = PhotoImage(file = "back.png")
button_back = tk.Button(window, width = 68, height = 35, image = pic_back)#, text = 'C')
button_back.place(x=241, y=150)
#pic_back = PhotoImage(file = "back.png")
button_share = tk.Button(window, width = 9, height = 2, text = '1/x')
button_share.place(x=4, y=200)
button_square  = tk.Button(window, width = 9, height = 2, text = 'X'+chr(178))
button_square.place(x=83, y=200)
button_sqr = tk.Button(window, width = 9, height = 2, text = chr(8730))
button_sqr.place(x=162, y=200)
button_div = tk.Button(window, width = 9, height = 2, text = chr(247), font='Arial 9')
button_div.place(x=241, y=200)
button_mlt = tk.Button(window, width = 9, height = 2, text = chr(215), font='Arial 9')
button_mlt.place(x=241, y=250)
button_sbtr = tk.Button(window, width = 9, height = 2, text = chr(8722), font='Arial 9')
button_sbtr.place(x=241, y=300)
button_add = tk.Button(window, width = 9, height = 2, text = chr(43), font='Arial 9')
button_add.place(x=241, y=350)
button_plus_minus = tk.Button(window, width = 9, height = 2, text = chr(43)+'/'+chr(8722), font='Arial 9')
button_plus_minus.place(x=4, y=400)
button_res = tk.Button(window, width = 9, height = 2, text = '=', font='Arial 9', background='blue', foreground='white')
button_res.place(x=241, y=400)

# КНОПКИ ЦИФР
# button_7 = tk.Button(window, width = 9, height = 2, text = '7', command = put_digit(7))
# button_7.place(x=4, y=250)
# button_8 = tk.Button(window, width = 9, height = 2, text = '8', command = put_digit(8))
# button_8.place(x=83, y=250)
# button_9 = tk.Button(window, width = 9, height = 2, text = '9', command = put_digit_9())
# button_9.place(x=162, y=250)
# button_4 = tk.Button(window, width = 9, height = 2, text = '4', command = put_digit(4))
# button_4.place(x=4, y=300)
button_5 = tk.Button(window, width = 9, height = 2, text = '5', command = put_digit(5))
button_5.place(x=83, y=300)
# button_5.config(command = put_digit(5))
# button_6 = tk.Button(window, width = 9, height = 2, text = '6', command = put_digit(6))
# button_6.place(x=162, y=300)
# button_1 = tk.Button(window, width = 9, height = 2, text = '1', command = put_digit(1))
# button_1.place(x=4, y=350)
# button_2 = tk.Button(window, width = 9, height = 2, text = '2', command = put_digit(2))
# button_2.place(x=83, y=350)
# button_3 = tk.Button(window, width = 9, height = 2, text = '3', command = put_digit(3))
# button_3.place(x=162, y=350)
# button_0 = tk.Button(window, width = 9, height = 2, text = '0', command = put_digit(0))
# button_0.place(x=83, y=400)
# button_point = tk.Button(window, width = 9, height = 2, text = ',')#, command = put_digit(','))
# button_point.place(x=162, y=400)

started = True
tk.mainloop()

