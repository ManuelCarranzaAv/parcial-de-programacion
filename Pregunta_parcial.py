#-Usando el do while realizar un bucle que cuando nos pida agregar la letra a,
#y mientras se siga cumpliendo imprima una y otra vez hasta que coloquemos que se coloque una letra distinta con lo que finalizara el bucle
while True:
    letra = input("Ingrese solo la letra a: \n")
    if letra !="a":
        break
print("Usted fallo, no coloco la letra a")