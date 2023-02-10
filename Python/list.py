'''
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    result = [[i,j, k] 
    for i in range(x+1) 
    for j in range(y+1) 
    for k in range(z+1) 
    if (i+j+k) != n]
    print(result)
    print(len(result))
'''

list1 = [1,2,3,4,5]

print(*list1, sep=":D")

list1.insert(len(list1), 6)

print(*list1, sep=":D")

del list1[1::2]

list1.sort(reverse=True)

print(list1)

