'''
def isPalindrome(str):
    startIndex = 0
    endIndex = len(str) - 1
    
    for x in str:
        if str[x] != str[x]:
            return False
        return True

print(isPalindrome('13321'))
'''
'''
def isPalindrome(str):
 
    # Run loop from 0 to len/2
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True
 
# main function
s = "malayalam"
ans = isPalindrome(s)
 
if (ans):
    print("Yes")
else:
    print("No")
'''
'''
import functools

my_list = [1, 2, 3, 4, 5]
my_list3 = [5,4,3,2,1]

def add_it(x, y):

    return (x + y)

sum4 = functools.reduce(add_it, my_list)

print(sum4)

sum3 = functools.reduce(lambda x, y: x + y, my_list)

print(sum3)

double = lambda x: x+x

print(list(map(double, my_list)))

print(sum(my_list))
'''
""" 
my_list = [1,2,3,4,5]

class ChangeList(object):

    def __init__(self, any_list):

        self.any_list = any_list

    def do_add(self):

      self.sum = sum(self.any_list)

create_sum = ChangeList(my_list)

create_sum.do_add()

print(create_sum.sum)
 """