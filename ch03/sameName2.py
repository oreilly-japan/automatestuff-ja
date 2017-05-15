def spam():
    global eggs   # ❶
    eggs = 'spam' # ❷

eggs = 'global'
spam()
print(eggs)
