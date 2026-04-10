'''
Faça um programa para a leitura de quatro notas parciais de um aluno. O programa deve calcular a média alcançada pelo aluno e apresentar:
    A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    A mensagem "Em recuperação", se a média for entre cinco, incluindo o cinco, e sete;
    A mensagem "Reprovado", se a média for menor que cinco
'''

nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
nota3 = float(input("Digite sua terceira nota: "))
nota4 = float(input("Digite sua quarta nota: "))

def calcular_media(n1, n2, n3, n4):
    return round((n1 + n2 + n3 + n4) / 4 ,2)

media = calcular_media(nota1, nota2, nota3, nota4)

if(media >= 7):
    print(f"Média: {media}, Status: Aprovado!")
elif(media >= 5):
    print(f"Média: {media}, Status: Em Recuperação!")
else:
    print(f"Média: {media}, Status: Reprovado!")