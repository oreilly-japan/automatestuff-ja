#! python3
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont
import os

FONT_DIR = r'C:\Windows\Fonts'
EXAMPLE = '愛Uniqフォント'
FONT_SIZE = 16

fonts = []
for fname in os.listdir(FONT_DIR):
    if fname.endswith('.ttf') or fname.endswith('.ttc'):
        fonts.append(fname)

im = Image.new('RGBA', (750, len(fonts) * FONT_SIZE), 'white')
draw = ImageDraw.Draw(im)

y = 0
for font in fonts:
    draw.text((0, y), font, fill='red')
    for i in range(0, 4):
        try:
            f = ImageFont.truetype(font, FONT_SIZE, index=i)
            draw.text((150 + 150*i, y), EXAMPLE, fill='black', font=f)
        except:
            pass
    y += FONT_SIZE
        
im.save('fontlist.png')
