  
import json



def val_num(video_id):
    val=0
    for i in video_id:
        val+=ord(i)

    return val

f = open('Video.json')
  

data = json.load(f)
  
print('[')
for i in range(len(data)):
    print('{ "videoId": "'+data[i]['videoId']+'", "title": "'+data[i]['title']+'", "videoNo": "'+str(i+1)+'"},')
print(']')
# Closing file
f.close()