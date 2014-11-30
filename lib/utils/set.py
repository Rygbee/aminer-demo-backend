import pymongo
from bson import ObjectId
import xlrd
import string

db = pymongo.Connection('166.111.7.105',30017)['bigsci']
db.authenticate('kegger_bigsci',"datiantian123!@#")
venue = db['venue']

data = xlrd.open_workbook('data.xlsx')
table = data.sheets()[0]
conferenceID = table.col_values(0)
conferenceName = table.col_values(1)
nrows = table.nrows

Id2Name = {}

for i in range(1,nrows):
	Id2Name[conferenceID[i]] = conferenceName[i]

g = {}

fr = open('ans.txt','r')

for line in fr.readlines():
	a,b = line.split()
	if g.has_key(b) is False:
		g[b] = {"name":Id2Name[float(b)], "Id":b,
				"nameList":[venue.find_one({"_id":ObjectId(a)})['name'],],"IdList":[ObjectId(a),]}
	else:
		g[b]["nameList"].append(venue.find_one({"_id":ObjectId(a)})['name'])
		g[b]["IdList"].append(ObjectId(a))

relationship = db['venue_dupl']

for key in g.keys():
	relationship.insert(g[key])

fr.close()
