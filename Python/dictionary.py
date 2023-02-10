squares = {1:1, 2:4, 3:9, 4:16, 5:25}

dictionary0 = {}

print(squares[5])

print(squares.keys())

print(squares.values())

squares[6] = 36

print(squares)

squares[3] = "wrong square"

print(squares)

print(squares.pop(6))

print(squares)

del squares[3]

print(squares)

print(len(squares))

myDict = {"name": "Li Mingyao", "age": 24, "nationality": "Singaporean"}

print(myDict["age"])

profits = {"Q1": 540390, "Q2": 320980, "Q3": 550021, "Q4": 190900}

q1_ave = int(profits["Q1"] / 3)
q2_ave = int(profits["Q2"] / 3)
q3_ave = int(profits["Q3"] / 3)
q4_ave = int(profits["Q4"] / 3)
#y_ave = int((profits["Q1"] + profits["Q2"] + profits["Q3"] + profits["Q4"])\
#    /12)

y_ave = int(sum(profits.values())/12)

profits["Q4"] += 350000

print(profits["Q4"])

print(profits)

fin_sum = {"Q1": q1_ave, "Q2": q2_ave, "Q3": q3_ave, "Q4": int(profits["Q4"] / 3)}

print("Fin sum =", fin_sum)


list1 = [['Matt','Ben', 'Jerry'],[1,2,3,4,5], ['Denmark', 'England', 'Scotland']]


for i in list1:
    for x in i:
        print (x)
        
dept_list = ["Amy", "Simon", "Vaishak", "Adam", "Siti"]
promoted = ["Simon", "Vaishak", "Siti", "MingYao", "Khairul"]
dept_promoted = []

for employee in dept_list:
    for name in promoted:
        if name == employee:
            dept_promoted.append(name)
            
print(dept_promoted)

#marks = {'Math':0, 'English':0, 'Science':0}
marks = {}.fromkeys(['Math','English','Science'], 0)
print(marks)

marks['History'] = 90
marks['Geography'] = 60
marks['English'] = 70

marks.popitem()

science_marks = marks.pop('Science')

subjects = sorted(marks.keys())

scores = sorted(marks.values())

array_2d = [[1, 2, 3, 4],[5, 6], [7,8,9], [10,11,12]]

for i in range(len(array_2d)):
    for j in (range(len(array_2d[i]))):
        print(array_2d[i][j])
        

