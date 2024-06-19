
import Funcion as func
while True:
    print("")
    print("Trabajo Calfun")
    print("1.- Registrar trabajador")
    print("2.- Listar los todos los trabajadores")
    print("3.- Imprimir planilla de sueldos")
    print("4.- Salir del Programa")
    try:
        opc = int(input("Ingrese Una Opcion: "))
    except:
        print("Ingrese Un Numero")
    else:
        if opc == 1:
            func.Registros()

        elif opc==2:
            func.trabajadores()

        elif opc==3:
            func.sueldos()

        elif opc==4:
            print("Salir Del Programa")
            func.archivo()
            break
