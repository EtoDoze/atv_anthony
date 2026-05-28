# Inteiros sem sinal
# Decimal -> Binário
# Verificação de Overflow

numero = int(input("Digite um número decimal: "))
bits = int(input("Digite a quantidade de bits: "))

# maior valor possível
maximo = (2 ** bits) - 1

print(f"\nMaior valor possível com {bits} bits: {maximo}")

# verificar overflow
if numero > maximo:
    print("OVERFLOW POSITIVO!")
else:
    # converter para binário com n bits
    binario = format(numero, f'0{bits}b')

    print(f"Decimal: {numero}")
    print(f"Binário: {binario}")