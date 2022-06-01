  
import json



with open('Item.txt') as videoItemId:
    lines = videoItemId.readlines()
    lines=str(lines)
    lines=lines.replace("\\n","").replace("\\r","")
    print(lines)
videoItemId.close()


with open('UserRating.csv') as userRatingID:
    userRating=userRatingID.read()
    userRating=str(userRating)
    print(userRating)


userRatingID.close()
