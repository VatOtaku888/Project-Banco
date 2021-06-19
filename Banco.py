#.......MODULOS.......#
from time import sleep;
import colorama #Modulo colorama
from colorama import Fore, Back, Style #Estilos 
colorama.init (autoreset = True) 

#......COMIENZO.......#
sleep(1)
print(f"""{Fore.GREEN}
     _ )    \     \ |   __|   _ \    
     _ \   _ \   .  |  (     (   |   
     ___/ _/  _\ _|\_| \___| \___/    

  _ \ _ \   _ \     | __|   __| __ __| 
  __/   /  (   | \  | _|   (       |   
 _|  _|_\ \___/ \__/ ___| \___|   _|   
                                                                                                                                                        
""")
sleep(1)
print(f"""
{Fore.YELLOW}[-]{Style.RESET_ALL}     HOLA BIENVENIDO AL BANCO DESEAS
{Fore.YELLOW}[-]{Style.RESET_ALL}     VER TU DINERO? O METERLE DINERO
{Fore.YELLOW}[-]{Style.RESET_ALL}     A TU CUENTA DE BANCO? {Fore.GREEN}Y/N
""")

#.......CODES........#


BancoStart = str(input(f":")) #input de comienzo
D = 0 #Dinero Valor NUmerico
count = 1

#.......BANCO........#
while count < 2: # Ciclo De el programa
    if BancoStart == "Yes" or BancoStart == "yes" or BancoStart == "YES" or BancoStart == "Y" or BancoStart == "y": #Eleccion Aceptar
        print(f"""
{Fore.YELLOW}[E]{Style.RESET_ALL}     Hay multiples funciones
{Fore.YELLOW}[O]{Style.RESET_ALL}     Opciones:
{Fore.YELLOW}[T]{Style.RESET_ALL}     {Fore.GREEN}saldo,Trabajo,Donar{Style.RESET_ALL} Y para cerrar el programa usa {Fore.GREEN}end{Style.RESET_ALL}
        """)
#......MENUS........#
        Op = str(input(":")) # Opciones
        if Op == "Saldo" or Op == "saldo" or Op == "SALDO":
            print(f"""
{Fore.YELLOW}[S]{Style.RESET_ALL}     Tu sueldo Es {Fore.GREEN}{D}{Style.RESET_ALL}
        """)

#......TRABAJOS.....#

        elif Op == "Trabajo" or Op == "trabajo" or Op == "TRABAJO":
            print(f"""
\n{Fore.YELLOW}[E]{Style.RESET_ALL}     Trabajos:
{Fore.YELLOW}[T]{Style.RESET_ALL}     {Fore.GREEN}Bombero,Policia,Prostituta{Style.RESET_ALL} y usa {Fore.GREEN}Regresar{Style.RESET_ALL} Para salir de el menu de trabajo
            """)

#.......POLICIA.....#

            Trabajos = str(input(":"))
            sleep(1)
            if Trabajos == "Policia" or Trabajos == "POLICIA" or Trabajos == "policia":
                
                G= 1000 #Ganancias
                D= D + G #Acumulador
                print(f"""
\n{Fore.YELLOW}[P]{Style.RESET_ALL}     Trabajaste para policia y el dinero que ganaste fue {Fore.GREEN}{G}{Style.RESET_ALL} Dolares\n
""")

#......PROSTITUTA..#

            elif Trabajos == "Prostituta" or Trabajos == "prostituta" or Trabajos == "PROSTITUTA":
                G= 1000 #Ganancias
                D= D + G #Acumulador
                print(f"""
\n{Fore.YELLOW}[P]{Style.RESET_ALL}     Trabajaste para ser una PUTA XD y ganaste {Fore.GREEN}{G}{Style.RESET_ALL} Dolares\n
                """)

#.......BOMBERO...#

            elif Trabajos == "Bombero" or Trabajos == "BOMBERO" or Trabajos == "bombero":
                G= 1000 #Ganancias
                D = D + G #Acumulador
                print(f"""
\n{Fore.YELLOW}[B]{Style.RESET_ALL}     Trabajaste Para Bombero, Salvaste el día!! y ganaste {Fore.GREEN}{G}{Style.RESET_ALL} Dolares\n
""")

#.......REGRESAR-#

            elif Trabajos == "Regresar" or Trabajos == "regresar" or Trabajos == "REGRESAR":
                None

#CERRAR PROGRAMA#

            elif Trabajos == "End" or Trabajos == "end" or Trabajos == "END":
                count = count + 1

#.OPCION_INVALIDA.#

            else: 
                print(f"{Fore.YELLOW}[E]{Style.RESET_ALL}     {Fore.RED}Elige una Opcion Valida!!{Style.RESET_ALL}\n{Fore.YELLOW}[E]{Style.RESET_ALL}     {Fore.RED}Eso no es un trabajo que esta en la lista")

#....CERRAR MENU...#

        elif Op == "end" or Op == "END" or Op == "End":
            count = count + 1 #Acumulador

#.....DONACIONES...#

        elif Op == "Donar" or Op == "DONAR " or Op == "donar": #Opcion Donativa
            print(f"{Fore.YELLOW}[P]{Style.RESET_ALL}     Menciona a la persona que quieras ")
            PeR = str(input(":"))
            print(f"""
{Fore.YELLOW}[D]{Style.RESET_ALL}     Muy bien eligiste a {Fore.GREEN}{PeR}{Style.RESET_ALL} Cuanto Quieres donar?
            """)
            P = int(input(":"))
            Do = P

#....DINERO VALIDO.#

            if Do < D:
                D = D - P
                print(f"{Fore.YELLOW}[D]{Style.RESET_ALL}     Haz donado {Fore.GREEN}{Do}{Style.RESET_ALL} Dolares a {Fore.GREEN}{PeR}{Style.RESET_ALL} Ahora tienes {Fore.GREEN}{D}{Style.RESET_ALL} Dolares!!!")
            else:
                print(f"\n{Fore.YELLOW}[E]{Style.RESET_ALL}     {Fore.RED}Oopsss No tienes Tanto dinero para donar eso\n")
        else:
            print(f"{Fore.YELLOW}[E]{Style.RESET_ALL}     {Fore.RED}Error No Seleccionaste una opcion valida!{Style.RESET_ALL}\n{Fore.YELLOW}[E]{Style.RESET_ALL}     {Fore.RED}Vuelve a intentarlo")

#......ELECCION_NO....#

    elif BancoStart == "No" or BancoStart == "NO" or BancoStart == "no" or BancoStart == "nO" or BancoStart == "N" or BancoStart == "n":
        print(f"{Fore.YELLOW}[N]{Style.RESET_ALL}     Vuelva Pronto!!!!\n{Fore.YELLOW}[N]{Style.RESET_ALL}     Aunque No se por que decidiste elegir no")
        count = count + 1
    
#.....INVALIDO.......#

    else:
        count = count + 1
        print(f"{Fore.YELLOW}[E]{Style.RESET_ALL}     {Fore.RED}ELIGE UNA OPCION VALIDA{Style.RESET_ALL}\n{Fore.YELLOW}[E]{Style.RESET_ALL}     {Fore.RED}ESA NO ES UNA OPCION VALIDA")

