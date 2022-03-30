import glob
import math
import numpy as np
from PIL import Image
import os

def loadImginVector(imagePath):
    imageVectors = []
    for imagePath in glob.glob(imagePath):
        img = Image.open(imagePath).resize((32,32))
        imageData = img.getdata()
        imageVector = np.array(imageData).flatten()
        imageVectors.append(imageVector)
    return imageVectors



def loadTestImginVector(imagePath):
    imageVectors = []
    imageNames = []
    for imagePath in glob.glob(imagePath):
        imageName=os.path.basename(imagePath)
        #print(os.path.splitext(imageName)[0])
        img = Image.open(imagePath).resize((32,32))
        imageData = img.getdata()
        imageVector = np.array(imageData).flatten()
        imageVectors.append(imageVector)
        imageNames.append(imageName)

    return imageVectors,imageNames


def computeEuclideanDistance(nonClassifiedData, classifiedData):
    distance = 0
    dataDimention = len(classifiedData)
    for i in range(dataDimention):
        distance =  distance + pow((nonClassifiedData[i] - classifiedData[i]),2)
        euclideanDistance = math.sqrt(distance)
    return euclideanDistance

def countNeighbour(k,class1,class2):
    class1Count = 0
    class2Count = 0
    for i in range(k):
        if (class1[class1Count]) < (class2[class2Count]):
            class1Count += 1
        else:
            class2Count += 1
    return class1Count,class2Count

if __name__ == '__main__':

    forestVector = loadImginVector('forest/*')
    mountainVector = loadImginVector('mountain/*')
   
    nonClassifiedDocuments,imageNames = loadTestImginVector('test/*')

    print()
    print()

    print("Results: ")
    print("--------")
    for nonClassifiedData in nonClassifiedDocuments:

        forestImageDistanceList =  sorted([computeEuclideanDistance(nonClassifiedData,classifiedData) for classifiedData in forestVector])
        mountainImageDistanceList = sorted([computeEuclideanDistance(nonClassifiedData,classifiedData) for classifiedData in mountainVector])
        k = 10

        forestImageDistanceList=[]
        mountainImageDistanceList=[]
        for classifiedData in forestVector:
            forestImageDistanceList.append(computeEuclideanDistance(nonClassifiedData,classifiedData)) 
        sorted(forestImageDistanceList)

        for classifiedData in mountainVector:
            mountainImageDistanceList.append(computeEuclideanDistance(nonClassifiedData,classifiedData)) 
        sorted(mountainImageDistanceList)
        
        countNearestNeighbour = countNeighbour(k,forestImageDistanceList,mountainImageDistanceList)
        
        forestCount = countNearestNeighbour[0]
        mountainCount = countNearestNeighbour[1]
        print(imageNames[0], " -->  ",end="")
        imageNames.pop(0)
        if forestCount > mountainCount:
            print('forest')
            
        else:
            print("mountain")
            