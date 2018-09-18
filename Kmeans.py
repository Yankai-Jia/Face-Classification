from numpy import *
import numpy as np 
import matplotlib.pyplot as plt  
  

def euclDistance(vector1, vector2):  
    return sqrt(sum(power(vector2 - vector1, 2)))  
  
def Centroids(dataSet, k):  
    numpixel, attr = dataSet.shape  
    centroids = zeros((k, attr))  
    for j in range(k):  
        i = random.randint(0, numpixel)
        centroids[j , :] = dataSet[i, :]  
    return centroids  
  
def kmeans(dataSet, k):  
    numpixel = dataSet.shape[0]  
    Assign = mat(zeros((numpixel, 2)))  
    Changed = True  
    centroids =Centroids(dataSet, k)  
  
    while Changed:  
        Changed = False      
        for i in range(numpixel):  
            minDistance  = 1000000.0  
            minIndex = 0          
            for j in range(k):  
                distance = euclDistance( dataSet[i, :], centroids[j, :])  
                if minDistance >  distance:  
                    minDistance  = distance  
                    minIndex = j  
            if Assign[i, 0] != minIndex:  
                Changed = True  
                Assign[i, :] = minIndex,minDistance**2
   
        for j in range(k):
            centroidj=Assign[:,0].A==j
            dataj=nonzero(centroidj)
            clusterj=dataSet[dataj[0]]  
            centroids[j, :] = mean(clusterj, axis = 0)
            
    return centroids, Assign

  
def result(file_name, data):
   
    m, n = np.shape(data)
    f = open(file_name, "w")
    for i in range(m):
        pixel = []
        for j in range(n):
            pixel.append(str(data[i, j]))
        f.write("\t".join(pixel) + "\n")
    f.close()
