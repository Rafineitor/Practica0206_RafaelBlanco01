#Divisa

dic = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}

divisa = input("Ingrese una divisa: ")

if divisa in dic:
    print(dic[divisa])
else:
    print("La divisa no se encuentra en el diccionario.")