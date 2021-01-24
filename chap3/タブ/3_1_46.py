import tkinter as tk
#1, tkinter内のttkクラスをインポート
import tkinter.ttk as ttk

def press_button1():
    label1["text"] = "pressed button1"

def press_button2():
    label2["text"] = "pressed button2"

# タブ切り替え時のコールバック
def chg_tab(event):
    print(notebook.select())

root = tk.Tk()
root.geometry("300x150")
root.title("Notebook")
#2. Notebookオブジェクトを作成
notebook = ttk.Notebook(root)
#3. タブとなるフレームを作成
tab1 = tk.Frame(notebook)
tab2 = tk.Frame(notebook)
#4. Notebookにタブを追加
notebook.add(tab1, text="tab1")
notebook.add(tab2, text="tab2")
# ウィンドウサイズが変わった時用にタブのレスポンシブを有効
notebook.pack(expand=True, fill="both")
# tab1をマスターとしたウィジェット
label1 = tk.Label(tab1, text="tab1 label")
button1 = tk.Button(tab1, text="tab1 button1", command=press_button1)
# tab2をマスターとしたウィジェット
label2 = tk.Label(tab2, text="tab2 label2")
button2 = tk.Button(tab2, text="tab2 button2", command=press_button2)
[widget.pack(pady=10) for widget in (label1, button1, label2, button2)]

# Notebookの持っているタブID(ウィジェット名)
tabids = notebook.tabs()
print(tabids)
# 現在の選択されているタブID(ウィジェット名)
print(notebook.select())
# タブ切り替え時のコールバック
notebook.bind("<<NotebookTabChanged>>", chg_tab)
# 2番目のタブを選択
notebook.select(tabids[1])
print(notebook.select())

root.mainloop()