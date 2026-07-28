# Criação do Agente de IA para a empresa Soluções LOGICAR

Challenge da **Alura** em parceria com a **Oracle** - para criar um Agente Inteligente,  que transforma documentos técnicos em conhecimento estruturado por meio de classificação temática, extração de palavras-chave e técnicas de Inteligência Artificial.

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Google Gemini](https://img.shields.io/badge/Google%20Gemini-1.0%20Pro-orange.svg)
![Colab](https://img.shields.io/badge/Google%20Colab-Suportado-yellow.svg)
![Status](https://img.shields.io/badge/Status-Funcionando-brightgreen.svg)

## 🏆 Desafio

1. Criar um agente de IA
2. Processar documentos (PDF/CSV)
3. Fazer deploy na Oracle Cloud (OCI)

## 📌 Sobre o Projeto

Um **Agente Inteligente** capaz de analisar documentos PDF e responder perguntas utilizando :

- 🧠 **Google Gemini Pro** para processamento de linguagem natural
- 📄 **PyPDF2** para extração de texto de documentos
- ☁️ **Google Colab** como ambiente de desenvolvimento
- 🚀 **OCI** para deploy na nuvem


## 🎯 Objetivo
Facilitar a consulta e análise de documentos complexos, permitindo que colaboradores obtenham respostas rápidas e precisas em linguagem natural.


## 💡 Solução Proposta

A solução recebe documentos técnicos em PDF (como relatórios de riscos a direitos humanos) e utiliza **técnicas avançadas de Inteligência Artificial** (Google Gemini) para analisar o conteúdo e retornar **informações estruturadas e respostas em linguagem natural**.

## ⚙️ Funcionalidades Técnicas

### 📥 Processamento de Documentos
- **Upload de PDFs** via Google Colab
- **Extração automática** de texto com PyPDF2
- **Limpeza e preparação** do texto para análise

### 🧠 Inteligência Artificial
- **Modelo:** Google Gemini Pro (via API)
- **Técnica:** RAG (Retrieval-Augmented Generation)
- **Contexto:** Os documentos são usados como base de conhecimento
- **Personalização:** O agente responde APENAS com base no documento fornecido
