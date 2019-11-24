import re
with open('land.txt') as file:
    t = re.findall('\d', file.read() )


t = [int(x) for x in t]

print(sum(t))