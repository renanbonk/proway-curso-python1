import datetime

def exemplo01():
    email= input("Digite seu e-mail: ")
    senha= input ("Digite sua senha: ")
    print("E-mail digitado: ", email)
    print("Senha digitado: ", senha)


def exemplo02():
   print("-------Exemplo 02--------- ")
   #toda entrada ultilizando o input vem como str(string texto)
   #Fazemos a conversão de str para int do que o usuário digitou
   idade = int (input("digite a sua idade"))
   #obter o ano atual ultlizando o momento atual, obtido atraves da classe datetime
   ano_atual = datetime.datetime.now().year
   #calcular o ano de nascimento
   ano_nascimento = ano_atual -  idade
   print ("Ano de nascimento: ", ano_nascimento)
  

def exemplo03():
   nome =input("Digite o nome: ")
   sobrenome=input("Digite o sobrenome: ")
   nome_completo = nome + " " + sobrenome
   print("Nome completo: ", nome_completo)


def exemplo04():
    produto =input("Digite o nome do produto: ")
    quantidade= int(input("Digite a quantidade: "))
    preco_unitario= float(input("Digite o preço unitário: "))
    preco= quantidade*preco_unitario
    print("Preço total: ", preco)

def exemplo05():
   peso=float(input("Digite seu peso: "))
   altura=float(input("Digie sua altura: "))
   imc= peso/(altura*altura) 
   print("IMC: ",imc)

def exemplo06():
    nome= input ("Digite seu nome: ")
    idade= float (input("Diigite sua idade: ")) 
    nota1 = float (input ("Digite a nota 01: "))
    nota2 = float (input ("Digite a nota 02: "))
    nota3 = float (input ("Digite a nota 03: "))
    media =(nota1 + nota2 + nota3)/3
    print("Media: ", media)


def exemplo07():
    ladoMaior= int(input("Digite os valores que representam os lados maiores")
    ladoMenor= ind(input("Digite os valores que representam os lados menores")




exemplo06()