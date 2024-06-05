import tkinter as tk 
from tkinter import *

window = tk.Tk()
window.title("POKEMON ADVENTURE")

main = PhotoImage(file = "main.png")
label1 = tk.Label(window, image=main)

label2 = tk.Label(window, text = "Mini Map")

minimap = PhotoImage(file = "minimap.png")
label3 = tk.Label(window, image = minimap)

button1 = tk.Button(window, text = "MAP", anchor = "center")
button2 = tk.Button(window, text = "INVENTORY", anchor = "center")
button3 = tk.Button(window, text = "POKEDEX", anchor = "center")
button4 = tk.Button(window, text = "ROSTER",anchor = "center")
button5 = tk.Button(window, text ="JOURNAL",anchor = "center" )
button6 = tk.Button(window, text ="HELP",anchor = "center" )
button7 = tk.Button(window, text = "SHOP",anchor = "center")

logo = PhotoImage(file ="logo.png")
label4 = tk.Label(window,image = logo )

button8 = tk.Button(window, text = "N")
button9 = tk.Button(window, text = "NE")
button10 = tk.Button(window, text = "E")
button11 = tk.Button(window, text = "SE" )
button12 = tk.Button(window, text = "S")
button13 = tk.Button(window, text = "SW")
button14 = tk.Button(window, text ="W")
button15 = tk.Button(window, text = "NW")

label1.place(x = 10 , y = 200)
label2.place(x = 600, y = 200 )
label3.place(x = 600, y = 230)
button1.place(x =600, y = 400)
button2.place(x = 600, y = 425)
button3.place(x = 600, y = 450 )
button4.place(x = 600, y =505)
button5.place(x=600, y = 530)
button6.place(x = 600, y = 555)
button7.place(x = 600, y =480)
label4.place(x = 200, y = 690)
button8.place(x = 50, y =655)
button9.place(x = 70, y = 655)
button10.place(x = 70, y =680 )
button11.place(x = 70, y = 705 )
button12.place( x =50 , y = 705)
button13.place( x = 20, y = 705 )
button14.place(x =20, y = 680)
button15.place(x =20, y = 655 )

window.mainloop()