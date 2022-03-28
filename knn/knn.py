import glob
import math
import numpy as np
from PIL import Image

def loadImginVector(img_path):
    img_vectors = []
    for img_path in glob.glob(img_path):
        img = Image.open(img_path).resize((32,32))
        print(img.info)
        img_data = img.getdata()
        img_vector = np.array(img_data).flatten()
        img_vectors.append(img_vector)
    return img_vectors

def calculate_distance(testVec, examVec):
    distance = 0
    for i in range(len(examVec)):
        distance += (testVec[i] - examVec[i]) * (testVec[i] - examVec[i])
    return math.sqrt(distance)

def count_neighbour(k,class1,class2):
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

    testDocuments = loadImginVector('test/*')

    for test_vector in testDocuments:

        forest_distance =  sorted([calculate_distance(test_vector,exam_vector) for exam_vector in forestVector])
        mountain_distance = sorted([calculate_distance(test_vector,exam_vector) for exam_vector in mountainVector])
        #print('forest distance: ', forest_distance, 'mountain_distance: ', mountain_distance )
        k = 10
        countNearestNeighbour = count_neighbour(k,forest_distance,mountain_distance)
        forestCount = countNearestNeighbour[0]
        mountainCount = countNearestNeighbour[1]

        if forestCount > mountainCount:
            print('forest')
            
        else:
            print("mountain")
            