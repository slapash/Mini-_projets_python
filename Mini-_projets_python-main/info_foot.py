#résultats matchs en cours 
#résultats anciens matchs
#joueurs équipe
#stats équipes 
#anciens résultats
class Equipe:

    def __init__(self, pays, joueurs, systeme_equipe, competitions, statistiques,entraineur):

        self.pays = pays
        self.joueurs = joueurs
        self.system_equipe = systeme_equipe
        self.competitions = competitions
        self.entraineur = entraineur
        self.statistiques = statistiques

BAR = Equipe("espagne", ["Stegen", "Pique", "Alonso", "Chreistensen", "Roberto"
            ,"Pedri", "Busquets", "Gavi", "Raphinha", "Lewandowski", "Dembele"],
            "4-3-3", ["Champions league", "La liga"],{
            "Matchs joués" : 22,
            "Victoires" : 14,
            "Nuls": 5,
            "Défaites" : 3}, "Xavi")

REA = Equipe("espagne", ["Courtois", "Mendy", "Alaba", "Militao", "Carvajal", "Kroos", "Tchouameni", "Modric", "Junior", "Benzema", "Valverde"],
            "4-3-3",["Champions league", "La liga"],{
             "Matchs joués" : 19,
             "Victoires" : 15,
             "Nuls" : 3,
             "Défaites" : 1   
            },"Carlo Ancelotti")

    

def menu():
    global quit
    affichage = input("Choisissez une équipe:\nBAR : FC Barcelone\nREA : Real Madrid\nQ : Quitter\n----------\n")
    if affichage == "Q":
        quit = True
    elif affichage == "BAR":
        menu_intern("BAR")
    elif affichage == "REA":
        menu_intern("REA")

def menu_intern(equipe):
    global quit
    affichage = input("1 : Pays\n2 : Joueurs\n3 : Systeme\n4 : Statistiques\n5 : Entraineur\nQ : Quitter\n----------\n")
    if affichage == "Q":
        quit = True
    if equipe == "BAR":
        if affichage == "1":
            print(BAR.pays)
        elif affichage == "2":
            print(BAR.joueurs)
        elif affichage == "3":
            print(BAR.system_equipe)
        elif affichage == "4":
            print(BAR.statistiques)
        elif affichage == "5":
            print(BAR.entraineur)
        elif affichage == "Q":
            quit = True
        else:
            print("entrée erronée")
    if equipe == "REA":
        if affichage == "1":
            print(REA.pays)
        elif affichage == "2":
            print(REA.joueurs)
        elif affichage == "3":
            print(REA.system_equipe)
        elif affichage == "4":
            print(REA.statistiques)
        elif affichage == "5":
            print(REA.entraineur)
        elif affichage == "Q":
            quit = True
        else:
            print("entrée erronée")

quit = False

while quit == False:
    menu()
