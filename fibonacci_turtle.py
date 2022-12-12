import turtle
import math
 
def fiboPlot(n):
    a = 0
    b = 1
    first_square = a
    second_square = b
    # Configurando a cor da caneta de plotagem para azul.
    x.pencolor("blue")
    # Criando o primeiro quadrado.
    x.forward(b * element)
    x.left(90)
    x.forward(b * element)
    x.left(90)
    x.forward(b * element)
    x.left(90)
    x.forward(b * element) 
    temp = second_square
    second_square = second_square + first_square
    first_square = temp

    # criando os outros quadrados.
    for i in range(1, n):
        x.backward(first_square * element)
        x.right(90)
        x.forward(second_square * element)
        x.left(90)
        x.forward(second_square * element)
        x.left(90)
        x.forward(second_square * element)
        temp = second_square
        second_square = second_square + first_square
        first_square = temp
    # Levando a caneta para o início da plotagem em espiral.
    x.penup()
    x.setposition(element, 0)
    x.seth(0)
    x.pendown() 
    # Indicando a cor da caneta de plotagem para vermelho.
    x.pencolor("red") 
    x.left(90)

    for i in range(n):
        print(b)
        fdwd = math.pi*b * element / 2
        fdwd /= 90
        for j in range (90):
            x.forward(fdwd)
            x.left(1)
        temperatura = a
        a = b
        b = temperatura + b
        
# Este "elemento" representa os aumentos.
# Elemento que aumenta ou diminui a magnitude
# Do gráfico por um dado elemento.
element = 1
# Tomando a entrada da saída para o número de
# Iterações que o algoritmo executará..
n = int(input('Digite o número de iterações (deve ser > 1): '))

# Fractal espiral de Fibonacci sendo plotado
# e imprimindo o número de Fibonacci equivalente.
if n > 0:
    print("Série de Fibonacci para", n, "elementos :")
    x = turtle.Turtle()
    x.speed(100)
    fiboPlot(n)
    turtle.done()
else:
    print("Número de iterações deve ser > 0")