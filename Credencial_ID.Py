def verificar_aptitud_para_conducir():
    
    nombre = input("Ingresa tu nombre: ")
    edad = int(input("Ingresa tu edad: "))
    altura = float(input("Ingresa tu altura en cm: "))
    vision = float(input("Ingresa tu visión (sobre 10): "))

    if edad >= 18 and altura > 150 and vision >= 8:
        print(f"{nombre}, estás capacitado para conducir.")
    else:
        print(f"{nombre}, no estás capacitado para conducir.")
        if edad < 18:
            print("- Debes tener al menos 18 años.")
        if altura <= 150:
            print("- Debes medir más de 150 cm.")
        if vision < 8:
            print("- Debes tener una visión de al menos 8 sobre 10.")

verificar_aptitud_para_conducir()