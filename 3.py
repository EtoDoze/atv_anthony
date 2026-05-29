def complemento2(numero, bits):

    # Limites
    minimo = -(2 ** (bits - 1))
    maximo = (2 ** (bits - 1)) - 1

    # Overflow
    if numero < minimo or numero > maximo:
        return "Overflow!"

    # Positivo
    if numero >= 0:
        return format(numero, f'0{bits}b')

    # Negativo
    numero = (1 << bits) + numero

    return format(numero, f'0{bits}b')


# TESTES
print(complemento2(5, 8))
print(complemento2(-5, 8))
print(complemento2(127, 8))
print(complemento2(-128, 8))
print(complemento2(128, 8))