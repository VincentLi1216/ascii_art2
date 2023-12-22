import cv2

try:
    img_path = util.read_file_from_finder()

    img = cv2.imread(img_path)
except:
    pass
