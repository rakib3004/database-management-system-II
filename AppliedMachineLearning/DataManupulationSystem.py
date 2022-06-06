import random
from datetime import datetime
import json


def generateTimeStamp(time):
    time=time.replace("\r","")

    dateTime= datetime.strptime(time, '%m/%d/%y %H:%M:%S')

    time_stamp = datetime.timestamp(dateTime)
    return int(time_stamp)

def countRating(u_item):
    splitNumberForTimeStamp=0
    item_no=0
    for ux in u_item:
        
        item_no=item_no+1
        if(item_no>3):
            try:
                ux=int(ux)
                if(ux>0 and ux<6):
                    splitNumberForTimeStamp=splitNumberForTimeStamp+1
            except:
                a=2018



    return splitNumberForTimeStamp



item_list=[]
with open('Item.txt') as videoItemId:
    item_list = videoItemId.readlines()
   
userDataFile=open('user.data','w')
with open('Testing.csv') as videoItemId:
    userRating=videoItemId.read()
    userRating=userRating.split('\n')
    print(userRating)
    user_index=0
    for u_item in userRating:
        
        
        u_item=u_item.split(',')
        user_index=u_item[0]
        timestamp=random.randint(455555,475555)
        print('Unit Testing:', u_item[1],u_item[2])
        ts_start=str(u_item[1])+':'+str(random.randint(0,59))
        ts_finish=str(u_item[2])+':'+str(random.randint(0,59))
        timestampStart=generateTimeStamp(ts_start)
        timestampFinish=generateTimeStamp(ts_finish)
        print('Quality Assurance: ', timestampStart,timestampFinish)
        time_start=min(timestampStart,timestampFinish)
        time_finish=max(timestampStart,timestampFinish)
        timeStampRange=time_finish-time_start
        timeStampList=[]
        splitNumberForTimeStamp=countRating(u_item)
        for index in range(splitNumberForTimeStamp+1):
            timeStampList.append(time_start+(index*timeStampRange))
        
        random.shuffle(timeStampList)

        f = open('Video.json')
  

        data = json.load(f)

        

        item_no=0
        rating_index=0
        for ux in u_item:
            item_no=item_no+1
            if(item_no>3):
                ux=int(ux)
                item_index=str(item_list[item_no])
                item_index=item_index.replace("\n","").replace("\r","")
                if(ux>0 and ux<6):
                    
                    #str(user_index)+"\t"+str(item_index)+"\t"+str(ux)+"\t"+str(timeStampList[rating_index])+"\n"
                    
                    if(int(user_index)<10):
                        user_id="0"+str(user_index)
                    else:
                        user_id=str(user_index)
                    
                    writeInData='{ "userId": "'+"bsse11"+user_id+'", "userNo": "'+str(user_index)+'", "videoId": "'+str(data[int(item_index)]['videoId'])+'", "videoNo": "'+str(item_index)+'", "rating": "'+str(ux)+".0"+'", "timestamp": "'+str(timeStampList[rating_index])+'"},'


                    print(writeInData)
                    userDataFile.write(writeInData)
                    rating_index=rating_index+1
                    
                if(item_no>59):
                    break
                
            
videoItemId.close()
userDataFile.close()