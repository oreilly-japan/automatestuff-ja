#! python3
# resizeAndAddLogo.py - カレントディレクトリのすべての画像を300x300に収まる
#                       ようにサイズ変更し、catlogo.pngを右下に追加する。

import os
from PIL import Image

SQUARE_FIT_SIZE = 300               # ❶
LOGO_FILENAME = 'catlogo.png'       # ❷

logo_im = Image.open(LOGO_FILENAME)  # ❸
logo_width, logo_height = logo_im.size # ❹

os.makedirs('withLogo', exist_ok=True)

# カレントディレクトリの全画像をループする
for filename in os.listdir('.'):  # ❶
    if not (filename.endswith('.png') or filename.endswith('.jpg')) \
       or filename == LOGO_FILENAME:  # ❷
        continue # 画像以外とロゴ画像はスキップする  # ❸
    im = Image.open(filename)  # ❹

    # 画像をサイズ変更する
    im.thumbnail((SQUARE_FIT_SIZE, SQUARE_FIT_SIZE))
    width, height = im.size

    # ロゴを追加する
    print('ロゴを追加中 {}...'.format(filename))   # ❶
    im.paste(logo_im, (width-logo_width, height-logo_height), logo_im)  # ❷

    # 変更を保存する
    im.save(os.path.join('withLogo', filename))  # ❸


