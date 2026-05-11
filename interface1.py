import streamlit as st

# Configuração inicial da página
st.set_page_config(page_title="Gestão de Inquilinos", page_icon="🏠")

# Inicializa a lista de inquilinos e o controle de navegação no estado da sessão
if 'inquilinos' not in st.session_state:
    st.session_state.inquilinos = []

if 'pagina' not in st.session_state:
    st.session_state.pagina = 'home'

# --- Funções de Navegação ---
def ir_para(nome_da_pagina):
    st.session_state.pagina = nome_da_pagina

# --- INTERFACE ---

# 1. Tela Inicial (Menu)
if st.session_state.pagina == 'home':
    st.title("🏠 Sistema de Gestão de Aluguel")
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
        cpf = st.text_input("CPF")
        imovel = st.text_input("Identificação do Imóvel (Ex: Ap 102)")
        valor = st.number_input("Valor do Aluguel (R$)", min_value=0.0, format="%.2f")
        
        enviado = st.form_submit_button("Salvar Cadastro")
        
        if enviado:
            if nome and cpf:
                # Salva os dados na lista
                novo_inquilino = {"nome": nome, "cpf": cpf, "imovel": imovel, "valor": valor}
                st.session_state.inquilinos.append(novo_inquilino)
                st.success(f"Inquilino {nome} cadastrado com sucesso!")
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
        # Exibe os dados em uma tabela bonitinha
        st.table(st.session_state.inquilinos)
        
        # Opcional: Mostrar como cartões métricos
        st.write(f"**Total de inquilinos:** {len(st.session_state.inquilinos)}")

    if st.button("⬅️ Voltar ao Menu"):
        ir_para('home')
        