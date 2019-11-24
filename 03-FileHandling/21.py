t = []
with open('numbersinrows.txt') as file:
    for line in file:
        t += line.split(",")
        
        
t = [int(i) for i in t]
print(f'Ilość liczb z listy: {len(t)}\nSuma tych liczb jest równa: {sum(t)}')
        