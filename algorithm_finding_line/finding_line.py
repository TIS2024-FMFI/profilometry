import numpy as np
import cv2
import os

class HladanieCiary():
    '''
    Pre aplikovanie noveho algoritmu, vo funkcii aplikuj_na_subor treba dat algoritmus = 1. algoritmus =2 je stary algoritmus.
    Pre aplikovanie na cely subor fotiek, treba nastavit path, kde sa fotky nachadzaju, a out_path, kde chceme fotky ulozit a je
    potrebne vytvorit tento subor.
    '''
    def __init__(self,path,out_path = "",zobraz = False, pripona = 'jpg'):
        self.path = path
        self.out_path = out_path
        self.zobraz = zobraz
        self.pripona = pripona
    
    def hladaj_ciaru_alg1(self, path):
        img = cv2.imread(path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        height, width = img.shape
        #print(f"Výška: {height}, Šírka: {width}")


        najvacsie = []

        prvy = 0

        cl = 0
        for col in range(width):
            column_pixels = img[:, col]
            if max(column_pixels) > 80: #150
                if prvy ==0:
                    prvy = np.argmax(column_pixels)
                najvacsie.append((col, np.argmax(column_pixels)))
                #print(np.argmax(column_pixels))
            
                cl+=1

        new_img = np.zeros((height, width, 3), dtype=np.uint8)


        #print(prvy)

        referencna = []
        priem  =0
        objekt = []
        for i in najvacsie:
            if abs(i[1]-prvy) < 20: #20
                referencna.append(i)
                priem+=i[1]
            else:
                if (i[1] > prvy):
                    objekt.append(i)
                
        # points = np.array(najvacsie, dtype=np.int32)
        # cv2.polylines(new_img, [points], isClosed=False, color=(0, 0, 255), thickness=2)

        cv2.line(new_img, (0, priem//len(referencna)), (img.shape[1],priem//len(referencna)), (200,120,100),3)

        body = np.array(objekt, np.int32)
        # print(body)
        # cv2.polylines(new_img, [body], isClosed=False, color=(0, 0, 255), thickness=2)

        #print(body)
        for i in objekt:
            cv2.circle(new_img, (i[0], i[1]), radius=2, color=(0, 0, 255), thickness=-1)
        
        return new_img
  
    def hladaj_ciaru_alg2(self, path):
        img = cv2.imread(path)

        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(img, 100,200)

        lines = cv2.HoughLinesP(edges,rho=1, theta = 1*np.pi/180, threshold =100, minLineLength=100, maxLineGap=50)

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
                    if abs(line[0][1] - first_line[0][0][1]) > 10:
                        second_line.append(line)
                    else:
                        first_line.append(line)

        if first_line[0][0][1] > second_line[0][0][1]:
            pom = first_line
            first_line = second_line
            second_line = pom
            

        avg_f_l = 0
        for i in first_line:
            avg_f_l+=i[0][1]

        avg_s_l = 0
        for i in second_line:
            avg_s_l+=i[0][1]

        cv2.line(img, (0, avg_f_l//len(first_line)), (1500,avg_f_l//len(first_line)), (200,120,100),3)
        cv2.line(img, (0, avg_s_l//len(second_line)), (1500,avg_s_l//len(second_line)), (200,120,100),3)
        
        return img
    
    def vykresli(self):
        img = self.hladaj_ciaru_alg1(self.path)
        cv2.imshow("window", img)
        cv2.waitKey(0)
    
    def aplikuj_na_subor(self, algoritmus):
        directory = self.path
        for filename in os.listdir(directory):
            if filename.endswith("."+self.pripona):
                #print(filename)
                file_path = os.path.join(directory, filename)
                try:
                    output_file = os.path.join(self.out_path, filename)
                    
                    if algoritmus == 1:
                        img = self.hladaj_ciaru_alg1(file_path)
                        
                    if algoritmus == 2:
                        img = self.hladaj_ciaru_alg2(file_path)
                    
                    if self.zobraz:
                        cv2.imshow("window", img)
                        cv2.waitKey(0)
                    elif output_file != "":
                        print(output_file)
                        cv2.imwrite(output_file, img)
                except:
                    pass


# h = HladanieCiary("images\\fisrt_scans\\340-145825.jpg", "finding_line\\with_lines_point2", zobraz=False)
# h.aplikuj_na_subor(1)

h = HladanieCiary("images\\gombik", "images\\gombik_alg", zobraz=False, pripona='png')
h.aplikuj_na_subor(1)