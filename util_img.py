import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

import util

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


def text_sorter(text, to_show=False):
    sorted_text = []
    zipped_lists = []

    for char in ascii_text:
        dark_pixel_count = dark_pixel_counter(char) 
        zipped_lists.append((dark_pixel_count, char))
    
    sorted_list = sorted(zipped_lists)
    sorted_num, sorted_text = zip(*sorted_list)

    normalized_num = util.mapping(sorted_num, 0, 255)

    if to_show:
        print(f"zipped_lists: {zipped_lists}")
        print(f"sorted_list: {sorted_list}")
        print(f"sorted_text: {sorted_text}")
        print(f"normalized_num: {normalized_num}")
        for text in sorted_text:
            print(text*100)

    return dict(zip(normalized_num, sorted_text))

def return_text_by_number(darkness_dict, darkness):
    ans = util.find_closest(darkness_dict.keys(), darkness)
    return darkness_dict[ans]

def resize(img, new_width, ratio_constant=0.17):
    orig_height, orig_width = img.shape
    new_height = int(new_width*orig_height*ratio_constant/orig_width)
    new_size = (new_width, new_height)
    resized_img = cv2.resize(img, new_size)
    return resized_img





if __name__ == "__main__":

    ascii_text = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
    # util.json_writer(text_sorter(ascii_text), "./darkness_dict.json")
    

    darkness_dict = util.json_reader("./darkness_dict.json")
    print(darkness_dict)
    print(return_text_by_number(darkness_dict, 218))
    
        
