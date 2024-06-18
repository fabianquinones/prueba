comunas=["centro","colina", "industrias"]

"""clientes= { "Cliente":" ",
            "Dirección":" ",
            "Sector":" ",
            "Cil. 5kg":" ", 
            "Cil. 15kg":" ", 
            "Cil. 45kg":" "
            }"""

def registrarPedido (clientes):

    print("bienvenido a registro cliente por favor entregenos sus datos:")
    while True:
        try:
            nombre=input("ingrrese su nombre y apellido: ")
            if len(nombre)> 0:
                break
            else:
                print("debe ingresar algo ;0")
        except:
            print("algo escribio mal :0")

    while True:
        try:
            direccion=input("ingrese su direccion ")
            if len(direccion) > 0:
                break
            else:
                print("debe ingresar algo ;0")
        except:
            print("algo escribio mal :0")
    #sector
    while True:
        try:
            sector1=input("ingres su sector puede ser Centro, Colina o Industrias: ").lower()
            if sector1  in comunas:
                sector=sector1
                break
            else:
                print("comuna no encontrada o no ingresso nada :0")
        except ValueError:
            print("algo ingreso mal :S")
    while True:
        try:            
            cil5kg=int(input("cuatos silindros de 5kg lleva: "))
            if cil5kg >= 0:
                break
            else:
                print("comuna no encontrada o no ingresso nada :0")
        except ValueError:
            print("algo ingreso mal :S")
    while True:
        try:  
            cil15kg=int(input("cuatos silindros de 15kg lleva:"))
            if cil15kg >= 0:
                break
            else:
                print("comuna no encontrada o no ingresso nada :0")
        except ValueError:
            print("algo ingreso mal :S")
    while True:
        try:
            cil45kg=int(input("cuantos silindros de 45kg lleva:"))
            if cil45kg >= 0:
                break
            else:
                print("comuna no encontrada o no ingresso nada :0")
        except ValueError:
            print("algo ingreso mal :S")
    
    clientes.append({
        "cliente":nombre,
        "direccion":direccion,
        "sector": sector,
        "cil5kg": cil5kg,
        "cil15kg": cil15kg,
        "cil45kg": cil45kg
    })




def ListarPedido(clientes):
    print(clientes)



def ImprimirHoja(clientes):
    listaPedidosaImprimir=[]
    seleccionSector=input("seleccione un sector puede ser Centro, Colina o Industrias").lower
    if seleccionSector not in comunas:
        print("Ese sector no esta en la lista ¡Ingresa uno que si este!")
    else:

        for seleccionSector in clientes:
            if cliente["sector"] == seleccionSector:
                listaPedidosaImprimir.append(cliente)
        with open("Hoja".txt,"r","w") as archivo:
            for cliente in listaPedidosaImprimir:
                archivo.write(f"client:{cliente["cliente"]}")
                archivo.write(f"direccion:{cliente["direccion"]}")
                archivo.write(f"sector:{cliente["sector"]}")
                archivo.write(f"cil5kg:{cliente["cil5kg"]}")
                archivo.write(f"cil15kg:{cliente["cil15kg"]}")
                archivo.write(f"cil45kg:{cliente["cil45kg"]}")
    print("archivo generado")

