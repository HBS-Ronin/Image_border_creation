import cv2
import glob

#####Selecting Directory for the images######
dir = f'/Users/danyalsiddiqui/Pictures/Japan Edited Pictures' #The folder your pictures are in
extension = f'/*.jpg' #pic extension
filenames = dir+extension

##### Directory for saving images with borders ######
save_dir = dir+f'/with_borders/'

####Declaring key variables####
asp_ratio = 4/5  #apect ratio for the final picture
inv_asp_ratio = 1/asp_ratio
min_bd_thi = 0.05 #the minimum border thickness as a percentage of the greatest dimmesnion of the picture 
border_colour = (255, 255, 255) #The border colour in RGB

###Getting the full paths for images and and the file names for images######
jpg_fs = glob.glob(filenames)

len_of_dir = len(dir)+1
pic_list = []
for f in jpg_fs:
    pic_list.append(f[len_of_dir:])



def add_border(file_name, colour):
    """
    Arguments: File name and the border colour in (R, G, B) int values
    Returns: Image with border
    """

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



### calling the add_border function for each file path and saving the resultant image with borders in the save_dir####
for idx, path in enumerate(jpg_fs):
    img = add_border(path, colour=border_colour)
    cv2.imwrite((save_dir+pic_list[idx]), img)

