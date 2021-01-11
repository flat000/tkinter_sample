import tkinter as tk

root = tk.Tk()
root.title("grid:rowspan, columnspan")
root.geometry("350x170")

frame1 = tk.Frame(root, background="#ece")
frame2 = tk.Frame(root, background="#cec")

# rowspan=2
label11 = tk.Label(frame1, text="r0,c0,rs2", relief="groove")
label11.grid(row=0, column=0, rowspan=2)
label12 = tk.Label(frame1, text="row0,col1", relief="groove")
label12.grid(row=0, column=1)
label13 = tk.Label(frame1, text="row1,col1", relief="groove")
label13.grid(row=1, column=1)
label14 = tk.Label(frame1, text="row2,col1", relief="groove")
label14.grid(row=2, column=1)

# columnspan=3
label21 = tk.Label(frame2, text="+++ r0,c0,cs3 +++", relief="groove")
label21.grid(row=0, column=0, columnspan=3)
label22 = tk.Label(frame2, text="row1,col0", relief="groove")
label22.grid(row=1, column=0)
label23 = tk.Label(frame2, text="row1,col1", relief="groove")
label23.grid(row=1, column=1)
label24 = tk.Label(frame2, text="row1,col2", relief="groove")
label24.grid(row=1, column=2)

frame1.pack(padx=5, pady=5)
frame2.pack(padx=5, pady=5)

root.mainloop()