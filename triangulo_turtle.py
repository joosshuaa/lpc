import turtle
# Da um nome ao objeto da tela.
wn=turtle.Screen() 
# define a cor da caneta. 
tess=turtle.Turtle() 
 
def triangle(x,y):
    # Variável que usa o metodo penup para  desativar a caneta .
    # Nota: existe uma propriedade chamada pen(caneta),
    # que indica se a caneta está desenhando ou não,
    # por padrão a caneta está sempre ativada.
    tess.penup()
    # Variável que o metodo goto para mover o cursor em x posição.
    tess.goto(x,y)
    # Variável que usa o metodo pendown para ativar ou desenhar com a caneta .
    tess.pendown()

    for i in range(3):
        # Manda a variável tess se mover 100 unidades para frente.
        tess.forward(100)
        # Roda de 120 graus para esquerda.
        tess.left(120)
        # Desenha o segundo lado do retângulo.
        tess.forward(100)
        
# Usada para vincular diversão a um evento de clique do mouse da tela.
turtle.onscreenclick(triangle,1)
# Escuta todas as entradas do módulo turtle.
turtle.listen()
# Fornece primitivas gráficas turtle. 
turtle.done()