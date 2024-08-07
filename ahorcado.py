import random 

def obtener_palabra_secreta() -> str:
    palabras = [
        'python', 'javascript', 'java', 'angular', 
        'django', 'tensorflow', 'react', 'typescript',
        'git', 'flask'
    ]
    return palabras[random.randrange(len(palabras))]

def mostrar_progreso(palabra_secreta, letras_adivinadas):
    adivinado = ''
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            adivinado += letra
        else:
            adivinado += "_"
    return adivinado

def juego_ahorcado():
    palabra_secreta = obtener_palabra_secreta()
    letras_adivinadas = []
    intentos = 7
    juego_terminado = False
    print(f"Hay {intentos} intentos disponibles.")
    print(mostrar_progreso(palabra_secreta, letras_adivinadas), f"La palabra tiene {len(palabra_secreta)} letras.")
    while not juego_terminado and intentos > 0:
        adivinanza = input("Introduce una letra: ").lower()
        if len(adivinanza) != 1 or not adivinanza.isalpha():
            print("Se requiere letra válida.")
        elif adivinanza in letras_adivinadas:
            print("Letra ya usada.")
        else:
            letras_adivinadas.append(adivinanza)
            if adivinanza in palabra_secreta:
                print(f"Acertaste!")
            else:
                intentos -= 1
                print(f"Letra errónea: {adivinanza}.")
                print(f"Quedan {intentos} intentos.")

        progreso_actual = mostrar_progreso(palabra_secreta, letras_adivinadas)
        print(progreso_actual)

        if "_" not in progreso_actual:
            juego_terminado = True
            print(f"Ganaste! La palabra secreta es: {palabra_secreta}")

    if intentos == 0:
        print("Perdiste!")

juego_ahorcado()


