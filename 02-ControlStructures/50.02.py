x= int(input("Podaj dowolna liczbę:"))
x2 = x

z= ''
while x >= 1:
    z = str(x % 2) + z
    print(f' {x:3}|{x % 2}')
    x = x//2
    print(f'{x2}(10) = {z}(2)')