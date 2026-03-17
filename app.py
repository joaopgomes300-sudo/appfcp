import streamlit as st
import requests

# Configuração da página para parecer uma App
st.set_page_config(page_title="Porto App", page_icon="🔵", layout="centered")

# Estilo CSS para parecer uma App de telemóvel
st.markdown("""
    <style>
    .stApp { background-color: #00264d; } /* Azul escuro fundo */
    [data-testid="stSidebar"] { background-color: #001a33; }
    .main-card {
        background-color: white;
        padding: 15px;
        border-radius: 15px;
        margin-bottom: 15px;
        color: #00264d;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    .team-name { font-weight: bold; font-size: 1.1rem; }
    .score { font-size: 1.5rem; font-weight: 900; color: #00428c; }
    </style>
    """, unsafe_allow_html=True)

API_KEY = "39ef6a8b48ea4d0ea3a5157105ec0ddf"
PORTO_ID = 503
headers = {"X-Auth-Token": API_KEY}

def get_data(endpoint):
    url = f"https://api.football-data.org/v4/{endpoint}"
    res = requests.get(url, headers=headers)
    return res.json()

# Menu Lateral
st.sidebar.title("🔵 FCP Navigation")
aba = st.sidebar.radio("Menu", ["Resultados", "Plantel", "Calendário"])

if aba == "Resultados":
    st.title("⚽ Resultados")
    dados = get_data(f"teams/{PORTO_ID}/matches?status=FINISHED")
    
    if 'matches' in dados:
        for jogo in reversed(dados['matches'][-10:]):
            casa = jogo['homeTeam']
            fora = jogo['awayTeam']
            score = jogo['score']['fullTime']
            
            # Criar um "botão" expansível para ver estatísticas
            with st.expander(f"🗓️ {jogo['utcDate'][:10]} | {casa['shortName']} {score['home']} - {score['away']} {fora['shortName']}"):
                col1, col2, col3 = st.columns([2,1,2])
                with col1:
                    st.image(casa['crest'], width=60)
                    st.write(f"**{casa['name']}**")
                with col2:
                    st.markdown(f"<p class='score'>{score['home']} - {score['away']}</p>", unsafe_allow_html=True)
                with col3:
                    st.image(fora['crest'], width=60)
                    st.write(f"**{fora['name']}**")
                
                st.divider()
                st.write(f"🏆 **Competição:** {jogo['competition']['name']}")
                st.write(f"📍 **Jornada:** {jogo.get('matchday', 'N/A')}")

elif aba == "Plantel":
    st.title("🦁 Plantel Principal")
    dados = get_data(f"teams/{PORTO_ID}")
    if 'squad' in dados:
        for j in dados['squad']:
            # Correção do erro: usamos o método .get() para não dar erro se faltar o número
            numero = j.get('jerseyNumber', 'S/N')
            st.markdown(f"""
            <div style='background: white; padding: 10px; border-radius: 10px; margin-bottom: 5px; color: black;'>
                <b>#{numero}</b> - {j['name']} <br>
                <small>📍 {j['position']} | 🏳️ {j['nationality']}</small>
            </div>
            """, unsafe_allow_html=True)

elif aba == "Calendário":
    st.title("📅 Próximos Jogos")
    dados = get_data(f"teams/{PORTO_ID}/matches?status=SCHEDULED")
    if 'matches' in dados:
        for jogo in dados['matches'][:5]:
            st.info(f"📅 {jogo['utcDate'][:10]} vs **{jogo['awayTeam']['name'] if jogo['homeTeam']['id'] == PORTO_ID else jogo['homeTeam']['name']}**")
            
