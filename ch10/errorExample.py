def spam():
    bacon()

def bacon():
    raise Exception('これはエラーメッセージです。')

spam()
