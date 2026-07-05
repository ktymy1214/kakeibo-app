# 家計簿アプリ
import json
import os
print("===家計簿アプリ===")

# 支出の入力
def add_expense():
    date = input("日付を入力してください(YYYY/MM/DD)")
    amount = int(input("金額を入力してください。(半角数字)"))
    category = input("カテゴリーを入力してください。(食費／光熱費／教育費／雑費など)")
    memo = input("メモを入力してください(ラーメン／電気代／国語ドリルなど)")
    # 辞書形式で返す
    expense = {
        "date": date,
        "amount": amount,
        "category": category,
        "memo": memo
    }

    print("登録しました。")    
    return expense

# 支出の保存（Jsonファイル）
def save_expense(expense):
    FILE_NAME = 'data/expenses.json'
    # 空ファイルの場合は空の辞書を登録
    if os.path.getsize(FILE_NAME) == 0:
        with open(FILE_NAME, 'w', encoding='utf-8') as file:
            json.dump([], file)
    # 保存ファイル読み込み
    with open(FILE_NAME,'r', encoding='utf-8') as file:
        loaded_data = json.load(file)
    # 辞書データの追加
    loaded_data.append(expense)
    # ファイル保存
    with open(FILE_NAME,'w', encoding='utf-8') as file:
        json.dump(loaded_data, file, ensure_ascii=False, indent=2)

# メイン処理
while True :
    # メニュー表示
    print("\nメニュー")
    print("1.支出を登録")
    print("2.支出一覧")
    print("0.終了")

    choice = input ("選択してください\n")

    if choice == "0": # 終了
        print("アプリを終了します。")
        break
    elif choice == "1": # 支出の登録
    #    print ("支出登録は未実装です。")
        expenses=add_expense()
        save_expense(expense)
    elif choice == "2": # 支出一覧の表示
        print("支出一覧は未実装です。")
    else:
        print("0,1,2 のいずれかを入力してください。")

