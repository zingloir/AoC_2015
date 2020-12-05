with open("input") as f:
    etage = f.read()

i = 0
a = 0
b = 0
while i < len(etage):
    if etage[i] == "(":
        a += 1
    else:
        b += 1
    if a - b == -1:
        print(i + 1)
    i += 1
print(a-b)

a = 0
b = 0
i = 0
first = True
for c in etage:
    i += 1
    if c == "(":
        a += 1
    else:
        b += 1
    if a - b == -1 and first:
        first = False
        print("First: ", i)
print("Etage: ", a - b)
