#Base de datos.

lista = []
dic1 = {}
dic2 = {}

def info (a,b,c):
    a[c]=b
    print (a)
    return a

while True:
    menu = int(input("""Escoja una de las siguientes opciones:
    1) Añadir alumno/a.
    2) Eliminar alumno/a.
    3) Mostrar alumno/a.
    4) Listar todo el alumnado.
    5) Listar alumnado aprobado.
    6) Terminar."""))

    if menu == 1:
        NIF = input("Ingrese NIF del alumno/a: ")
        nombre = input("Ingrese el nombre del alumno/a: ")
        apellidos = input("Ingrese los apellidos del alumno/a: ")
        tlf = input("Ingrese el telefono del alumno/a: ")
        correo = input("Ingrese el correo del alumno/a: ")
        aprobado = input("Ingrese si ha aprobado el/la alumno/a:")
    
        dic2 = {'nombre':nombre,'apellidos':apellidos,'tlf':tlf,'correo':correo,'aprobado':aprobado}
        info(dic1,dic2,NIF)
    lista.append(dic1)

    if menu == 2:
        NIF = input("Ingrese NIF del alumno/a: ")
        del dic1[NIF]
    
    if menu == 3:
        NIF = input("Ingrese NIF del alumno/a: ")
        print (dic1[NIF])

    if menu == 4:
        print (dic1)

    if menu == 5: