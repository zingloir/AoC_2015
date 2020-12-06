import re
with open("input") as f:
    lines = (f.readlines())

# Zeilenumbruch entfernen
for i in range(len(lines)):
    lines[i] = lines[i].replace('\n', '')


# Gibt True zurück, wenn der String die Voraussetzungen aus Part 1 erfüllt, sonst False
def part1(checkme):
    # Prüfung ob verbotene Strings enhalten sind
    findforbidden = False
    patternforbidden = '(ab|cd|pq|xy)'
    match = re.search(patternforbidden, checkme)
    if match is not None:
        return False

    findvowel = False
    finddouble = False
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_counter = 0
    last_char = ''
    for c in line:
        # Prüfung ob Buchstabenpärchen enthalten sind
        if c == last_char:
            finddouble = True
        last_char = c
        # Prüfung ob Buchstabe ein Vokal ist
        if c in vowels:
            vowel_counter += 1
    # Prüfung, ob ausreichend Vokale enthalten sind
    if vowel_counter >= 3:
        findvowel = True

    # Falls alle Voraussetzungen erfüllt sind, return True
    if findvowel and finddouble:
        return True
    else:
        return False

def part2(checkme):
    findtwice = False
    i = 0
    # Prüfung, ob doppelte Buchstabenpaare enthalten sind
    while i < len(checkme):
        if checkme[i:i+2] in checkme[i+2:]:
            findtwice = True
        i += 1

    # Prüfung ob Paare mit Abstand enthalten sind
    findgap = False
    i = 0
    while i < len(checkme) - 2:
        if checkme[i] == checkme[i + 2]:
            findgap = True
        i += 1

    # Prüfung, ob alle Voraussetzungen erfüllt sind
    if findtwice and findgap:
        return True
    else:
        return False


nice_counter_p1 = 0
nice_counter_p2 = 0
for line in lines:
    if part1(line):
        nice_counter_p1 += 1
    if part2(line):
        nice_counter_p2 += 1
print("P1:", nice_counter_p1)
print("P2:", nice_counter_p2)
