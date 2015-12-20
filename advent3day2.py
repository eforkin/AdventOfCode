i = open('advent3.txt')
content = i.read()
houses = 1
SantaoldPositionx = 0
SantanewPositionx = 0
SantaoldPositiony = 0
SantanewPositiony = 0
RobotoldPositionx = 0
RobotnewPositionx = 0
RobotoldPositiony = 0
RobotnewPositiony = 0
conditionMet = False
positionList = [[0,0]]
for index, c in enumerate(content):
	if index % 2 == 0:
		if c == '<':
			SantanewPositionx = SantaoldPositionx - 1
			SantanewPositiony = SantaoldPositiony
		if c == '>':
			SantanewPositionx = SantaoldPositionx + 1
			SantanewPositiony = SantaoldPositiony
		if c == '^':
			SantanewPositionx = SantaoldPositionx
			SantanewPositiony = SantaoldPositiony + 1
		if c == 'v':
			SantanewPositionx = SantaoldPositionx
			SantanewPositiony = SantaoldPositiony - 1
		for d in range(len(positionList)):
			if positionList[d] == [SantanewPositionx, SantanewPositiony]:
				conditionMet = True		
		if conditionMet == False:
			houses += 1
			positionList.append([SantanewPositionx, SantanewPositiony])

		SantaoldPositionx = SantanewPositionx
		SantaoldPositiony = SantanewPositiony
		conditionMet = False
	else:			
		if c == '<':
			RobotnewPositionx = RobotoldPositionx - 1
			RobotnewPositiony = RobotoldPositiony
		if c == '>':
			RobotnewPositionx = RobotoldPositionx + 1
			RobotnewPositiony = RobotoldPositiony
		if c == '^':
			RobotnewPositionx = RobotoldPositionx
			RobotnewPositiony = RobotoldPositiony + 1
		if c == 'v':
			RobotnewPositionx = RobotoldPositionx
			RobotnewPositiony = RobotoldPositiony - 1
		for e in range(len(positionList)):
			if positionList[e] == [RobotnewPositionx, RobotnewPositiony]:
				conditionMet = True		
		if conditionMet == False:
			houses += 1
			positionList.append([RobotnewPositionx, RobotnewPositiony])

		RobotoldPositionx = RobotnewPositionx
		RobotoldPositiony = RobotnewPositiony
		conditionMet = False
print houses


i.close()