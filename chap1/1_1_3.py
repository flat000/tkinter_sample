import tkinter as tk

def action_btn_press():
    print("ボタンが押されました")

root = tk.Tk()
root.title("アクションの組み込み")
root.geometry("350x150")
lb = tk.Label(text="ラベル")

#commandオプションに関数名を指定
bt = tk.Button(text="ボタン", command = action_btn_press)
lb.pack()
bt.pack()
root.mainloop()