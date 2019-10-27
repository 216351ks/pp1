lim= int(input('Limit prędkości :'))
pre= int(input('Podaj prędkość:'))

if(pre - lim) <=10:
    print(f'Mandat: {(pre-lim)* 5} zł')
else:
    print(f'Mandat: {50+((pre-lim-10)*15)} zł')