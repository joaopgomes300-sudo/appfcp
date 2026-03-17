import streamlit as st
import requests

# Configuração da página
st.set_page_config(page_title="Porto Resultados", page_icon="🔵")

# Estilo CSS corrigido para visibilidade total
st.markdown("""
    <style>
    /* Forçar o fundo da página para um tom cinza claro */
    .stApp {
        background-color: #f0f2f6;
    }
    /* Estilo dos cartões de jogo */
    .jogo-card {
        background-color: #ffffff !important;
        padding: 20px;
        border-radius: 12px;
        border-left: 8px solid #00428c;
        margin-bottom: 15px;
        box-shadow: 0px 4px 6px rgba(0,0,0,0.1);
    }
    /* Forçar a cor do texto dentro dos cartões para Preto/Azul */
    .jogo-card h4, .jogo-card p, .jogo-card b, .jogo-card span {
        color: #1e1e1e !important;
        margin: 0;
    }
    .data-texto {
        color: #666666 !important;
        font-size: 0.8rem;
    }
    .resultado-texto {
        font-size: 1.1rem;
        color: #00428c !important;
    }
    </style>
    """, unsafe_allow_html=True)

# Título Simples
st.title("🔵 FC Porto")
st.subheader("Resultados Recentes")

# Configurações da API
API_KEY = "39ef6a8b48ea4d0ea3a5157105ec0ddf"
PORTO_ID = 503
URL = f"https://api.football-data.org/v4/teams/{PORTO_ID}/matches?status=FINISHED"

headers = {"X-Auth-Token": API_KEY}

try:
    response = requests.get(URL, headers=headers)
    if response.status_code == 200:
        jogos = response.json()['matches']
        # Mostra os últimos 8 jogos, do mais recente para o mais antigo
        for jogo in reversed(jogos[-8:]):
            casa = jogo['homeTeam']['name']
            fora = jogo['awayTeam']['name']
            gols_casa = jogo['score']['fullTime']['home']
            gols_fora = jogo['score']['fullTime']['away']
            data = jogo['utcDate'][:10]
            
            # Formatação da data (DD/MM/AAAA)
            data_pt = "/".join(reversed(data.split("-")))

            # HTML do Card com texto forçado em cor escura
            st.markdown(f"""
                <div class="jogo-card">
                    <span class="data-texto">{data_pt}</span><br>
                    <b class="resultado-texto">{casa} {gols_casa} — {gols_fora} {fora}</b>
                </div>
                """, unsafe_allow_html=True)
    else:
        st.error("Erro ao ligar à API. Verifica a tua chave.")
except Exception as e:
    st.error(f"Erro técnico: {e}")
