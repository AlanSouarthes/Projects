#Arquivo Control
from model import impares, media
from model import numeroInicialFinal
from model import somarInicioFim #Conecta a classe model e control
from model import tabuada
import this
from model import numeroInicialFinal
from model import somarInicioFim
from model import tabuada
from model import impares
from model import somar10Numeros
from model import leia
from model import media
from model import ePar
from model import fatorial

this.opcao = -1
this.num = -1
this.i = 0 #Contator começa zerado




def exercicio01():
    inicio = int(input("Informe o Início: "))
    fim = int(input("Informe o Fim: "))
    print(somarInicioFim(inicio,fim))

def exercicio02():
    num = int(input("Informe um número que deseja multiplicar: "))
    fim = int(input("Informe até onde deve ser multplicada: "))
    print(tabuada(num,fim))

def exercicio03():
    inicio = int(input("Informe um número inicial"))
    fim = int(input("Informe o número final"))
    print(numeroInicialFinal(inicio,fim))

def exercicio04():
    inicio = int(input("Informe um número inicial"))
    fim = int(input("Informe o número final"))
    print(impares(inicio,fim))

def exercicio05():
    for i in range (0,10,1):
        num =int(input('Informe {} º número: '.format(i+1)))
        soma = somar10Numeros(num)
    print ("A soma dos números digitados é: {}".format(soma))

def exercicio06():
    while this.num !=0:
        this.num =int(input('Informe um número: '))
        soma = leia(this.num)
    print ("A soma dos números digitados é: {}".format(soma))

def exercicio07():
    while(this.num != 0):
        this.num = int(input("Digite um número: "))
        if ePar(this.num) == True:
            soma = somar10Numeros(this.num)
            this.i += 1 #Contar quantos números foram digitados
    print("A média dos números digitados é: {}".format(media(soma,this.i)))


def exercicio08():
    while(this.num != 0):
        this.num = int(input("Informe um número: "))
        #Primeira digitação do usuário
        if this.num != 0:
            if this.i == 0:
                maior = this.num
                menor = this.num
            this.i += 1

            if this.num > maior:
                maior = this.num

            if this.num < menor:
                menor = this.num
    print(f"O maior númeor digitado é: {maior}\n O menor número digitado é: {menor}")

def exercicio09():
    num = int(input("Informe um número: "))
    print(fatorial(num))

def exercicio10():
    quantidade = int(input("Informe a quantidade de jogadores: "))
    for i in range(0,quantidade,1):
        altura = float(input(f"{i + 1}altura"))
        while(altura <= 0):
            if altura <= 0:
                print("Erro!! Digite uma altura positiva!")
            altura = float(input(f"{i +1 }ª altura: "))


        soma = somar10Numeros(altura)

    print(f"A média da altura desse time é {media(soma,quantidade)}")

def exercicio11():
    this.venc = ""
    for i in range(0, 16, 1):
        nota = float(input(f"{i+1}ª Nota"))
        while(nota < 0 or nota > 10):
            print("Erro!!Informe uma nota mairo que 10")
        cand = input(f"{i+1}i+1ª candidata: ")

        if i == 0:
            maior = nota

        if nota > maior:
            maior = nota
            this.venc = cand
    print(f"A vencedora é: {this.venc}, sua nota foi {maior}")








def menu():
    print("\nEscolha uma das opções abaixo: \n" +
          "0. Sair\n  "        +
          "1. Exercício 01\n " +
          "2. Exercício 02\n"  +
          "3. Exercício 03\n"  +
          "4. Exercício 04\n"  +
          "5. Exercício 05\n"  +
          "6. Exercício 06\n"  +
          "7. Exercício 07\n"  +
          "8. Exercício 08\n"  +
          "9. Exercício 09\n"  +
          "10. Exercício 10\n" +
          "11. Exercicio 11\n")

    this.opcao = int(input())


def operacao():
    while(this.opcao != 0):
        menu() #Chamar o Menu
        if this.opcao == 0:
            print("Obrigado")
        elif this.opcao == 1:
            exercicio01()
        elif this.opcao == 2:
            exercicio02()
        elif this.opcao == 3:
            exercicio03()
        elif this.opcao == 4:
            exercicio04()
        elif this.opcao == 5:
            exercicio05()
        elif this.opcao == 6:
            exercicio06()
        elif this.opcao == 7:
            exercicio07()
        elif this.opcao == 8:
            exercicio08()
        elif this.opcao == 9:
            exercicio09()
        elif this.opcao == 10:
            exercicio10()
        elif this.opcao == 11:
            exercicio11()
        else:
            print("Erro!! Escolha uma opção válida!")



