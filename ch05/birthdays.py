birthdays = {'アリス': '4/1', 'ボブ': '12/12', 'キャロル': '4/4'}  # ❶

while True:
    print('名前を入力してください: (終了するにはEnterだけ押してください)')
    name = input()
    if name == '':
        break

    if name in birthdays:  # ❷
        print(name + 'の誕生日は' + birthdays[name])  # ❸
    else:
        print(name + 'の誕生日は未登録です。')
        print('誕生日を入力してください:')
        bday = input()
        birthdays[name] = bday  # ❹
        print('誕生日データベースを更新しました。')
