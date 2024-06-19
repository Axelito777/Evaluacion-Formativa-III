import csv

Desc_A=float.__round__
Desc_S=float.__round__
Lista = ['Trabajador', 'Cargo', 'Sueldo Bruto', 'Desc. Salud', 'Desc. AFP', 'Liquido A Pagar']
matriz = []
lista2=['Trabajadores']
Ceo=[]
Desarrollador=[]
Analista_De_Datos=[]
matriz2=[]
lista3=['Planilla De Sueldo']
matriz3=[]
def Registros():
 while True:
            print("Registrar Trabajadores")
            Trabajador = input("Ingrese Su Nombre y Apellido: ")
            
            cargo = input("Ingrese Su Cargo: ").upper()
            if cargo=="CEO" or cargo=="DESARROLLADOR" or cargo=="ANALISTA DE DATOS":
                if cargo=="CEO":
                    Ceo.append([Trabajador])
                elif cargo=="DESARROLLADOR":
                    Desarrollador.append(Trabajador)
                elif cargo=="ANALISTA DE DATOS":
                    Analista_De_Datos.append(Trabajador)
                sueldo = int(input("Ingrese Su sueldo Bruto: "))
                if cargo=="CEO":
                    Ceo.append([sueldo])
                elif cargo=="DESARROLLADOR":
                    Desarrollador.append(sueldo)
                elif cargo=="ANALISTA DE DATOS":
                    Analista_De_Datos.append(sueldo)
                Desc_S =int (sueldo * 0.07)
                Desc_A =int (sueldo * 0.12)
                Liquido =int (sueldo - (Desc_S + Desc_A))
                fila = [Trabajador, cargo, sueldo, Desc_S, Desc_A, Liquido]
                matriz2.append(Trabajador)
                matriz.append(fila)
                matriz3.append([Trabajador,sueldo])
                print("Escriba SI Para Terminar o Aprete enter para continuar")
                opc = input("").upper()
                if opc == "SI":
                    print("Salir")
                    print("")
                    break
            else:
                print("NO EXISTE SU CARGO")
def trabajadores():
       print(lista2)
       print(matriz2)
def sueldos():
       pregunta=input("Desea Buscar Un cargo en especifico SI/NO: ").upper()
       if pregunta=="SI":
        pregunta2=input("Ingrese El Cargo: ").upper()
        if pregunta2=="CEO":
            print("Lista de ceo")
            print(Ceo)
        elif pregunta2=="ANALISTA DE DATOS":
            print("lista de analista de datos")
            print(Analista_De_Datos)
        elif pregunta2=="DESARROLLADOR":
            print("Lista de desarrolladores")
            print(Desarrollador)
       elif pregunta=="NO":    
        print(lista3)
        print(matriz3)

def archivo():
    import csv
    #Crear el contexto para abrir un nuevo archivo .csv
    with open('nuevo_archivo.csv', 'w', newline='', encoding='utf-8') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
    # Escribir una fila en el archivo CSV
        escritor_csv.writerow(Lista)
    # Escribir múltiples filas en el archivo CSV
        escritor_csv.writerows(matriz)
    print ("Se creo correctamente el archivo .csv"); 

    import csv
    with open('nuevo_archivo.csv', 'r', newline='', encoding='utf-8') as archivo_csv:
        lector_csv = csv.reader (archivo_csv);
        for x in lector_csv:
            print (x) 
       
