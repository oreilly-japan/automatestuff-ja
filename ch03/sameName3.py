def spam():
    global eggs    # ❶
    eggs = 'spam'  # グローバル変数になる

def bacon():
    eggs = 'bacon' # ローカル変数になる ❷

def ham():
    print(eggs)    # グローバル変数になる ❸

eggs = 42          # グローバル変数になる
spam()
print(eggs)
