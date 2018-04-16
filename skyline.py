building1 = [2,9,10]
building2 = [3,7,15]
building3 = [5,12,12]
building4 = [15,20,10]
building5 = [19,24,8]
bdlist = [building1,building2,building3,building4,building5]

def skyline(buildinglist):
	collectionArray = []
	rightXvalue = []
	returnArray = []
	for index in buildinglist:
		rightXvalue.append(index[1])
	maxRightValue = max(rightXvalue)

	for index in range(0,maxRightValue + 2):
		collectionArray.append(0)
	
	for bldg in buildinglist:
		for height in range(bldg[0],bldg[1]):
			if collectionArray[height] < bldg[2]:
				collectionArray[height] = bldg[2]

	for index in range(0,len(collectionArray) - 1):
		if collectionArray[index] != collectionArray[index + 1]:
			returnArray.append((index + 1,collectionArray[index+1]))
	print(collectionArray)
	print(returnArray)


skyline(bdlist)


