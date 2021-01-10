import tkinter as tk

root = tk.Tk()
root.geometry("300x150")
root.title("LabelFrame relief")

frame1 = tk.LabelFrame(root, text="flat", relief="flat", width=60, height=40)
frame2 = tk.LabelFrame(root, text="raised", relief="raised", width=60, height=40)
frame3 = tk.LabelFrame(root, text="sunken", relief="sunken", width=60, height=40)
frame4 = tk.LabelFrame(root, text="groove", relief="groove", width=60, height=40)
frame5 = tk.LabelFrame(root, text="ridge", relief="ridge", width=60, height=40)

frame1.grid(column=0, row=0)
frame2.grid(column=1, row=0)
frame3.grid(column=2, row=0)
frame4.grid(column=0, row=1)
frame5.grid(column=1, row=1)

root.mainloop()