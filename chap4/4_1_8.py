import tkinter as tk

root = tk.Tk()
root.title("grid:sticky")
root.geometry("340x140")

frame1 = tk.Frame(root, background="#eee")
frame2 = tk.Frame(root, background="#eee")
# rowspan=2
label11 = tk.Label(frame1, text="r0,c0,rs2", relief="groove")
# sticky=tk.N+tk.S のようにも書ける、上から下
label11.grid(row=0, column=0, rowspan=2, sticky="ns")
label12 = tk.Label(frame1, text="row0,col1", relief="groove")
label12.grid(row=0, column=1)
label13 = tk.Label(frame1, text="row1,col1", relief="groove")
label13.grid(row=1, column=1)
label14 = tk.Label(frame1, text="row2,col1", relief="groove")
label14.grid(row=2, column=1)

# columnspan=3
label21 = tk.Label(frame2, text="+++ r0,c0,cs3 +++", relief="groove")
# sticky=tk.W+tk.E のようにも書ける、左から右
label21.grid(row=0, column=0, columnspan=3, sticky="we")
label22 = tk.Label(frame2, text="row1,col0", relief="groove")
label22.grid(row=1, column=0)
label23 = tk.Label(frame2, text="row1,col1", relief="groove")
label23.grid(row=1, column=1)
label24 = tk.Label(frame2, text="row1,col2", relief="groove")
label24.grid(row=1, column=2)

frame1.pack(padx=5, pady=5)
frame2.pack(padx=5, pady=5)

root.mainloop()