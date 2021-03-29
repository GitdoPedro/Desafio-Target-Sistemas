faturamentoMensal = {'SP'    : 67836.43,
                     'RJ'    : 36678.66,
                     'MG '   : 29229.88,
                     'ES'    : 27165.48,
                     'Outros':19849.53 }

total = 0
percentual = 0
for estado in faturamentoMensal:
    total+= faturamentoMensal[estado]
    
print("Percentual de faturamento por estado: ")


for estado in faturamentoMensal:
    print(estado+" ", end = "")
    percentual = (faturamentoMensal[estado]*100)/total
    print('{:0,.2f} % ' .format(percentual))

    
    
