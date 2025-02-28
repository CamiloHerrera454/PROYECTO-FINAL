import random #IMPORTANTE

palabras = ['pelota', 'futbol', 'computadora', 'celular', 'cuaderno', 'libro', 'dormitorio', 'cielo', 'estrella', 'estadio']
secreta = random.choice(palabras) #ALEATORIO
cadena = "-" * len(secreta) #GENERA CADENA DE GUIONES DE ACUERDO A LA PALABRA
print("Bienvenidos al Juego del Ahorcado")
intentos = 0

while True: #BUCLES-BREAK
    print(cadena)
    letra = input("Ingresa una letra: ") #EL USUARIO INGRESA UNA LETRA
    if letra in secreta: #VERIFICA SI LA LETRA ESTA EN LA PALABRA SECRETA
        for i in range(len(secreta)):
            if secreta[i] == letra: #SI LA LETRA EN LA POSICION I ESTA EN LA LETRA QUE INGRESE EL USUARIO
                cadena = cadena[:i] + letra + cadena[i+1:] #ACTUALIZA LA CADENA
        if cadena == secreta: #VERIFICA SI LA CADENA COINCIDE CON LA PALABRA SECRETA
            print(f"Felicidades has ganado el juego, la palabra secreta era {secreta}")
            break #ROMPE EL BUCLE INFINITO
    else:
        intentos += 1
        if intentos == 1:
            print("  O")
        elif intentos == 2:
            print("  O")
            print(" /")
        elif intentos == 3:
            print("  O")
            print(" /|")    
        elif intentos == 4:
            print("  O")
            print(" /|\\")
        elif intentos == 5:
            print("  O")
            print(" /|\\")
            print(" /")
        elif intentos == 6:
            print("  O")
            print(" /|\\")
            print(" / \\")
            print(f"Has perdido el juego, la palabra secreta era {secreta}")
            break
