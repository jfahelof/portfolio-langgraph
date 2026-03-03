from langgraph.graph import StateGraph, END
from state import CVState
from nodes import extrair_skills, calcular_compatibilidade, no_decisao, gerar_feedback


builder = StateGraph(CVState)

# Adicionando nós
builder.add_node("extrair_skills", extrair_skills)
builder.add_node("calcular_compatibilidade", calcular_compatibilidade)
builder.add_node("no_decisao", no_decisao)
builder.add_node("gerar_feedback", gerar_feedback)

# Ponto de entrada
builder.set_entry_point("extrair_skills")

# Fluxo do grafo
builder.add_edge("extrair_skills", "calcular_compatibilidade")
builder.add_edge("calcular_compatibilidade", "no_decisao")
builder.add_edge("no_decisao", "gerar_feedback")
builder.add_edge("gerar_feedback", END)

graph = builder.compile()
