menu = ['espresso','mocha','latte','cappucino','cortado','americano']

def find_coffe(coffe):
    if coffe[0] == 'c':
        return coffe

map_coffe = map(find_coffe, menu) #return all
print(map_coffe)
for x in map_coffe:
    print(x)

filter_codde = filter(find_coffe, menu) #only retturn true
print(filter_codde)
for x in filter_codde:
    print(x)
    
    
# a = [[96], [69]]

# b = ''.join(list(map(str, a)))
# print(''.join(list(map(str, a))))

# print(*(x for x in b))

# for x in b:
#     print(x)


list_of_dicts = [{'key1': 'value1'}, {'key2': 'value2'}, {'key3': 'value3'}]

for dictionary in list_of_dicts:
    for key, value in dictionary.items():
        print(f"{key}: {value}")

result = {key: value for dictionary in list_of_dicts for key, value in dictionary.items()}
print(result)

numbers = [15, 30, 47, 82, 95]
def lesser(numbers):
   return numbers < 50


small = list(map(lesser, numbers))
print(small)