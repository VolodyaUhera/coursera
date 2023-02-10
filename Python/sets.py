basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}

print(basket)

print('orange' in basket)

num = [0,1,2,3,4,5]
print(1 in num)

a = set('abracadabra')
b = set('alacazam')
a                                  # unique letters in a
{'a', 'r', 'b', 'c', 'd'}
a - b                              # letters in a but not in b
{'r', 'd', 'b'}
a | b                              # letters in a or b or both
{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
a & b                              # letters in both a and b
{'a', 'c'}
a ^ b     

a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)