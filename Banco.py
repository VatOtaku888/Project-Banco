#.......MODULOS.......#
from time import sleep;
import colorama #Modulo colorama
from colorama import Fore, Back, Style #Estilos 
from colorama import Cursor,init,Fore
colorama.init (autoreset = True) 

#......COMIENZO.......#

print("\nHOLA BIENVENIDO AL BANCO DESEAS\nVER TU DINERO? O METERLE DINERO\nA TU CUENTA DE BANCO? " + f"{Fore.GREEN}Y/N")

#.......CODES........#


BancoStart = str(input(":")) #input de comienzo
D = 0 #Dinero Valor NUmerico
count = 1

#.......BANCO........#
while count < 2: # Ciclo De el programa
    if BancoStart == "Yes" or BancoStart == "yes" or BancoStart == "YES" or BancoStart == "Y" or BancoStart == "y": #Eleccion Aceptar
        print(f"\nHay multiples opciones\nOpciones\n" + Fore.GREEN + "saldo,Trabajo,Donar", "Y para cerrar el programa " + Fore.GREEN + "end")
#......MENUS........#
        Op = str(input(":")) # Opciones
        if Op == "Saldo" or Op == "saldo" or Op == "SALDO":
            print(f"\nTu sueldo Es " + Fore.GREEN + f"{D}")

#......TRABAJOS.....#

        elif Op == "Trabajo" or Op == "trabajo" or Op == "TRABAJO":
            print("\nTrabajos\n" +Fore.GREEN + "Policia,Prostuta,Bombero" + Fore.WHITE + " y usa "  +Fore.GREEN + " Regresar" + Fore.WHITE + " Para salir de el menu de trabajo")

#.......POLICIA.....#

            Trabajos = str(input(":"))
            sleep(1)
            if Trabajos == "Policia" or Trabajos == "POLICIA" or Trabajos == "policia":
                
                G= 1000 #Ganancias
                D= D + G #Acumulador
                print(f"\nTrabajaste para policia y el dinero que ganaste fue " + Fore.GREEN + f" {G}"+ Fore.WHITE + " Dolares\n")

#......PROSTITUTA..#

            elif Trabajos == "Prostituta" or Trabajos == "prostituta" or Trabajos == "PROSTITUTA":
                G= 1000 #Ganancias
                D= D + G #Acumulador
                print(f"\nTrabajaste para ser una PUTA XD y ganaste " + Fore.GREEN + f"{G}" + Fore.WHITE +  " Dolares\n")

#.......BOMBERO...#

            elif Trabajos == "Bombero" or Trabajos == "BOMBERO" or Trabajos == "bombero":
                G= 1000 #Ganancias
                D = D + G #Acumulador
                print(f"\nTrabajaste Para Bombero, Salvaste el día!! y ganaste "+ Fore.GREEN + f"{G} "+ Fore.WHITE + " Dolares\n")

#.......REGRESAR-#

            elif Trabajos == "Regresar" or Trabajos == "regresar" or Trabajos == "REGRESAR":
                None

#.OPCION_INVALIDA.#

            else: 
                print(Fore.RED + "Elige una Opcion Valida!!\nEso no es un trabajo que esta en la lista")

#....CERRAR MENU...#

        elif Op == "end" or Op == "END" or Op == "End":
            count = count + 1 #Acumulador

#.....DONACIONES...#

        elif Op == "Donar" or Op == "DONAR " or Op == "donar": #Opcion Donativa
            PeR = str(input(f"Menciona a la persona que quieras\n:"))
            P = int(input(f"Muy bien eligiste a "+ Fore.GREEN + f"{PeR}"+ Fore.WHITE + " Cuanto Quieres donar?\n:"))
            Do = P

#....DINERO VALIDO.#

            if Do < D:
                D = D - P
                print(f"Haz donado " + Fore.GREEN + f"{Do}" + Fore.WHITE + " Dolares a "+ Fore.GREEN + f"{PeR}"+ Fore.WHITE + " Ahora tienes "+ Fore.GREEN + f"{D}"+ Fore.WHITE +"D olares!!!")
            else:
                print(Fore.RED + "\nOopsss No tienes Tanto dinero para donar eso\n")
        else:
            print(f"{Fore.RED}Error No Seleccionaste una opcion valida!\nVuelve a intentarlo")

#......ELECCION_NO....#

    elif BancoStart == "No" or BancoStart == "NO" or BancoStart == "no" or BancoStart == "nO" or BancoStart == "N" or BancoStart == "n":
        print("Vuelva Pronto!!!!\nAunque No se por que decidiste elegir no")
        count = count + 1
    
#.....INVALIDO.......#

    else:
        count = count + 1
        print(Fore.RED + "ELIGE UNA OPCION VALIDA\nESA NO ES UNA OPCION VALIDA")

