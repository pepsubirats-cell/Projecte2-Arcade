import random

# JOC 1: PEDRA, PAPER, TISORES
def janken():
    opcions = ['pedra', 'paper', 'tisores']
    resultat = {'guanyes': 0, 'perds': 0, 'empats': 0}

    print("Benvingut a Pedra, Paper o Tisores!")
    print("Selecciona el mode de joc:")
    print("1. Al millor de 3")
    print("2. Al millor de 5")
    
    while True:
        mode = input("Selecciona el mode (1 o 2): ")
        if mode == '1':
            rondes_a_guanyar = 2
            break
        elif mode == '2':
            rondes_a_guanyar = 3
            break
        else:
            print("Mode no valid. Torna-ho a intentar.")

    while resultat['guanyes'] < rondes_a_guanyar and resultat['perds'] < rondes_a_guanyar:
        jugada_usuari = input("Introdueix la teva jugada (pedra, paper, tisores) o 'sortir' per acabar: ").lower()
        
        if jugada_usuari == 'sortir':
            print("Sortint del joc...")
            break
            
        if jugada_usuari not in opcions:
            print("Jugada no valida. Torna-ho a intentar.")
            continue
        
        jugada_robot = random.choice(opcions)
        print("El robot ha triat:", jugada_robot)
        


        if jugada_usuari == jugada_robot:
            resultat['empats'] += 1
            print("Empat")
        elif (
            (jugada_usuari == 'pedra' and jugada_robot == 'tisores') or
            (jugada_usuari == 'paper' and jugada_robot == 'pedra') or
            (jugada_usuari == 'tisores' and jugada_robot == 'paper')
        ):
            resultat['guanyes'] += 1
            print("Has guanyat aquesta ronda")
        else:
            resultat['perds'] += 1
            print("Has perdut aquesta ronda")
        
        print("Marcador: Tu", resultat['guanyes'], "-", resultat['perds'], "Robot (Empats:", resultat['empats'], ")")

    if resultat['guanyes'] == rondes_a_guanyar:
        print("HAS GUANYAT LA PARTIDA")
    elif resultat['perds'] == rondes_a_guanyar:
        print("Has perdut la partida")
    
    print("Resultats finals: Tu", resultat['guanyes'], "-", resultat['perds'], "Robot (Empats:", resultat['empats'], ")")


# JOC 2: ENDEVINAR EL NUMERO
def nana():
    nombre_secret = random.randint(1, 100)
    intents = 0
    
    print("He pensat un nombre entre 1 i 100")
    
    while True:
        entrada = input("Introdueix un numero: ")
        
        if entrada == 'sortir':
            print("El numero era", nombre_secret)
            break
        
        numero_usuari = int(entrada)
        intents += 1
        
        if numero_usuari < nombre_secret:
            print("Massa baix")
        elif numero_usuari > nombre_secret:
            print("Massa alt")
        else:
            print("Has endevinat el numero")
            print("El numero era", nombre_secret)
            print("Has necessitat", intents, "intents")
            break

        #quebin

        