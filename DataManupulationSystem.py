  
import json



with open('Item.txt') as videoItemId:
    lines = videoItemId.readlines()
    lines=str(lines)

    lines=lines.replace("\\n","").replace("\\r","")
    print(lines)

videoItemId.close()


with open('UserRating.csv') as userRatingID:
    userRating=userRatingID.read()
    userRating=userRating.split('\n')
    for u_item in userRating:
        u_item=u_item.split(',')
        for ux in u_item:
            

   



userRatingID.close()
