myList = [1, 2, 3, "fuf", "r4r"]
print(myList)
# print(myList[0])
# print(myList[1])
# print(myList[2])
# print(myList[3])
# print(myList[4])
# print()
# print(myList[-1])
# print(myList[-2])
# print(myList[-3])
# print(myList[-4])
# print(myList[-5])

myList[1] = 3
print(myList)

myList.append(56)
print(myList)

myList.insert(2, 7)
print(myList)

myList[0] = 0
print(myList)

myList.remove(56)
print(myList)

myList.pop(2)
print(myList)

myList2 = [56, 56, "fdgfg", "gfdg", 34]
print(myList2)

unionList = myList + myList2
print(unionList)

numberList = [6, 76, 34, 56,  67]
numberList.sort()
print(numberList)
numberList.reverse()
print(numberList)

leterList = ["gfg", 'dfsdg', 'agfg']
leterList.sort()
print(leterList)
leterList.reverse()
print(leterList)

print(len(leterList))

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[2][2])
