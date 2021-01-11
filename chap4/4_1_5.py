import tkinter as tk

root = tk.Tk()
root.title("anchor")

root.geometry("300x150")
label1 = tk.Label(root, text="text", relief="groove")
# 指定なし
label1.pack()
label2 = tk.Label(root, text='anchor="se"', relief="groove")
# 東南(右下)
label2.pack(anchor="se")
label3 = tk.Label(root, text="text", relief="groove")
# 指定なし
label3.pack()
label4 = tk.Label(root, text='anchor="nw"', relief="groove")
# 北西(左上)
label4. pack(anchor="nw")

root.mainloop()