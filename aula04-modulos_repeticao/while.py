cp = 0

while cp < 3:
    print(f"Produto {cp}")
    cp += 1

#while decrescente
i = 4

while i >= 0:
    print(i)
    i -= 1

#repretição com entrada de usuário
jogar = 'sim'

while jogar.lower() == "sim":
    print("Repete ou inicia o jogo")
    jogar = input("Deseja jogar novamente?")

#modificadores de laço (break e continue)
i = 0
while i < 10:
    i += 1

    if i == 3 or i == 5:
        continue

    if i == 7:
        break

    print(f"Produto 2: {i}")