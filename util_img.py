import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

def dark_pixel_counter(text):

    img = np.zeros((255, 255), dtype=np.uint8)
    img.fill(255)

    font_path = "./MesloLGS_NF_Bold.ttf"

    # 載入字體
    font = ImageFont.truetype(font_path, 192)

    # 將 NumPy 陣列轉為 PIL 影像
    imgPil = Image.fromarray(img)

    # 在圖片上加入文字
    draw = ImageDraw.Draw(imgPil)
    draw.text((30, 30),  text, font = font, fill = 0)


    # 將 PIL 影像轉回 NumPy 陣列
    img = np.array(imgPil)

    # 方法一：直接計算值為 0 的像素數量
    black_pixels_count = np.sum(img == 0)
    # print(black_pixels_count)
    return black_pixels_count



if __name__ == "__main__":

    text = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'

    for char in text:
        print(char, dark_pixel_counter(char))


