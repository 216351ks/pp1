t = [32,16,5,8,24,7]
with open('tablica.txt','w') as file:
    for x in t:
        file.write(str(x) + '\n')