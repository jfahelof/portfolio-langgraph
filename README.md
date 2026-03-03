# 🧠 Sistema Inteligente de Análise de Currículos com LangGraph

Este projeto implementa um sistema automatizado de análise de currículos utilizando **LangGraph + Gemini (Google Generative AI)**.

O sistema é capaz de:

- 🔎 Extrair habilidades técnicas do currículo  
- 📊 Calcular a compatibilidade com uma vaga  
- 🎯 Tomar uma decisão automática  
- 💡 Gerar feedback personalizado para melhoria do currículo  

---

## 🚀 Arquitetura do Projeto

O fluxo é estruturado como um **grafo direcionado (DAG)** usando LangGraph.

### 🔄 Fluxo do Sistema

Currículo → Extração de Skills → Cálculo de Compatibilidade → Decisão → Feedback

Cada nó transforma o estado do sistema até gerar o resultado final.

---

## 📂 Estrutura do Projeto

```
LangGraph/
│
├── .env
├── cv.txt
├── job.txt
├── state.py
├── nodes.py
├── graph.py
├── main.py
├── requirements.txt
└── README.md
```

### 📄 Descrição dos Arquivos

- **cv.txt** → Texto do currículo  
- **job.txt** → Texto da descrição da vaga  
- **state.py** → Definição do estado compartilhado do grafo  
- **nodes.py** → Implementação dos nós (LLM + lógica de negócio)  
- **graph.py** → Construção e compilação do grafo  
- **main.py** → Execução do sistema  
- **.env** → Chave da API do Google Gemini  

---

## 🧩 Tecnologias Utilizadas

- Python 3.11+  
- LangGraph  
- LangChain  
- Google Gemini (via `langchain-google-genai`)  
- python-dotenv  

---

## ⚙️ Como Executar

### 1️⃣ Clonar o repositório

```bash
git clone <seu-repositorio>
cd LangGraph
```

### 2️⃣ Criar ambiente virtual (recomendado)

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
```

No Windows:

```bash
venv\Scripts\activate
```

### 3️⃣ Instalar dependências

```bash
pip install -r requirements.txt
```

### 4️⃣ Configurar chave da API

Crie um arquivo `.env` na raiz do projeto:

```
GOOGLE_API_KEY=sua_chave_aqui
```


### 5️⃣ Executar o projeto

```bash
python main.py
```

---

## 🧠 Como Funciona Internamente

O sistema utiliza um estado compartilhado (`CVState`) que é passado entre os nós do grafo:

```python
{
  "cv_text": str,
  "job_text": str,
  "extracted_skills": list,
  "score": float,
  "decision": str,
  "feedback": str
}
```

---

## 🔹 Nós do Grafo

### extrair_skills
- Usa LLM para extrair habilidades técnicas do currículo  
- Retorna uma lista JSON estruturada  

### calcular_compatibilidade
- Analisa skills vs descrição da vaga  
- Retorna score entre 0 e 100  

### no_decisao
Regra de negócio:
- ≥ 75 → Candidatar-se  
- ≥ 50 → Melhorar Currículo  
- < 50 → Não Compatível  

### gerar_feedback
- Gera recomendações específicas para melhorar o currículo  

---

## 📊 Exemplo de Saída

```python
{
  "score": 95.0,
  "decision": "Candidatar-se",
  "feedback": "Sugestões detalhadas para melhoria..."
}
```

---

## 🎯 Objetivo do Projeto

Este projeto demonstra:

- Uso prático de LangGraph  
- Orquestração de múltiplas chamadas a LLM  
- Pipeline estruturado com estado compartilhado  
- Aplicação real de IA para triagem de currículos  

---

## 🔮 Possíveis Evoluções

- Transformar em API com FastAPI  
- Criar interface web com Streamlit  
- Upload automático de PDF  
- Multi-agentes especializados  
- Fluxo condicional no grafo  
- Persistência de histórico  

---

## 👨‍💻 Autor

Projeto desenvolvido para estudo de arquiteturas baseadas em LLMs, LangGraph e aplicações reais de IA.
