import streamlit as st
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.vectorstores import Chroma
from langchain_classic.chains import RetrievalQA
from langchain_core.prompts import PromptTemplate
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFDirectoryLoader

# --- 1. CONFIGURAÇÃO DA PÁGINA E ESTILO 
st.set_page_config(
    page_title="Soluções Logicar",
    page_icon="🚚",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Injeção de CSS para layout Profissional
st.markdown("""
<style>
    /* Cores: Azul Marinho (#1B263B), Cinza (#F0F2F6), Laranja Logística (#F39C12) */
    .block-container { padding-top: 2rem; max-width: 1100px; }
    
    /* Sidebar Escura Corporativa */
    section[data-testid="stSidebar"] { 
        background-color: #0D1B2A; 
        color: white; 
    }
    
    /* Títulos da Sidebar */
    .sidebar-title { font-size: 1.5rem; font-weight: 700; color: #E0E1DD; margin-bottom: 0px; }
    .sidebar-sub { color: #778DA9; font-size: 0.9rem; margin-bottom: 20px; }
    
    /* Botões Modernos em Azul/Slate */
    .stButton>button {
        width: 100%; border-radius: 8px; 
        background-color: #415A77; 
        color: white; border: none;
        transition: 0.3s;
    }
    .stButton>button:hover { 
        background-color: #F39C12; /* Laranja ao passar o mouse para destaque */
        color: white; 
    }
    
    /* Ajuste de cor do Divider na lateral */
    hr { border-color: #415A77; }
</style>
""", unsafe_allow_html=True)

# --- 2. CONFIGURAÇÃO DA CHAVE API ---
api_key = os.getenv("GEMINI_API_KEY")

# --- 3. SIDEBAR  ---
with st.sidebar:
    st.markdown('<div class="sidebar-title">🚚 Soluções Logicar</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-sub">Assistente Logístico</div>', unsafe_allow_html=True)
    st.divider()
    
    st.subheader("Atuação Especializada em:")
    st.markdown("""
    - 📦 Logística Urbana
    - 🚗 Aluguel de Frota
    - 🏍️ Entregas Rápidas
    """)
    

# --- 4. INICIALIZAÇÃO DO AGENTE (Lógica RAG) ---
if api_key:
    os.environ["GOOGLE_API_KEY"] = api_key

    @st.cache_resource
    def inicializar_agente(key):
        # Carrega todos os PDFs da pasta "documentos"
        if not os.path.exists("documentos"):
            os.makedirs("documentos") # Cria a pasta se não existir
            
        loader = PyPDFDirectoryLoader("documentos")
        documentos = loader.load()
        
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        chunks = text_splitter.split_documents(documentos)

        embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-2", google_api_key=key)
        vectorstore = Chroma.from_documents(documents=chunks, embedding=embeddings)

        llm = ChatGoogleGenerativeAI(model="gemini-flash-latest", google_api_key=key, temperature=0)

        # PROMPT TEMPLATE
        template_final = """
        Você é o assistente virtual oficial da Soluções Logicar. 
        Sua função é responder dúvidas dos usuários utilizando UNICAMENTE as informações presentes nos manuais fornecidos.

        =========================
        REGRAS DE CONDUTA
        =========================
        1. Utilize apenas o contexto recuperado. Nunca invente informações.
        2. Explique com suas próprias palavras de forma clara, objetiva e cordial.
        3. Use listas ou parágrafos curtos para facilitar a leitura.
        4. Introduza respostas baseadas em regras com: "Conforme a política da empresa...", "Segundo as diretrizes internas..." ou "De acordo com o procedimento da Soluções Logicar...".
        5. Nunca mencione nomes de arquivos (.pdf, etc) ou detalhes técnicos.
        6. Se a informação não existir, responda exatamente: "Não encontrei essa informação na documentação da empresa."
        7. Se a pergunta for fora do tema, diga: "No momento, posso ajudar apenas com informações presentes na documentação interna da Soluções LOGICAR. Sinta-se à vontade para perguntar sobre aluguel de frotas, fretes de entrega ou detalhes dos nossos serviços."

        =========================
        DIRETRIZES ESPECÍFICAS LOGICAR
        =========================
        - CNH: Exigir sempre CNH DEFINITIVA. Proibido PPD.
        - MANUTENÇÃO: Revisão a cada 10.000km ou vistoria mensal.
        - ENTREGAS: O frete é baseado exclusivamente na quilometragem (KM).
        - ESTADO DO VEÍCULO: Devolução sem avarias; danos são cobrados.

        CONTEXTO: {context}
        PERGUNTA: {question}
        RESPOSTA DO ASSISTENTE:"""

        PROMPT = PromptTemplate(template=template_final, input_variables=["context", "question"])

        return RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=vectorstore.as_retriever(search_kwargs={"k": 3}),
            chain_type_kwargs={"prompt": PROMPT}
        )

    agente_logicar = inicializar_agente(api_key)

    # --- 5. INTERFACE DE CHAT ---
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Olá! Sou o assistente da **Soluções Logicar**. Posso responder dúvidas sobre logística, frota e procedimentos internos. Como posso ajudar?"}
        ]

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    col1, col2 = st.columns([5, 1]) 
    with col2:
        if st.button("🗑️ Limpar"):
            st.session_state.messages = [
                {"role": "assistant", "content": "Olá! Sou o assistente da **Soluções Logicar**. Posso responder dúvidas sobre logística, frota e procedimentos internos. Como posso ajudar?"}
            ]
            st.rerun()

    if prompt := st.chat_input("Pergunte sobre os veículos, fretes, serviços ou políticas nos manuais..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Analisando documentação interna..."):
                try:
                    resultado = agente_logicar.invoke(prompt)
                    resposta = resultado['result']
                except Exception as e:
                    resposta = "Desculpe, ocorreu um erro ao consultar os manuais. Tente novamente."
                
                st.markdown(resposta)
                st.session_state.messages.append({"role": "assistant", "content": resposta})
else:
    st.error("Chave API não configurada! Verifique as Secrets do ambiente.")
