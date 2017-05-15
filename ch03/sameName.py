def spam():
    eggs = 'spam local'  # ❶
    print(eggs) # 'spam local'を表示

def bacon():
    eggs = 'bacon local' # ❷
    print(eggs) # 'bacon local'を表示
    spam()
    print(eggs) # 'bacon local'を表示

eggs = 'global'          # ❸
bacon()
print(eggs)     # 'global'を表示
