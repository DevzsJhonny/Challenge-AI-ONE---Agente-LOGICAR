# Criação do Agente de IA - Soluções Logicar 🚚

Challenge da **Alura** em parceria com a **Oracle** (ONE) para a criação de um Agente Inteligente utilizando a técnica de RAG (Retrieval-Augmented Generation). 

O projeto trata-se de uma empresa fictícia de serviços de entrega e aluguel de carros e transforma os manuais de logística e tabelas de aluguel de carros em um assistente interativo capaz de responder consultas em tempo real.

![alt text](https://img.shields.io/badge/Python-3.9+-blue.svg) 
![alt text](https://img.shields.io/badge/Google%20Gemini-1.5%20Flash-orange.svg)
![alt text](https://img.shields.io/badge/Framework-LangChain-green.svg)
![alt text](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow.svg)

link da aplicação: https://challenge-alura-agente-logicar-solucoes-logisticas-e-automoveis.streamlit.app/#solucoes-logicar

 <h2>🏆 Desafio </h2>

Desenvolver um sistema que entenda documentos específicos (PDF/CSV).
Implementar a arquitetura RAG para evitar "alucinações" da IA.
Criar uma interface amigável com Streamlit.
Realizar o deploy em uma instância na Oracle Cloud Infrastructure (OCI).

<h2>📌 Sobre a Soluções Logicar</h2>
O agente foi treinado com uma base de dados fictícia de uma empresa que une logística de transporte e aluguel de veículos.

Contexto: Regras de frete, modelos de carros (HB20, Corolla, Compass), políticas de atraso e manutenção.

<h2>⚙️ Funcionalidades Técnicas</h2>
Extração de Dados: Uso da biblioteca pypdf para leitura de documentos técnicos.<br>
Fragmentação (Chunking): Divisão de textos via RecursiveCharacterTextSplitter para otimizar a busca.<br>
Banco de Dados Vetorial: Uso do ChromaDB para armazenamento e recuperação eficiente de informações.

<h2>🧠 Inteligência Artificial (RAG)</h2>
Modelo de Chat: gemini-1.5-flash-latest (alta velocidade e precisão).<br>
Embeddings: models/gemini-embedding-2 para representação numérica do conhecimento.<br>
Framework: LangChain para orquestração do fluxo entre o PDF e a IA.

<h2>🚀 Interface e Deploy</h2>
Interface: Desenvolvida em Streamlit para um chat fluido e intuitivo.<br>
Nuvem: Hospedado na Oracle Cloud (OCI) utilizando instâncias de computação (Virtual Machine).

<h2>🛠️ Tecnologias Utilizadas</h2>
Python (Linguagem base)<br>
LangChain (Orquestrador da IA)<br>
Google Gemini API (Cérebro do agente)<br>
ChromaDB (Banco de dados de vetores)<br>
Streamlit (Interface Web)<br>
Oracle Cloud (OCI) (Infraestrutura de nuvem)

<h2>📖 Como Rodar o Projeto </h2>
Clone este repositório.<br>
Instale as dependências: pip install -r requirements.txt.<br>
Adicione sua GEMINI_API_KEY nas variáveis de ambiente.<br>
Execute o comando: streamlit run app.py.
