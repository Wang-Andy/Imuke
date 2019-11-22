import datetime
import requests

def current_time():
    current_time=datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
    return current_time

def data(clientid='IN_000005',openID=None,clientNO='Oaae8fo0DAo=',key='8a3d4b8a3f13bc8c013f13bc8c9c0000'):
    timestamp=current_time()
    if openID:
        data=clientid+openID+timestamp+key
    else:
        data=clientid+timestamp+clientNO+key
    return data

def sign(openID=None):
    message=data(openID=openID)
    url='http://passport.1768.com/pass-info/encryptController.do'
    para={'type':0,'key':123,'raw':message}
    sign=requests.post(url=url,data=para)
    return sign

def interface(url,clientid='IN_000005',openID=None,clientNO='Oaae8fo0DAo='):
    host='http://passport.1768.com'
    url=host+url
    signstamp=sign(openID=openID)
    timestamp=current_time()
    if openID:
        para={'clientid':clientid,
              'redirect_uri':'http://m.1768.com',
              'response_type':'code',
              'openID': openID,
              'timestamp':timestamp,
              'sign':signstamp}
        respose=requests.post(url=url,data=para).text
    else:
        para={'clentid':clientid,
              'client_secret':'AC5CE9592D684198A560D881B0FEF21C',
              'response_type':	'code',
              'media_source':    'game_wap',
              'clientNo':  clientNO,
              'timestamp':timestamp,
              'sign':signstamp}
        response=requests.post(url=url,data=para)
    return response

a=current_time()
print(a)

openID=''
b=data(openID=openID)
print(b)
c=sign(openID=openID)
print(c)
url='/pass-info/oauth2/3rdPartAuth.do'
d=interface(url=url,openID=openID)
print(d)
