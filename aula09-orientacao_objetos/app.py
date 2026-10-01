from Disciplina import Disciplina
from Aluno import Aluno

pcap = Disciplina("Pensamento Computacional e Automação com Python", "Alexandre Russi")
cs = Disciplina("Computer Science", "Maurício 'MauMau'")

print(f"Disciplina: {pcap.nome} | Professor: {pcap.professor}")
print(f"Disciplina: {pcap.nome} | Professor: {cs.professor}")

print("")

lucas = Aluno("Lucas Ramos de Sousa", "573901", "Ciencia da Computacao")

print(f"Aluno: {lucas.nome} | RM: {lucas.rm} | Curso: {lucas.curso}")

print("")
lucas.vincular_disciplina(pcap)
lucas.vincular_disciplina(cs)

print(f"Disciplinas do Lucas:")

for disciplina in lucas.disciplinas:
    print(f"-{disciplina.nome} | Professor: {disciplina.professor}")

print("")

lucas.adicionar_nota(pcap, 9.0)
lucas.adicionar_nota(pcap, 10.0)
lucas.adicionar_nota(pcap, 7.0)
lucas.adicionar_nota(cs, 7.0)
lucas.adicionar_nota(cs, 7.5)
lucas.adicionar_nota(cs, 10)

print(f"Notas do Lucas:")
for disciplina, notas in lucas.notas_disciplina.items():
    print(f"{disciplina}: ")
    for i, nota in enumerate(notas):
        print(f"Nota {i+1}: {nota}")

print("")

print(f"Médias do Lucas:")
for disciplina in lucas.disciplinas:
    print(f"{disciplina.nome}: {lucas.calcular_media(disciplina):.2f}")

print("")

print(f"Média Geral do Lucas: {lucas.calcular_media_geral():.2f}")
