# このプログラムは挨拶を表示して名前と年齢を尋ねる ❶
    
print('Hello world!')  # ❷
print('What is your name?') # 名前を尋ねる
my_name = input()  # ❸
print('It is good to meet you, ' + my_name)  # ❹
print('The length of your name is:')  # 名前の長さを表示 ❺
print(len(my_name))
print('What is your age?') # 年齢を尋ねる ❻
my_age = input()
print('You will be ' + str(int(my_age) + 1) + ' in a year.') # 来年の年齢を表示
