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
    return dataSet


def main():
    print("step 1:loading data")
    dataSet = loadDataSet("score.txt")
    numSamples, dim = np.mat(dataSet).shape
    print(dim)
    fr = open("imgCluster_female3.txt")
    cluster=[]
    for line in fr.readlines():
        lines = line.strip().split("\t")
        p=[]
        for x in lines:
            p.append(x)
        cluster.append(p)
    fr.close()
    
    j=0
    for i in range(dim):
        if(int(float(cluster[i][0]))==0):
            if(dataSet[0][i]<4):
                j=j+1
        if(int(float(cluster[i][0]))==1):
            if(dataSet[0][i]>=4 and dataSet[0][i]<7):
                j=j+1
        if(int(float(cluster[i][0]))==2):
            if(dataSet[0][i]>=7):
                j=j+1
    acc=j/dim
    print("accuarcy")
    print (acc)
    
    


if __name__ == "__main__": main()
