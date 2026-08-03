import streamlit as st
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.vectorstores import Chroma
from langchain_classic.chains import RetrievalQA
from langchain_core.prompts import PromptTemplate
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

# 1. Configuração Visual
st.set_page_config(page_title="Soluções Logicar", page_icon="🚚")
st.title("🚚 Soluções Logicar")
st.markdown("Assistente Virtual de Logística e Aluguel de Automóveis")

# 2. PEGAR A CHAVE AUTOMATICAMENTE
# Ele tenta pegar da variável de ambiente que definimos no Colab
api_key = os.getenv("GEMINI_API_KEY")

if api_key:
    os.environ["GOOGLE_API_KEY"] = api_key

    @st.cache_resource
    def inicializar_agente(key):
        loader = PyPDFLoader("dados_logicar.pdf")
        documentos = loader.load()
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        chunks = text_splitter.split_documents(documentos)

        embeddings = GoogleGenerativeAIEmbeddings(
            model="models/gemini-embedding-2",
            google_api_key=key
        )
        vectorstore = Chroma.from_documents(documents=chunks, embedding=embeddings)

        llm = ChatGoogleGenerativeAI(
            model="gemini-flash-latest",
            google_api_key=key,
            temperature=0
        )

        template_logicar = """
        Você é o assistente virtual oficial da Soluções Logicar.
        Use APENAS os trechos do documento fornecidos abaixo para responder à pergunta.
        Se a informação não estiver no texto, responda: "Sinto muito, mas não encontrei essa informação no manual da Soluções Logicar."

        CONTEXTO:
        {context}

        PERGUNTA:
        {question}

        RESPOSTA:"""

        PROMPT = PromptTemplate(template=template_logicar, input_variables=["context", "question"])

        return RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=vectorstore.as_retriever(),
            chain_type_kwargs={"prompt": PROMPT}
        )

    # O agente já inicia com a chave automática
    agente_logicar = inicializar_agente(api_key)

    # 3. Interface de Chat
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Como posso ajudar?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Consultando manual..."):
                resultado = agente_logicar.invoke(prompt)
                st.markdown(resultado['result'])
                st.session_state.messages.append({"role": "assistant", "content": resultado['result']})
