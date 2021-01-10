import tkinter as tk

root = tk.Tk()
lb = tk.Label(text="MSゴシック, サイズ20, 太字でない, 斜体, 下線なし, 取消線あり", font=("MSゴシック", 20, "normal", "italic", "normal", "overstrike"))
lb.pack()

root.mainloop()