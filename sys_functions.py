from helpers import forca_opcao, meu_index, print_de_opcoes

lista_tipo_dados = ['1', '2']
lista_dados_opcao = ['1', '0']
lista_dados_especificos = ['1', '2', '3', '4', '5']

lista_circuitos = ["Monaco", "Anhembi", "Paris"]
sensor_DHT_umidade = [35, 55, 15]
sensor_DHT_temp = [30, 15, 5]
sensor_proximidade_destrocos = [50, 150, 200]

lista_pilotos = ["King", "Mortara", "De Vries"]
equipe_pilotos = ["Mahindra", "Mahindra", "Mahindra"]
colocacao_pilotos = ["23", "20", "17"]
pontos_pilotos = ["4", "7", "21"]


def sys_dados():
    print(f"Bem-vindo ao banco de dados Mahindra Racing,\naqui você encontrará todos os tipos de dados "
          f"capturados pelos nossos sensores e muito mais!\n")

    def exibir_diagrama():
        print("\nDiagrama de informações:\n"
              "Umidade:\n - abaixo de 30% = ambiente seco\n - acima de 70% = possibilidade de chuva\n "
              "- entre 30 e 50 = estado ideal\n - entre 51 e 69 = em alerta de chuva\n"
              "Temperatura:\n - entre 25 e 50ºC = normal\n - acima de 80ºC = temperatura elevada\n - "
              "abaixo de 25ºC = temperatura abaixo\n - entre 51 e 79 = temperatura em alerta\n"
              "Proximidade:\n - acima ou igual a 200m = destroços não detectados\n - abaixo de 200m = "
              "objeto detectado\n - abaixo ou igual a 50m = destroços detectados\n")

    def exibir_resultado(local_circuito):
        print(f"\nResultado: O circuito de(o) {lista_circuitos[local_circuito]} está com "
              f"umidade de {sensor_DHT_umidade[local_circuito]}%, "
              f"temperatura está em {sensor_DHT_temp[local_circuito]}ºC, "
              f"e a distância do sensor de proximidade é de {sensor_proximidade_destrocos[local_circuito]} metros\n")

    def exibir_dado_especifico(local_circuito, dado_especifico):
        if dado_especifico == '1':
            print("Umidade:\n - abaixo de 30% = ambiente seco\n - acima de 70% = possibilidade de chuva\n - entre 30 e 50% = estado ideal\n - entre 51 e 69% = em alerta de chuva\n"
                  f"Umidade está em {sensor_DHT_umidade[local_circuito]}%\n")
        elif dado_especifico == '2':
            print("Temperatura:\n - entre 25 e 50ºC = normal\n - acima de 80ºC = temperatura elevada\n - "
                  "abaixo de 25ºC = temperatura abaixo\n - entre 51 e 79 = temperatura em alerta\n"
                  f"Temperatura está em {sensor_DHT_temp[local_circuito]}ºC\n")
        elif dado_especifico == '3':
            print("Proximidade:\n - acima ou igual a 200m = destroços não detectados\n - abaixo de 200m = "
                  "objeto detectado\n - abaixo ou igual a 50m = destroços detectados\n"
                  f"Distância do sensor de proximidade é de {sensor_proximidade_destrocos[local_circuito]} metros\n")

    def exibir_dados_piloto(local_piloto):
        print(f"\nDados do piloto {lista_pilotos[local_piloto]}:\n"
              f"Equipe: {equipe_pilotos[local_piloto]}\n"
              f"Colocação: {colocacao_pilotos[local_piloto]}\n"
              f"Pontos: {pontos_pilotos[local_piloto]}\n")

    while True:
        escolha_tipo_dado = forca_opcao("Deseja acessar dados do circuito ou dos pilotos? (1 - Circuito, 2 - Pilotos)\n--> ",
                                        lista_tipo_dados, "Opção inválida! Digite 1 para Circuito ou 2 para Pilotos.")
        if escolha_tipo_dado == '1':
            escolha_circuito = forca_opcao("Digite um circuito que deseja procurar dados\n --> ", lista_circuitos,
                                           "Opção Inválida!\nPor favor, escolha um dos circuitos disponíveis:\n" + print_de_opcoes(lista_circuitos))
            local_circuito = meu_index(lista_circuitos, escolha_circuito)
            escolha_tipo_dados = forca_opcao("Você deseja ver opções detalhadas ou específicas? (1 - opções detalhadas e 2 - opções específicas)\n--> ",
                                             lista_tipo_dados, "Digite apenas os números correspondentes ao caminho indicado")
            if escolha_tipo_dados == '1':
                exibir_diagrama()
                exibir_resultado(local_circuito)
            elif escolha_tipo_dados == '2':
                dados_especifico = forca_opcao("Qual dado você deseja procurar?\n 1 - Umidade\n 2 - Temperatura\n 3 - Proximidade\n--> ",
                                               lista_dados_especificos, "Digite apenas os números correspondentes ao caminho indicado")
                exibir_dado_especifico(local_circuito, dados_especifico)

        elif escolha_tipo_dado == '2':
            escolha_piloto = forca_opcao("Digite o piloto que deseja procurar dados\n --> ", lista_pilotos,
                                         "Opção inválida!\nPor favor, escolha um dos pilotos disponíveis:\n" + print_de_opcoes(lista_pilotos))
            local_piloto = meu_index(lista_pilotos, escolha_piloto)
            exibir_dados_piloto(local_piloto)

        escolha_dados = forca_opcao("O que você deseja fazer?\n 1 - Nova pesquisa\n 0 - Voltar para o menu\n--> ",
                                    lista_dados_opcao, "Opção inválida! Digite apenas os números correspondentes ao caminho indicado")
        if escolha_dados == '1':
            continue
        elif escolha_dados == '0':
            break
