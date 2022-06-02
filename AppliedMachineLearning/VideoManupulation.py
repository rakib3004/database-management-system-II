  
import json



def val_num(video_id):
    val=0
    for i in video_id:
        val+=ord(i)

    return val

# Opening JSON file
f = open('Video.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)
  
# Iterating through the json
# list
for i in data:
    print(i['topic'])
  
# Closing file
f.close()