# Função para inserir os resultados dos candidatos
def inserir_resultados():
    resultados = {}
    print("Insira os resultados dos candidatos.")
    while True:
        nome = input("Digite o nome do candidato (ou digite 'fim' para encerrar): ")
        if nome.lower() == 'fim':
            break
        
        #Solicitação das notas de cada etapa
        nota_e = input(f"Digite a nota de entrevista para o candidato {nome}: ")
        nota_t = input(f"Digite a nota de teste teórico para o candidato {nome}: ")
        nota_p = input(f"Digite a nota de teste prático para o candidato {nome}: ")
        nota_s = input(f"Digite a nota de avaliação de soft skills para o candidato {nome}: ")
        
        #Concatenação das notas no formato eX_tX_pX_sX
        resultado = f"e{nota_e}_t{nota_t}_p{nota_p}_s{nota_s}"
        resultados[nome] = resultado
    return resultados

# Função para buscar candidatos com notas maiores ou iguais às especificadas pelo usuário
def buscar_candidatos(resultados, nota_e, nota_t, nota_p, nota_s):
    candidatos_compativeis = []
    for nome, resultado in resultados.items():
        notas = [int(nota[1:]) for nota in resultado.split('_')]
        if all(nota >= min_nota for nota, min_nota in zip(notas, [nota_e, nota_t, nota_p, nota_s])):
            candidatos_compativeis.append(nome)
    return candidatos_compativeis

# Solicitando os resultados dos candidatos
resultados = inserir_resultados()

# Solicitando as notas mínimas ao usuário
nota_e = int(input("Digite a nota mínima para a etapa de entrevista: "))
nota_t = int(input("Digite a nota mínima para a etapa de teste teórico: "))
nota_p = int(input("Digite a nota mínima para a etapa de teste prático: "))
nota_s = int(input("Digite a nota mínima para a etapa de avaliação de soft skills: "))

# Buscando candidatos compatíveis
candidatos_compativeis = buscar_candidatos(resultados, nota_e, nota_t, nota_p, nota_s)

# Exibindo os candidatos compatíveis
if candidatos_compativeis:
    print("Candidatos compatíveis:")
    for candidato in candidatos_compativeis:
        print(candidato)
else:
    print("Nenhum candidato encontrado com as notas mínimas especificadas.")