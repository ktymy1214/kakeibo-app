print("===家計簿アプリ===")

def add_expense():
    date = input("日付を入力してください(YYYY/MM/DD)")
    amount = input("金額を入力してください。(半角数字)")
    category = input("カテゴリーを入力してください。(食費／光熱費／教育費／雑費など)")
    memo = input("メモを入力してください(ラーメン／電気代／国語ドリルなど)")

    print("登録しました。")    

while True :
    print("\nメニュー")
    print("1.支出を登録")
    print("2.支出一覧")
    print("0.終了")

    choice = input ("選択してください")

    if choice == "0":
        print("アプリを終了します。")
        break
    elif choice == "1":
    #    print ("支出登録は未実装です。")
        add_expense()
    elif choice == "2":
        print("支出一覧は未実装です。")
    else:
        print("0,1,2 のいずれかを入力してください。")

