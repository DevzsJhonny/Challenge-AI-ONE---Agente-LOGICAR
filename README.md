# Criação do Agente de IA - Soluções Logicar 🚚

Challenge da **Alura** em parceria com a **Oracle** (ONE) para a criação de um Agente Inteligente utilizando a técnica de **RAG (Retrieval-Augmented Generation)**. 

O projeto apresenta uma empresa fictícia de serviços de entrega e locação de veículos. O agente transforma manuais complexos de logística e frota em um assistente interativo capaz de responder consultas precisas em tempo real.

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg) 
![Google Gemini](https://img.shields.io/badge/Google%20Gemini-1.5%20Flash-orange.svg)
![Framework](https://img.shields.io/badge/Framework-LangChain-green.svg)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen.svg)

## 🚀 Link da Aplicação
[Clique aqui para acessar o Agente Soluções Logicar](https://challenge-alura-agente-logicar-solucoes-logisticas-e-automoveis.streamlit.app/)

## 🏆 Desafio 
- Desenvolver um sistema que interprete documentos específicos (PDF/CSV).
- Implementar a arquitetura RAG para evitar "alucinações" da IA.
- Criar uma interface amigável e corporativa com Streamlit.
- Realizar a disponibilização em ambiente de nuvem.

## 📌 Sobre a Soluções Logicar
O agente foi alimentado com uma base de conhecimento detalhada abrangendo:
- **Logística e Entregas:** Valores de frete por KM, categorias de veículos (motos, vans, carretos e carretas) e prazos de entrega.
- **Locação de Frota:** Modelos disponíveis (HB20, Onix, Corolla, Cronos, Yaris e Motos) e valores de diárias.
- **Políticas e Diretrizes:** Requisitos de **CNH Definitiva**, regras contra avarias e plano de manutenção preventiva.

## ⚙️ Funcionalidades Técnicas
- **Extração de Dados:** Uso da biblioteca `pypdf` para leitura de múltiplos documentos técnicos.
- **Fragmentação (Chunking):** Divisão estratégica de textos via `RecursiveCharacterTextSplitter` para otimizar a recuperação de contexto.
- **Banco de Dados Vetorial:** Uso do **ChromaDB** para armazenamento e busca semântica eficiente.

## 🧠 Inteligência Artificial (RAG)
- **Modelo de Chat:** `gemini-1.5-flash-latest` (focado em alta velocidade e precisão).
- **Embeddings:** `models/gemini-embedding-2` para representação numérica do conhecimento.
- **Framework:** `LangChain` para orquestração do fluxo entre a documentação e a IA.

## 🚀 Interface e Deploy
- **Interface:** Desenvolvida em Streamlit com design corporativo e histórico de chat.
- **Nuvem:** Disponibilizado via Streamlit Community Cloud (com integração contínua via GitHub).

## 🛠️ Tecnologias Utilizadas
- **Python** (Linguagem base)
- **LangChain** (Orquestrador da IA)
- **Google Gemini API** (Cérebro do agente)
- **ChromaDB** (Banco de dados de vetores)
- **Streamlit** (Interface Web)

## 📖 Como Rodar o Projeto Localmente
1. Clone este repositório.
2. Instale as dependências: `pip install -r requirements.txt`.
3. Adicione sua `GEMINI_API_KEY` nas variáveis de ambiente ou no arquivo de segredos.
4. Execute o comando: `streamlit run app.py`.
