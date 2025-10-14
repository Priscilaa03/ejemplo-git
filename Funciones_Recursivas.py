def sumar_naturales(numero: int) -> int:
    if numero == 1:
        return numero
    else:
        return numero + sumar_naturales(numero - 1)
    
def calcular_potencia(base: int, exponente: int) -> int:
    if exponente == 0:
        potencia = 1
        return potencia
    else:
        potencia = base * calcular_potencia(base, exponente - 1)
        return potencia
    
def sumar_digitos(numero: int) -> int:
    suma = 0
    for i in str(numero):
        suma += int(i)
    return suma
    
def calcular_fibonacci(numero: int) -> int:
    if numero == 0:
        return 0
    elif numero == 1:
        return 1
    else:
        return calcular_fibonacci(numero - 1) + calcular_fibonacci(numero - 2)