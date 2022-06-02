
  
item_list=[]
with open('Item.txt') as videoItemId:
    item_list = videoItemId.readlines()
   
userDataFile=open('user.data','w')
with open('UserRating.csv') as videoItemId:
    userRating=videoItemId.read()
    userRating=userRating.split('\n')
    user_index=0
    for u_item in userRating:
        u_item=u_item.split(',')
        user_index=user_index+1
        timestamp=u_item[1]
        item_no=0
        for ux in u_item:
            item_no=item_no+1
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