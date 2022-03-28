import glob
import math
import numpy as np
from PIL import Image

def loadImginVector(img_path):
    img_vectors = []
    for img_path in glob.glob(img_path):
        img = Image.open(img_path).resize((32,32))
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
    return class1_count,class2_count

if __name__ == '__main__':

    iceVector = loadImginVector('forest/*')
    fireVector = loadImginVector('mountain/*')

    test_vector = loadImginVector('forest.png')[0]
    
    ice_distance =  sorted([calculate_distance(test_vector,exam_vector) for exam_vector in iceVector])
    fire_distance = sorted([calculate_distance(test_vector,exam_vector) for exam_vector in fireVector])

    k = 3
    countNeig = count_neighbour(k,ice_distance,fire_distance)
    iceCount = countNeig[0]
    fireCount = countNeig[1]

    if iceCount > fireCount:
        print('forest')
    else:
        print("mountain")