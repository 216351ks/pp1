tab = []
with open('numbers.txt','r') as tekst:
    for line in tekst:
        tab.append(int(line))
        
tab.sort()
for i in tab:
    print(i, end='')
    