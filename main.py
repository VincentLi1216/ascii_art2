import cv2

import util, util_img

darkness_dict = util.json_reader("./darkness_dict.json")

try:
    img_path = util.read_file_from_finder()

    img = cv2.imread(img_path,cv2.IMREAD_GRAYSCALE)
    img = util_img.resize(img, 1700)
    img_height, img_width = img.shape

    for i in range(img_height):
        print("\n")
        for j in range(img_width):
            brightness = img[i][j]
            print(util_img.return_text_by_number(darkness_dict, brightness), end="")
    # cv2.imshow("my img", img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
except Exception as error:
    # handle the exception
    print("An exception occurred:", error) # An exception occurred: division by zero
