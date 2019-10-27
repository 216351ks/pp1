x = 0
y = 0
for i in range(1,51):
    if i % 2:
        y += i
else:
    x += i
    
print(f'suma parzystych {x}\n suma nieparzystych {y}')