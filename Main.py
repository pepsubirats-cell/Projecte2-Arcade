from jocs import janken, nana

def mostrar_menu():
    print("")
    print("Benvingut al menu de jocs")
    print("1. Pedra, paper o tisores")
    print("2. Endevinar numeros")
    print("S. Sortir")

def main():
    while True:
        mostrar_menu()
        opcio = input("Selecciona una opcio (1, 2, S): ").strip().upper()

        if opcio == '1':
            janken()
        elif opcio == '2':
            nana()
        elif opcio == 'S':
            print("Gracies per jugar")
            break
        else:
            print("Opcio no valida")

if __name__ == "__main__":
    main()
