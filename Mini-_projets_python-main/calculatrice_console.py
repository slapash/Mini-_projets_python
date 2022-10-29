#Calculatrice dans la console
def menu():
    global quitter
    choix = input("Choisissez l'opération que vous voulez effectuer:\n+ : addition\nx : multiplication\n- : soustraction\nD : division\nQ : quitter\n------------------\n")
    if choix == "+":
        addition(input_deux_chiffres())
    elif choix == "Q":
        quitter = True
    elif choix == "x":
        multiplaction(input_deux_chiffres())
    elif choix == "-":
        soustraction(input_deux_chiffres())
    elif choix == "D":
        division(input_deux_chiffres())
        
    else:
        print("saisie incorrecte")
        menu()
        
def division(chiffres_input):
    (premier, second) = chiffres_input
    try:
        print("le resultat:", premier / second, end="\n\n")
    except:
        print("opération invalide")
def soustraction(chiffres_input):
    (premier, second) = chiffres_input
    print("le resultat:", premier - second, end="\n\n")

def multiplaction(chiffres_input):
    (premier, second) = chiffres_input
    print("le resultat:", premier * second, end="\n\n")

def addition(chiffres_input):
    (premier, second) = chiffres_input
    print("le resultat:", premier + second, end="\n\n")
    
def input_deux_chiffres():
    premier_chiffre = float(input("entrez le premier chiffre : "))
    second_chiffre = float(input("entrez le second chiffre : "))
    return premier_chiffre, second_chiffre

quitter = False

while quitter == False:
    menu()