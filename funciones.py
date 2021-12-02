#1Que retorne verdadero si el número ingresado es par,caso contrario falso
def number_is_even(number):
    return True if number % 2 == 0 else False

#1Que retorne verdadero si el número ingresado es impar,caso contrario falso
def number_is_odd(number):
    return True if number % 2 != 0 else False

#1Que retorne los numeros pares de un intervalo
def list_ever_numbers(number):
    list = []
    for i in range(number):
     list.append(i) if i % 2== 0 else None 

    return list

#2 Elabore módulo que almacene una función que tome como argumento dos números enteros y devuelva el mayor.
def funcion (n1, n2):
    return max(n1, n2)

#3 Elabore un módulo que almacene una función que calcule la longitud de una expresión de texto ingresada por teclado. 
def calcular_longitud(text):
    con = 0


    for _ in text:
        con += 1
    return con

#4 Elabore un módulo llamado operaciones que almacene dos funciones: funcion_suma() y función_prod() que sumen y multipliquen respectivamente todos los números de una lista. Por ejemplo: funcion_suma() ([1,2,3,4]) debería imprimir 10 y función_prod ([1,2,3,4]) debería devolver 24. 

def funcion_suma(a):
    return sum(a)


def funcion_mult(a):
    producto = 1
    for i in a:
        producto *= i
    return producto

#5 Elabore un módulo que almacena tres funciones: 
   # Una función que imprima la serie de fibonacci
def fibonacci(n):
    if n<=2:
        return n-1
    a=0
    c=1
    print("0")
    for i in range(3, n+1):
        b=c
        c=c+a
        a=b
        print(a)
    return c 
def fibonacci_sum(n):
    if n<=2:
        return n-1
    a=0
    c=1
    sum = 0
    for i in range(3, n+1):
        b=c
        c=c+a
        a=b
        sum+=a
    print(sum)
    return sum 
def fact(n):
    if n == 0:
        r = 1
    else:
        r = n * fact(n - 1)
    return r



