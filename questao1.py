anterior = 0
proximo = 0
seq = []

numero = input()

while(proximo <= int(numero)):
  seq.append(proximo)
  proximo = proximo + anterior
  anterior = proximo - anterior
  if(proximo == 0):
      proximo = proximo + 1


if int(numero) in seq:
    print('o número ' + numero + ' está contido em')
   

else:
    print('o número ' + numero + ' não está contido em')
    
print(seq)
