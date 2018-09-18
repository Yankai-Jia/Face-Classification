from numpy import * 
import time 
import matplotlib.pyplot as plt 
from Kmeans import *
from math import *
import re

def loadDataSet(fileName):
    dataSet = []
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip().split('\t')
        intEStrList = re.findall("-?\d+\.\d+e.\d+", line)
        person=[]
        for eachIntEStr in intEStrList:
            foundEPower = re.search("(?P<intPart>-?\d+\.\d+)e(?P<ePower>.\d+)",eachIntEStr)
            if(foundEPower):
                intPart = foundEPower.group("intPart")
                ePower = foundEPower.group("ePower")
                intPartValue = float(intPart)
                ePowerValue = float(ePower)
                wholeOrigValue = intPartValue * math.pow(math.e, ePowerValue)
                person.append(wholeOrigValue)
        dataSet.append(person)
    
    print(dataSet)
    fr.close()
    return np.mat(dataSet)
    

def main():
    print ("when k =2")
    print("step 1:loading data")
    dataSet = loadDataSet("rect_score.txt")
    result('mal.txt',dataSet)
    #showData(dataSet)
    print("step 2:clustering")
    k = 2
    centroids, cluster = kmeans(dataSet, k)
    result('imgCen_male2.txt',centroids)
    result('imgCluster_male2.txt',cluster)
    print(cluster)
    print("step 3: result")
    
    


if __name__ == "__main__": main()
