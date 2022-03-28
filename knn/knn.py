import glob
import math
import numpy as np
from PIL import Image
import os

def loadImginVector(img_path):
    img_vectors = []
    for img_path in glob.glob(img_path):
        img = Image.open(img_path).resize((32,32))
        img_data = img.getdata()
        img_vector = np.array(img_data).flatten()
        img_vectors.append(img_vector)
    return img_vectors



def loadTestImginVector(img_path):
    img_vectors = []
    for img_path in glob.glob(img_path):
        imageName=os.path.basename(img_path)
        print(os.path.splitext(imageName)[0])
        img = Image.open(img_path).resize((32,32))
        img_data = img.getdata()
        img_vector = np.array(img_data).flatten()
        img_vectors.append(img_vector)
    return img_vectors, imageName


def calculateDistance(testVec, examVec):
    distance = 0
    for i in range(len(examVec)):
        distance += (testVec[i] - examVec[i]) * (testVec[i] - examVec[i])
    return math.sqrt(distance)

def countNeighbour(k,class1,class2):
    class1_count = 0
    class2_count = 0
    for i in range(k):
        if (class1[class1_count]) < (class2[class2_count]):
            class1_count += 1
        else:
            class2_count += 1
        #print(class1_count,class2_count)
    return class1_count,class2_count

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
            