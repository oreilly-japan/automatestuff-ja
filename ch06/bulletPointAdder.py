#! python3
# bulletPointAdder.py - クリップボードのテキストの各行に
# 点を打って、Wikipediaの箇条書きにする

import pyperclip
text = pyperclip.paste()

# 行を分割して、'*'を追加する
lines = text.split('\n')
for i in range(len(lines)):    # "lines"リストの各要素をループする
    lines[i] = '* ' + lines[i] # "lines"の要素に"* "を追加する

text = '\n'.join(lines)

pyperclip.copy(text)

