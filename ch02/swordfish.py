while True:
    print('あなたはだれ？')
    name = input()
    if name != 'Joe':  # ❶
        continue  # ❷
    print('こんにちはJoe。パスワードは何？（魚の名前）')
    password = input()  # ❸
    if password == 'swordfish':
        break  # ❹
print('認証しました。')  # ❺
