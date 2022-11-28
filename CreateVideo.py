import os
import cv2


path = "Images"

images = []


for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    #if ext == '.jpg':
    file_name = path+"/"+file

    print(file_name)
               
    images.append(file_name)
        
print(len(images))
count = len(images)

## frames = cv2.imread(images[0])
##height, width, channel = frames.shape

##size = (width, height)

##out = cv2.VideoWriter("sunset.mp4", cv2.VideoWriter_fourcc(*'DIVX'), 30, size)

##for img in range(count-1, 0, -1):
##    frames = cv2.imread(images[img])
##    out.write(frames)

##out.release()
##print("video is finished!")

