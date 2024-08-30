# A. Print com o nome completo
print('Bem-vindos a loja do LF')

# B. Input do Valor do pedido e Quantidade de parcelas
valorDoPedido = float(input('Entre com o valor do Pedido: '))
quantidadeParcelas = int(input('Entre com a quantidade de Parcelas: '))

# C. Juros 
# E. Implementação do if, elif e else
if quantidadeParcelas < 4:
    juros = 0.0

elif quantidadeParcelas >= 4 and quantidadeParcelas < 6:
    juros = 0.04

elif quantidadeParcelas >= 6 and quantidadeParcelas < 9:
    juros = 0.08

elif quantidadeParcelas >= 9 and quantidadeParcelas < 13:
    juros = 0.16

else:
    juros = 0.32

# D. Valor da Parcela e Valor Total Parcelado
valorDaParcela = (valorDoPedido * (1 + juros)) / quantidadeParcelas
valorTotalParcelado = valorDaParcela * quantidadeParcelas

print(f'O valor das parcelas é de: R$ {valorDaParcela:.2f}')
print(f'O valor total parcelado é de: R$ {valorTotalParcelado:.2f}')