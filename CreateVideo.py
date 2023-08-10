import os
import cv2

path="images"

img=[]

for file in os.listdir(path):
    name, ext= os.path.splitext(file)

    if ext in ["jpg"]:
        file_name=path+"/"+file_name

        print(file_name)

        img.append(file_name)

count=len(img)

frame=cv2.imread(img[0])
height,width,channels=frame.shape
size=(width,height)
out=cv2.VideoWriter("project.avi",cv2.VideoWriter_fourcc(*'DIVX'),0.8,size)

for i in range(0,count-1):
    frame=cv2.imread(img[i])
    out.write(frame)

out.release()
print("Done!")