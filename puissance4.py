import time

def AfficheGrille(list):
    for i in range(7):
        print(list[0][i],list[1][i],list[2][i],list[3][i],list[4][i],list[5][i],list[6][i],list[7][i])
        
def ColonneADeLaPlace(colonne,grille):
    if grille[colonne][0]=="  ":
        return True
    return False

def Pasfini(grille):
    if "  " in grille[1]:
        return True
    elif "  " in grille[2]:
        return True
    elif "  " in grille[3]:
        return True
    elif "  " in grille[4]:
        return True
    elif "  " in grille[5]:
        return True
    elif "  " in grille[6]:
        return True
    elif "  " in grille[7]:
        return True
    return False

def MettreColonne(grille,colonne,cjoueur):
    if Pasfini(grille):
            if ColonneADeLaPlace(colonne,grille):
                i=5
                if grille[colonne][i]=="  ":
                    grille[colonne][i]=cjoueur
                else:
                    while grille[colonne][i]!="  ":
                        i-=1
                    grille[colonne][i]=cjoueur
            else:
                print("")
                print("Il n'y a plus aucun emplacement de libre, vous passez votre tour..")
                time.sleep(3)
                jouer=False
    else:
        print("Grille pleine")
        jouer=False
        
def testgagne(grille):
    #horizontalement 
    for i in range(6):
        if grille[1][i]==grille[2][i]==grille[3][i]==grille[4][i]!="  ":
            grille[1][i]="⚫"
            grille[2][i]="⚫"
            grille[3][i]="⚫"
            grille[4][i]="⚫"
            return True
        elif grille[2][i]==grille[3][i]==grille[4][i]==grille[5][i]!="  ":
            grille[2][i]="⚫"
            grille[3][i]="⚫"
            grille[4][i]="⚫"
            grille[5][i]="⚫"
            return True
        elif  grille[3][i]==grille[4][i]==grille[5][i]==grille[6][i]!="  ":
            grille[3][i]="⚫"
            grille[4][i]="⚫"
            grille[5][i]="⚫"
            grille[6][i]="⚫"
            return True 
        elif grille[4][i]==grille[5][i]==grille[6][i]==grille[7][i]!="  ":
            grille[4][i]="⚫"
            grille[5][i]="⚫"
            grille[6][i]="⚫"
            grille[7][i]="⚫"
            return True 

    for i in range(7):#VERTICALEMENT
        if grille[i][5]==grille[i][4]==grille[i][3]==grille[i][2]!="  ":
            grille[i][5]="⚫"
            grille[i][4]="⚫"
            grille[i][3]="⚫"
            grille[i][2]="⚫"
            return True
        elif grille[i][4]==grille[i][3]==grille[i][2]==grille[i][1]!="  ":
            grille[i][4]="⚫"
            grille[i][3]="⚫"
            grille[i][2]="⚫"
            grille[i][1]="⚫"
            return True
        elif grille[i][3]==grille[i][2]==grille[i][1]==grille[i][0]!="  ":
            grille[i][3]="⚫"
            grille[i][2]="⚫"
            grille[i][1]="⚫"
            grille[i][0]="⚫"
            return True 
    
    #DIAGONALE VERS LA DROITE
    if grille[1][3]==grille[2][2]==grille[3][1]==grille[4][0]!="  ":
        grille[1][3]="⚫"
        grille[2][2]="⚫"
        grille[3][1]="⚫"
        grille[4][0]="⚫"
        return True
    elif grille[1][4]==grille[2][3]==grille[3][2]==grille[4][1]!="  ":
        grille[1][4]="⚫"
        grille[2][3]="⚫"
        grille[3][2]="⚫"
        grille[4][1]="⚫"
        return True
    elif grille[5][0]==grille[2][3]==grille[3][2]==grille[4][1]!="  ":
        grille[5][0]="⚫"
        grille[2][3]="⚫"
        grille[3][2]="⚫"
        grille[4][1]="⚫"
        return True
    elif grille[1][5]==grille[2][4]==grille[3][3]==grille[4][2]!="  ":
        grille[1][5]="⚫"
        grille[2][4]="⚫"
        grille[3][3]="⚫"
        grille[4][2]="⚫"
        return True
    elif grille[5][1]==grille[2][4]==grille[3][3]==grille[4][2]!="  ":
        grille[5][1]="⚫"
        grille[2][4]="⚫"
        grille[3][3]="⚫"
        grille[4][2]="⚫"
        return True
    elif grille[5][1]==grille[6][0]==grille[3][3]==grille[4][2]!="  ":
        grille[5][1]="⚫"
        grille[6][0]="⚫"
        grille[3][3]="⚫"
        grille[4][2]="⚫"
        return True
    elif grille[2][5]==grille[3][4]==grille[4][3]==grille[5][2]!="  ":
        grille[2][5]="⚫"
        grille[3][4]="⚫"
        grille[4][3]="⚫"
        grille[5][2]="⚫"
        return True
    elif grille[6][1]==grille[3][4]==grille[4][3]==grille[5][2]!="  ":
        grille[6][1]="⚫"
        grille[3][4]="⚫"
        grille[4][3]="⚫"
        grille[5][2]="⚫"
        return True
    elif grille[6][1]==grille[7][0]==grille[4][3]==grille[5][2]!="  ":
        grille[6][1]="⚫"
        grille[7][0]="⚫"
        grille[4][3]="⚫"
        grille[5][2]="⚫"
        return True
    elif grille[3][5]==grille[4][4]==grille[5][3]==grille[6][2]!="  ":
        grille[3][5]="⚫"
        grille[4][4]="⚫"
        grille[5][3]="⚫"
        grille[6][2]="⚫"
        return True
    elif grille[7][1]==grille[4][4]==grille[5][3]==grille[6][2]!="  ":
        grille[7][1]="⚫"
        grille[4][4]="⚫"
        grille[5][3]="⚫"
        grille[6][2]="⚫"
        return True
    elif grille[4][5]==grille[5][4]==grille[6][3]==grille[7][2]!="  ":
        grille[4][5]="⚫"
        grille[5][4]="⚫"
        grille[6][3]="⚫"
        grille[7][2]="⚫"
        return True
    #DIAGONALE VERS LA GAUCHE
    if grille[1][2]==grille[2][3]==grille[3][4]==grille[4][5]!="  ":
        grille[1][2]="⚫"
        grille[2][3]="⚫"
        grille[3][4]="⚫"
        grille[4][5]="⚫"
        return True
    elif grille[5][5]==grille[4][4]==grille[3][3]==grille[2][2]!="  ":
        grille[5][5]="⚫"
        grille[4][4]="⚫"
        grille[3][3]="⚫"
        grille[2][2]="⚫"
        return True 
    elif grille[1][1]==grille[4][4]==grille[3][3]==grille[2][2]!="  ":
        grille[1][1]="⚫"
        grille[4][4]="⚫"
        grille[3][3]="⚫"
        grille[2][2]="⚫"
        return True 
    elif grille[6][5]==grille[5][4]==grille[4][3]==grille[3][2]!="  ":
        grille[6][5]="⚫"
        grille[5][4]="⚫"
        grille[4][3]="⚫"
        grille[3][2]="⚫"
        return True 
    elif grille[2][1]==grille[5][4]==grille[4][3]==grille[3][2]!="  ":
        grille[2][1]="⚫"
        grille[5][4]="⚫"
        grille[4][3]="⚫"
        grille[3][2]="⚫"
        return True
    elif grille[2][1]==grille[1][0]==grille[4][3]==grille[3][2]!="  ":
        grille[2][1]="⚫"
        grille[1][0]="⚫"
        grille[4][3]="⚫"
        grille[3][2]="⚫"
        return True
    elif grille[7][5]==grille[6][4]==grille[5][3]==grille[4][2]!="  ": 
        grille[7][5]="⚫"
        grille[6][4]="⚫"
        grille[5][3]="⚫"
        grille[4][2]="⚫"
        return True
    elif grille[3][1]==grille[6][4]==grille[5][3]==grille[4][2]!="  ":
        grille[3][1]="⚫"
        grille[6][4]="⚫"
        grille[5][3]="⚫"
        grille[4][2]="⚫"
        return True    
    elif grille[3][1]==grille[2][0]==grille[5][3]==grille[4][2]!="  ":
        grille[3][1]="⚫"
        grille[2][0]="⚫"
        grille[5][3]="⚫"
        grille[4][2]="⚫"
        return True    
    elif grille[7][4]==grille[6][3]==grille[5][2]==grille[4][1]!="  ":
        grille[7][4]="⚫"
        grille[6][3]="⚫"
        grille[5][2]="⚫"
        grille[4][1]="⚫"
        return True    
    elif grille[3][0]==grille[6][3]==grille[5][2]==grille[4][1]!="  ":
        grille[3][0]="⚫"
        grille[6][3]="⚫"
        grille[5][2]="⚫"
        grille[4][1]="⚫"
        return True
    elif grille[7][3]==grille[6][2]==grille[5][1]==grille[4][0]!="  ":
        grille[7][3]="⚫"
        grille[6][2]="⚫"
        grille[5][1]="⚫"
        grille[4][0]="⚫"
        return True 
    
    return False

grille=[["1","2","3","4","5","6"," "],["  ","  ","  ","  ","  ","  "," 1"],["  ","  ","  ","  ","  ","  "," 2"],["  ","  ","  ","  ","  ","  "," 3"],["  ","  ","  ","  ","  ","  "," 4"],["  ","  ","  ","  ","  ","  "," 5"],["  ","  ","  ","  ","  ","  "," 6"],["  ","  ","  ","  ","  ","  "," 7"]]
print("Bienvenue dans le jeu du Puissance 4 !")
time.sleep(1)
règles=input("Connaissez-vous les règles du jeu ?")
if règles=="non" or règles=="Non":
    print("D'accord, voici quelques explications :")
    time.sleep(1)
    print("")
    print("Le Puissance4 se joue à deux. Les joueurs lâchent leurs jetons à tour de rôle.")
    time.sleep(4)
    print("")
    print("Pour gagner une partie de puissance 4, il suffit d'être le premier à aligner 4 jetons de sa couleur horizontalement, verticalement ou diagonalement.")
    time.sleep(4)
    print("")
    print("Vous aurez la possibilité d'envoyer votre jeton dans les colonnes numérotées de 1 à 7.")
    time.sleep(4)
    print("")
    print("Si lors d'une partie, tous les jetons sont joués sans qu'il y est d'alignement de jetons, la partie s'arrête.Si le joueur envoie son jeton dans une colonne déjà pleine, il passera son tour.")
    time.sleep(6)
    print("")
    print("Pour plus de visibilité, en cas de victoire, les jetons qui permettent celle-ci seront de couleur noire. ")
    time.sleep(6)
    print("")
else:
    print("")
    print("")
    print("Attention, lors d'une victoire les 4 jetons alignés seront de couleur noir pour identifier correctement l'origine de la victoire.")
    time.sleep(3)
    print()
    print()
    print("Très bien, nous allons commencer.")
    time.sleep(1)
joueur1=input("Quel est le prénom du Joueur1 ?")
joueur2=input("Et vous, joueur 2 ?")
print()
print(joueur1,"quelle couleur de jeton voulez-vous")
couleur=input("jaune ou rouge ?")
print()
if couleur=="jaune":
    cjoueur1="🟡"
    cjoueur2="🔴"
    print(joueur2,"aura donc les jetons rouges.")
elif couleur=="rouge":
    cjoueur1="🔴"
    cjoueur2="🟡"
    print(joueur2,"aura donc les jetons jaunes.")
else:
    print("ERREUR, on a dit jaune ou rouge..")
    print()
    print(joueur1,"aura les jetons jaunes.")
    print(joueur2,"aura donc les jetons rouges")
    cjoueur1="🟡"
    cjoueur2="🔴"
time.sleep(3)
print("")
print("")
jouer=True
tour=1
i=5
scorej1=0
scorej2=0
reset=False
while jouer:
    if reset:
        grille=[["1","2","3","4","5","6"," "],["  ","  ","  ","  ","  ","  "," 1"],["  ","  ","  ","  ","  ","  "," 2"],["  ","  ","  ","  ","  ","  "," 3"],["  ","  ","  ","  ","  ","  "," 4"],["  ","  ","  ","  ","  ","  "," 5"],["  ","  ","  ","  ","  ","  "," 6"],["  ","  ","  ","  ","  ","  "," 7"]]
        tour=1
        print()
        invjetons=input("Voulez-vous inverser la couleur des jetons ?")
        if invjetons=="Oui" or invjetons=="oui":
            if cjoueur1=="🟡":
                cjoueur1="🔴"
                cjoueur2="🟡"
            else:
                cjoueur1="🟡"
                cjoueur2="🔴"
            time.sleep(1)
            print()
            print("Changement bien pris en compte.")
            time.sleep(1)
            print("")
            print(joueur1,cjoueur1)
            print(joueur2,cjoueur2)
            time.sleep(3)
            print("")
            print("")
        reset=False
    tour+=1
    tourpair=[0,2,4,6,8,10,12,14,16,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50]
    tourimpair=[1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49,51]
    if tour in tourpair:
        AfficheGrille(grille)
        print("Jouez",joueur1)
        colonne=int(input("Quelle colonne ? (1à7)"))
        if colonne>7 or colonne<1:
            print("Nous sommes désolés, le jeu comporte uniquement 7 colonnes.")
        else:
            MettreColonne(grille,colonne,cjoueur1)
            print()
            print()
            if testgagne(grille):
                print("Bravo !")
                print("Le gagnant est",joueur1)
                time.sleep(1)
                AfficheGrille(grille)
                time.sleep(4)
                scorej1+=1
                print("Voici vos scores :")
                print(joueur1,scorej1)
                print(joueur2,scorej2)
                partie=input("Souhaitez vous relancer une partie ?")
                if partie=="oui" or partie=="Oui":
                    jouer=True
                    reset=True
                else:
                    jouer=False
                    print("A bientôt!")
    elif tour in tourimpair:
        AfficheGrille(grille)
        print("Jouez",joueur2)
        colonne=int(input("Quelle colonne ? (1à7)"))
        if colonne>7 or colonne<1:
            print("Nous sommes désolés, le jeu comporte uniquement 7 colonnes.")
        else:
            MettreColonne(grille,colonne,cjoueur2)
            print()
            print()
            if testgagne(grille):
                print("Bravo !")
                time.sleep(1)
                print("Le gagnant est",joueur2)
                AfficheGrille(grille)
                time.sleep(4)
                scorej2+=1
                print("Voici vos scores :")
                print(joueur1,scorej1)
                print(joueur2,scorej2)
                partie=input("Souhaitez vous relancer une partie ?")
                if partie=="oui" or partie=="Oui":
                    jouer=True
                    reset=True
                else:
                    jouer=False
                    print("")
                    print("A bientôt !")

    
    
