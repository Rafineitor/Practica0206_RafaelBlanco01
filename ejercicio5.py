#Traductor

dic = {}

while True:
    traduccion = input("Introduzca las palabras en español e ingles separadas por dos puntos: ")
    if traduccion == 'terminar':
        break
    else:
        traduccion = traduccion.split(":")
        for i in traduccion:
            dic[traduccion[0]] = traduccion[1]
        print(dic)
        
frase = input("Ingrese una frase en español: ")
frase = frase.split(" ")

for i in frase:
    if i in dic:
        print(dic[i])
    else:
        print(i)