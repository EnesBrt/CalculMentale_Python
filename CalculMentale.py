import random

# =============================================
# Opération niveau facile
# =============================================

def additionsFacile():
    i = 0
    for i in range(10):
        
        a = random.randrange(1, 10)
        b = random.randrange(1, 10)
        print(a, '+', b)
        rep = a + b
        res = int(input("entrer un résultat : "))
        
        if res == rep:
            print(True)

        else:
            print(False)
    

def soustractionsFacile():
    i = 0
    for i in range(10):

        a = random.randrange(1, 10)
        b = random.randrange(1, 10)
        print(a, '-', b)
        rep = a - b
        res = int(input("enter un résultat : "))
        
        if res == rep:
            print(True)
        else:
            print(False)


def multiplicationsFacile():
    i = 0
    for i in range(10):
        
        a = random.randrange(1, 10)
        b = random.randrange(1, 10)
        print(a, '*', b)
        rep = a * b
        res = int(input("entrer un résultat : "))
        
        if res == rep:
            print(True)
        else:
            print(False)


def divisionsFacile():
    i = 0
    for i in range(10):
        
        a = random.randrange(1, 10)
        b = random.randrange(1, 10)
        print(a, '/', b)
        rep = a / b
        res = int(input("entrer un résultat : "))
        
        if res == rep:
            print(True)
        else:
            print(False)

# =============================================
# Opération niveau moyen
# =============================================

def additionsMoyen():
    i = 0
    for i in range(30):
        
        a = random.randrange(10, 100)
        b = random.randrange(10, 100)
        print(a, '+', b)
        rep = a + b
        res = int(input("entrer un résultat : "))
        
        if res == rep:
            print(True)
        else:
            print(False)


def soustractionsMoyen():
    i = 0
    for i in range(30):
        
        a = random.randrange(10, 100)
        b = random.randrange(10, 100)
        print(a, '-', b)
        rep = a - b
        res = int(input("entrer un résultat : "))
        
        if res == rep:
            print(True)
        else:
            print(False)


def multiplicationsMoyen():
    i = 0
    for i in range(30):
        
        a = random.randrange(10, 100)
        b = random.randrange(10, 100)
        print(a, '*', b)
        rep = a * b
        res = int(input("entrer un résultat : "))
        
        if res == rep:
            print(True)
        else:
            print(False)


def divisionsMoyen():
    i = 0
    for i in range(30):
        
        a = random.randrange(10, 100)
        b = random.randrange(10, 100)
        print(a, '/', b)
        rep = a / b
        res = int(input("entrer un résultat : "))
        
        if res == rep:
            print(True)
        else:
            print(False)

# =============================================
# Opération nevrau difficile
# =============================================

def additionsDifficile():
    i = 0
    for i in range(50):
        
        a = random.randrange(100, 1000)
        b = random.randrange(100, 1000)
        print(a, '+', b)
        rep = a + b
        res = int(input("entrer un résultat : "))
        
        if res == rep:
            print(True)
        else:
            print(False)


def soustractionsDifficile():
    i = 0
    for i in range(50):
        
        a = random.randrange(100, 1000)
        b = random.randrange(100, 1000)
        print(a, '-', b)
        rep = a - b
        res = int(input("entrer un résultat : "))
        
        if res == rep:
            print(True)
        else:
            print(False)


def multiplicationsDifficile():
    i = 0
    for i in range(50):

        a = random.randrange(100, 1000)
        b = random.randrange(100, 1000)
        print(a, '*', b)
        rep = a * b
        res = int(input("entrer un résultat : "))
        
        if res == rep:
            print(True)
        else:
            print(False)


def divisionsDifficile():
    i = 0
    for i in range(50):
        
        a = random.randrange(100, 1000)
        b = random.randrange(100, 1000)
        print(a, '/', b)
        rep = a / b
        res = int(input("entrer un résultat : "))
        
        if res == rep:
            print(True)
        else:
            print(False)

# =============================================
# les 3 niveaux de difficulé 
# =============================================


def choixFacile():

    while True:

        print("choisissez entre ces 4 opération : ")
        print("1 - addition")
        print("2 - soustraction")
        print("3 - multiplication")
        print("4 - division")

        ask = input("entrer votre choix(1, 2, 3 ou 4) : ")

        if ask == "1":
            additionsFacile()
            break
        elif ask == "2":
            soustractionsFacile()
            break
        elif ask == "3":
            multiplicationsFacile()
            break
        elif ask == "4":
            divisionsFacile()
            break


def choixMoyen():

    while True:

        print("choisissez entre ces 4 opération : ")
        print("1 - addition")
        print("2 - soustraction")
        print("3 - multiplication")
        print("4 - division")

        ask = input("entrer votre choix(1, 2, 3 ou 4) : ")

        if ask == "1":
            additionsMoyen()
            break
        elif ask == "2":
            soustractionsMoyen()
            break
        elif ask == "3":
            multiplicationsMoyen()
            break
        elif ask == "4":
            divisionsMoyen()
            break


def choixDifficile():

    while True:

        print("choisissez entre ces 4 opération : ")
        print("1 - addition")
        print("2 - soustraction")
        print("3 - multiplication")
        print("4 - division")

        ask = input("entrer votre choix(1, 2, 3 ou 4) : ")

        if ask == "1":
            additionsDifficile()
            break
        elif ask == "2":
            soustractionsDifficile()
            break
        elif ask == "3":
            multiplicationsDifficile()
            break
        elif ask == "4":
            divisionsDifficile()
            break

# =============================================
# Choix de la Difficulé
# =============================================


def choixDifficulte():
    
    while True:

        print("vous avez le choix entre 3 niveau de difficulté : ")
        print("F - Facile")
        print("M - moyen")
        print("D - Difficile")

        askDifficulty = input("Choisissez votre niveau de difficulté (F, M, D): ")

        if askDifficulty == "F":
            choixFacile()
            break
        elif askDifficulty == "M":
            choixDifficile()
            break
        elif askDifficulty == "D":
            choixDifficile()
            break

choixDifficulte()
