import os,sys

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog

# 自作モジュールをインポート
from nums_kind_mkdirs import *

# ユーザーがディレクトリを指定する関数
def dirdialog_clicked():
    iDir = os.path.abspath(os.path.dirname(sys.argv[0]))
    iDirPath = filedialog.askdirectory(initialdir = iDir)
    entry1.set(iDirPath)

# 実行ボタン押下時の実行関数
def conductMain():
    text = ""

    # ユーザーが入力した情報を取得
    dirPath = entry1.get() 
    input_dir_name = entry2.get()
    input_dir_count = entry3.get()

    # 入力条件を満たさなかったとき、エラーハンドリングで警告メッセージを表示
    try:
        if dirPath:
            if int(input_dir_count) <= 100:
                if co.get() != 'SERECT':
                    if co.get() == '01-xx':
                        mkdir_nums(dirPath, input_dir_name, input_dir_count)
                    elif co.get() == 'No.1-No.xx':
                        mkdir_numbers(dirPath, input_dir_name, input_dir_count)
                    elif co.get() == '英語表記(One~)':
                        mkdir_eng_nums(dirPath, input_dir_name, input_dir_count)
                    elif co.get() == '漢数字(一~)':
                        mkdir_kansuuji(dirPath, input_dir_name, input_dir_count)
                    elif co.get() == 'ローマ数字(I~)':
                        mkdir_roman_numbers(dirPath, input_dir_name, input_dir_count)
                    else:
                        pass
                    text += dirPath
                else:
                    messagebox.showwarning("警告", "数字の表記が選択されていません")
            else:   
                messagebox.showwarning("警告", "最大、100個までのフォルダを作成することが可能です")
        # 3つの項目の入力欄に何も入力されてないとき、エラーメッセージを表示
        elif not dirPath and not input_dir_name and not input_dir_count:
            messagebox.showerror("エラー", "何も入力されていません")
        else:  
            messagebox.showerror("エラー", "パスの指定がありません。")

    # フォルダの作成個数入力欄が半角英数字以外のとき、エラーメッセージを表示
    except ValueError:
        messagebox.showerror("エラー", "半角英数字で数字を入力してください")
    # 同一のフォルダが存在しているとき、エラーメッセージを表示
    except FileExistsError:
        messagebox.showwarning("警告", "既に同じ名前のフォルダが存在します")

    # 100個以下のディレクトリが生成されたら、作成メッセージを表示
    if text:
        messagebox.showinfo("フォルダ作成情報", "{}個のフォルダが作成されました!".format(input_dir_count))

if __name__ == "__main__":

    # rootの作成
    root = Tk()
    root.title("自動フォルダ作成ツール")

    # アイコンデータ(Base64)
    data = '''
    R0lGODlhIAAgAPcAADqD0juD0juE0jyE0z6G0z+G00GI1EKI1EOJ1ESJ1EWK1EaK
    1EaK1UmM1UqN1UiM1kmN1kqN1kuN1kyO1k+Q11GR11KS11OT2FSU2FWU2FWV2FaU
    2FaV2FaU2VeV2ViW2VmX2VqX2luY2VyY2l2Z2mCb2mCb22Gb22Od22Sd22Se3Gmg
    3Gmh3Gmh3Wui3Wqh3m6j3m6k3nGm33On3nWo33iq4Hir4Xqs4X2t4X+u4oKx4oWy
    44ez44e05Iq25Iu25Iy25Iy35Y245Y645Y+45ZC55ZG55ZG55pa955e96Jm/6JvA
    6JzA6J3C6J7C6J/C6J/D6J7C6aHD6aHE6aTG6qXG6qbH66fH66jI7KnJ7KzL7K3M
    7a/M7bLP7rTP7bbQ7bbR77jS7r3V8L7W8L/X8cLZ8cPZ8cPa8cPa8sXa8sjc8srd
    883f88zf9M3g887h88/h9M/h9dDh9NHi9dPj9dXk9dXl9dbl9tfm9tjm9dnn9djm
    9tjn9tnn9trn9tno9tro9t7p993q99/r99/r+OHs+ODs+ePt+OXv+ebv+ebw+ujw
    +ujx+unx+uvy+uzz+uzz++7z++71++/1+/L3/PP3/Pf6/ff6/vn7/fn7/vr8/vv9
    /vv9//7+/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    AAAAAAAAAAAAAAAAACH5BAEAAJ4ALAAAAAAgACAAAAj+AD0JHEiwoMGDCBMqXMiw
    ocOHnvrgGMGEEcSFclpUqHhRYcaNFjsS3CSIC5MdFSrsYMJSpMBFTCoAmElzJpwi
    MlzMWPJnU0NIVzbUnIngwxACNCP8IHTxI0dPPYYygGGEpdWrTKSEIaRJoNOQUSAM
    HUsWAAo0Xb8K9OKhrNuZEYAM8iSpzJdAnASuSUE2AYsnZ9wIHjyYTqJMB/3kSDBU
    ApFCLj01gnKhJgIbcyKZGZLThefPoEHTcHLnEpkTNS004bMlxNuyDVp4ynPjAM0T
    Y+z0ePCarIISnhAhoTBTgY47aVQI6D22QxJPlcCQmJmByp6gzIcGeMFGYB0aBQB/
    qDijx4fY7DQdDIHs6dCRCcbxqFkxAD1NEV0oCZykBUSGKoBk0ZZ9ABhQAx4DdRJH
    DBxM0YYQDhAIAAVKKEKQIUE0oAAGCkgIgAliWELQI1gM6OECOwhSkCbJLeehBlY4
    YhAh5nlowAxv+FQQJnXwEKF9CtBAhn6RFWnkkQgFBAA7
    '''

    # アイコンの設置
    root.tk.call('wm', 'iconphoto', root._w, PhotoImage(data=data))

# ========================================================================================================
    # Frame1の作成
    frame1 = ttk.Frame(root, padding=10, relief="groove")
    frame1.grid(row=0, column=1, padx=10, pady=10, ipadx=20, sticky=E)

    # 「フォルダ参照」ラベルの作成
    IDirLabel = ttk.Label(frame1, text="フォルダ参照＞＞", padding=(25, 5, 5, 0))
    IDirLabel.pack(side=LEFT)

    # 「フォルダ参照」エントリーの作成
    entry1 = StringVar()
    IDirEntry = ttk.Entry(frame1, textvariable=entry1, width=30)
    IDirEntry.pack(side=LEFT)

    # 「フォルダ参照」ボタンの作成
    IDirButton = ttk.Button(frame1, text="参照", command=dirdialog_clicked)
    IDirButton.pack(side=LEFT)

# ========================================================================================================
    # frame2の作成
    frame2 = ttk.Frame(root, padding=10)
    frame2.grid(row=2, column=1, sticky=E)

    # 「フォルダ名:」ラベルの作成
    IFileLabel = ttk.Label(frame2, text="フォルダ名:", padding=(5, 0))
    IFileLabel.pack(side=LEFT)

    # 「フォルダ名」エントリーの作成
    entry2 = StringVar()
    IFileEntry = ttk.Entry(frame2, textvariable=entry2, width=20)
    IFileEntry.pack(side=LEFT)

    IFileLabel = ttk.Label(frame2, text="__")
    IFileLabel.pack(side=LEFT)

    # 「番号:」ラベルの作成
    IFileLabel = ttk.Label(frame2, text="No.", padding=(5, 0))
    IFileLabel.pack(side=LEFT)

    # 「フォルダ番号」エントリーの作成
    entry3 = StringVar()
    IFileEntry = ttk.Entry(frame2, textvariable=entry3, width=10)
    IFileEntry.pack(side=LEFT, padx=0)

    # 「まで」ラベルの作成
    IFileLabel = ttk.Label(frame2, text="まで", padding=(0, 5, 8, 5))
    IFileLabel.pack(side=LEFT)

    # コンボボックスの作成
    nums_kind = ["SERECT", "01-xx", "No.1-No.xx", "英語表記(One~)", "漢数字(一~)", "ローマ数字(I~)"]
    co = ttk.Combobox(frame2, state="readonly", values=nums_kind, width=12)
    co.set(nums_kind[0])
    co.pack(side=LEFT, padx=(2, 10))

# ========================================================================================================
    # Frame3の作成
    frame3 = ttk.Frame(root, padding=10)
    frame3.grid(row=4,column=1,sticky=W)

    # 実行ボタンの設置
    button1 = ttk.Button(frame3, text="作成", command=conductMain)
    button1.pack(fill = "x", padx=85, side = "left")

    # キャンセルボタンの設置
    button2 = ttk.Button(frame3, text=("閉じる"), command=root.quit)
    button2.pack(fill = "x", padx=30, side = "left")

    root.mainloop()