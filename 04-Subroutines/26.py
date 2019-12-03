def podatek(dochod):
    return round(dochod * 0.17 if dochod <= 5000 else (dochod - 5000) * 0.32 + dochod * 0.17)
podaj = int(input('podaj dochód: '))

print(f"Podatek należny to {podatek(podaj)} zł")