import streamlit as st
import pandas as pd
from datetime import datetime

# Configurações iniciais da página
st.set_page_config(page_title="SecurePass - Reconhecimento Facial", layout="wide")

# --- ESTILO CUSTOMIZADO ---
st.markdown("""
    <style>
    .stApp { background-color: #f5f7f9; }
    [data-testid="stMetricValue"] { font-size: 1.8rem; }
    </style>
    """, unsafe_allow_html=True)

# --- CABEÇALHO ---
st.title("🛡️ SecurePass: Gestão de Acesso Inteligente")
st.write("Solução em Reconhecimento Facial para Residências e Condomínios.")

st.divider()

# --- ÁREA DE APRESENTAÇÃO DO PRODUTO ---
tab1, tab2, tab3 = st.tabs(["📊 Dashboard de Acessos", "👥 Gestão de Usuários", "⚙️ Configurações do Sistema"])

with tab1:
    st.header("Monitoramento em Tempo Real")
    
    # Métricas principais
    m1, m2, m3 = st.columns(3)
    m1.metric("Moradores Ativos", "124", "+2 nesta semana")
    m2.metric("Acessos Temporários", "12", "Expira em 24h")
    m3.metric("Alertas de Segurança", "0", "Normal", delta_color="normal")

    st.subheader("Últimas Identificações")
    
    # Simulação de logs de acesso (Dicionário corrigido)
    dados_logs = [
        {"Hora": "14:20", "Nome": "Ana Silva", "Tipo": "Morador", "Status": "Acesso Liberado"},
        {"Hora": "14:15", "Nome": "João Souza", "Tipo": "Temporário (Airbnb)", "Status": "Acesso Liberado"},
        {"Hora": "13:55", "Nome": "Carlos Oliveira", "Tipo": "Morador", "Status": "Acesso Liberado"},
        {"Hora": "13:30", "Nome": "Desconhecido", "Tipo": "N/A", "Status": "Alerta Enviado"},
    ]
    
    df_logs = pd.DataFrame(dados_logs)
    
    # Exibindo a tabela formatada
    st.dataframe(df_logs, use_container_width=True, hide_index=True)

with tab2:
    st.header("Gestão de Moradores e Visitantes")
    col1, col2 = st.columns(2)
    
    with col1:
        st.text_input("Nome do Usuário")
        st.selectbox("Tipo de Acesso", ["Permanente", "Temporário", "Serviço"])
        st.date_input("Data de Início")
        
    with col2:
        st.file_uploader("Upload de Foto para Reconhecimento", type=['jpg', 'png', 'jpeg'])
        if st.button("Cadastrar no Sistema"):
            st.success("Usuário cadastrado com sucesso!")

with tab3:
    st.header("Configurações")
    st.toggle("Ativar Reconhecimento em Tempo Real", value=True)
    st.slider("Precisão do Algoritmo (Threshold)", 0.0, 1.0, 0.85)