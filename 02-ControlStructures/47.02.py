n = int(input("Podaj kwotę w zł:"))

m5= n // 5
m2 = ( n - m5 * 5)//2
m1= n - m5 *5 -m2 *2


print(f"5zł - {m5} szt")
print(f"2zł - {m2} szt")
print(f"1zł - {m1} szt")