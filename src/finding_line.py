import numpy as np
import cv2
import os

class HladanieCiary():
    '''
    Pre aplikovanie noveho algoritmu, vo funkcii aplikuj_na_subor treba dat algoritmus = 1. algoritmus =2 je stary algoritmus.
    Pre aplikovanie na cely subor fotiek, treba nastavit path, kde sa fotky nachadzaju, a out_path, kde chceme fotky ulozit a je
    potrebne vytvorit tento subor.
    '''
    def __init__(self,path ,out_path, konstanta,zobraz = False, pripona = 'jpg'):
        self.path = path
        self.out_path = out_path
        self.zobraz = zobraz
        self.pripona = pripona
        self.konstanta = konstanta
        self.posun_poc = 1
        self.vsetky_body = []
             
    def hladaj_ciaru_alg1(self, img):
        if isinstance(img, str):
            img = cv2.imread(img)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        height, width = img.shape
        najvacsie = []
        prvy = 0

        for col in range(width):
            column_pixels = img[:, col]
            if max(column_pixels) > 80: #150
                if prvy ==0:
                    prvy = np.argmax(column_pixels)
                najvacsie.append((col, np.argmax(column_pixels)))

        new_img = np.zeros((height, width, 3), dtype=np.uint8)

        referencna = []
        priemerReferencna = 0
        objekt = []
        for i in najvacsie:
            if abs(i[1]-prvy) < 30: #20
                referencna.append(i)
                priemerReferencna+=i[1]
            else:
                if (i[1] > prvy):
                    objekt.append(i)
                
        # points = np.array(najvacsie, dtype=np.int32)
        # cv2.polylines(new_img, [points], isClosed=False, color=(0, 0, 255), thickness=2)

        cv2.line(new_img, (0, priemerReferencna//len(referencna)), (img.shape[1],priemerReferencna//len(referencna)), (200,120,100),3)

        for i in objekt:
            cv2.circle(new_img, (i[0], i[1]), radius=2, color=(0, 0, 255), thickness=-1)
        
        nove_body = []
        for i in objekt:
            pom_b = (i[0], i[1] * self.posun_poc * self.konstanta, i[1]-priemerReferencna//len(referencna))
            nove_body.append(pom_b)
        
        nove_body = np.array(nove_body, np.int32)
        self.vsetky_body.append(nove_body)
        self.posun_poc+=1
        return new_img
    
    def vykresli(self, path):
        img = self.hladaj_ciaru_alg1(path)
        cv2.imshow("window", img)
        cv2.waitKey(0)
    
    def aplikuj_na_obrazok(self, obrazok):
        pom_obr = obrazok.split('\\')
        img = self.hladaj_ciaru_alg1(obrazok)
        cv2.imwrite(pom_obr[0]+'_alg\\' + pom_obr[1], img)
        
    
    def aplikuj_na_subor(self):
        directory = self.path
        for filename in os.listdir(directory):
            if filename.endswith("."+self.pripona):
                file_path = os.path.join(directory, filename)
                try:
                    output_file = os.path.join(self.out_path, filename)
                    
                    img = self.hladaj_ciaru_alg1(file_path)
                    
                    if self.zobraz:
                        cv2.imshow("window", img)
                        cv2.waitKey(0)
                    elif output_file != "":
                        #print(output_file)
                        cv2.imwrite(output_file, img)
                except:
                    pass
                
        #self.vykresli_vsetky_body()

    def vykresli_vsetky_body(self):
        combined_img = np.zeros((1080, 1920, 3), dtype=np.uint8)

        for body in self.vsetky_body:
            for point in body:
                cv2.circle(combined_img, (point[0], int(point[1]*0.01)), radius=2, color=(0, 255, 0), thickness=-1)
        
        cv2.imshow("All Points", combined_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()