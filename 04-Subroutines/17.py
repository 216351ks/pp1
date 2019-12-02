from random import randint

def rzucKostka():
    return randint(1,6)

rzuty = [rzucKostka() for x in range(3)]

print(f"wyrzucone oczka: {','.join(str(y) for y in rzuty)}")

print(f'suma wyrzuconych oczek jest równa: {sum(rzuty)}')
