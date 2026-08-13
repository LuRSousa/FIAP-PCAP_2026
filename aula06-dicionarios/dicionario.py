eng2sp = dict()
print(eng2sp)

eng2sp['one'] = 'uno'
print(eng2sp)
print()

eng2sp = {
    'one': 'uno',
    'two': 'dos',
    'three': 'tres'
}
print(eng2sp)
print()

print(eng2sp['two'])
print()

#Verifica se o texto pedido é uma chave
print('one' in eng2sp)
print('uno' in eng2sp) #É um valor, então retorna false
print()

#Para verificar se um valor está na tabela colocasse todos numa lista e compara
vals = eng2sp.values()
print('uno' in vals)
print()