x = input('Podaj dowolną liczbę: ')

y = ['zero','jeden','dwa','trzy','cztery','pięć','sześć','siedem','osiem','dziewięć']


int (x)


for a in x:
    print(y[int(a)], end='')
print()