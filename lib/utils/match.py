import pymongo
import xlrd
import re
import string

db = pymongo.Connection('166.111.7.105',30017)['bigsci']
db.authenticate('kegger_bigsci',"datiantian123!@#")
venue = db['venue']

data = xlrd.open_workbook('data.xlsx')
table = data.sheets()[0]
conferenceID = table.col_values(0)
conferenceName = table.col_values(1)
nrows = table.nrows

filterList = ["and","networks","computing","first"]

#precomputation
reg1 = r'\(.*\)'
splitre1 = re.compile(reg1)
reg2 = r'[^\w\.]*'
splitre2 = re.compile(reg2)

nameList = []
for i in range(1,nrows):
	arr = re.split(splitre1,conferenceName[i])
	wordList = []
	for word in arr:
		Arr = re.split(splitre2,word)
		for entry in Arr:
			wordList.append(string.lower(entry))
	#if int(conferenceID[i]) == 4899:
	#print wordList
	nameList.append(wordList)

fw = open('ans.txt','w')

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
	name = item['name']
	name = string.lower(name).strip()
	arr = re.split(splitre2,name)
	arrLen = len(arr)
	short_name = False
	if item.has_key('short_name'):
		short_name = item['short_name']
		short_name = string.lower(short_name)
	p = -1
	val = 0.0
	for i in range(nrows-1):
		tmp = 0.0
		if len(nameList[i]) == 1 and short_name != False:
			if nameList[i][0] == short_name.strip():
				tmp = 1.0
		elif len(nameList[i]) == 1:
			if nameList[i][0] == name:
				tmp = 1.0
			elif name.split()[0] == nameList[i][0]:
				tmp = 0.9
		else:
			flag = 1
			for word in nameList[i]:
				if len(word) == 0: continue
				if word[-1] == '.' and name.find(word) != -1:
					continue
				if word not in arr:
					flag = 0
					break
			if flag:
				tmp = len(nameList[i])/arrLen
		if tmp > val:
			val = tmp
			p = i
	if p != -1 and val > 0.1:
		print name
		fw.write("%s %s\n" % (str(item['_id']), str(conferenceID[p+1])))

	item = get()

fw.close()
