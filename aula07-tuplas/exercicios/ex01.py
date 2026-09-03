#Pegar CSV com lista de email do dominio aluno da fiap (ALUN, FIAP, etc)
#Separar username do domain de todos e contar quanto tem de cada um em uma tupla

emails = (
    "ana.silva@alura.com.br",
    "bruno.souza@fiap.com.br",
    "carlos.oliveira@alura.com.br",
    "diana.costa@caelum.com.br",
    "eduardo.santos@alura.com.br",
    "fernanda.lima@fiap.com.br",
    "gabriel.martins@alura.com.br",
    "helena.rocha@caelum.com.br",
    "igor.almeida@alura.com.br",
    "juliana.ribeiro@fiap.com.br",
    "lucas.carvalho@alura.com.br",
    "mariana.mendes@caelum.com.br",
    "nicolas.ferreira@alura.com.br",
    "patricia.gomes@fiap.com.br",
    "rafael.pereira@alura.com.br",
    "sabrina.teixeira@caelum.com.br",
    "thiago.araujo@alura.com.br",
    "vanessa.barbosa@fiap.com.br",
    "william.nunes@alura.com.br",
    "yasmim.correia@caelum.com.br",
    "andre.moura@alura.com.br",
    "beatriz.cardoso@fiap.com.br",
    "daniel.farias@alura.com.br",
    "elaine.machado@caelum.com.br",
    "felipe.dias@alura.com.br",
    "giovana.monteiro@fiap.com.br",
    "henrique.freitas@alura.com.br",
    "isabela.castro@caelum.com.br",
    "joao.vieira@alura.com.br",
    "karina.rezende@fiap.com.br",
    "leonardo.campos@alura.com.br",
    "leticia.nogueira@caelum.com.br",
    "marcos.batista@alura.com.br",
    "natalia.pinto@fiap.com.br",
    "otavio.moraes@alura.com.br",
    "priscila.tavares@caelum.com.br",
    "rodrigo.barros@alura.com.br",
    "simone.cunha@fiap.com.br",
    "vinicius.coelho@alura.com.br",
    "aline.dantas@caelum.com.br",
    "caio.azevedo@alura.com.br",
    "debora.siqueira@fiap.com.br",
    "evandro.pacheco@alura.com.br",
    "flavia.assis@caelum.com.br",
    "gustavo.melo@alura.com.br",
    "isadora.peixoto@fiap.com.br",
    "jorge.valente@alura.com.br",
    "luana.borges@caelum.com.br",
    "murilo.queiroz@alura.com.br",
    "renata.xavier@fiap.com.br",
    "sergio.amorim@alura.com.br"
)

usernames = []
domains = []

for email in emails:
    #usernames.append(email.split("@")[0])
    nome = email.split("@")[0].split(".")[0]
    sobrenome = email.split("@")[0].split(".")[1]
    
    usernames.append(nome + " " + sobrenome)
    domains.append(email.split("@")[1])

dict_domains = dict()

for d in domains:
    if d not in dict_domains:
        dict_domains[d] = 1
    else:
        dict_domains[d] += 1
        
print(dict_domains)
print()

usernames = tuple(usernames)
print(usernames)
print()

#usernames[0], usernames[-1] = usernames[-1], usernames[0]

#print(usernames)
#print()
