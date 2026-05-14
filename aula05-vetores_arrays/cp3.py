'''
Crie um programa em Python que: 
 
 Percorra toda a matriz de temperaturas. 
 
 Calcule a média de temperatura de cada sala. 
 
 Identifique quantas vezes cada sala registrou temperatura maior ou igual a 33. 
 
 Mostre, para cada sala: 
 
 número da sala; 
 
 média das temperaturas; 
 
 quantidade de registros críticos. 
 
 
 
 Ao final, informe qual sala teve a maior quantidade de registros críticos. 
'''

temperaturas = [[28, 31, 34, 33], [25, 27, 29, 28], [32, 35, 36, 34], [24, 26, 25, 27]]

tot_crit = []

for i in range(len(temperaturas)):
    soma_temp = 0
    crit = 0

    for c in range(len(temperaturas[i])):
        soma_temp += temperaturas[i][c]

        
        if(temperaturas[i][c] >= 33):
            crit += 1

    tot_crit.append(crit)

    print(f"Sala {i+1}")
    print(f"Media: {soma_temp/4}")
    print(f"Registros criticos: {crit}\n")

maior_crit = max(tot_crit)
sala_crit = tot_crit.index(maior_crit) + 1
print(f"Sala com maior risco: Sala {sala_crit}")