#......COMIENZO.......#

print('''
HOLA BIENVENIDO AL BANCO DESEAS 
VER TU DINERO? O METERLE DINERO 
A TU CUENTA DE BANCP? Y/N
''')
#.......MODULOS......#

import colorama #Modulo colorama
from colorama import Fore, Back, Style #Estilos 
colorama.init (autoreset = True) 

#.......CODES........#

BancoStart = str(input(":")) #input de comienzo
D = 0 #Dinero Valor NUmerico
count = 1
#.......BANCO........#
while count < 2: # Ciclo De el programa
    if BancoStart == "Yes" or BancoStart == "yes" or BancoStart == "YES" or BancoStart == "Y": #Eleccion Aceptar
        print('''
En este banco online hay demasiadas opciones 
Ejemplo:
saldo, Trabajo, Donar y para cerrar el programa end
            ''')
#......MENUS........#
        Op = str(input(":")) # Opciones
        if Op == "Saldo" or Op == "saldo" or Op == "SALDO":
            print(Fore.GREEN + f"\nTu sueldo Es {D} ")

#......TRABAJOS.....#

        elif Op == "Trabajo":
            print(Fore.GREEN + '''
TRABAJOS:
Policia, Prostituta, Bombero
                 ''')

#.......POLICIA.....#

            Trabajos = str(input(":"))
            if Trabajos == "Policia" or Trabajos == "POLICIA" or Trabajos == "policia":
                G= 1000 #Ganancias
                D= D + G #Acumulador
                print(f"\nTrabajaste para policia y el dinero que ganaste fue {G} Dolares\n")

#......PROSTITUTA..#

            elif Trabajos == "Prostituta" or Trabajos == "prostituta" or Trabajos == "PROSTITUTA":
                G= 1000 #Ganancias
                D= D + G #Acumulador
                print(f"\nTrabajaste para ser una PUTA XD y ganaste {G} Dolares\n")

#.......BOMBERO...#

            elif Trabajos == "Bombero" or Trabajos == "BOMBERO" or Trabajos == "bombero":
                G= 1000 #Ganancias
                D = D + G #Acumulador
                print(f"\nTrabajaste Para Bombero, Salvaste el día!! y ganaste {G} Dolares\n")

#.OPCION_INVALIDA.#

            else: 
                print(Fore.RED + "Elige una Opcion Valida!!\nEso no es un trabajo que esta en la lista")

#....CERRAR MENU...#

        elif Op == "end" or Op == "END" or Op == "End":
            count = count + 1 #Acumulador

#.....DONACIONES...#

        elif Op == "Donar" or Op == "DONAR " or Op == "donar": #Opcion Donativa
            PeR = str(input(f"Menciona a la persona que quieras\n:"))
            P = int(input(f"Muy bien eligiste a {PeR} Cuanto Quieres donar?\n:"))
            Do = P

#....DINERO VALIDO.#

            if Do < Dinero:
                Dinero = Dinero - Do
                print(f"Haz donado {Do} Dolares a {PeR} Ahora tienes {D} Dolares!!")
            else:
                print("Oopsss No tienes Tanto dinero para donar eso")
        else:
            print(Fore.RED + '''
Error No Seleccionaste una opcion valida!
Vuelve a intentarlo
            ''')

#......ELECCION_NO....#

    elif BancoStart == "No" or BancoStart == "NO" or BancoStart == "no" or BancoStart == "nO" or BancoStart == "N":
        print('''
Vuelva Pronto!!!!
Aunque No se por que decidiste elegir no
        ''')
        count = count + 1
    
#.....INVALIDO.......#

    else:
        count = count + 1
        print(Fore.RED + "ELIGE UNA OPCION VALIDA\nESA NO ES UNA OPCION VALIDA")

