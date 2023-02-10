""" 
list1 = [1,2,3,4,5]
list2 = ["a","b","c","d",]
list3 = [1,"cat",3,"dog",5]

new_list = []

print(list1, "\n", list2, "\n", list3)

print(list1[-1])

print(list1[3:])

print(list1[:])

print("довжина list1 =", len(list1))

list1.append(6)
list1.append(6)

print("довжина list1 =", len(list1))

print(list1[:])

list1.remove(6)

print(list1[:])

del list1[1]

print(list1[:])

extract_element = list1.pop(3)

print(extract_element)

print(list1[:])

list1.extend(list2)

print(list1[:])

extended_list = list1 + list2

list1.insert(6, "alfhabet")

print(list1[:])

list1.reverse()

print(list1[:])

list_of_list = [ [1, 2],[3, 4],[5, 6] ] 

print(list_of_list[2][0])
 
ls00 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
ls01 = [ [1,2,3], [4,5,6], [7,8,9], [13,14,15] ]
 
print(len(ls00), "and ", len(ls01))

ls00.append(16)

ls01.reverse()

ls01.insert(3,[10,11,12])

print(ls01)

ls02 = [16,17,18]

ls01.append(ls02)

print(ls01)

ls01.sort()

print(ls01)

"""
'''
list1 = [[10,9,1],[11,8,1],[12,7,1]]

def getKey(item):
    return item[1]

list1.sort(key = getKey)

print(list1)

list1.sort()

print(list1)

list1.sort(reverse=True)

print(list1)

string1 = "a-q-b-c-d-q-q-q"

print(sorted(string1))

print(list1 * 3)

myList = [["Mingqi T.", 9],["Wen Qi W.", 6],["Jenn A.", 8]]
herList = [["Siti H.", 7],["Abinayaa", 5]]

myAve = (myList[0][1] + myList[1][1] +myList[2][1]) / len(myList)
print(myAve)

herAve = (herList[0][1] + herList[1][1]) / len(herList)
print(herAve)

teamlist = myList + herList

teamlist.append(["Ahmed B.", 8])

print(teamlist)

teamlist.sort(reverse=True)

print(teamlist)
'''
'''
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

row = [[row[i] for row in matrix] for i in range(4)]
print(row)

#matrix2 = [[x*2 for x in matrix2] for i in range(matrix2)]
#print(matrix2)

vec = [[1,2,3], [4,5,6], [7,8,9]]
print(vec)
vec =[num for elem in vec for num in elem]
print(vec)

matrix2 = [1,2,3,4,5,6,7,8]
print(matrix2)
matrix2 = [x**2 for x in matrix2]
print(matrix2)

lust = [i**3 for i in range(10)]

# def getKey(item):
#     return item

print(lust)

# num = 0
num = [sum(lust)]

print(num)
print(type(num))

# num = [0]
# for i in lust:
#     num[0]+=i

# print(num)
'''
