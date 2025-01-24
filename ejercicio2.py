#Datos

dic = {}

nombre = input("Ingrese su nombre:")
edad = input("Ingrese su edad: ")
direccion = input("Ingrese su direccion: ")
telefono = input("Ingrese su numero de telefono: ")

dic[nombre]= nombre
dic[edad]= edad
dic[direccion]= direccion
dic[telefono]= telefono

print("",dic[nombre],"tiene" ,dic[edad],"vive en" ,dic[direccion], "y su numero de telefono es" ,dic[telefono])