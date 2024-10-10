def variant_1():
    r= int(input("Row= "))
    c=int(input("Col= "))
    if r == c:
        return 1
    if c == 0:
        return 1
    sum = 0
    if r +1 == c:
        sum = 1
    if c -1 == 0:
        sum= 1
    if sum == 0:
        return r+c
    else:
        return r
    
print(variant_1())