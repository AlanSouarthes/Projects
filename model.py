#Arquivo Model
import this
this.soma = 0
this.num = 0
this.qtde = 0
this.alt = 0

#Faça um algoritmo que faça a soma dos números inteiros entre 1 e 100.

# While = utilizo enquanto não sei quantas vezes vou repetir

# For = Eu sei quantas repetiçoes serão.

def somarInicioFim(inicio, fim):
    soma = 0#Instanciar a variavel
    for i in range(inicio,fim+1,1):
        soma += i
    return soma

#Contrua um programa que exiba a tabuada de 1 ate N.
def tabuada(num, fim):
    multiplicacao = ""#Instanciando uma variavel do tipo texto
    for i in range(1,fim+1,1):
         multiplicacao +="{} * {} = {}\n".format(num,i, num * i)
    return multiplicacao

def numeroInicialFinal(inicio, fim):
    mostrar = ""
    for i in range(1,fim+1, 1):
        mostrar += "{}\n ".format(i)
    return mostrar

def impares(inicio, fim):
    impar = ""
    for i in range(inicio, fim+1, 1):
        if i % 2 != 0:
            impar += "{}\n".format(i)
    return impar


#
def somar10Numeros(num):
    this.soma += num
    return this.soma

def leia(num):
    this.soma += num
    return this.soma

def media(soma,qtde):
    return soma / qtde

def ePar(num):
    if num % 2 == 0:
        return True
    else:
        return False

def fatorial(num):
    aux = num
    fat = 1
    while(num >1):
        fat = fat * num
        num -= 1
    return(f"O fatorial de {aux} é {fat}")




