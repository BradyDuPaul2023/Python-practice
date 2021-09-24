def greaterThanTen(x):
    if x > 10:
        return "x is greater than 10"
    elif x == 10:
        return "x is 10"
    else:
        return "x is less than 10"
print(greaterThanTen(11))

def potato(x, y):
    if x + y > 10:
        return "potato"
    elif x + y == 10:
        return "tomato"
    else:
        return "topato"

print(potato(5, 4))