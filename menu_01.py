"""
Menú principal
"""

##  DECLARACIÓN DE MÉTODOS PARA EL PROGRAMA ##


# Método "login" #
"""
 "login": retorna "True" si los datos fueron accesados correctamente, de lo contrario retorna "False"
"""    
def login(user,pasword):  
    output1 = user in administradores
    if output1 == True:
        output2 = administradores[user] == pasword
        if output2 == True:
            print("Welcome: ",user)
            return True
        else:
            print("Contraseña incorrecta")
            return False
    else:
        print("user incorrecto")
        return False


## DEGLARACIÓN DE VARIABLES GLOBALES PARA EL PROGRAMA   ##

# diccionario con admin y contraseña #
administradores = {"Sharon":"sharon01","David":"david01"}


##  PROGRAMA PRINCIPAL  ##
while True:
    print("-----SISTEMA DE VENTAS-----")
    print("\t 1) Administrador")
    print("\t 2) Cliente")
    print("\t 3) Salir")
    opcion = int(input("Escribe la opción deseada: "))
    if opcion == 1:
        print("Para ingresar escribe tu usuario y contraseña de ADMINISTRADOR")
        usuario = input("Usuario: ")
        contraseña = input("Contraseña: ")
        if login(usuario,contraseña) == True:
            print("")
    elif opcion == 2:
        pass
    elif opcion == 3:
        print("Gracias por usar nuestra Aerolinea, vuelva pronto!")
        break
    
    print("\n")




