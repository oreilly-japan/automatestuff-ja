def spam():
    print(eggs)  # エラー！
    eggs = 'spam local'  # ❶

eggs = 'global'  # ❷
spam()
