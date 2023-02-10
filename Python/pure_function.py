my_list = [1,2,3]

def add_item(lst, item):
    nl = lst.copy()
    nl.append(item)
    return nl

new_list =  add_item(my_list, 4)

print(my_list)
print(new_list)



