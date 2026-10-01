from Disciplina import Disciplina

class Aluno:
    def __init__(self, nome, rm, curso):
        self.nome = nome
        self.rm = rm
        self.curso = curso
        self.disciplinas = []
        self.notas_disciplina = {}

    def get_aluno(self):
        return(self)

    def vincular_disciplina(self, disciplina):
        self.disciplinas.append(disciplina)

        self.notas_disciplina.setdefault(disciplina.nome, [])

    def adicionar_nota(self, disciplina: Disciplina, nota):
        if len(self.notas_disciplina[disciplina.nome]) >= 3:
            print("Já foram adicionadas as 3 notas")
            return
        
        self.notas_disciplina[disciplina.nome].append(nota)

    def calcular_media(self, disciplina: Disciplina) -> float:
        notas = self.notas_disciplina.get(disciplina.nome, [])

        if not notas:
            return 0

        return sum(notas) / len(notas)

    def calcular_media_geral(self) -> float:
        medias = []

        for disciplina in self.disciplinas:
            media_d = self.calcular_media(disciplina)
            medias.append(media_d)

        if not medias:
            return 0

        return sum(medias) / len(medias)

