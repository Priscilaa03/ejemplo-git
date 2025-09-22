def get_int (mensaje:str, mensaje_error: str, minimo : int, maximo: int, reintentos: int) -> int|None:
    contador = 0
    while contador != reintentos:
        numero = int(input(mensaje))
        if numero < maximo and numero > minimo:
            return numero
        else:
            contador += 1
            print(mensaje_error)
    return None

def get_float (mensaje:str, mensaje_error: str, minimo : float, maximo: float, reintentos: float) -> float|None:
    contador = 0
    while contador != reintentos:
        numero = float(input(mensaje))
        if numero < maximo and numero > minimo:
            return numero
        else:
            contador += 1
            print(mensaje_error)
    return None

def get_string(longitud: int, texto : str) -> str|None:
    contador = 0
    
    for i in texto:
        contador += 1
    
    if contador > longitud:
        return None
    else:
        return texto
