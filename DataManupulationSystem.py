  


with open('Item.txt') as videoItemId:
    item_list = videoItemId.readlines()
    print('---01----')
    item_list=str(item_list)
    print('---02----')

    item_list=item_list.replace("\\n","").replace("\\r","")
    print('---03----')

    print(item_list)

videoItemId.close()


with open('UserRating.csv') as userRatingID:
    userRating=userRatingID.read()
    userRating=userRating.split('\n')
    for u_item in userRating:
        u_item=u_item.split(',')
        user_index=u_item[0]
        timestamp=u_item[1]
        item_no=0
        for ux in u_item:
            item_no=item_no+1
            ux=int(ux)
            if(ux>0 and ux<6):
                print(user_index,item_list[item_no],ux,timestamp)
   



userRatingID.close()
