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

#caso1 n=5 bits=4 r=0101
#caso2 n=15 bits=4 r=1111
#caso3 n=16 bits=4 r=Overflow
#caso4 n=255 bits=8 r=11111111
