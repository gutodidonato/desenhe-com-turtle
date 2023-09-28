from turtle import *
import random
screen = Screen()
aposta = screen.textinput(title="Faça sua aposta", prompt="Qual tartaruga vai ganhar? (pela cor) ")

timot = Turtle()
nicolas = Turtle()
pedro = Turtle()
denner = Turtle()
maria = Turtle()

def iniciar(y,turtle, color):
    turtle.shape("turtle")
    turtle.penup()
    turtle.goto(-240,y)
    turtle.color(color)
    

iniciar(-100, timot, "red")
iniciar(-50, nicolas, "purple")
iniciar(0, pedro, "pink")
iniciar(50, denner, "blue")
iniciar(100, maria, "gray")    
screen.setup(width=500,height=400)





def random_move(turtle):
    valor = random.randint(0,20)
    turtle.forward(valor)
    
def jogar():
    vencedora = ""
    lista = [timot, denner, pedro, nicolas, maria]
    while True:
        for i in range(len(lista)):
            random_move(lista[i])
            posicao = lista[i].xcor()
            if posicao >= 240:
                vencedora = lista[i]
                break
        
        if vencedora:
            cor_vencedora = vencedora.color()[0]
            if aposta == cor_vencedora:
                screen.textinput(title="Você venceu!", prompt=f"A tartaruga {cor_vencedora} venceu!")
                break
            else:
                screen.textinput(title="Você perdeu", prompt=f"A tartaruga {cor_vencedora} venceu!")
                break

jogar()

    
screen.exitonclick()


