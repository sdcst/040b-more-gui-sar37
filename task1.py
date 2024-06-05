import tkinter as tk 
from tkinter import *
from tkinter import ttk


window = tk.Tk()
window.title("tk")

label1 = tk.Label(window, text = "Principal")
label2 = tk.Label(window, text = "Interest Rate")
label3 = tk.Label(window, text = "Years")

entry1 = tk.Entry(window, text = "")
entry2 = tk.Entry(window, text ="")
combo = ttk.Combobox(window,values=["1","2","3"])
label4 = tk.Label(window, text = "-")

label5 = tk.Label(window, text = "Amount")
entry5 = tk.Entry(window, text = "")

label1.grid(row =1,column = 1 )
label2.grid(row= 1, column = 2)
label3.grid(row = 1, column = 3)
entry1.grid(row =2 ,column =1)
entry2.grid(row = 2, column = 2)
combo.grid(row = 2, column = 3)
label4.grid(row = 3,column = 1)
label5.grid(row = 5, column = 1)
entry5.grid(row=5, column =2)

window.mainloop()