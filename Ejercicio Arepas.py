print("Bienvenido a la calculadora de masa para arepas, ingresa los datos y te diré la cantidad de masa resultante")

agua = input("Ingrese la cantidad de agua de la masa: ")
agua_int = int(agua)

harina = input("Ingrese la cantidad de harina de la masa: ")
harina_int = int(harina)

cant_masa = harina_int + agua_int
print(f"La cantidad de masa es {cant_masa}g")
