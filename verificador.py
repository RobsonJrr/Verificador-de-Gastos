import csv

def carregar_dados(caminho_arquivo):
    """Lê o arquivo CSV e retorna uma lista de dicionários."""
    transacoes = []
    try:
        with open(caminho_arquivo, mode='r', encoding='utf-8') as arquivo:
            leitor_csv = csv.DictReader(arquivo)
            for linha in leitor_csv:
                linha['valor'] = float(linha['valor'])
                transacoes.append(linha)
        return transacoes
    except FileNotFoundError:
        print(f"Erro: O arquivo {caminho_arquivo} não foi encontrado.")
        return []

def calcular_totais_por_categoria(transacoes):
    """Agrupa os gastos por categoria e soma os valores."""
    totais = {}
    for item in transacoes:
        cat = item['categoria']
        valor = item['valor']
        
        if cat in totais:
            totais[cat] += valor
        else:
            totais[cat] = valor
    return totais

def exibir_relatorio(totais):
    """Imprime um relatório formatado no console."""
    print("\n" + "="*30)
    print("  RELATÓRIO DE GASTOS")
    print("="*30)
    
    gasto_total = sum(totais.values())
    
    for categoria, valor in totais.items():
        percentual = (valor / gasto_total) * 100
        print(f"{categoria:15}: R$ {valor:>8.2f} ({percentual:>5.1f}%)")
    
    print("-"*30)
    print(f"TOTAL GERAL:    R$ {gasto_total:>8.2f}")
    print("="*30)

def main():
    arquivo_nome = 'gastos.csv'
    dados = carregar_dados(arquivo_nome)
    
    if dados:
        resumo = calcular_totais_por_categoria(dados)
        exibir_relatorio(resumo)

if __name__ == "__main__":
    main()