i = open('advent3.txt')
content = i.read()
houses = 1
oldPositionx = 0
newPositionx = 0
oldPositiony = 0
newPositiony = 0
conditionMet = False
positionList = [[0,0]]
for c in content:
	if c == '<':
		newPositionx = oldPositionx - 1
		newPositiony = oldPositiony
	if c == '>':
		newPositionx = oldPositionx + 1
		newPositiony = oldPositiony
	if c == '^':
		newPositionx = oldPositionx
		newPositiony = oldPositiony + 1
	if c == 'v':
		newPositionx = oldPositionx
		newPositiony = oldPositiony - 1
	for d in range(len(positionList)):
		if positionList[d] == [newPositionx, newPositiony]:
			conditionMet = True		
	if conditionMet == False:
		houses += 1
		positionList.append([newPositionx, newPositiony])

	oldPositionx = newPositionx
	oldPositiony = newPositiony
	conditionMet = False
print houses


i.close()