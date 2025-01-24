#Productos/Precios

dic = {'pan':1.40, 'huevos':2.30, 'cebolla':0.85, 'aceite':4.35}

articulo = input("¿Que producto desea comprar?: ")
cantidad = float(input("¿Cuantas unidades del producto desea comprar?: "))

if articulo in dic:
    print("El precio de",articulo,"es de:",(dic[articulo]*cantidad))
else:
    print("El producto no se encuentra disponible actualmente.")