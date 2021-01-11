import tkinter as tk

root = tk.Tk()
root.title("fill")

root.geometry("300x150")
label = tk.Label(root, text='fill="x", padx=5, pady=50', relief="groove")

# 横方向拡大 外側余白=5, 外側縦余白=50
label.pack(fill="x", padx=5, pady=50)

root.mainloop()