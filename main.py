import keyboard
# Banner
print('''
___ _  _    ___ _ ____ _  _ ___  ____ 
 |  |  |     |  | |___ |\ | |  \ |__| 
 |  |__|     |  | |___ | \| |__/ |  | 
 
  Bienvenido, crearemos tu tienda...
''')
# var
global nombreTienda
global descripcion
global producto1

# tienda y descripcion
def data():
    nombreTienda = input("Ingresa el nombre de tu Tienda en linea")
    descripcion = input("Que productos vendes?")


data()

# opciones para llenar
print("Presiona la opcion que desees para ir completando tu tienda")


# guardar producto
def press1():
    print("1-Guardar  primer producto")
    while True:
        if keyboard.read_key() == "1":
            producto1 = input("Ingresa el nombre de tu 1er producto: ")
            print("Felicidades Guardaste " + producto1)



press1()
