import json

with open('dados.json') as f:
    dados = json.load(f)

menor = float('inf')
maior = float('-inf')

soma = 0
dias_com_faturamento = 0
for d in dados:
    if d['valor'] > 0:
        soma += d['valor']
        dias_com_faturamento += 1
    if d['valor'] < menor:
        menor = d['valor']
    if d['valor'] > maior:
        maior = d['valor']
media_mensal = soma / dias_com_faturamento

dias_acima_da_media = 0
for d in dados:
    if d['valor'] > media_mensal:
        dias_acima_da_media += 1

print(f"Menor faturamento diário: R${menor:.2f}")
print(f"Maior faturamento diário: R${maior:.2f}")
print(f"Dias com faturamento acima da média mensal: {dias_acima_da_media}")
