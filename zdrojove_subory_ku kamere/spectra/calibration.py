import numpy as np

class Calibration:

    def __init__(self, arr):
        self.arr_c = arr
        


    def Calibrate(self):
        if(len(self.arr_c)<3):
            self.arr_c = [[0,0],[640,640],[1280,1280]]
        matica_c = []
        for i in range(len(self.arr_c)):
            matica_c.append(self.arr_c[i][0])
        #matica_c.append(0)
        matica = np.array(matica_c)#np.array([[1, self.x1, self.x1*self.x1], [1, self.x2, self.x2*self.x2], [1,self.x3, self.x3*self.x3]])
        #print(self.x1)
        equal_c = []
        for i in range(len(self.arr_c)):
            equal_c.append(self.arr_c[i][1])
        #equal_c.append(0)
        equal = np.array(equal_c)
        if(len(equal_c) == 3):
            #print("3 body")
            x = np.polyfit(matica,equal,2) #np.linalg.solve(matica, equal)#potom 3
        elif(len(equal_c)>3):
            #print("viac bodov")
            x = np.polyfit(matica,equal,3)
        #print(x)
        #quit()
        self.allX = []
        for i in range(len(x)):
            self.allX.append(x[i])
        """
        self.A = x[2]
        self.B = x[1]
        self.C = x[0]
        """
    def GetWaveLenghtByPx(self,pixel):
        #print(self.A + self.B * pixel + self.C * pixel * pixel)
        
        #return self.A + self.B * pixel + self.C * pixel * pixel
        #self.allX = self.allX[::-1]
        #print(self.allX[::-1])
        self.countAll = []
        getWL = 0
        for i in range(len(self.allX[::-1])):
            if(i == 0):
                self.countAll.append(self.allX[::-1][i])
                #print(i)
                #print(self.allX[::-1][i])
            else:
                self.countAll.append(self.allX[::-1][i]*pixel**(i))
                #print(i)
                #print(self.allX[::-1][i])
            #print(self.allX[::-1][i])
        #print (sum(self.countAll))
        return sum(self.countAll)#self.A + self.B * pixel + self.C * pixel * pixel
    
