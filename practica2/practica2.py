horarios = {
    'Maria': ('08', '16'),
    'Juan':  ('09', '17'),
    'Lucía': ('07', '15'),
    'Diego': ('10', '18'),
    'Ana':   ('08', '14'),
    'Raúl':  ('12', '20'),
}

def mostrar_registros():
    print("\nMostrando todos los registros de horarios:")
    for i, (nombre, (entrada, salida)) in enumerate(horarios.items(), start=1):
        print(f"{i}. {nombre}: {entrada} - {salida}")

def contar_entradas():
    try:
        hora = int(input("\nIntroduce una hora (0-23): "))
        if 0 <= hora <= 23:
            contador = sum(1 for entrada, salida in horarios.values() if int(entrada) <= hora)
            print(f"{contador} persona(s) entraron antes o a las {hora} h.")
        else:
            print("Hora fuera de rango (0-23).")
    except ValueError:
        print("Entrada no válida, debe ser un número entero.")

def menu():
    while True:
        print("\n========== MENÚ ==========")
        print("1) Mostrar registros")
        print("2) Contar entradas")
        print("3) Salir")
        opcion = input("Elige una opción (1-3): ").strip()
        if opcion == '1':
            mostrar_registros()
        elif opcion == '2':
            contar_entradas()
        elif opcion == '3':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")

if __name__ == '__main__':
    menu()
