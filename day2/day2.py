# Import Regular Expressions, Input einlesen
import re
lines = []
with open("input2") as f:
    lines = f.readlines()

# Pattern für Regular Expression
pattern = '([0-9]+)x([0-9]+)x([0-9]+)'

# Variablen für gesamte benötigtes Material
paper = 0
ribbon = 0

# Berechnung für jede Zeile
for line in lines:
    # Maße aus line auslesen
    match = re.search(pattern, line)
    w = int(match.group(1))
    l = int(match.group(2))
    h = int(match.group(3))

    # Kleinste Werte für kleinste Fläche suchen
    s1 = w
    s2 = l
    if l <= w:
        s2 = w
        s1 = l
    if h <= s2:
        s2 = s1
        s1 = h
    # Berechnung Fläche und slack, Summe mit Gesamtbedarf für jeweils paper und ribbon
    paper += ((2 * l * w) + (2 * w * h) + (2 * h * l)) + (s1 * s2)
    ribbon += (s1 * 2 + s2 * 2) + (w * l * h)

# Ausgabe Gesamtbedarf
print("Gesamtbedarf an Papier in square feet: ", paper)
print("Gesamtbedarf an Schnur in feet: ", ribbon)
