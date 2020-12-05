import hashlib

# Gegebener Input
secret = 'iwrupvqb'

# Prüfen, ob secret gemeisam mit übergebener Zahl einen Hashwert mit req Anzahl führender Nullen ergibt
def checkHash(number, req):
    result = hashlib.md5((secret + str(number)).encode()).hexdigest()
    for i in range(len(result)):
        if result[i] != "0":
            return False
        if i >= req - 1:
            return True

# Solange Nummern probieren, bis passender Nummer mit korrektem Hashwert gefunden wurde
def findNumber(req):
    found = False
    num = 0
    while not found:
        found = checkHash(num, req)
        if found:
            print("Für", req, "führende Nullen:", num)
            break
        num += 1


findNumber(5)
findNumber(6)
