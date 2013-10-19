import re
from bs4 import BeautifulSoup

soup = BeautifulSoup(open("dwinelleall.html"), "html5lib")
building = "DWINELLE"
tt = soup.select("td font")
times = []
rooms = []
regex = re.compile("[A-Z][a-zA-Z]*[ ]+[0-9]+[\-][0-9]+[A|P]")
for i in range(len(tt)):
	isLocation = False
	isTime = False
 	myString = tt[i].string
	try:
  		isLocation = building in myString
 		isTime = regex.match(myString) != None
 	except TypeError:
 		pass
 	if isLocation == True:
 		rooms.append(myString)
 	if isTime == True:
		times.append(myString)
for i in range(len(rooms)):
	if "(" in rooms[i]:
		rooms[i] = re.sub(r'\([^)]*\)', '', rooms[i])
schedule = {}
for i in range(len(times)):
	if schedule.has_key(times[i]):
		value = schedule.get(times[i])
		if rooms[i] not in value:
			value.append(rooms[i])
		schedule[times[i]]=value
	else:
		schedule[times[i]]=[rooms[i]]
roomsNoDuplicates = []
for r in rooms:
	if r not in roomsNoDuplicates:
		roomsNoDuplicates.append(r)
unoccupied = {}
for key in schedule.keys():
	value = []
	for room in roomsNoDuplicates:
		if room not in schedule.get(key):
			value.append(room)
	unoccupied[key]=value
monday = {}
for key in unoccupied.keys():
	if "M" in key:
		monday[key] = unoccupied.get(key)
tuesday = {}
for key in unoccupied.keys():
	if "Tu" in key:
		tuesday[key] = unoccupied.get(key)
wednesday = {}
for key in unoccupied.keys():
	if "W" in key:
		wednesday[key] = unoccupied.get(key)
thursday = {}
for key in unoccupied.keys():
	if "Th" in key:
		thursday[key] = unoccupied.get(key)
friday = {}
for key in unoccupied.keys():
	if "F" in key:
		friday[key] = unoccupied.get(key)
print(friday.items())