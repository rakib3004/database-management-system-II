with open('user.data') as videoItemId:
    userRating=videoItemId.read()
    #userRating=userRating.split('\t')
    
    for u_item in userRating:
        u_item=u_item.split('\t')
        print(u_item)
        