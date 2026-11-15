user_nombre = "Gabo"
user_apellido = "Glz"
ci = 1234567
saldo = 100000
total_depositado = 0
total_retirado = 0
print("Ingrese sus datos")
user_nombreN = input("Nombre: ")
user_apellidoN = input("Apellido: ")
ciN = int(input("C.I. "))
op1 = "1-Depositar dinero"
op2 = "2-Retirar dinero"
op3 = "3-Consultar saldo"
op4 = "4-Salir"
if user_nombre == user_nombreN and user_apellido == user_apellidoN and ci == ciN:
    print("Acceso autorizado")
    opcionesingresar = 0
    while opcionesingresar != 4:
        print(op1)
        print(op2)
        print(op3)
        print(op4)
        opcionesingresar = int(input("Ingrese una opción: "))
        if opcionesingresar == 1:
            deposito = int(input("Ingrese la cantidad que desea depositar: "))
            while deposito <= 0:
                print("Debe ser mayor a 0")
                deposito = int(input("Ingrese la cantidad que desea depositar: "))
            saldo = saldo + deposito
            total_depositado = total_depositado + deposito
            print("Consulte su saldo presionando 3")
        elif opcionesingresar == 2:
            retiro = int(input("Ingrese la cantidad que desea retirar: "))
            while retiro <= 0 or retiro > saldo:
                if retiro <= 0:
                    print("Debe ser mayor a 0")
                else:
                    print("El monto supera tu saldo actual")
                retiro = int(input("Ingrese la cantidad que desea retirar: "))
            saldo = saldo - retiro
            total_retirado = total_retirado + retiro
            print("Consulte su saldo presionando 3")
        elif opcionesingresar == 3:
            print("Saldo actual:", saldo)
        elif opcionesingresar != 4:
            print("Opción inválida")
    print("Saldo:", saldo)
    if total_depositado > 0:
        print("Cantidad depositada:", total_depositado)
    else:
        print("No se realizaron depósitos")
    if total_retirado > 0:
        print("Cantidad retirada:", total_retirado)
    else:
        print("No se realizaron retiros")
else:
    print("Acceso denegado")