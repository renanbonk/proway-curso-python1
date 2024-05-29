def exemplo01():
    numero = int(input("Digite um numero: "))
   #"=="Comparar se o número informado é o 10
    if numero == 10: #se 
        print("é o número 10")
    else: #senão
        print("é diferente do número 10")

    # operadore relacionais
    # =         igual
    # >         maior
    # >=        maior ou igual
    # <         menor
    # <=        menor ou igual
    # !=        diferente

def exemplo02():
    ano_nascimento =int(input("Digite o seu ano de nascimento: "))
    if ano_nascimento > 2010:
        print("Geração alpha")
    elif ano_nascimento > 1998:
        print("Geração z")
    elif ano_nascimento > 1981:
        print("Geração y")
    elif ano_nascimento > 1961:
        print("Geração x")
    else:
        print("Baby boomers")


def exemplo03():

    produto1 = input("Digite o nome do produto: ")
    quantidade1 = int(input("Digite a quantidade: "))
    preco_unitario1 = float(input("Digite o preço unitário: "))

    produto2 = input("Digite o nome do produto: ")
    quantidade2 = int(input("Digite a quantidade: "))
    preco_unitario2 = float(input("Digite o preço unitário: "))

    produto1_total_parcial = quantidade1*preco_unitario1
    produto2_total_parcial = quantidade2*preco_unitario2

    total_compra = produto1_total_parcial + produto2_total_parcial

    forma_pagamento =int(input("\n\nFormas de pagamento: \n1 - A vista\n2 - A prazo\nEscolha: "))
    if forma_pagamento ==1:
        valor_desconto = total_compra * 0.05 
        valor_a_ser_pago = total_compra - valor_desconto
        print("O valor total da compra é: R$", total_compra)
        print("O valor do descobto é: R$", valor_desconto)
        print("O valor total a ser pago é R$:", valor_a_ser_pago)

    elif forma_pagamento == 2:
            quantidade_parcelas = int(input("informe a quantidade de parcelas: "))
            if quantidade_parcelas <= 10:
                print ("O valor a ser pago é: R$", total_compra)
            else:
                valor_acrescimo = total_compra * 0.18
                valor_a_ser_pago = total_compra + valor_acrescimo
                valor_cada_parcela = valor_a_ser_pago / quantidade_parcelas
                print("O valor total da compra é: R$", total_compra, "\nO valor do juros é: R$", valor_acrescimo)
                print("O valor total a ser pago: R$", valor_a_ser_pago)
                print("O valor de cada parcela é: R$", valor_cada_parcela)


def exemplo04():
    login = input("Digite o login: ")
    senha = input("Digite a senha: ")
    if login.lower().strip() == "admin" and senha == "1234":
        print("Login e/ou senha invádida")
    else:
        print("Login e/ou senha inválida")

    #Tabela verdade
    # V e V => V
    # F e V => F
    # V e F => F
    # F e F => F

def exemplo05():
    nome = input("Digite o nome do produto").strip
    produto_vencido_texto = input ("produto vencido? [sim/não]")
    preco_unitario = float(input("Digite o preço unitário").replace(",", ".").replace("R$",""))

    if produto_vencido_texto == "sim" or produto_vencido_texto == "s" or produto_vencido_texto == "y" or produto_vencido_texto == "yes":
        produto_vencido = true
    else:
        produto_vencido = false

def exemplo06():
    nome = input("Digite seu nome: ").strip()
    peso = float(input("Digite seu peso: "))
    altura = float(input("Digite sua altura: "))
    imc= peso/(altura*altura)
    print ("O imc é: ", imc)
    if imc <= 15.5:
        imc = abaixo do peso
    elif imc < 25:
        imc = Peso nornal
    elif imc <30:
        imc = sobrepeso
    elif imc <35: 
        imc = Obesidade grau I
    elif imc <40: 
        imc = Obesidade grau II
    elif imc >40: 
        imc = Obesidade grau III


exemplo06()

# Ex. 01: Solicite o nome, peso, altura, calcule o imc e a apresentar a classificação (buscar tabela no google)
# Ex. 02: Solicite os 3 lados e apresentar se é um triangulo equilatero, isósceles, escaleno
# Ex. 03: Solicite 3 notas, apresente a média e o status(reprovado, em exame, aprovado)
# Ex. 04: Solicite um caracter e apresente se é vogal ou consoante
# Ex. 05: Solicite um número e apresente se é positivo, negativo ou neutro.
# Ex. 06: Solicite um número e apresente se é ímpar ou negativo
# Ex. 07: Solicite um número e apresente se é maior que 8000
# Ex. 08: Solciite a idade e apresente se é bebê, criança, adolescente, adulto ou idoso
# Ex. 09: Solicite 3 números e apresente qual o menor e qual o maior
# Ex. 10: Solicite 3 números e apresente em ordem crescente
# Ex. 11: Solicite 3 números e apresente em ordem decrescente
# Ex. 12: Solicite os seguintes dados e realize a conversão da temperatura:
#           - Temperatura
#           - Temperatura origem
#           - Temperatura destino
#        Temperaturas suportadas: Celsius, Fahrenheit e Kelvin
         
   
