from dotenv import load_dotenv
import os
import json
from langchain_google_genai import ChatGoogleGenerativeAI
from state import CVState



# Configuração

load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")




llm = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview",
    temperature=0,
    api_key=API_KEY
)



# Função utilitária

def extrair_texto(resposta):
    """
    Normaliza a resposta do Gemini.
    Pode vir como string simples ou lista estruturada.
    """
    conteudo = resposta.content

    if isinstance(conteudo, list):
        return conteudo[0]["text"]

    return conteudo



# Nodes do LangGraph


def extrair_skills(state: CVState):
    prompt = f"""
    Extraia as principais habilidades técnicas deste currículo:

    {state['cv_text']}

    Retorne APENAS uma lista JSON válida.
    Exemplo:
    ["Python", "SQL", "Machine Learning"]
    """

    resposta = llm.invoke(prompt)
    texto = extrair_texto(resposta)

    try:
        skills = json.loads(texto)
    except json.JSONDecodeError:
        raise ValueError(f"O modelo não retornou um JSON válido:\n{texto}")

    return {"extracted_skills": skills}


def calcular_compatibilidade(state: CVState):
    prompt = f"""
    Considerando as habilidades do candidato: {state['extracted_skills']}

    E a descrição da vaga:
    {state['job_text']}

    Forneça uma pontuação de compatibilidade entre 0 e 100.
    Retorne APENAS o número.
    """

    resposta = llm.invoke(prompt)
    texto = extrair_texto(resposta).strip()

    try:
        score = float(texto)
    except ValueError:
        raise ValueError(f"O modelo não retornou um número válido:\n{texto}")

    return {"score": score}


def no_decisao(state: CVState):
    score = state["score"]

    if score >= 75:
        decisao = "Candidatar-se"
    elif score >= 50:
        decisao = "Melhorar Currículo"
    else:
        decisao = "Não Compatível"

    return {"decision": decisao}


def gerar_feedback(state: CVState):
    prompt = f"""
    Com base na descrição da vaga:

    {state['job_text']}

    E na pontuação de compatibilidade: {state['score']}

    Sugira melhorias específicas para o currículo do candidato.
    Seja direto e profissional.
    """

    resposta = llm.invoke(prompt)
    texto = extrair_texto(resposta)

    return {"feedback": texto}
