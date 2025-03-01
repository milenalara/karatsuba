from math import ceil, floor

# multiplica dois numeros inteiros (u e v) com n casas decimais
def karatsuba(u, v, n):
    if n <= 3:
        return u * v
    m = ceil(n / 2)
    p = floor(u / (10 ** m))
    q = u % (10 ** m)
    r = floor(v / (10 ** m))
    s = v % (10 ** m)
    pr = karatsuba(p, r, m)
    qs = karatsuba(q, s, m)
    y = karatsuba(p + q, r + s, m + 1)
    uv = pr * (10 ** (2 * m)) + (y - pr - qs) * (10 ** m) + qs
    return uv

# cenario de testes 1: numeros pequenos
print("12 * 24 = " + str(karatsuba(12, 24, 2))) # deve retornar 408

# cenario de testes 2: numeros pequenos
print("7 * 8 = " + str(karatsuba(7, 8, 1))) # deve retornar 56

# cenario de testes 3: numeros grandes
print("12345678 * 87654321 = " + str(karatsuba(12345678, 87654321, 8))) # deve retornar 1082152022374638

# cenario de testes 4: numeros grandes
print("9999991 * 999983 = " + str(karatsuba(9999991, 999983, 6))) # deve retornar 9999821000083

# cenario de testes 5: potencias de 10
print("12345 * 10000 = " + str(karatsuba(12345, 10000, 5))) # deve retornar 123450000

# cenario de testes 6: potencias de 10
print("10000 * 10000 = " + str(karatsuba(10000, 10000, 5))) # deve retornar 100000000

# cenario de teste 7: numeros negativos
print("1234 * (-5678) = " + str(karatsuba(1234, -5678, 4))) # deve retornar -7006652

# cenario de teste 8: numeros negativos
print("(-1234) * (-5678) = " + str(karatsuba(-1234, -5678, 4))) # deve retornar 7006652