# Einlesen des Inputs
with open("input") as f:
    directions = f.read()

# Initialisieren der Variablen
houses = 1
track = [["1"]]
who = 0
x = [0, 0]
y = [0, 0]

# Track wird anhand der Instruktionen aktualisiert und ggf. erweitert
for i in directions:
    if i == ">":
        # Wenn der rechte Rand erreicht wird, wird die Zeile um eine 0 am Ende erweitert
        if x[who] == len(track[y[who]]) - 1:
            track[y[who]].append("0")
        x[who] += 1
    elif i == "<":
        # Wenn der linke Rand erreicht wird, wird in jede bestehende Zeile am Anfang eine 0 hinzugefügt
        if x[who] == 0:
            i = 0
            while i in range(len(track)):
                track[i] = ["0"] + track[i]
                i += 1
            # Position der jeweils anderen Person anpassen
            x[(who + 1) % 2] += 1
        else:
            x[who] -= 1
    elif i == "^":
        # Wenn der obere Rand erreicht wird, wird oben eine Zeile angefügt und mit x + 1 Nullen gefüllt
        if y[who] == 0:
            track = [["0"] * (x[who] + 1)] + track
            # Position der anderen Person anpassen
            y[(who + 1) % 2] += 1
        else:
            y[who] -= 1
    elif i == "v":
        # Wenn der untere Rand erreicht wird, wird unten eine Zeile angefügt und mit x + 1 Nullen gefüllt
        if y[who] == len(track) - 1:
            track.append(["0"] * (x[who] + 1))
        y[who] += 1
        # Wenn die neue Zeile nicht ausreichend lang ist, wird sie mit der nötigen Anzahl an Nullen aufgefüllt
    while x[who] >= len(track[y[who]]):
        track[y[who]].append("0")
    if track[y[who]][x[who]] != "1":
        houses += 1
        track[y[who]][x[who]] = "1"
    # Switchen zwischen Santa und Robo Santa, 0 ist Santa, 1 ist Robo Santa
    who = (who + 1) % 2

print("Anzahl der belieferten Häuser:", houses)
