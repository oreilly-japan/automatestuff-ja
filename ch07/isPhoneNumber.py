def is_phone_number(text):
    if len(text) != 12:  # ❶
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():  # ❷
            return False
    if text[3] != '-':  # ❸
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():  # ❹
            return False
    if text[7] != '-':  # ❺
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():  # ❻
            return False
    return True  # ❼

print('415-555-4242 は電話番号:')
print(is_phone_number('415-555-4242'))
print('Moshi moshi は電話番号:')
print(is_phone_number('Moshi moshi'))

#message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
message = '明日415-555-1011に電話してください。オフィスは415-555-9999です。'
for i in range(len(message)):
    chunk = message[i:i+12]   # ❶
    if is_phone_number(chunk):  # ❷
      print('電話番号が見つかりました: ' + chunk)
print('完了')

