x = int(input( 'Podaj długość boku a:'))
y = int(input( 'Podaj długość boku b:'))
for i in range(1, x+1):
    if i == 1 or i == x:
        print("*" * y)
    else:
        print('*' + '' * (y-2) + '*')