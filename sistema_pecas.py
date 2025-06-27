
import streamlit as st
import sqlite3
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Sistema Trevo", layout="wide")

# Conexão com banco
conn = sqlite3.connect("pecas.db")
cursor = conn.cursor()

# Login simples
def login():
    st.sidebar.image("https://i.imgur.com/lQ0CN1F.jpg", width=200)
    st.sidebar.title("Login")
    user = st.sidebar.text_input("Usuário")
    senha = st.sidebar.text_input("Senha", type="password")
    if st.sidebar.button("Entrar"):
        if (user == "willian" or user == "brenda") and senha == "admin1234":
            return True
        else:
            st.sidebar.error("Usuário ou senha inválidos")
    return False

# Carregar dados
def carregar_dados():
    df = pd.read_sql_query("SELECT * FROM pecas", conn)
    return df

# Layout principal
if login():
    st.title("📦 Sistema Inteligente de Controle de Peças - Trevo")
    st.markdown("### Peças em Estoque")
    df = carregar_dados()

    # Destaque visual
    def cor_linha(row):
        if row["quantidade"] == 0:
            return ["background-color: red; color: white"] * len(row)
        elif row["quantidade"] < 3:
            return ["background-color: yellow; color: black"] * len(row)
        else:
            return [""] * len(row)

    st.dataframe(df.style.apply(cor_linha, axis=1), use_container_width=True)

    # Exportação
    st.download_button("⬇️ Exportar para Excel", data=df.to_excel(index=False), file_name="pecas.xlsx")
