'''
Faça um programa que receba o ano de nascimento da pessoa e retorne:
Se o voto é obrigatório este ano;
Se o voto é opcional este ano;
Se o voto é proibido este ano
'''

ano_nascimento = int(input("Digite seu ano de nascimento: "))

idade = 2026 - ano_nascimento

def verificar_obrigatoriedade_voto(i):
    if(i >= 18 and i < 70):
        print(f"Você tem {i} anos, seu voto é obrigatório")
    elif(i < 16):
        print(f"Você tem {i} anos, você não pode votar.")
    else:
        print(f"Você tem {i} anos, seu voto é opcional.")

verificar_obrigatoriedade_voto(idade)