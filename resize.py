import cv2
import os
import numpy as np
for a in range(60,361):
    filename = 'D:\\\\Anh\\\\Python\\\\trung\\\\data\\\\500000\\\\' + str(a) +'.png'
    print(a)
    path = 'D:\\\\Anh\\\\Python\\\\trung\\\\data2\\\\500000\\\\' + str(a) +'.jpg'
    print(a)
    frame = cv2.imread(filename)
    print(a)
    cv2.imwrite(path,frame)
    print(a)
    cv2.waitKey(0)
    print(a)
print('Done file')

