#Função sem retorno e sem parâmetro
def print_lyrics():
    print("I ain't gonna live forever")
    print("I just ant to live while I'm alive")

print_lyrics()
print_lyrics()
print()

#Função sem retorno e com parâmetro
def boas_vindas(nome):
    print(f"Olá, {nome}!! Seja bem-vindo")

nome = input("Digite seu nome: ")
boas_vindas(nome)
print()

#Função com retorno e com parâmetro
def soma(a, b):
    return a + b

print(soma(2, 10))