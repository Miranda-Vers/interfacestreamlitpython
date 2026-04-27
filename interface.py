import streamlit as st
import pandas as pd
import numpy as np

# Configuração da página
##st.set_page_config(page_title="Minha Apresentação Interativa", layout="centered")
st.set_page_config(
    page_title="BioAccess - Reconhecimento Facial", 
    layout="wide", 
    initial_sidebar_state="expanded"
)
# --- TÍTULO E INTRODUÇÃO ---
st.title("🚀 Apresentação com Streamlit")
st.subheader("Transformando scripts Python em interfaces web")

st.markdown("""
Esta é uma breve demonstração de como você pode usar o Streamlit para criar 
apresentações dinâmicas. Você pode incluir textos, gráficos e elementos de entrada.
""")

# --- BARRA LATERAL (Interatividade) ---
st.sidebar.header("🏢 BioAccess")
nome_usuario = st.sidebar.text_input("Qual é o seu nome?", "Visitante")
exibir_dados = st.sidebar.checkbox("Mostrar tabela de dados brutos")

# --- SEÇÃO 1: GRÁFICOS ---
st.header(f"Bem-vindo, {nome_usuario}!")
st.write("Abaixo, um exemplo de gráfico gerado aleatoriamente:")

# Criando dados fictícios
dados = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['Vendas', 'Custo', 'Lucro']
)

# Exibindo o gráfico de linha
st.line_chart(dados)

# --- SEÇÃO 2: TABELAS ---
if exibir_dados:
    st.write("### Dados Detalhados")
    st.dataframe(dados) # Tabela interativa
else:
    st.info("A tabela de dados está oculta. Use a barra lateral para visualizar.")

# --- SEÇÃO 3: FEEDBACK ---
st.divider()
status = st.radio("O que achou desta interface?", ("Incrível", "Útil", "Pode melhorar"))

if st.button("Enviar Feedback"):
    st.success(f"Obrigado pelo feedback, {nome_usuario}! Você selecionou: {status}")