import re


komunikat = 'wtorek - 23C, środa - 17C, czwartek - 25C'
cyfry = re.findall('\d{2}C',komunikat)
for i in cyfry:
    print(i)