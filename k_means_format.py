
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


fr = open("imgCen_female2.txt")
centroids=[]
for line in fr.readlines():
    lines = line.strip().split("\t")
    person=[]
    for x in lines:
        person.append(x)
    centroids.append(person)

fr.close()
    

fr = open("imgCluster_female2.txt")
cluster=[]
j=0
for line in fr.readlines():
    lines = line.strip().split("\t")
    j=j+1
    p=[]
    for x in lines:
         p.append(x)
    cluster.append(p)
fr.close()

fr = open("fem.txt")
dataSet=[]
for line in fr.readlines():
    lines = line.strip().split("\t")
    data=[]
    for x in lines:
         data.append(x)
    dataSet.append(data)
fr.close()

fr = open("fem_score.txt")
scoreSet=[]
for line in fr.readlines():
    lines = line.strip().split("\t")
    score=[]
    for x in lines:
         score.append(x)
    scoreSet.append(data)
print(scoreSet)
fr.close()

numSamples, dim = np.mat(dataSet).shape
mark = ['*','o']
j=0
for i in range(numSamples):
    markIndex = int(float(cluster[i][0]))
    
    plt.plot(float(dataSet[i][3]), float(dataSet[i][1]), mark[markIndex])
for i in range(2):
    plt.plot(float(centroids[i][3]),float( centroids[i][1]), mark[i], markersize = 20)
acc=j/numSamples


plt.title("picture score data")  
  
plt.xlabel("nose")  
plt.ylabel("left eye")  
  
  
plt.show()    


