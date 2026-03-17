import streamlit as st
import requests

# Configurações Iniciais
st.set_page_config(page_title="FC Porto Digital", page_icon="🔵", layout="wide")
API_KEY = "39ef6a8b48ea4d0ea3a5157105ec0ddf"
PORTO_ID = 503
headers = {"X-Auth-Token": API_KEY}

# --- MENU LATERAL ---
st.sidebar.image("https://upload.wikimedia.org/wikipedia/pt/1/1c/FC_Porto.png", width=100)
st.sidebar.title("Porto App")
aba = st.sidebar.radio("Ir para:", ["Resultados", "Plantel", "Calendário"])

# --- FUNÇÃO PARA CARREGAR DADOS ---
def get_data(endpoint):
    url = f"https://api.football-data.org/v4/{endpoint}"
    return requests.get(url, headers=headers).json()

# --- ABA: RESULTADOS ---
if aba == "Resultados":
    st.header("🔵 Últimos Resultados")
    dados = get_data(f"teams/{PORTO_ID}/matches?status=FINISHED")
    
    for jogo in reversed(dados['matches'][-10:]):
        with st.expander(f"⚽ {jogo['homeTeam']['shortName']} {jogo['score']['fullTime']['home']} - {jogo['score']['fullTime']['away']} {jogo['awayTeam']['shortName']}"):
            col1, col2, col3 = st.columns(3)
            with col1:
                st.image(jogo['homeTeam']['crest'], width=50)
                st.write(jogo['homeTeam']['name'])
            with col2:
                st.headline("VS")
                st.write(jogo['utcDate'][:10])
            with col3:
                st.image(jogo['awayTeam']['crest'], width=50)
                st.write(jogo['awayTeam']['name'])
            st.write("**Competição:** " + jogo['competition']['name'])

# --- ABA: PLANTEL ---
elif aba == "Plantel":
    st.header("🦁 Plantel Principal")
    dados = get_data(f"teams/{PORTO_ID}")
    for jogador in dados['squad']:
        st.write(f"👕 **{jogador['jerseyNumber'] if jogador['jerseyNumber'] else ''}** - {jogador['name']} ({jogador['position']})")

# --- ABA: CALENDÁRIO ---
elif aba == "Calendário":
    st.header("📅 Próximos Jogos")
    dados = get_data(f"teams/{PORTO_ID}/matches?status=SCHEDULED")
    for jogo in dados['matches'][:5]:
        st.info(f"{jogo['utcDate'][:10]} | {jogo['homeTeam']['name']} vs {jogo['awayTeam']['name']}")
