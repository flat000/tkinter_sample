import tkinter as tk
# スクロール付きテキストボックスのインポート
import tkinter.scrolledtext as tksc

root = tk.Tk()
# 縦スクロール付きテキストエリア
st = tksc.ScrolledText(width=30, height=5)
st.pack()
root.mainloop()

