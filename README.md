# PROYECTO-FINAL
ACTIVIDAD AUTÓNOMA NRO. 1, 2, 3, y 4.
Autor: Herrera Cabezas Camilo Nicolas

Materia: Lógica de Programación

Nivel: 1er Semestre

Objetivo: El objetivo de esta introducción es resaltar la importancia de la programación en la era digital actual. Se menciona cómo aprender a programar no solo ayuda a comprender mejor la tecnología, sino también a desarrollar habilidades lógicas y creativas. Además, se presenta el proyecto del juego del ahorcado en Python como una oportunidad práctica para aplicar estos conocimientos y habilidades aprendidas en los temas 1, 2 , 3, y 4.

Principales funcionalidades del programa:
Puntos importantes resaltados durante su desarrollo:

-import random: Importa la librería random, la cual es esencial para seleccionar una palabra de forma aleatoria.
-secreta = random.choice(palabras): Selecciona una palabra aleatoria de la lista de palabras.
-cadena = "-" * len(secreta): Genera una cadena de guiones de acuerdo a la longitud de la palabra secreta.
-Bucle while True:: Mantiene el juego en ejecución hasta que se rompa el bucle con un break.
-Entrada del usuario (input): El usuario ingresa una letra para adivinar.
-Actualización de la cadena: Si la letra está en la palabra secreta, la cadena se actualiza con la letra correcta.
-Dibujo del ahorcado: Basado en el número de intentos fallidos, se dibuja el ahorcado.
-Condición de victoria: Si la cadena coincide completamente con la palabra secreta, el usuario gana.
-Condición de derrota: Si se agotan los intentos, el usuario pierde y se revela la palabra secreta.
