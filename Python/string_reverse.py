# str[statr:stop:step]

# trial = "reversal"[::-1]

# print(trial)

def string_reverse(str):
    if len(str) == 0:
        return(str)
    else:
        return string_reverse(str[1:]) + str[0]
    
string332 = "123456"
reverse = string_reverse(string332)
print(reverse)