""" 
file = open('text.txt', mode = 'r')

data = file.readline()

print(data)

file.close() 
"""
""" 
with open ('text.txt', mode= 'r') as file:
    data = file.readlines()
    
    print(data)

try:
    with open('sample/newfile44.txt', 'w') as file:
        file.writelines(["This is a new file created!", "\nThis is another line to be added."])
except FileNotFoundError as e:
    print("ERROR", e, sep=' ')
   """ 
"""    
with open ('text.txt', mode= 'r') as file:
    data = file.readlines()
    
    data.append('Hell')
    print(data)
 """