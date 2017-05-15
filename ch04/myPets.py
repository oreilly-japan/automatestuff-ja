my_pets = ['Zophie', 'Pooka', 'Fat-tail']
print('ペットの名前を入力してください:')
name = input()
if name not in my_pets:
    print(name + 'という名前のペットは飼っていません。')
else:
    print(name + 'は私のペットです。')
