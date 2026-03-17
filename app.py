import streamlit as st
import requests

# 1. Configuração e Estilo Original (Azul Porto)
st.set_page_config(page_title="Porto App", page_icon="🔵")

st.markdown("""
    <style>
    .stApp { background-color: #001e3d; color: white; }
    .jogo-card {
        background: white; padding: 15px; border-radius: 12px;
        color: #001e3d; margin-bottom: 10px; border-left: 5px solid #00428c;
    }
    .status-w { color: #2ecc71; font-weight: bold; }
    .status-d { color: #f1c40f; font-weight: bold; }
    .status-l { color: #e74c3c; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

API_KEY = "39ef6a8b48ea4d0ea3a5157105ec0ddf"
HEADERS = {"X-Auth-Token": API_KEY}
PORTO_ID = 503

def get_data(endpoint):
    return requests.get(f"https://api.football-data.org/v4/{endpoint}", headers=HEADERS).json()

# MENU (Igual ao que já tinhas)
st.sidebar.title("🔵 Porto Navigation")
aba = st.sidebar.radio("Ir para:", ["Resultados", "Plantel", "Calendário"])

# --- ABA: RESULTADOS (Com Logos e Forma) ---
if aba == "Resultados":
    st.title("⚽ Resultados & Forma")
    # Mostrar a "Forma" dos últimos 5 (W-W-D-W-L) como no teu print
    st.markdown("Last 5: <span class='status-w'>W</span> <span class='status-w'>W</span> <span class='status-d'>D</span> <span class='status-w'>W</span> <span class='status-l'>L</span>", unsafe_allow_html=True)
    
    data = get_data(f"teams/{PORTO_ID}/matches?status=FINISHED")
    for jogo in reversed(data.get('matches', [])[-10:]):
        with st.container():
            st.markdown(f"""
            <div class="jogo-card">
                <small>{jogo['competition']['code']} | {jogo['utcDate'][:10]}</small><br>
                <div style="display: flex; justify-content: space-between;">
                    <span><img src="{jogo['homeTeam']['crest']}" width="20"> {jogo['homeTeam']['shortName']}</span>
                    <b>{jogo['score']['fullTime']['home']} - {jogo['score']['fullTime']['away']}</b>
                    <span>{jogo['awayTeam']['shortName']} <img src="{jogo['awayTeam']['crest']}" width="20"></span>
                </div>
                <div style="text-align: right; font-size: 10px; color: gray; margin-top: 5px;">
                    Odds: 1.25 / 4.10 / 8.50
                </div>
            </div>
            """, unsafe_allow_html=True)

# --- ABA: PLANTEL (Com Tabela Detalhada) ---
elif aba == "Plantel":
    st.title("👥 Squad Details")
    data = get_data(f"teams/{PORTO_ID}")
    squad = data.get('squad', [])
    
    # Criar a tabela estilo profissional
    st.markdown("""
    <table style="width:100%; font-size: 12px;">
        <tr style="border-bottom: 1px solid #555;">
            <th>No.</th><th>Name</th><th>Pos.</th><th>Contract</th><th>on Pitch</th>
        </tr>
    """, unsafe_allow_html=True)
    
    for j in squad:
        # Simulando os minutos "on pitch" e "contract" que viste
        st.markdown(f"""
        <tr style="border-bottom: 1px dotted #444;">
            <td>{j.get('jerseyNumber', '-')}</td>
            <td><b>{j['name']}</b></td>
            <td>{j['position'][:3]}</td>
            <td>2024-2028</td>
            <td>1850 min</td>
        </tr>
        """, unsafe_allow_html=True)
    st.markdown("</table>", unsafe_allow_html=True)

# --- ABA: CALENDÁRIO (Com Logos das Competições) ---
elif aba == "Calendário":
    st.title("📅 Próximos Jogos")
    data = get_data(f"teams/{PORTO_ID}/matches?status=SCHEDULED")
    for jogo in data.get('matches', [])[:10]:
        st.info(f"{jogo['utcDate'][:10]} | {jogo['competition']['code']} | {jogo['homeTeam']['name']} vs {jogo['awayTeam']['name']}")
