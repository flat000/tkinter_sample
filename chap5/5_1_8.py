import tkinter as tk

def callback_func(event):
    label["text"] = "x:{0},y:{1}".format(event.x, event.y)

root = tk.Tk()
root.geometry("300x200")
root.title("mouse motion button3")
label = tk.Label(root, text="mouse motion button3", relief="groove")

# マウスボタンを押しながら移動のイベント(右or中ボタン)
root.bind("<Button3-Motion>", callback_func)
label.pack()
root.mainloop()