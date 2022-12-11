from urllib import request
req = request.Request('http://10.12.105.35:9200/')
res = request.urlopen(req)
if res.code == 200:
    print("test mysql环境ES正常")
else:
    print("test mysql环境ES挂了")

req = request.Request('http://10.12.102.109:9200/')
res = request.urlopen(req)
if res.code == 200:
    print("release mysql环境ES正常")
else:
    print("release mysql环境ES挂了")

