import tkinter as tk

root = tk.Tk()
root.title("expand")

root.geometry("300x250")
label = tk.Label(root, text='fill="y", expand=True, pady=10', relief="groove")

# 横方向拡大 外側余白=5, 外側縦余白=50
label.pack(fill="y", expand=True, pady=10)

root.mainloop()