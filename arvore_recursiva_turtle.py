from turtle import *

speed('fastest')
# Colocando a tartaruga para cima .
rt(-90)
# O Ângulo que vai ficar entre  a base e o y. 
angle = 30
  
def y(sz, degree_of_elevation):   
  
    if degree_of_elevation > 0:
        colormode(255)
        # Separando a faixa rgb para verde
        # em intervalos identicos para cada nível,
        # e indicando a cor de acordo
        # com o nível atual.
        pencolor(0, 255//degree_of_elevation, 0)
        # Iniciando o desenho da base.
        fd(sz)
        rt(angle)
        # Iniciando a recursividade para colocar a arvore a direita.  
        y(0.8 * sz, degree_of_elevation-1)
        pencolor(0, 255//degree_of_elevation, 0)
        lt( 2 * angle)
        # Iniciando a recursividade para colocar a arvore a esquerda.
        y(0.8 * sz, degree_of_elevation-1)
        pencolor(0, 255//degree_of_elevation, 0)
        rt(angle)
        fd(-sz)  

# Tamanho da arvore 80 e de nivel 7.
y(80, 7)