# verificador-de-gastos

# 💰 Verificador de Gastos (Calculadora de Orçamento)

Este é um programa simples em Python que ajuda a organizar as finanças de casa. Ele lê uma lista de gastos salvos em um arquivo de planilha (formato `.csv`), soma tudo o que você gastou por categoria (como Alimentação, Transporte, Moradia) e mostra um relatório organizado direto na tela.

## 🚀 O que o programa faz?

* 📂 **Lê os seus gastos:** Abre o arquivo com a lista das suas compras.
* 🧮 **Soma tudo sozinho:** Junta os valores que pertencem à mesma categoria.
* 📈 **Mostra a porcentagem:** Calcula quanto cada categoria representa no seu bolso (ex: descobrir se você está gastando mais com comida ou com lazer).
* 🛡️ **Evita travamentos:** Se você esquecer de criar o arquivo de gastos, o programa não trava; ele apenas avisa que o arquivo sumiu.

## 📁 Como deve ser o arquivo de gastos (`gastos.csv`)

O programa precisa de um arquivo de texto chamado `gastos.csv` na mesma pasta. O conteúdo dele deve ser assim:

```csv
data,descricao,categoria,valor
01/05/2024,Aluguel,Moradia,1200.00
02/05/2024,Supermercado,Alimentacao,450.50
05/05/2024,Internet,Lazer,100.00
10/05/2024,Restaurante,Alimentacao,80.00
12/05/2024,Gasolina,Transporte,200.00
