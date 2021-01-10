import tkinter as tk

root = tk.Tk()
strvar = tk.StringVar()
en = tk.Entry(textvariable=strvar)
en.pack()
root.mainloop()