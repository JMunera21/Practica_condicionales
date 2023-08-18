NombreUsuario=int(input("Digita Tu Nombre: "))
EdadUsuario=int(input("Digita Tu Edad: "))

if EdadUsuario>=0 and EdadUsuario<=15:
    print(f"{NombreUsuario},Usted es un niño")
elif EdadUsuario>15 and EdadUsuario<=28:
    print (f" {NombreUsuario} , Usted es una Joven")
elif EdadUsuario>28 and EdadUsuario<=60:
    print ("{NombreUsuario} usted es Adulto")
elif EdadUsuario>60 and EdadUsuario<110:
    print(f"{NombreUsuario},usted es un suggar")
else:
    print("Edad Invalida")