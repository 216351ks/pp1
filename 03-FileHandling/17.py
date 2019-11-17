import re


tekst = 'to be, or not to be, that is the question'
samogłoski = re.findall('[aeiou]', tekst)
print(len(samogłoski))