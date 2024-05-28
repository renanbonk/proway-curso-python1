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


exemplo02()
         
   
