# A. Print com nome completo e menu para cliente
print('Bem vindos a loja de Marmitas do LF\n')
print('--------------------------------------Menu---------------------------------------------')
print('Tamanho P de Bife Acebolado (BA) custa 16 reais e o Filé de Frango (FF) custa 15 reais.')
print('Tamanho M de Bife Acebolado (BA) custa 18 reais e o Filé de Frango (FF) custa 17 reais.')
print('Tamanho G de Bife Acebolado (BA) custa 22 reais e o Filé de Frango (FF) custa 21 reais.\n')

# E. Acumulador para somar os valores dos pedidos
total_pedido = 0

while True:
    # B. Input do sabor
    sabor = input('\nEntre com o sabor desejado (BA/FF): ').upper()
    # Verifica se o sabor é válido
    if sabor != 'BA' and sabor != 'FF':
        print('Sabor inválido. Tente novamente.')
        continue

    # C. input do tamanho
    tamanho = input('Entre com o tamanho desejado (P/M/G): ').upper()
    # Verifica se o tamanho é válido
    if tamanho != 'P' and tamanho != 'M' and tamanho != 'G':
        print('Tamanho inválido. Tente novamente.')
        continue

    # D. Lógica de cálculo de preço com if e elif
    if sabor == 'BA':
        if tamanho == 'P':
            total_pedido += 16
            print('Você pediu Bife Acebolado no tamanho P: R$ 16.00\n')
        elif tamanho == 'M':
            total_pedido += 18
            print('Você pediu Bife Acebolado no tamanho M: R$ 18.00\n')
        elif tamanho == 'G':
            total_pedido += 22
            print('Você pediu Bife Acebolado no tamanho G: R$ 22.00\n')
    elif sabor == 'FF':
        if tamanho == 'P':
            total_pedido += 15
            print('Você pediu Filé de Frango no tamho P: R$ 15.00\n')
        elif tamanho == 'M':
            total_pedido += 17
            print('Você pediu Filé de Frango no tamho M: R$ 17.00\n')
        elif tamanho == 'G':
            total_pedido += 21
            print('Você pediu Filé de Frango no tamho G: R$ 21.00\n')

    # F. Input para perguntar se deseja mais alguma coisa
    continuar = input('Deseja mais alguma coisa? (S/N): ').upper()

    if continuar == 'S':
        continue
    else:
        break
# G. Print do acumulador
print(f'\nO valor total a ser pago: R$ {total_pedido:.2f}')