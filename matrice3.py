matrice = []

for i in range(3):
    colonne = []
    for j in range(3):
        coeff = int(input(f"entrer la ligne {i+1} la colonne {j+1} | a{i+1}/{j+1} : "))
        
        colonne.append(coeff)
    matrice.append(colonne)


def afficherMatrice(matrice, message) :
    print()
    print("="*5 , f"{message}", "="*5)
    for i in range(3) :
        for j in range(3) :
            print(matrice[i][j], end="\t")
        print()
    # print()




def transposer(matrice) :
    tMatrice = [[0,0,0],[0,0,0],[0,0,0]]

    for i in range(3) :
        for j in range(3) :
            tMatrice[j][i] = matrice[i][j]
    afficherMatrice(tMatrice, "Matrice transposé")
    return tMatrice
transposer(matrice)



mInversible = False
def det(matrice) :
    global mInversible
    print("="*5, "det", "="*5)
    a = matrice[0][0]
    b = matrice[0][1]
    c = matrice[0][2]
    d = matrice[1][0]
    e = matrice[1][1]
    f = matrice[1][2]
    g = matrice[2][0]
    h = matrice[2][1]
    i = matrice[2][2]

    det = a*(e*i-h*f) - b*(d*i-g*h) + c*(d*h-g*e)
    if det != 0:
        mInversible = True

    print(f"det(M) = {det}")
    return det
determinant = det(matrice)


def echelonneMatrice(matrice):
    matrice_echelone = [
        [matrice[0][0], matrice[0][1], matrice[0][2]],
        [matrice[1][0], matrice[1][1], matrice[1][2]],
        [matrice[2][0], matrice[2][1], matrice[2][2]],
    ]

    alpha = matrice_echelone[0][0]
    beta = matrice_echelone[1][0]
    gama = matrice_echelone[2][0]

    l1 = matrice_echelone[0]
    l2 = matrice_echelone[1]
    l3 = matrice_echelone[2]

    # Echelonné la deuxieme ligne
    for i in range(3):
        l2[i] = alpha*l2[i] - beta * l1[i]

    # Echelonné la troisieme ligne
    for i in range(3):
        l3[i] = alpha*l3[i] - gama * l1[i]

    a = matrice_echelone[1][1]
    b = matrice_echelone[2][1]

    for i in range(3):
        l3[i] = a*l3[i] - b * l2[i]

    afficherMatrice(matrice_echelone, "la matrice echelonné")
    return matrice_echelone

format_echelonné = echelonneMatrice(matrice)
if (matrice[1][0] == 0 and matrice[2][0] == 0 and matrice[2][1] == 0) :
    print("matrice deja echelonne !")
else :
    format_echelonné


def rang(matrice):
    rang = 0

    for ligne in matrice:
        ligne_nulle = True

        for coeff in ligne:
            if coeff != 0:
                ligne_nulle = False

        if not ligne_nulle:
            rang += 1

    print(f"rang(M) = {rang}")
    return rang
rang_matrice = rang(format_echelonné)

if rang_matrice == 3 :
    print("+ les vecteur des matrice sont libre")
    for i,ligne in enumerate(matrice) :
        print(f"v{i+1} = {tuple(ligne)}")
else :
    print("+ les vecteur des matrice sont liée")


def com(matrice) :
    coMatrice = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]

    a = matrice[0][0]
    b = matrice[0][1]
    c = matrice[0][2]
    d = matrice[1][0]
    e = matrice[1][1]
    f = matrice[1][2]
    g = matrice[2][0]
    h = matrice[2][1]
    i = matrice[2][2]

    coMatrice[0][0] = e*i - h*f
    coMatrice[0][1] = -(d*i - g*f)
    coMatrice[0][2] = d*h - g*e

    coMatrice[1][0] = -(b*i - c*h)
    coMatrice[1][1] = a*i - g*c
    coMatrice[1][2] = -(a*h - g*b)

    coMatrice[2][0] = b*f - e*c
    coMatrice[2][1] = -(a*f - d*c)
    coMatrice[2][2] = a*e - b*d

    afficherMatrice(coMatrice, "coMatrice")
    return coMatrice

com_matrice = com(matrice)


def inverse(matrice):
    from fractions import Fraction
    matrice_inversible = [[0,0,0],[0,0,0],[0,0,0]]
    
    com_transposer = transposer(com_matrice)
    
    det_inv = Fraction(1,determinant)

    for i in range(3) :
        for j in range(3) :
            matrice_inversible[i][j] = Fraction(det_inv * com_transposer[i][j])
    
    afficherMatrice(matrice_inversible,"Matrice inversible")

if mInversible :
    inverse(matrice)
else :
    print("la matrice n'est pas inverse")