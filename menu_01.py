"""
Menú principal
"""
## IMPORTACION DE LIBRERIAS ##
import getpass

##  DECLARACIÓN DE CLASES   ##
class Vuelo:
    def __init__(self, destino, horasalida, horallegada, costoturista, costonegocios, costoprimera, lugaresturista, lugaresnegocios, lugaresprimera, fechasalida):
        self.destino = destino
        self.horasalida = horasalida
        self.horallegada = horallegada
        self.costoturista = int(costoturista)
        self.costonegocios = int(costonegocios)
        self.costoprimera = int(costoprimera)
        self.lugaresturista = int(lugaresturista)
        self.lugaresnegocios = int(lugaresnegocios)
        self.lugaresprimera = int(lugaresprimera)
        self.fechasalida = fechasalida

class Persona:
    def __init__(self, nombre, apellido, edad, password):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.password = password

class Administrador(Persona):
    def __init__(self, nombre, apelldo, edad, password, carrera, sueldo):
        super().__init__(nombre, apelldo, edad, password)
        self.carrera = carrera
        self.sueldo = sueldo

class Usuario(Persona):
    def __init__(self, nombre, apelldo, edad, password, usuario):
        super().__init__(nombre, apelldo, edad, password)
        self.usuario = usuario

##  DECLARACIÓN DE MÉTODOS PARA EL PROGRAMA ##

# Login #
"""
 "login": retorna "True" si los datos fueron accesados correctamente, de lo contrario retorna "False"
"""    
def login(list):
    user = input("Usuario: ")
    password = getpass.getpass(prompt = "Contraseña: ")  
    output1 = user in list
    if output1 == True:
        temp1 = list[user]
        output2 = (password == temp1.password)
        if output2 == True:
            global usuarioactivo
            usuarioactivo =  user
            print("\t¡WELCOME!: ",usuarioactivo)
            print
            return True
        else:
            print("Contraseña incorrecta")
            return False
    else:
        print("Usuario incorrecto")
        return False

# Declarar vuelo #
"""
Se solicita al usuario todos los datos necesarios y se agrega un objeto de la clase Vuelo a la lista de vuelos
"""
def nuevovuelo():
    destino = input("Destino: ")
    hsalida = input("Hora Salida: ")
    hllegada = input("Hora Llegada: ")
    cturista = input("Costo de viaje Turista: ")
    cnegocios = input("Costo de viaje Negocios: ")
    cprimera = input("Costo de viaje Primera Clase: ")
    lturista = input("Lugares disponibles clase Turista: ")
    lnegocios = input ("Lugares disponibles clase Negocios: ")
    lprimera = input ("Lugares dispoibles Primera Clase: ")
    fsalida = input ("Fecha de salida: ")
    flight = Vuelo(destino,hsalida,hllegada,cturista,cnegocios,cprimera,lturista,lnegocios,lprimera,fsalida)
    listavuelos.append(flight)
    print("Vuelo registrado satisfactoriamente")

# Imprimir data de un vuelo#
def printvuelo(flight,number):
            print()
            print("VUELO NÚMERO ",number)
            print("\t 1) Destino: ",flight.destino)
            print("\t 2) Hora Salida: ",flight.horasalida)
            print("\t 3) Hora Llegada: ",flight.horallegada)
            print("\t 4) Costo de viaje Turista: ",flight.costoturista)
            print("\t 5) Costo de viaje Negocios: ",flight.costonegocios)
            print("\t 6) Costo de viaje Primera Clase: ",flight.costoprimera)
            print("\t 7) Lugares disponibles clase Turista: ",flight.lugaresturista)
            print("\t 8) Lugares disponibles clase Negocios: ",flight.lugaresnegocios)
            print("\t 9) Lugares dispoibles Primera Clase: ",flight.lugaresprimera)
            print("\t 10) Fecha de salida: ",flight.fechasalida)

# Listar vuelos registrados #
"""
Lista todos los vuelos que estan agregados en una lista, donde se especifica el número máximo de vuelos a numerar
"""
def listarvuelos(listinput,nmax):
    if len(listinput) == 0:
        print("No hay vuelos registrados")
    else:
        i = 0
        while i < nmax and i < len(listinput):
            Vuelo = listinput[i]
            print()
            print("VUELO NÚMERO ",i+1)
            print("Destino: ",Vuelo.destino)
            print("Hora Salida: ",Vuelo.horasalida)
            print("Hora Llegada: ",Vuelo.horallegada)
            print("Costo de viaje Turista: ",Vuelo.costoturista)
            print("Costo de viaje Negocios: ",Vuelo.costonegocios)
            print("Costo de viaje Primera Clase: ",Vuelo.costoprimera)
            print("Lugares disponibles clase Turista: ",Vuelo.lugaresturista)
            print("Lugares disponibles clase Negocios: ",Vuelo.lugaresnegocios)
            print("Lugares dispoibles Primera Clase: ",Vuelo.lugaresprimera)
            print("Fecha de salida: ",Vuelo.fechasalida)
            i += 1
            
# Listar vuelos registrados (Solo el nombre)#
def listavuelosname(listinput,nmax):
    if len(listinput) == 0:
        print("No hay vuelos registrados")
    else:
        i = 0
        while i < nmax and i < len(listinput):
            Vuelo = listinput[i]
            print()
            print("VUELO NÚMERO ",i+1)
            print("Destino: ",Vuelo.destino)
            i += 1

# Eliminación de un vuelo #
def deletevuelo(listinput, nmax):
    if len(listinput) == 0:
        print("Ya no quedan vuelos por eliminar")
    else:
        delete = int(input("Escribe el número del vuelo que deseas eliminar: "))
        if  delete > 0 and delete <= nmax and delete <= len(listinput):
            flight = listinput.pop(delete-1)
            print()
            print("Vuelo {0} con destino a {1}, eliminado con éxito".format(delete, flight.destino))
        else:
            print("El vuelo que especificaste no existe")

# Modificar dato de un vuelo #
def modificarvuelo(listinput, nmax):
    print()
    if len(listinput) == 0:
        print("No hay vuelos que puedas modificar")
    else:
        modify = int(input("Escribe el número del vuelo que deseas modificar: "))
        if  modify > 0 and modify <= nmax and modify <= len(listinput):
            Vuelo = listinput[modify-1]
            printvuelo(Vuelo,modify)
            print("\t 11) Regresar")
            opcion = int(input("Selecciona una opción para modificar: "))
            if opcion == 1:
                Vuelo.destino = input("Ingresa el nuevo destino: ")
            elif opcion == 2:
                Vuelo.horasalida = input("Ingresa la nueva hora de salida: ")
            elif opcion == 3:
                Vuelo.horallegada = input("Ingresa la nueva hora del llegada: ")
            elif opcion == 4:
                Vuelo.costoturista = input("Ingresa el nuevo costo del viaje Turista: ")
            elif opcion == 5:
                Vuelo.costonegocios = input("Ingresa el nuevo costo del viaje Negocios: ")
            elif opcion == 6:
                Vuelo.costoprimera = input("Ingresa el nuevo costo del viaje Primera Clase: ")
            elif opcion == 7:
                Vuelo.lugaresturista = input("Ingresa los nuevos lugares disponibles en Turista: ")
            elif opcion == 8:
                Vuelo.lugaresnegocios = input("Ingresa los nuevos lugares disponibles en Negocios: ")
            elif opcion == 9:
                Vuelo.lugaresprimera = input("Ingresa los nuevos lugares disponibles en Primera Clase: ")
            elif opcion == 10:
                Vuelo.fechasalida = input("Ingresa la nueva fecha de salida: ")
            elif opcion == 11:
                print("No se ha modificado nada del vuelo")
            print("Dato actualizado con éxito")
            printvuelo(Vuelo,modify)
        else:
            print("\t El vuelo que especificaste no existe")

# Obtener el mayor de un número #
def namemayor3(a, A, b, B, c, C): 
    value = a
    output = A
    if value < b:
        value = b
        output = B
        if value < c:
            value = c
            output = C
    return output

# Info administrador #
def infoadmin(user):
    temp1 = administradores[user]
    print("Nombre: ",temp1.nombre)
    print("Apellido: ",temp1.apellido)
    print("Edad: ",temp1.edad)
    print("Carrera: ",temp1.carrera)
    print("Sueldo: ",temp1.sueldo)

# Info usuario #
def infouser(user):
    temp1 = listausuarios[user]
    print("Nombre: ",temp1.nombre)
    print("Apellido: ",temp1.apellido)
    print("Edad: ",temp1.edad)
    print("Password: ",temp1.password)
    print("Usuario: ",temp1.usuario)

# Registro usuario nuevo #
def nuevousuario():
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    edad = input("Edad: ")
    password = input("Password: ")
    usuario = input("Usuario: ")
    new = Usuario(nombre, apellido, edad, password, usuario)
    listausuarios.update({usuario : new})
    print("Usuario registrado exitosamente")

# Venta de boletos #
def venta(listinput,nmax):
    if len(listinput) == 0:    
        print("No hay vuelos disponibles por el momento")
    else:
        print()
        nflight = int(input("Ingrese el número de vuelo: "))
        
        if  nflight > 0 and nflight <= nmax and nflight <= len(listinput):
            seflight = listinput[nflight-1]

            print()
            nboletos = int(input("Número de boletos: "))

            print()
            print("Clase:")
            print("\n 1) Trusita")
            print("\n 2) Negocios")
            print("\n 3) Primera Clase")
            print()
            tclass = int(input("Opcion: "))
            
            print()
            print("Forma de pago: ")
            print("\n 1) Tarjeta de crédito")
            print("\n 2) Efectivo")
            print()
            tpago = int(input("Opcion: "))

            if tclass == 1:
                seflight.lugaresturista = seflight.lugaresturista - nboletos
                ingreso = nboletos * seflight.costoturista
                global nturista
                nturista += nboletos
            elif tclass == 2:
                seflight.lugaresnegocios = seflight.lugaresnegocios - nboletos
                ingreso = nboletos * seflight.costonegocios
                global nnegocios
                nnegocios += nboletos
            elif tclass == 3:
                seflight.lugaresprimera = seflight.lugaresprimera - nboletos
                ingreso = nboletos * seflight.costoprimera
                global nprimera
                nprimera += nboletos
            
            if tpago == 1:
                global pagotarjeta
                pagotarjeta += ingreso
                global ntarjeta
                ntarjeta += 1
            elif tpago == 2:
                global efectivototal
                efectivototal += ingreso
                global nefectivo
                nefectivo += 1

            print()
            print("TÚ COMPRA SE REALIZÓ CON EXITO")


## DEGLARACIÓN DE VARIABLES GLOBALES PARA EL PROGRAMA   ##

# diccionario con admin y contraseña #
sharon = Administrador("Sharon", "Reyes", "21", "1", "Mecatrónica", "$30,000")
david = Administrador("David", "Rojas", "22", "2", "Mecatrónica", "$45,000")
administradores = {"Sharon": sharon,"David": david}
Amy = Usuario("Amairani","Cruz","21","123","Amy")
listausuarios = {"Amy": Amy}
usuarioactivo = " "
# vuelos máximos permitidos, por default se dan 10#
nmaxvuelos = 1
# lista de vuelos, será llenada con objetos de la clase vuelos#
listavuelos = []
flight = Vuelo("PROTECO","12:00","03:00","450","780","1500",6,6,3,"29 Junio 2019")
listavuelos.append(flight)
# Valores monterarios iniciales #
efectivototal = 0
pagotarjeta = 0
ventas = efectivototal + pagotarjeta
nefectivo = 0
ntarjeta = 0
# Número de voletos vendidos de diferentes clases #
nturista = 0
nnegocios = 0
nprimera = 0



##  PROGRAMA PRINCIPAL  ##
if __name__ == "__main__":
    while True:
        print()
        print("-----SISTEMA DE VENTAS-----")
        print("\t 1) Administrador")
        print("\t 2) Cliente")
        print("\t 3) Salir")
        opcion = int(input("Escribe la opción deseada: "))
        if opcion == 1:
            while True:
                print()
                print("-----ADMINISTRADOR-----")
                print("\t 1) Ingresar")
                print("\t 2) Regresar")
                opcion = int(input("Escribe la opción deseada: "))
                if opcion == 1:
                    
                    if login(administradores) == True:
                        while True:
                            print()
                            print("-----ADMINISTRACIÓN DEL SISTEMA DE VENTAS-----")
                            print("\t 1) Ingresar número máximo de vuelos")
                            print("\t 2) Ingresar vuelos")
                            print("\t 3) Listar vuelos")
                            print("\t 4) Cancelar vuelos")
                            print("\t 5) Actualizar vuelos")
                            print("\t 6) Estadísticas de pago")
                            print("\t 7) Estadísticas de clases")
                            print("\t 8) Información administrador")
                            print("\t 9) Regresar")
                            opcion = int(input("Escribe la opción deseada: "))
                            if opcion == 1:
                                print()
                                print("-----CONTROL DEL NÚMERO DE VUELOS-----")
                                print("El número máximo de vuelos actual es: ",nmaxvuelos)
                                inp1 = int(input("Ingresa el nuevo número máximo de vuelos: "))
                                if inp1 > 0:
                                    nmaxvuelos = inp1
                                    print("El número máximo de vuelos actual ahora es: ",nmaxvuelos)
                                else:
                                    print("Favor de escribr un número valido")

                            elif opcion == 2:
                                print()
                                print("-----INGRESAR NUEVO VUELO-----")
                                if len(listavuelos) < nmaxvuelos:
                                    nuevovuelo() 
                                else:
                                    print("Número de vuelos máximo alcanzado")

                            elif opcion == 3:
                                print()
                                print("-----LISTADO DE LOS VUELOS REGISTRADOS-----")
                                listarvuelos(listavuelos, nmaxvuelos)

                            elif opcion == 4:
                                print()
                                print("-----CANCELACIÓN DE VUELOS-----")
                                listavuelosname(listavuelos,nmaxvuelos)
                                deletevuelo(listavuelos,nmaxvuelos)

                            elif opcion == 5:
                                print()
                                print("-----MODIFICAR VUELOS-----")
                                listavuelosname(listavuelos,nmaxvuelos)
                                modificarvuelo(listavuelos,nmaxvuelos)

                            elif opcion == 6:
                                print()
                                print("-----ESTADÍSTICAS DE PAGO-----")
                                print("\t 1) Saldo total en efectivo: $", efectivototal)
                                print("\t 2) Saldo de pagos por tarjeta: $", pagotarjeta)
                                ventas = efectivototal + pagotarjeta
                                print("\t 3) Saldo total de ventas: $",ventas)
                                print("\t 4) Número de pagos realizados en efectitvo: ", nefectivo)
                                print("\t 5) Número de pagos realizados con tarjeta: ", ntarjeta)

                            elif opcion == 7:
                                print()
                                print("-----ESTADÍSTICAS DE CLASE-----")
                                print("\t 1) Boletos vendidos de la Clase Turista: ", nturista)
                                print("\t 2) Boletos vendidos de la Clase Negocios: ", nnegocios)
                                print("\t 3) Boletos vendidos de Primera Clase: ", nprimera)
                                ganadora = namemayor3(nturista, "Turista", nnegocios, "Negocios", nprimera, "Primera Clase")
                                print("\t 4) Clase con mayor número de ventas: ", ganadora)

                            elif opcion == 8:
                                print()
                                print("-----INFORMACIÓN DEL ADMINISTRADOR-----")
                                infoadmin(usuarioactivo)

                            elif opcion == 9:
                                break
                if opcion == 2:
                    break
        elif opcion == 2:
            while True:
                        print()
                        print("-----MENÚ DEL CLIENTE-----")
                        print("\t 1) Ingresar")
                        print("\t 2) Registrarse")
                        print("\t 3) Regresar")
                        opcion = int(input("Elige una opción: "))
                        if opcion == 1:
                            if login(listausuarios) == True:
                                while True:
                                    print()
                                    print("MENÚ DE USUARIO")
                                    print("\t 1) Ver vuelos disponibles")
                                    print("\t 2) Comprar vuelos")
                                    print("\t 3) Ver mi información")
                                    print("\t 4) Regresar")
                                    opcion = int(input("Elige una opción: "))
                                    if opcion == 1:
                                        print()
                                        print("-----VUELOS DISPONIBLES-----")
                                        listarvuelos(listavuelos, nmaxvuelos)
                                    elif opcion == 2:
                                        print()
                                        print("-----VUELOS DISPONIBLES-----")
                                        listarvuelos(listavuelos, nmaxvuelos)
                                        print()
                                        print("-----COMPRAR BOLETOS DE VUELO----")
                                        venta(listavuelos,nmaxvuelos)
                                    elif opcion == 3:
                                        print()
                                        print("-----INFORMACIÓN DEL CLIENTE-----")
                                        infouser(usuarioactivo)
                                    elif opcion == 4:
                                        break
                        elif opcion == 2:
                            print()
                            ("-----REGISTRO DEL CLIENTE-----")
                            nuevousuario()
                        elif opcion == 3:
                            break
        elif opcion == 3:
            print("Gracias por usar nuestra Aerolinea, vuelva pronto!")
            break




