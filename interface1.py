import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="PCF") # ISSO DEVE VIR PRIMEIRO
# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="PCF - Reconhecimento Facial", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- ESTILIZAÇÃO CUSTOMIZADA ---
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stButton>button { width: 100%; border-radius: 8px; height: 3em; background-color: #070d14; color: white; }
    </style>
    """, unsafe_allow_html=True)

# --- BARRA LATERAL ---
st.sidebar.header("🏢 PCF")

nome_apresentador = st.sidebar.text_input("Nome do Apresentador", "Equipe PCF")
menu = st.sidebar.selectbox("Ir para:", ["Introdução", "Simulador Biométrico", "Análise de Dados"])

st.sidebar.divider()
exibir_detalhes = st.sidebar.checkbox("Exibir logs técnicos", value=False)

# --- LÓGICA DE NAVEGAÇÃO ---

if menu == "Introdução":
    st.title("🚀 PCF: O Futuro do Acesso Predial")
    st.subheader(f"Apresentado por: {nome_apresentador}")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        Nossa solução utiliza **Visão Computacional** para transformar a segurança em prédios comerciais e residenciais. 
        Diferenciamos automaticamente dois fluxos principais:
        
        * **👥 Convívio Normal:** Moradores e funcionários (Acesso Ultra Rápido).
        * **🛠️ Especializados:** Prestadores de serviço e manutenção (Acesso Controlado).
        """)
        st.info("💡 *Dica: Use o menu lateral para testar o protótipo.*")
    with col2:
        st.markdown("O sistema opera via redes neurais convolucionais para garantir precisão de 99.9%.")

elif menu == "Simulador Biométrico":
    st.header("📸 Protótipo de Reconhecimento")
    st.write("Abaixo simulamos a lógica de identificação de perfis.")

    col_cam, col_res = st.columns([3, 2])
    
    with col_cam:
        
        
        st.warning("Simulação de Câmera Ativada (Hardware desativado para estabilidade).")
        simular_captura = st.button("Simular Captura de Rosto")

    with col_res:
        if simular_captura:
            with st.status("Processando biometria...", expanded=exibir_detalhes) as status:
                st.write("Buscando pontos nodais...")
                time.sleep(1)
                st.write("Consultando banco de dados...")
                time.sleep(0.8)
                status.update(label="Análise Concluída!", state="complete")

            perfil = st.radio("Escolha o perfil para demonstrar:", ["Normal", "Especializado", "Desconhecido"])
            
            if perfil == "Normal":
                st.success("✅ **ACESSO LIBERADO**")
                st.markdown("### Usuário: João Silva\n**Cargo:** Analista Financeiro - Sala 402")
            elif perfil == "Especializado":
                st.warning("⚠️ **AGUARDANDO AUTORIZAÇÃO**")
                st.markdown("### Empresa: Elevadores Atlas\n**Motivo:** Manutenção Preventiva")
            else:
                st.error("❌ **ACESSO NEGADO**")
                st.write("Pessoa não identificada.")

elif menu == "Análise de Dados":
    st.header("📊 Inteligência de Tráfego")
    
    chart_data = pd.DataFrame(
        np.random.randint(1, 50, size=(24, 2)),
        columns=['Acessos Normais', 'Acessos Especializados']
    )

    st.line_chart(chart_data)

    if exibir_detalhes:
        st.subheader("Tabela de Registros (Logs)")
        st.dataframe(chart_data, use_container_width=True)

st.divider()
st.write("### Avaliação da Interface")
feedback = st.select_slider("O que achou?", options=["Pode melhorar", "Bom", "Excelente", "Incrível"])

if st.button("Enviar Avaliação"):
    st.balloons()
    st.toast(f"Feedback de {nome_apresentador} recebido!")
