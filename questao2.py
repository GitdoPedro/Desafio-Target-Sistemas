import random

maior = 0
menor = 101
total = 0
diasFaturamentoMaiorMedia = 0
faturamentoDiario = []



for i in range(250): # 250 como uma média de dias úteis do ano
    faturamento = random.randint(1,1000) # faturamento hipotético de 1 a 1000
    faturamentoDiario.append(faturamento) 
    
    total += faturamento

mediaAnual = total/250

for dia in faturamentoDiario:
    if dia > maior:
        maior = dia
    if dia < menor:
        menor = dia

    if dia > mediaAnual:
        diasFaturamentoMaiorMedia += 1


print(" O menor valor de faturamento ocorrido em um dia do ano foi R$ {:0,.2f} " .format(menor))
print(" O maior valor de faturamento ocorrido em um dia do ano foi R$ {:0,.2f} " .format(maior))
print("Número de dias no ano em que o valor de faturamento diário foi superior à média anual foi: " ,diasFaturamentoMaiorMedia)
