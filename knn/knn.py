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
    for imagePath in glob.glob(imagePath):
        imageName=os.path.basename(imagePath)
        print(os.path.splitext(imageName)[0])
        img = Image.open(imagePath).resize((32,32))
        imageData = img.getdata()
        imageVector = np.array(imageData).flatten()
        imageVectors.append(imageVector)
    return imageVectors, imageName


def calculateDistance(NonClassifiedData, classifiedData):
    distance = 0
    dataDimention = len(classifiedData)
    for i in range(dataDimention):
        distance =  distance + pow((NonClassifiedData[i] - classifiedData[i]),2)
        euclideanDistance = math.sqrt(distance)
    return euclideanDistance

def countNeighbour(k,class1,class2):
    class1Count = 0
    class2_count = 0
    for i in range(k):
        if (class1[class1Count]) < (class2[class2_count]):
            class1Count += 1
        else:
            class2_count += 1
        #print(class1Count,class2_count)
    return class1Count,class2_count

if __name__ == '__main__':

    forestVector = loadImginVector('forest/*')
    mountainVector = loadImginVector('mountain/*')

    testDocuments,imageName = loadTestImginVector('test/*')

    print()
    print()

    print("Results: ")
    print("--------")
    for test_vector in testDocuments:

        forest_distance =  sorted([calculateDistance(test_vector,exam_vector) for exam_vector in forestVector])
        mountain_distance = sorted([calculateDistance(test_vector,exam_vector) for exam_vector in mountainVector])
        k = 10
        countNearestNeighbour = countNeighbour(k,forest_distance,mountain_distance)
        forestCount = countNearestNeighbour[0]
        mountainCount = countNearestNeighbour[1]
        
        if forestCount > mountainCount:
            print('forest')
            
        else:
            print("mountain")
            