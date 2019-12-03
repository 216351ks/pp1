def fib(n):
    a,b = 0, 1
    for x in range(n -1):
        a,b = b,a+b
        
    return a

for y in range (1, 21):
    print(fib(y))