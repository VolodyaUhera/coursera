'''
list = ["111","first item", "second item", "third item"]

for idx, item in enumerate(list):
    print(idx+1, item)
    
for i in list:
    if i =='111':
        print ("YES")
        break
    else:
        print("no")

favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

for dessert in favorites:
    if dessert != 'Churros':
        continue
    print('Other desserts I like are', dessert) 

'''
'''
import time
start_time = time.time()


for i in range(10):
    for j in range(10):
        print(0, end=" ")
    print()

print(round((time.time() - start_time), 10))
'''
input("")