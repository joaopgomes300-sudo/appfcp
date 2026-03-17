import streamlit as st
import requests

# Configuração da página (deve ser a primeira linha)
st.set_page_config(page_title="Porto Resultados", page_icon="🔵")

# Estilo CSS para as cores do Porto
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .stText { color: #00428c; }
    .jogo-card {
        background-color: white;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #00428c;
        margin-bottom: 10px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# Cabeçalho com Logótipo
col1, col2 = st.columns([1, 4])
with col1:
    st.image("https://upload.wikimedia.org/wikipedia/pt/1/1c/FC_Porto.png", width=70)
with col2:
    st.title("FC Porto")
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
        # Inverter para mostrar o mais recente primeiro e pegar os últimos 5
        for jogo in reversed(jogos[-8:]):
            casa = jogo['homeTeam']['name']
            fora = jogo['awayTeam']['name']
            gols_casa = jogo['score']['fullTime']['home']
            gols_fora = jogo['score']['fullTime']['away']
            data = jogo['utcDate'][:10]
            
            # Criar um "Card" para cada jogo
            with st.container():
                st.markdown(f"""
                <div class="jogo-card">
                    <small>{data}</small><br>
                    <strong>{casa} {gols_casa} — {gols_fora} {fora}</strong>
                </div>
                """, unsafe_allow_html=True)
    else:
        st.error("Sem ligação aos dados. Tenta mais tarde.")
except:
    st.error("Erro técnico ao carregar resultados.")

st.info("App atualizada automaticamente via Football-Data API.")
