def fibb(a):
    if a<=1:
        return a
    
    else:
        return fibb(a - 1) + fibb(a - 2)
    
for x in range(20):
    print(fibb(x))