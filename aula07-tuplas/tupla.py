#tuplas são imutáveis, não se altera valores já presentes nem adiciona-se valores novos
t = ('a', 'b', 'c', 'd')
print(type(t))

t1 = tuple("fiap")
print(type(t1))
print(t1)
print(t1[1:3]) #pega elementos do segundo ao terceiro

#Atribuição de tuplas
a = 5
b = 10
print(f"a = {a}, b = {b}")

a, b = b, a
print(f"a = {a}, b = {b}")

email = "fulano@gmail.com"
username, domain = email.split("@")
print(username)
print(domain)
