print("introduzca un precio a eleccion y se le devolvera con el IVA incluido")
precio = int(input("introduzca el precio: ")) //se lee el valor introducido por el usuario
IVA=0.21 //se define el valor del IVA
precio_IVA=precio + (precio * IVA) //se calcula el precio con IVA incluido
print("el precio con IVA incluido es: ", precio_IVA) //se devuelven el resultado