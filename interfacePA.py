import streamlit as st
import pandas as pd
import os

# Arquivo onde os dados serão salvos permanentemente
ARQUIVO_BANCO_DADOS = "banco_inquilinos.csv"

# Função para carregar dados do arquivo CSV para o session_state
def carregar_dados():
    if os.path.exists(ARQUIVO_BANCO_DADOS):
        return pd.read_csv(ARQUIVO_BANCO_DADOS).to_dict('records')
    return []

# Função para salvar dados no arquivo CSV
def salvar_dados():
    df = pd.DataFrame(st.session_state.inquilinos)
    df.to_csv(ARQUIVO_BANCO_DADOS, index=False)

# Configuração inicial da página
st.set_page_config(page_title="Portaria de Controle Facilitado", page_icon="🏢")

# Inicializa o estado da sessão carregando do arquivo
if 'inquilinos' not in st.session_state:
    st.session_state.inquilinos = carregar_dados()

if 'pagina' not in st.session_state:
    st.session_state.pagina = 'home'

# --- Funções de Navegação ---
def ir_para(nome_da_pagina):
    st.session_state.pagina = nome_da_pagina
    st.rerun() 

# --- INTERFACE ---

# 1. Tela Inicial (Menu)
if st.session_state.pagina == 'home':
    st.title("🏢 PCF - Portaria de Controle Facilitado")
    
    #
    st.write(""" PCF é uma solução de vanguarda para o controle de acesso predial, utilizando Visão Computacional e Inteligência de Dados para otimizar o fluxo de pessoas em ambientes corporativos e residenciais.""")    

    st.write("---")
    st.write("Bem-vindo! Escolha uma opção abaixo:")
    
    col1, col2 = st.columns(2)

    with col1:
        if st.button("➕ Cadastrar Novo Inquilino", use_container_width=True):
            ir_para('cadastro')
            
    with col2:
        if st.button("📋 Ver Inquilinos Cadastrados", use_container_width=True):
            ir_para('listagem')

# 2. Tela de Cadastro
elif st.session_state.pagina == 'cadastro':
    st.title("📝 Cadastro de Inquilino")
    
    with st.form("form_cadastro"):
        nome = st.text_input("Nome Completo")
        telefone = st.text_input("Número de Telefone")
        cpf = st.text_input("CPF")
        rg = st.text_input("RG")
        imovel = st.text_input("Identificação do Imóvel (Ex: Ap 102)")
        valor = st.number_input("Valor do Aluguel (R$)", min_value=0.0, format="%.2f")
        
        enviado = st.form_submit_button("Salvar Cadastro")
        
        if enviado:
            if nome and cpf:
                novo_inquilino = {
                    "nome": nome, 
                    "cpf": cpf, 
                    "imovel": imovel, 
                    "valor": valor, 
                    "telefone": telefone, 
                    "rg": rg
                }
                # Adiciona na lista da memória (sessão)
                st.session_state.inquilinos.append(novo_inquilino)
                
                # Salva no arquivo fisicamente do CSV (está como banco_inquilinos.csv)
                salvar_dados()
                
                st.success(f"Inquilino {nome} cadastrado e salvo no banco!")
            else:
                st.error("Por favor, preencha pelo menos o Nome e o CPF.")

    if st.button("⬅️ Voltar ao Menu"):
        ir_para('home')

# 3. Tela de Listagem
elif st.session_state.pagina == 'listagem':
    st.title("📋 Inquilinos Cadastrados")
    
    if not st.session_state.inquilinos:
        st.info("Nenhum inquilino cadastrado até o momento.")
    else:
        # Exibe os dados em uma tabela
        df_mostrar = pd.DataFrame(st.session_state.inquilinos)
        st.dataframe(df_mostrar, use_container_width=True)
        
        st.write(f"**Total de inquilinos:** {len(st.session_state.inquilinos)}")

    if st.button("⬅️ Voltar ao Menu"):
        ir_para('home')
