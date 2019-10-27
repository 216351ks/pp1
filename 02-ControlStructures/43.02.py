tab =[]
for a in range (1,4):
    tab.append(int(input(f" Podaj {a} liczbę:")))
print(f' Liczby w kolejności rosnącej: {", ".join([str(a) for a in sorted(tab)])}')