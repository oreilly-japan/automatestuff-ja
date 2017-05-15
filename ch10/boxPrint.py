def box_print(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('symbolは1文字の文字列でなければならない。')  # ❶
    if width <= 2:
        raise Exception('widthは2より大きくなければならない。')  # ❷
    if height <= 2:
        raise Exception('heightは2より大きくなければならない。')  # ❸
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)

for sym, w, h in (('*', 4, 4), ('O', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
    try:
        box_print(sym, w, h)
    except Exception as err:  # ❹
        print('例外が起こりました: ' + str(err))  # ❺
