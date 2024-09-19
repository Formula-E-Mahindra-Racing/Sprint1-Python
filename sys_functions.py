from helpers import forca_opcao, print_de_opcoes

def exibir_diagrama():
    print("\nDiagrama de informações:\n"
          "Umidade:\n - abaixo de 30% = ambiente seco\n - acima de 70% = possibilidade de chuva\n "
          "- entre 30 e 50% = estado ideal\n - entre 51 e 69% = em alerta de chuva\n"
          "\nTemperatura:\n - entre 25 e 50ºC = normal\n - acima de 80ºC = temperatura elevada\n - "
          "abaixo de 25ºC = temperatura baixa\n - entre 51 e 79 = temperatura em alerta\n"
          "\nProximidade:\n - acima ou igual a 200m = destroços não detectados\n - abaixo de 200m = "
          "objeto detectado\n - abaixo ou igual a 50m = destroços detectados\n")

def exibir_resultado(circuito):
    dados = circuitos[circuito]
    print(f"\nResultado: O circuito de {circuito} está com umidade de {dados['umidade']}%, "
          f"temperatura de {dados['temperatura']}ºC, e proximidade de {dados['proximidade']} metros.")

def exibir_dados_piloto(piloto):
    dados = pilotos[piloto]
    print(f"\nDados do piloto {piloto}:\n"
          f"Equipe: {dados['equipe']}\nColocação: {dados['colocacao']}\nPontos: {dados['pontos']}")

def sys_dados():
    print(f"Bem-vindo ao banco de dados Mahindra Racing!")
    while True:
        tipo_dado = forca_opcao("Deseja acessar dados do circuito ou dos pilotos? (1 - Circuito, 2 - Pilotos)\n--> ",
                                ['1', '2'], "Opção inválida!")
        if tipo_dado == '1':
            print_de_opcoes(circuitos.keys())
            circuito = forca_opcao("Digite o nome do circuito:\n--> ", circuitos.keys(), "Circuito inválido!")
            tipo_exibicao = forca_opcao("Você deseja ver opções detalhadas (1) ou específicas (2)?\n--> ", ['1', '2'],
                                        "Opção inválida!")
            if tipo_exibicao == '1':
                exibir_diagrama()
                exibir_resultado(circuito)
            else:
                dado = forca_opcao("Qual dado específico deseja ver?\n1 - Umidade\n2 - Temperatura\n3 - Proximidade\n--> ",
                                   ['1', '2', '3'], "Opção inválida!")
                if dado == '1':
                    print(f"Umidade: {circuitos[circuito]['umidade']}%")
                elif dado == '2':
                    print(f"Temperatura: {circuitos[circuito]['temperatura']}ºC")
                elif dado == '3':
                    print(f"Proximidade: {circuitos[circuito]['proximidade']} metros")
        elif tipo_dado == '2':
            print_de_opcoes(pilotos.keys())
            piloto = forca_opcao("Digite o nome do piloto:\n--> ", pilotos.keys(), "Piloto inválido!")
            exibir_dados_piloto(piloto)
        continuar = forca_opcao("Deseja fazer uma nova pesquisa? (1 - Sim, 0 - Não)\n--> ", ['1', '0'], "Opção inválida!")
        if continuar == '0':
            break

circuitos = {
    "Monaco" : {"umidade" : 35, "temperatura" : 30, "proximidade" : 50},
    "Sao Paulo" : {"umidade" : 60, "temperatura" : 11, "proximidade" : 150},
    "Paris" : {"umidade" : 25, "temperatura" : -5, "proximidade" : 200},
    "Miami" : {"umidade" : 60, "temperatura" : 30, "proximidade" : 499},
    "Tokyo" : {"umidade" : 30, "temperatura" : 5, "proximidade" : 379},
    "Rome" : {"umidade" : 10, "temperatura" : 35, "proximidade" : 250},
    "Mexico" : {"umidade" : 50, "temperatura" : 31, "proximidade" : 175},
    "Buenos Aires" : {"umidade" : 50, "temperatura" : 10, "proximidade" : 100},
    "Punta del Este" : {"umidade" : 20, "temperatura" : 20, "proximidade" : 200}
}

pilotos = {
    "King" : {"equipe" : "Mahindra", "colocacao" : 23, "pontos" : 4},
    "Mortara" : {"equipe" : "Mahindra", "colocacao" : 20, "pontos" : 7},
    "De Vries" : {"equipe" : "Mahindra", "colocacao" : 17, "pontos" : 21}
}
