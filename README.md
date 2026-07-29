Criação do Agente de IA - Soluções Logicar 🚚

Challenge da **Alura** em parceria com a **Oracle**(ONE) para a criação de um Agente Inteligente utilizando a técnica de RAG (Retrieval-Augmented Generation). 

O projeto se trata de uma empresa ficticia de serviços de entrega e aluguel de carros e transforma os manuais de logística e tabelas de aluguel de carros em um assistente interativo capaz de responder consultas em tempo real.

![alt text](https://img.shields.io/badge/Python-3.9+-blue.svg)

![alt text](https://img.shields.io/badge/Google%20Gemini-1.5%20Flash-orange.svg)

![alt text](https://img.shields.io/badge/Framework-LangChain-green.svg)

![alt text](https://img.shields.io/badge/Cloud-OCI-red.svg)

![alt text](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow.svg)

🏆 Desafio
Desenvolver um sistema que entenda documentos específicos (PDF/CSV).
Implementar a arquitetura RAG para evitar "alucinações" da IA.
Criar uma interface amigável com Streamlit.
Realizar o deploy em uma instância na Oracle Cloud Infrastructure (OCI).

📌 Sobre a Soluções Logicar
O agente foi treinado com uma base de dados fictícia de uma empresa que une logística de transporte e aluguel de veículos.
Contexto: Regras de frete, modelos de carros (HB20, Corolla, Compass), políticas de atraso e manutenção.

⚙️ Funcionalidades Técnicas
📥 Processamento e Memória
Extração de Dados: Uso da biblioteca pypdf para leitura de documentos técnicos.
Fragmentação (Chunking): Divisão de textos via RecursiveCharacterTextSplitter para otimizar a busca.
Banco de Dados Vetorial: Uso do ChromaDB para armazenamento e recuperação eficiente de informações.

🧠 Inteligência Artificial (RAG)
Modelo de Chat: gemini-1.5-flash-latest (alta velocidade e precisão).
Embeddings: models/gemini-embedding-2 para representação numérica do conhecimento.
Framework: LangChain para orquestração do fluxo entre o PDF e a IA.

🚀 Interface e Deploy
Interface: Desenvolvida em Streamlit para um chat fluido e intuitivo.
Nuvem: Hospedado na Oracle Cloud (OCI) utilizando instâncias de computação (Virtual Machine).

🛠️ Tecnologias Utilizadas
Python (Linguagem base)
LangChain (Orquestrador da IA)
Google Gemini API (Cérebro do agente)
ChromaDB (Banco de dados de vetores)
Streamlit (Interface Web)
Oracle Cloud (OCI) (Infraestrutura de nuvem)

📖 Como Rodar o Projeto
Clone este repositório.
Instale as dependências: pip install -r requirements.txt.
Adicione sua GEMINI_API_KEY nas variáveis de ambiente.
Execute o comando: streamlit run app.py.
