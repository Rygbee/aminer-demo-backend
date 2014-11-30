import pymongo
import string

db = pymongo.Connection('166.111.7.105',30017)['bigsci']
db.authenticate('kegger_bigsci',"datiantian123!@#")
venue = db['venue']
venue_dupl = db['venue_dupl']


venue_set = set()
cursor = venue_dupl.find()

for item in cursor:
	for entry in item['IdList']:
		venue_set.add(entry)

cnt = 0

cursor = venue.find()

def get():
	try:
		item = cursor.next()
	except pymongo.errors.AutoReconnection:
		item = get()
	return item

item = get()
while item is not None:
	if item['type'] != 1 and item['type'] != 2 and item['type'] != 10 and item['type'] != 11:
		item = get()
		continue
	if not item.has_key('name'):
		item = get()
		continue
	cnt += 1
	print cnt
	if item['_id'] not in venue_set:
		venue_dupl.insert({"name":item['name'],"Id":item['_id'],"nameList":[item['name'],],"IdList":[item['_id'],]})
	item = get()

fw.close()
