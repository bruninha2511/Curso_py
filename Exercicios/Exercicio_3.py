# exercicios de FOR e WHILE 
# exercicio um ***

from time import sleep
for con in range(10, -1 , -1):
  print(con)
  sleep(0.3)
print('Feliz ano novo!!!!')

# exercicio dois ***

num=int(input('Digite um número: '))

for n in range(1, 101):
  if n % num == 0:
    print('Os múltiplos de {} são {}'.format(num, n))

# exercicio três ***

num = int(input('Digite um numero: '))
for cont in range(1, 11):
  res= num * cont
  print(f'{num} x {cont} = {res}')

# exercicio quatro ***

soma1= 0 
cont1= 0

soma2= 0
cont2= 0

for c in range(1,11):
  num= int(input('Digite o {} valor: '.format(c)))
  if num % 2 == 0:
    soma1 += num 
    cont1 += 1
  elif num % 1 == 0:
    soma2 += num 
    cont2 += 1
   
print('Você informou {} números IMPARES e a soma foi {}'.format(cont2, soma2))

print('Você informou {} números PARES e a soma foi {}'.format(cont1, soma1))

# exercicio cinco ***
maior= 0
menor= 0

for n in range(1, 5):
  num = float(input('Digite o {} número:'.format(n)))
  if n == 1:
    maior = n
    menor = n
  else:
     if num > maior:
       maior = num
     if num < menor:
       menor = num

print('O maior número encontrado foi de {}'.format(maior))

print('O menor número encontrado foi de {}'.format(menor))
  
# exercicio seis 