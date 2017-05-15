print('名前を入力してください。')
name = input()
print('年齢を入力してください。')
age = int(input())

if name == 'Alice':
    print('やぁ、Alice。')
elif age < 12:
    print('Aliceじゃないね、お嬢ちゃん。')
else:
    print('君はAliceでも子供でもないね。')
