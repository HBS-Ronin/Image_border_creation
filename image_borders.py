import cv2
import glob
import matplotlib.pyplot as plt

dir = f'/Users/danyalsiddiqui/Pictures/Japan Edited Pictures'
extension = f'/*.jpg'
filenames = dir+extension

jpg_fs = glob.glob(filenames)

a = cv2.cvtColor(cv2.imread(jpg_fs[0]), cv2.COLOR_BGR2RGB)
b = cv2.copyMakeBorder(a, 200, 200, 200, 200, cv2.BORDER_CONSTANT, value = (255, 255, 255))

plt.imshow(b)
plt.show()
