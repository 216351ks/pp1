from random import randint


c = [randint(1,6) for _ in range (100)]

print(f'Szóstka : {c.count(6)}')
print(f'Piątka : {c.count(5)}')
print(f'czwórka : {c.count(4)}')
print(f'Trójka : {c.count(3)}')
print(f'Dwójka : {c.count(2)}')
print(f'Jedynka : {c.count(1)}')
