# A. Print com o nome completo
print('“Bem vindos a Fábrica de Camisetas do LF')

# B. Função com a escolha do modelo
def escolha_modelo():

    while True:
        # B-a. Pregunta o número de camisetas
        print('Entre com modelo desejado.')
        print('MCS - Manga Curta Simples.')
        print('MLS - Manga Longa Simples.')
        print('MCE - Manga Curta Com Estampa.')
        print('MLE - Manga Longa Com EStampa.')
        modelo = input('>> ').upper()
        # B-b. Retorna o valor do modelo
        if modelo != 'MCS' and modelo != 'MLS' and modelo != 'MCE' and modelo != 'MLE':
            print('Escolha inválida, entre com o modelo novamente')
            continue  
        elif modelo == 'MCS':
            return 1.80
        elif modelo == 'MLS':
            return 2.10
        elif modelo == 'MCE':
            return 2.90
        elif modelo == 'MLE':
            return 3.20
# C. Função com número de camisetas      
def num_camisetas():

    while True:
        try:
            # C-a. Pergunta o números de camisetas
            num_camisetas = int(input('Entre com o número de camisetas: '))

            # C-b. Retorna o números de camisetas com desconto
            if num_camisetas > 20000:
                print('Não aceitamos tantas camisetas de uma vez.')
                print('Por favor, entre com o número de camisetas novamente.')
            elif num_camisetas < 20:
                return num_camisetas, 0.0
            elif num_camisetas >= 20 and num_camisetas < 200:
                return num_camisetas, 0.05
            elif num_camisetas >= 200 and num_camisetas < 2000:
                return num_camisetas, 0.07
            elif num_camisetas >= 2000 and num_camisetas <= 20000:
                return num_camisetas, 0.12
        except:
            print('Erro inesperado ao processar o número de camisetas.')

# D. Função com o frete
def frete():

    while True:
        try:
            # D-a. Pergunta pelo serviço adicional do frete
            print('Escolha o tipo de frete:')
            print('1 - Frete por Transportadora - R$ 100.00')
            print('2 - Frete por Sedex - R$ 200.00')
            print('0 - Retirar pedido na Fábrica - R$ 0.00')
            frete_opcao = int(input('>> '))

            # D-b. Retorna o valor dos fretes
            if frete_opcao == 1:
                return 100.00
            elif frete_opcao == 2:
                return 200.00
            elif frete_opcao == 0:
                return 0.00
            else:
                print('Opção inválida.')
            
        except:
            print('Opção inválida.')

# E. Implementação do (Main)
if __name__ == '__main__':

    # Solicitação de escolha do modelo de camiseta
    preco_modelo = escolha_modelo()

    # Solicitação do número de camisetas
    num, desconto = num_camisetas()
    preco_unitario = preco_modelo * (1 - desconto)

    # Solicitação da escolha do tipo de frete
    valor_frete = frete()

    # Cálculo do valor total a pagar
    total = (preco_unitario * num) + valor_frete

    # Saída de console com pedido válido
    print(f'Total: R${total:.2f}')