def sum_of(**kwargs):
    sum = 0
    for k, v in kwargs.items():
        sum += v
    return round(sum, 2)

print(sum_of(coffe=2.99, cake = 5.55, juice=2.99))
