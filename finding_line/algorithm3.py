#na zaklade priemeru

import numpy as np
import cv2

img = cv2.imread('C:\\Users\\matej\\Desktop\\TIS\\profilometry\\images\\fisrt_scans\\480-145154.jpg')

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(img, 100,200)

lines = cv2.HoughLinesP(edges,rho=1, theta = 1*np.pi/180, threshold =100, minLineLength=100, maxLineGap=50)

y_threshold = 10

first_line = []
second_line = []

for line in lines:
    if len(first_line) == 0:
        first_line.append(line)
    else:
            # print("---------")
            # print(new_lines[0][0][1])
            # print(line[0][1])
            # print(abs(new_lines[0][0][1] - line[0][1]))
            # print("---------")
            if abs(line[0][1] - first_line[0][0][1]) > y_threshold:
                second_line.append(line)
            else:
                first_line.append(line)

avg_f_l = 0
for i in first_line:
    avg_f_l+=i[0][1]

avg_s_l = 0
for i in second_line:
    avg_s_l+=i[0][1]

cv2.line(img, (0, avg_f_l//len(first_line)), (1500,avg_f_l//len(first_line)), (200,120,100),3)
cv2.line(img, (0, avg_s_l//len(second_line)), (1500,avg_s_l//len(second_line)), (200,120,100),3)

cv2.imshow("window", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

