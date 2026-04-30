nomes = ["Lucas", "Leo", "Caio", "Enzo"]

for i in range(len(nomes)):
    for c in range(i+1, len(nomes)):
        print(nomes[i], nomes[c])