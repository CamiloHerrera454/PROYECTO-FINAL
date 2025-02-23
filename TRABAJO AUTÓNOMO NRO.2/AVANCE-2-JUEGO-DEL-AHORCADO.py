import random

palabras = ['pelota', 'futbol', 'computadora', 'celular', 'cuaderno', 'libro', 'dormitorio', 'cielo', 'estrella', 'estadio']
secreta = random.choice(palabras)
cadena = "-" * len(secreta)
print("Bienvenidos al Juego del Ahorcado")
intentos = 0

while True:
    print(cadena)
    letra = input("Ingresa una letra: ")
    if letra in secreta:
        for i in range(len(secreta)):
            if secreta[i] == letra:
                cadena = cadena[:i] + letra + cadena[i+1:]
        if cadena == secreta:
            print(f"Felicidades has ganado el juego, la palabra secreta era {secreta}")
            break

