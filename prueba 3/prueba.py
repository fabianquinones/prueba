import funciones as fn
clientes= []


while True:
    try:
        print("--------------------------------")
        print("|         pedidos duoc         |")
        print("--------------------------------")
        print("1. Registrar pedido")
        print("2. listar los todos los pedidos")
        print("3. imprimir hoja de ruta")
        print("4. salir del programa")
        opc=int(input())
        if opc== 1:
            fn.registrarPedido(clientes)
        elif opc==2:
            fn.ListarPedido(clientes)
        elif opc==3:
            fn.ImprimirHoja(clientes)
        elif opc==4:
            break
        else:
            print("selecciona una de las 4 opciones uwu")
    except ValueError:
        print ("escriba bien la opcion (con numeros)")