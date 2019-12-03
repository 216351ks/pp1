tab = [2,4,1,5,6]
def my_function(tab):
    print(f'suma: {sum(tab)}')
print(f"wartość: {','.join(str(x) for x in tab)}")  
my_function(tab)
