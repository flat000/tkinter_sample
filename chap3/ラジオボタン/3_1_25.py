import tkinter as tk

def get_rdval():
    # 選択値を取得する
    print(intvar.get())
    print(strvar.get())

root = tk.Tk()
root.geometry("150x150")
root.title("Radiobutton")
intvar = tk.IntVar()
strvar = tk.StringVar()
# 初期値をセット
intvar.set(0)
strvar.set("0")
# ラジオボタンを作成 1つ目のグループ
rd1 = tk.Radiobutton(text="ラジオ1", value=1, variable=intvar)
rd2 = tk.Radiobutton(text="ラジオ2", value=2, variable=intvar)
# ラジオボタンを作成 2つ目のグループ
rdabc = tk.Radiobutton(text="ラジオABC", value="abc", variable=strvar)
rddef = tk.Radiobutton(text="ラジオDEF", value="def", variable=strvar)
bt = tk.Button(text="選択値を出力", command=get_rdval)
[widget.pack() for widget in (rd1, rd2, rdabc, rddef, bt)]
root.mainloop()