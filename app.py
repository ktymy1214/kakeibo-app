print("===家計簿アプリ===")

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
        print ("支出登録は未実装です。")
    elif choice == "2":
        print("支出一覧は未実装です。")
    else:
        print("0,1,2 のいずれかを入力してください。")
