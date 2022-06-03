import sys
import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import sys


user_ID=17
#user_ID=int(user_ID)

header = ['user_id', 'item_id', 'rating', 'timestamp']
dataset = pd.read_csv('user.data', sep='\t', names=header)
print(dataset.head())


n_users = dataset.user_id.unique().shape[0]
n_items = dataset.item_id.unique().shape[0]


n_items = dataset['item_id'].max()
A = np.zeros((n_users, n_items), dtype=int)
for line in dataset.itertuples():
    A[line[1]-1, line[2]-1] = line[3]
#print("Original rating matrix : ", A)

for i in range(len(A)):
    for j in range(len(A[0])):
        if A[i][j] >= 3:
            A[i][j] = 1
        else:
            A[i][j] = 0

csr_sample = csr_matrix(A)
#print(csr_sample)

knn = NearestNeighbors(metric='cosine', algorithm='brute',
                       n_neighbors=3, n_jobs=-1)
knn.fit(csr_sample)

dataset_sort_des = dataset.sort_values(
    ['user_id', 'timestamp'], ascending=[True, False])


userBasedItem = dataset_sort_des[dataset_sort_des['user_id'] == user_ID].item_id
userBasedItem = userBasedItem.tolist()
userBasedItem = userBasedItem[:20]








indexList = []
for i in userBasedItem:
    distances, indices = knn.kneighbors(csr_sample[i], n_neighbors=3)
    indices = indices.flatten()
    indices = indices[1:]
    indexList.extend(indices)

indexList=set(indexList)
print("Items to be recommended: ",indexList)

youTubeVideoUrlListPlainText = open("YouTubeData/YouTubeVideoID.txt", encoding="utf8")

youTubeVideoUrlListFile=youTubeVideoUrlListPlainText.readlines()

youTubeVideoUrlListTitle = open("YouTubeData/YouTubeVideoTitle.txt", encoding="utf8")

youTubeVideoUrlTitleFile=youTubeVideoUrlListTitle.readlines()

youTubeVideoUrlListTopic = open("YouTubeData/YouTubeVideoTopic.txt", encoding="utf8")

youTubeVideoUrlTopicFile=youTubeVideoUrlListTopic.readlines()

videoDataSteam=1
videoID=1

print("Videos which are recommended for you:")
for f in indexList:
    if(f>60):
        continue
    #print(youTubeVideoUrlListFile[f], end='')
    print('{ "videoID":"'+youTubeVideoUrlListFile[f].strip()+'"'+', "videoTitle":"'+youTubeVideoUrlTitleFile[f].strip()+'" , "videoTopic":"'+youTubeVideoUrlTopicFile[f].strip()+'" },')

'''
    print('/"videoID"/:/"+'youTubeVideoUrlListFile[f], end='')


'''