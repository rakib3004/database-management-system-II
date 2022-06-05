import random
from datetime import datetime


def generateTimeStamp(time):
    time=time.replace("\r","")

    dateTime= datetime.strptime(time, '%m/%d/%y %H:%M:%S')

    time_stamp = datetime.timestamp(dateTime)
    return time_stamp




item_list=[]
with open('Item.txt') as videoItemId:
    item_list = videoItemId.readlines()
   
userDataFile=open('user.data','w')
with open('Testing.csv') as videoItemId:
    userRating=videoItemId.read()
    userRating=userRating.split('\n')
    user_index=0
    for u_item in userRating:
        u_item=u_item.split(',')
        user_index=u_item[0]
        timestamp=random.randint(455555,475555)
        timestampStart=generateTimeStamp(u_item[1])
        timestampFinish=generateTimeStamp(u_item[2])
        print('Quality Assurance: ', timestampStart,timestampFinish)


        item_no=0
        for ux in u_item:
            item_no=item_no+1
            if(item_no>4):
                ux=int(ux)
                item_index=str(item_list[item_no])
                item_index=item_index.replace("\n","").replace("\r","")
                if(ux>0 and ux<6):
                    print(user_index,item_index,ux,timestamp)
                    writeInData=str(user_index)+"\t"+str(item_index)+"\t"+str(ux)+"\t"+str(timestamp)+"\n"
                    userDataFile.write(writeInData)
                    t=22
                if(item_no>50):
                    break
            
videoItemId.close()
userDataFile.close()