import random

# from multiprocessing.pool import worker
#
# myList = [1, 2, 3, "fuf", "r4r"]
# print(myList)
# # print(myList[0])
# # print(myList[1])
# # print(myList[2])
# # print(myList[3])
# # print(myList[4])
# # print()
# # print(myList[-1])
# # print(myList[-2])
# # print(myList[-3])
# # print(myList[-4])
# # print(myList[-5])
#
# myList[1] = 3
# print(myList)
#
# myList.append(56)
# print(myList)
#
# myList.insert(2, 7)
# print(myList)
#
# myList[0] = 0
# print(myList)
#
# myList.remove(56)
# print(myList)
#
# myList.pop(2)
# print(myList)
#
# myList2 = [56, 56, "fdgfg", "gfdg", 34]
# print(myList2)
#
# unionList = myList + myList2
# print(unionList)
#
# work[sdelano-1] = "сделано"
#
# numberList = [6, 76, 34, 56,  67]
# numberList.sort()
# print(numberList)
# numberList.reverse()
# print(numberList)
#
# leterList = ["gfg", 'dfsdg', 'agfg']
# leterList.sort()
# print(leterList)
# leterList.reverse()
# print(leterList)
#
# print(len(leterList))
#
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(matrix[2][2])


questions = [
    "Сколько планет в Солнечной системе?",
    "Какой язык лучший для начала обучения?",
    "Какая функция позволяет узнать длину списка?",
    "Какая планета самая большая в солнечной системе",
    "Сколько лет нужно учиться в школе, чтобы поступить в колледж?",
]

answers = [
    "8",
    "Python",
    "len()",
    "Юпитер",
    "9",
]

indexes = list(range(len(questions)))
random.shuffle(indexes)

# current_answer = 0
correct_answer = 0
for i in indexes:
    answer = input(f"{questions[i]}\t")
    if answer == answers[i]:
        print(f"Correct!\n")
        correct_answer += 1
    else:
        print(f"Incorrect!\n")

print(f"Викторина заверешена!\nCorrect answers:", correct_answer)
