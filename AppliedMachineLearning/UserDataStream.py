videoItemId=open('account.json','w')
user_no=1
for user_id in range(1101,1183):
    accountInfo='{ "name": "'+"bsse"+str(user_id)+'", "userId": "'+str(user_no)+'", "email": "'+"bsse"+str(user_id)+"@gmail.com"+'", "password": "'+"iit"+str(user_id)+'"},\n'
    videoItemId.write(accountInfo)
    user_no=user_no+1

videoItemId.close()