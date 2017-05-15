#! python3
# mcb.pyw - クリップボードのテキストを保存・復元
# Usage:
# py.exe mcb.pyw save <keyword> - クリップボードをキーワードに紐づけて保存 ❶
# py.exe mcb.pyw <keyword> - キーワードに紐づけられたテキストをクリップボードにコピー
# py.exe mcb.pyw list - 全キーワードをクリップボードにコピー

import shelve, pyperclip, sys  # ❷

mcb_shelf = shelve.open('mcb')  # ❸

# クリップボードの内容を保存
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':  # ❶
    mcb_shelf[sys.argv[2]] = pyperclip.paste()  # ❷
elif len(sys.argv) == 2:
    # キーワード一覧と、内容の読み込み
    if sys.argv[1].lower() == 'list':  # ❶
        pyperclip.copy(str(list(mcb_shelf.keys())))  # ❷
    elif sys.argv[1] in mcb_shelf:
        pyperclip.copy(mcb_shelf[sys.argv[1]])  # ❸

mcb_shelf.close()
