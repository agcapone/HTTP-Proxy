import requests
import jwt
import time
import datetime
import uuid


def jwtoken(username):
    
    secret = "a9ddbcaba8c0ac1a0a812dc0c2f08514b23f2db0a68343cb8199ebb38a6d91e4ebfb378e22ad39c2d01d0b4ec9c34aa91056862ddace3fbbd6852ee60c36acbf"
    iat = int(time.time())
    date = datetime.datetime.now()
    day = date.strftime('%m/%d/%Y %H:%M:%S')
    uid = str(uuid.uuid4())
    user1 = str(username)
    payload = {'user': user1,'date':day, 'iat':iat, 'jti':uid}

    token = (jwt.encode(payload,
    secret,
    algorithm = 'HS512',
    ))
    return token

#result = jwt.decode(token,secret,algorithms=['HS512'])

#token1 = jwtoken()
#print("------token------")
#print(token1)
#print("------token------")
#print(result)
#print("------token------")
#print(uid)