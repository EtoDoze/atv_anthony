def sinal_magnitude(numero, bits):
    # Define o sinal
    if numero < 0:
        sinal = '1'
    else:
        sinal = '0'

    # Valor absoluto
    magnitude = abs(numero)

    # Converte para binário
    binario = bin(magnitude)[2:]

    # Quantidade de bits disponíveis para magnitude
    max_bits = bits - 1

    # Overflow
    if len(binario) > max_bits:
        return "Overflow!"

    # Completa com zeros
    binario = binario.zfill(max_bits)

    # Junta sinal + magnitude
    return sinal + binario


# TESTES
print(sinal_magnitude(5, 8))
print(sinal_magnitude(-5, 8))
print(sinal_magnitude(127, 8))
print(sinal_magnitude(-127, 8))