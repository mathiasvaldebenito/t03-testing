def factorial(n):
    resultado = 1
    while n > 1:
        resultado *= n
        n -= 1
    return resultado

def al_cuadrado(n):
    return n*n

def al_cubo(n):
    return n*n*n

def mod10(n):
    return n%10

print(factorial(3))
print(factorial(3))

print(al_cubo(2))

print(mod10(5))

print(al_cuadrado(2))
print(al_cuadrado(2))
print(al_cuadrado(3))
print(al_cuadrado(4))
print(al_cuadrado(3))

print(mod10(6))

print(factorial(3))