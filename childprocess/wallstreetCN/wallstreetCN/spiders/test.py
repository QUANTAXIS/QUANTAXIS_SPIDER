from mongodbQuery import querylist
query=querylist()
new_url = 'http://wallstreetcn.com/node/287070'
count = query.queryMongodbSame('title','news_url',new_url)
if count == 0:
    print 'no url in database'
else:
    print 'already in'
print count