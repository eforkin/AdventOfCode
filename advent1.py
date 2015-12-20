floorNumber = 0
position = 0
i = open('advent1.txt')
content = i.read()
for c in content:
	if c == '(':
		floorNumber += 1
		position += 1
	if c == ')':
		floorNumber -= 1
		position += 1
	if floorNumber == -1:
		print position
print floorNumber
i.close()