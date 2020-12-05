import re
with open("input") as f:
    lines = (f.readlines())

# Zeilenumbruch entfernen
for i in range(len(lines)):
    lines[i] = lines[i].replace('\n', '')

vowels = ['a', 'e', 'i', 'o', 'u']
patternforbidden = '(ab|cd|pq|xy)'
naughty_counter = 0
nice_counter = 0

for line in lines:
    findvowel = False
    finddouble = False
    findforbidden = False



    vowel_counter = 0
    last_char = ''
    match = re.search(patternforbidden, line)
    if match is not None:
        naughty_counter += 1
        continue

    for c in line:
        if c == last_char:
            finddouble = True
        last_char = c
        if c in vowels:
            vowel_counter += 1
    if vowel_counter >= 3:
        findvowel = True

    if findvowel and finddouble:
        nice_counter += 1
    else:
        naughty_counter += 1

print(nice_counter)
print(naughty_counter)
