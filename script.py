def fatorial(n):
  resultado = 1
  while(n > 0):
    resultado *= n
    n -= 1
  return(resultado)

def pascal(linha_n):
  linha = []
  i = linha_n
  while (i >= 0):
    termo = fatorial(linha_n)/(fatorial(i)*fatorial(linha_n - i))
    linha.append(int(termo))
    i -= 1
  return(linha)

altura = int(input("Digite a altura que deseja: "))
triangulo_pascal = []

for i in range(altura):
  triangulo_pascal.append(pascal(i))
  
for i in range(altura):
  print (triangulo_pascal[i])

####################################################
anterior2 = 0
anterior = 1
atual = anterior2 + anterior
n_termos = int(input("Digite quantos termos deseja: "))
fibonnacci = "0, 1"
entre_termos = ", "

if n_termos == 1:
  print ("0")

elif n_termos == 2:
  print (fibonnacci)

else:
  for i in range(n_termos - 2):
    fibonnacci += entre_termos + str(atual)
    anterior2 = anterior
    anterior = atual
    atual = anterior2 + anterior
  print (fibonnacci)
