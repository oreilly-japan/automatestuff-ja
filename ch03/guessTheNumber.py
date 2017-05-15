# 数当てゲーム
import random
secret_number = random.randint(1, 20)
print('1から20までの数を当ててください。')

# 6回聞く
for guesses_taken in range(1, 7):
    print('数を入力してください。')
    guess = int(input())

    if guess < secret_number:
        print('小さいです。')
    elif guess > secret_number:
        print('大きいです。')
    else:
        break # 当たり！

if guess == secret_number:
    print('当たり！' + str(guesses_taken) + '回で当たりました！')
else:
    print('残念。正解は' + str(secret_number) + 'でした。')
