# Base de Conhecimento

## Dados Utilizados

| Arquivo | Formato | Para que serve no Agente? |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores, dando continuidade ao atendimento |
| `perfil_investidor.json` | JSON | Personalizar recomendações de acordo com o perfil |
| `produtos_financeiros.json` | JSON | Apresentar produtos que se encaixam no perfil |
| `transacoes.csv` | CSV | Analisar padrão de gastos do cliente |

> [!TIP]
> **Quer um dataset mais robusto?** Você pode utilizar datasets públicos do [Hugging Face](https://huggingface.co/datasets) relacionados a finanças, desde que sejam adequados ao contexto do desafio.

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Acrescido produtos na base json de Produtos Financeiros para gerar mais sugestões de acordo com perfil

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Injetar os dados diretamente no prompt ou carregar arquivos via código, como abaixo:

``` python
import pandas as pd
import json

# CSV
historico = pd.read_csv('data/historico_atendimento.csv')
transacoes = pd.read_csv('data/transacoes.csv')

#JSON
with open('data/perfil_investidor.json', 'r', encoding='utf-8') as f:
  perfil = json.load(f)

with open('data/produtos_financeiros.json', 'r', encoding='utf-8') as f:
  produtos = json.load(f)
```
### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?
Os dados podem ser injetados diretamente no prompt. Em soluções mais robustas, serão codificados de forma dinâmica, como acima.

```text
DADOS DO CLIENTE E PERFIL (data/perfil_investidor.json):
(copiar código json)

TRANSACOES DO CLIENTE (data/transacoes.csv):
(copiar as transações csv)

HISTORICO DE ATENDIMENTO (data/historico_atendimento.csv):
(copiar o historico csv)

PRODUTOS DISPONIVEIS PARA SUGESTAO (data/produtos_financeiros.json):
(copiar os produtos json)
```

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

O exemplo abaixo se baseia nos dados originais da base de conhecimento e sintetiza as informações mais importantes.

```
Dados do Cliente:
- Nome: João Silva
- Perfil: Moderado
- Saldo disponível: R$ 5.000

Últimas transações:
- 01/11: Supermercado - R$ 450
- 03/11: Streaming - R$ 55
...

Produtos Disponíveis:
- Tesouro Selic (baixo)
- CDB Liquidez Diária (baixo)
- LCI/LCA (baixo)
- Fundo Multimercado (médio)
- Fundo Imobiliário (médio)
- Fundo de Ações (alto)
```
