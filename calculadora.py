#calculadora.py - versión 2
# Cambios:
# - Repite operaciones hasta que el usuario diga que no.
# - Limpia operación y valida división por cero.
# - Acepta coma decimal y formatea resultado

print("=== Calculadora Básica ===")
while True:
    n1_texto = input("Primer número: ").strip().replace(",", ".")
    n2_texto = input("Segundo número: ").strip().replace(",", ".")

    try:
        numero_1 = float (n1_texto)
        numero_2 = float(n2_texto)
    except ValueError:
        print("Entrada inválida. Debes escribir números (usa 3.5 o 3,5).")
        continue

    operacion = input("Elige la operación a realizar (+, -, *, /): ").strip().lower()

    if operacion == '+':
        resultado = numero_1 + numero_2
        print("Resultado:", f"{resultado:.2f}")
    elif operacion == '-':
        resultado == numero_1 - numero_2
        print("Resultado:", f"{resultado:.2f}")
    elif operacion == '*':
        resultado == numero_1 * numero_2
        print("Resultado:",f"{resultado:.2f}")
    elif operacion == '/':
        resultado == numero_1 / numero_2
        print("Resultado:", f"{resultado:.2f}")
    
    else:
        print("Operación no válida.")

    seguir = input("¿Deseas realizar otra operación? (s/n): ").strip().lower()
    if seguir != 's':
        print("Hasta luego")
        break



