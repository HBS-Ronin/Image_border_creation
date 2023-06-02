import cv2
import glob
import os
import matplotlib.pyplot as plt

dir = f'/Users/danyalsiddiqui/Pictures/Japan Edited Pictures'
extension = f'/*.jpg'
filenames = dir+extension

asp_ratio = 4/5
inv_asp_ratio = 1/asp_ratio
min_bd_thi = 0.05
border_colour = (255, 255, 255)

jpg_fs = glob.glob(filenames)
len_of_dir = len(dir)+1
pic_list = []
for f in jpg_fs:
    pic_list.append(f[len_of_dir:])


a = cv2.imread(jpg_fs[6])
# max_dim = max(a.shape)
def add_border(file_name, colour):

    a = cv2.imread(file_name)

    if a.shape[0]>a.shape[1]:
        top = bottom = round(min_bd_thi*a.shape[0])
        left = right = round(((2*top + a.shape[0])*inv_asp_ratio - a.shape[1])*0.5) 
    elif a.shape[0]<a.shape[1]:
        left = right = round(min_bd_thi*a.shape[1])
        top = bottom = round(((2*left + a.shape[1])*asp_ratio - a.shape[0])*0.5)
    else:
        top = bottom = round(min_bd_thi*a.shape[0])
        right = left = round(((2*min_bd_thi+1)*a.shape[0]*inv_asp_ratio - a.shape[0])*0.5)

    border_img = cv2.copyMakeBorder(a, top, bottom, left, right, cv2.BORDER_CONSTANT, value = colour)

    return border_img

save_dir = dir+f'/with_borders/'
# os.mkdir(save_dir)


for idx, path in enumerate(jpg_fs):
    img = add_border(path, colour=border_colour)
    cv2.imwrite((save_dir+pic_list[idx]), img)
# b = cv2.copyMakeBorder(a, top, bottom, left, left, cv2.BORDER_CONSTANT, value = (255, 255, 255))
# cv2.imwrite('test_img.jpg', b)
# print(b.shape[0]/b.shape[1])

# plt.imshow(b)
# plt.show()
