i = open('advent2.txt')
content = i.readlines()
sum1 = 0
for j in content:
	if 'x' != j[1]:
		length = j[0:2]
		if 'x' != j[4]:
			width = j[3: 5]
			if 'x' != j[-2]:
				height = j[6:8]
			else:
				height = j[6]
		else:
			width = j[3]
			if 'x' != j[-2]:
				height = j[5:7]
			else:
				height = [5]

	if 'x' == j[1]:
		length = j[0]
		if 'x' != j[3]:
			width = j[2: 4]
			if 'x' != j[-2]:
				height = j[5:7]
			else:
				height = j[5]
		else:
			width = j[2]
			if 'x' != j[2]:
				height = j[4:6]
			else:
				height = j[4]
	height = int(height)
	width = int(width)
	length = int(length)
	if length >= width and length >= height:
		sum1 += (width * 2) + (height * 2)
	elif width >= length and width >= height:
		sum1 += (length * 2) + (height * 2)
	else:
		sum1 += (width * 2) + (length * 2)
	sum1 += (length * width * height)

print sum1
i.close()