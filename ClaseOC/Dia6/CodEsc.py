print("Pon un caracter para salir del bucle.")
par = []
impar = []
try:
    while True:
        num = int(input("Dame un número: "))
        if num % 2 == 0:
            par.append(num)
        else:
            impar.append(num)
except ValueError:
    print(f"Saliste del bucle, de los núms. que me dijiste estos son pares: {par}, y estos impares: {impar}.")