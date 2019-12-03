import re

samogloski = ['a','e','i','o','u','y']

reduta = "Nam strzelać nie kazano. Wstąpiłem na działo. I spojrzałem na pole, dwieście armat grzmiało. Artyleryji ruskiej ciągną się szeregi, Prosto, długo, daleko, jako morza brzegi."


for x in samogloski:
    print(f"{x}: {len(re.findall(x, reduta))}")