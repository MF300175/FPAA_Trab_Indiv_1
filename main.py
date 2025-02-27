def karatsuba(x, y):
    if x < 10 or y < 10:  # Caso base: multiplicação direta
        return x * y
    
    n = max(len(str(x)), len(str(y)))
    m = n // 2  # Divide os números ao meio

    # Divide x e y em partes menores
    x_high, x_low = divmod(x, 10**m)
    y_high, y_low = divmod(y, 10**m)

    # Aplica recursão para calcular os três produtos principais
    z0 = karatsuba(x_low, y_low)
    z1 = karatsuba((x_low + x_high), (y_low + y_high))
    z2 = karatsuba(x_high, y_high)

    return (z2 * 10**(2*m)) + ((z1 - z2 - z0) * 10**m) + z0

if __name__ == "__main__":
    a = 12345678
    b = 87654321
    result = karatsuba(a, b)
    print(f"Resultado da multiplicação de {a} x {b}: {result}")
