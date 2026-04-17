import json
import pandas as pd
import streamlit as st
import requests # Para chamadas de API


# CARREGAR DADOS
perfil = json.load(open('./data/perfil_investidor.json'))
transacoes = pd.read_csv(open('./data/transacoes.csv'))
historico = pd.read_csv(open('./data/historico_atendimento.csv'))
produtos = json.load(open('./data/produtos_financeiros.json'))

# CONTEXTO

contexto = f"""
CLIENTE: {repr(perfil["nome"])}, {repr(perfil["idade"])} anos, perfil {repr(perfil["perfil_investidor"])}, renda mensal de R$ {repr(perfil["renda_mensal"])}
OBJETIVO: {repr(perfil["objetivo_investimento"])}
PATRIMONIO: R$ {repr(perfil["patrimonio"])}, RESERVA: R$ {repr(perfil["reserva_emergencia"])}, INVESTIDO: R$ {repr(perfil["investido"])}

HISTÓRICO DE ATENDIMENTO: {repr(historico.to_string(index=False))}

TRANSACOES: {repr(transacoes.to_string(index=False))}

PRODUTOS FINANCEIROS: {repr(json.dumps(produtos, indent=2))}
"""
# SYSTEM PROMPT

system_prompt = f"""
Você é Adin, um agente de sugestões de investimentos financeiros.

OBJETIVO:
Você é um agente financeiro inteligente especializado em investimentos.
Seu objetivo é sugerir investimentos que se encaixem no perfil do cliente.

REGRAS:
1. NUNCA afirmar que o cliente deve comprar ou vender algum ativo.
2. NUNCA sugerir investimentos fora do perfil do cliente.
3. Se não souber algo, admita e ofereça alternativas
4. Sempre confirme se o cliente entendeu as sugestões
5. Utilizar linguagem simples e explicativa sobre as sugestões de investimento
6. NUNCA responder sobre perguntas fora do perfil de finanças e investimentos
7. Recuse educadamente toda pergunta que for fora do assunto de finanças e investimentos
8. Caso o usuário insista em algum assunto fora de finanças e investimentos, responda que é um agente especializado em finanças e investimentos e não consegue fornecer respostas para outros tipos de assuntos.
"""

# CHAMAR O AGENTE
def chamar_agente(perfil, contexto, system_prompt):
    # Aqui você pode implementar a lógica para chamar o agente Adin
    # utilizando o perfil do cliente, o contexto e o system prompt.
    # Por exemplo, você pode usar uma API de linguagem natural para gerar sugestões de investimento com base nesses dados.
    pass

# INTERFACE DE USUÁRIO
st.title("Adin - Agente de Sugestões de Investimentos")
st.write("Olá! Eu sou Adin, seu agente de sugestões de investimentos. Estou aqui para ajudar você a encontrar as melhores opções de investimento com base no seu perfil e objetivos financeiros.")
if st.button("Gerar Sugestões de Investimento"):
    chamar_agente(perfil, contexto, system_prompt)
if pergunta := st.text_input("Faça uma pergunta sobre investimentos ou finanças:"):
    st.chat_message("user").write(pergunta)
    with st.spinner("..."):
        resposta = chamar_agente(perfil, contexto, system_prompt)
        st.chat_message("assistant").write(resposta)