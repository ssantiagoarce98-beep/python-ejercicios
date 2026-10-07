def analisis_productos(productos):
    total_mercaderia=0
    cantidad=0
    producto_mas_caro=productos[0]["precio"]
    for i in range(len(productos)):
        print ("---",productos[i]["nombre"],"---")
        print (productos[i]["precio"])
        print (productos[i]["stock"])
        if productos[i]["stock"]==0:
            print ("SIN STOCK")
        if productos[i]["stock"]>0 and productos[i]["stock"]<5:
            print ("POCO STOCK")
        if productos[i]["stock"]>0:
            cantidad+=1
        if producto_mas_caro<productos[i]["precio"]:
            producto_mas_caro=productos[i]["precio"]
        print ("Valor de",productos[i]["nombre"],"es", productos[i]["precio"]*productos[i]["stock"])
        total_mercaderia+=(productos[i]["precio"]*productos[i]["stock"])
    print ("Valor total:",total_mercaderia)
    print ("Cantidad de productos en stock:",cantidad)
    print ("Producto mas caro:",producto_mas_caro)
