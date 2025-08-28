def imprimir_y_multiplicar_por_dos(dato):
    if not isinstance(dato, (int, float)):
        print("Error: Solo se permiten números.")
        return
    print(dato)
    resultado = dato * 2
    print(resultado)

# Ejemplo
imprimir_y_multiplicar_por_dos(5)
imprimir_y_multiplicar_por_dos("5")  # Esto mostrará