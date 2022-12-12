import turtle
import random
# Criando duas tartarugas que representarão os jogadores.
# Jogador de número um é de cor verde e o 
# jogador de número dois é de cor azul.
player_one = turtle.Turtle()
player_one.color("green")
player_one.shape("turtle")
player_one.penup()
player_one.goto(-200,100)
player_two = player_one.clone()
player_two.color("blue")
player_two.penup()
player_two.goto(-200,-100)
# Criando as casas das tartarugas que será representada por um círculo.
# Aqui precisamos ter certeza que as casas das tartarugas estão em
# um ponto de partida diferente.
player_one.goto(300,60)
player_one.pendown()
player_one.circle(40)
player_one.penup()
player_one.goto(-200,100)
player_two.goto(300,-140)
player_two.pendown()
player_two.circle(40)
player_two.penup()
player_two.goto(-200,-100)
# Usando uma lista para criar os dados.
die = [1,2,3,4,5,6]

# Cálculos necessarios para repetir esse processo até atingir o objetivo.
for i in range(20):
     if player_one.pos() >= (300,100):
             print("O jogador um vence!")
             break
     elif player_two.pos() >= (300,-100):
             print("O jogador dois vence!")
             break
     else:
             player_one_turn = input("Pressione ENTER para iniciar o dado: ")
             die_outcome = random.choice(die)
             print("O resultado do lançamento do dado é: ")
             print(die_outcome)
             print("O número de etapas será: ")
             print(20*die_outcome)
             player_one.fd(20*die_outcome)
             player_two_turn = input("Pressione ENTER para iniciar o dado: ")
             die_outcome = random.choice(die)
             print("O resultado do lançamento do dado é: ")
             print(die_outcome)
             print("O número de etapas será: ")
             print(20*die_outcome)
             player_two.fd(20*die_outcome)
