#exercice login




logins = { }

#collecte les informations de l'utilisateur
def compte_input():
    pseudo = input("entrez votre pseudo : ")
    mot_de_passe = input("entrez votre mot de passe : ")
    return (pseudo, mot_de_passe)

#menu principal
def afficher_menu():
    menu = input(" 1 : nouveau compte \n 2 : se connecter \n 3 : quitter 4 : afficher les comptes")
    if menu == "1":
        tuple_p_m = compte_input()
        pseudo = ''.join(tuple_p_m[0:1])
        mdp = ''.join(tuple_p_m[1:2])
        nouveau_compte(pseudo, mdp)

    if menu == "2":
        se_connecter()
        
    
    if menu == "3":
        global quit
        quit = True
    
    if menu == "4":
        afficher_comptes()
        
#vérifie si les logins sont dans la base de données et s'ils sont corrects
def se_connecter():
    tuple_p_m = compte_input()
    pseudo =''.join(tuple_p_m[0:1])
    mdp = ''.join(tuple_p_m[1:2])


    try: 
        if logins[mdp] == pseudo:
            print("vous etes connectés")
            afficher_menu_in()
    except:
        print("logins incorrects")
        afficher_menu_in()
    
#affiche un menu apres avoir effectué une action
def afficher_menu_in():
    menu_in = input("3 : quitter \n 4 : menu")
    if menu_in =="4":
        afficher_menu()

    if menu_in == "3":
        global quit 
        quit = True

#affiche les comptes inscrits dans la base de donnée
def afficher_comptes():
    print(logins)
    afficher_menu_in()

#inscrire un nouveau compte dans la base de donnée
def nouveau_compte(pseudo, mot_de_passe):
    logins[mot_de_passe] = pseudo
    print("votre compte a été créé au nom de", pseudo)
    afficher_menu_in()
    return 0



quit = False

while (quit != True):
    
    afficher_menu()

    