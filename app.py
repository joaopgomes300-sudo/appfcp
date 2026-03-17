import streamlit as st
import requests
from datetime import datetime

# Configuração Base
st.set_page_config(page_title="FC Porto Hub", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #001e3d; color: white; }
    .fcp-table { width: 100%; border-collapse: collapse; margin-top: 20px; }
    .fcp-table th, .fcp-table td { 
        padding: 12px; border-bottom: 1px solid #34495e; text-align: center; 
    }
    .fcp-table th { background-color: #002d5c; color: #ffd700; }
    .jogo-card {
        background: white; padding: 15px; border-radius: 12px;
        color: #001e3d; margin-bottom: 10px; border-left: 5px solid #00428c;
    }
    </style>
    """, unsafe_allow_html=True)

API_KEY = "39ef6a8b48ea4d0ea3a5157105ec0ddf"
HEADERS = {"X-Auth-Token": API_KEY}
PORTO_ID = 503

def get_data(endpoint):
    return requests.get(f"https://api.football-data.org/v4/{endpoint}", headers=HEADERS).json()

aba = st.sidebar.radio("Ir para:", ["Resultados", "Plantel", "Calendário"])

# --- ABA: RESULTADOS (Reposta e funcional) ---
if aba == "Resultados":
    st.title("⚽ Resultados Recentes")
    data = get_data(f"teams/{PORTO_ID}/matches?status=FINISHED")
    if 'matches' in data:
        for jogo in reversed(data['matches'][-10:]):
            st.markdown(f"""
            <div class="jogo-card">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span style="width:30%; text-align:right;"><img src="{jogo['homeTeam']['crest']}" width="25"> {jogo['homeTeam']['shortName']}</span>
                    <b style="font-size:1.2em;">{jogo['score']['fullTime']['home']} - {jogo['score']['fullTime']['away']}</b>
                    <span style="width:30%; text-align:left;">{jogo['awayTeam']['shortName']} <img src="{jogo['awayTeam']['crest']}" width="25"></span>
                </div>
                <div style="text-align:center; font-size:10px; color:gray;">{jogo['utcDate'][:10]} | {jogo['competition']['code']}</div>
            </div>
            """, unsafe_allow_html=True)

# --- ABA: PLANTEL (Lista Completa e Fiel aos teus Prints) ---
elif aba == "Plantel":
    st.title("👥 Squad Details")
    
    # Esta lista contém TODOS os jogadores que tens no teu dicionário manual e nos prints
    meu_plantel = [
        # GUARDA-REDES
        {"num": 99, "nome": "Diogo Costa", "pos": "Guarda-redes", "nac": "Portugal", "band": "🇵🇹"},
        {"num": 14, "nome": "Cláudio Ramos", "pos": "Guarda-redes", "nac": "Portugal", "band": "🇵🇹"},
        {"num": 51, "nome": "Diogo Fernandes", "pos": "Guarda-redes", "nac": "Portugal", "band": "🇵🇹"},
        {"num": 24, "nome": "João Costa", "pos": "Guarda-redes", "nac": "Portugal", "band": "🇵🇹"},
        
        # DEFESAS
        {"num": 3, "nome": "Thiago Silva", "pos": "Defesa", "nac": "Brazil", "band": "🇧🇷"},
        {"num": 4, "nome": "Jakub Kiwior", "pos": "Defesa", "nac": "Poland", "band": "🇵🇱"},
        {"num": 5, "nome": "Jan Bednarek", "pos": "Defesa", "nac": "Poland", "band": "🇵🇱"},
        {"num": 12, "nome": "Zaidu Sanusi", "pos": "Defesa", "nac": "Nigeria", "band": "🇳🇬"},
        {"num": 18, "nome": "Nehuen Perez", "pos": "Defesa", "nac": "Argentina", "band": "🇦🇷"},
        {"num": 20, "nome": "Alberto Costa", "pos": "Defesa", "nac": "Portugal", "band": "🇵🇹"},
        {"num": 21, "nome": "Dominik Prpic", "pos": "Defesa", "nac": "Croatia", "band": "🇭🇷"},
        {"num": 52, "nome": "Martim Fernandes", "pos": "Defesa", "nac": "Portugal", "band": "🇵🇹"},
        {"num": 74, "nome": "Francisco Moura", "pos": "Defesa", "nac": "Portugal", "band": "🇵🇹"},
        {"num": 46, "nome": "Pedro Lima", "pos": "Defesa", "nac": "Brazil", "band": "🇧🇷"},
        {"num": "-", "nome": "Gabriel Brás", "pos": "Defesa", "nac": "Portugal", "band": "🇵🇹"},
        
        # MÉDIOS
        {"num": 8, "nome": "Victor Froholdt", "pos": "Médio", "nac": "Denmark", "band": "🇩🇰"},
        {"num": 10, "nome": "Gabri Veiga", "pos": "Médio", "nac": "Spain", "band": "🇪🇸"},
        {"num": 13, "phrase": "Pablo Rosario", "nome": "Pablo Rosario", "pos": "Médio", "nac": "Netherlands", "band": "🇳🇱"},
        {"num": 22, "nome": "Alan Varela", "pos": "Médio", "nac": "Argentina", "band": "🇦🇷"},
        {"num": 16, "nome": "Nico González", "pos": "Médio", "nac": "Spain", "band": "🇪🇸"},
        {"num": 31, "nome": "Otávio", "pos": "Médio", "nac": "Brazil", "band": "🇧🇷"},
        {"num": 42, "nome": "Seko Fofana", "pos": "Médio", "nac": "Ivory Coast", "band": "🇨🇮"},
        {"num": 86, "nome": "Rodrigo Mora", "pos": "Médio", "nac": "Portugal", "band": "🇵🇹"},
        {"num": "-", "nome": "André Oliveira", "pos": "Médio", "nac": "Portugal", "band": "🇵🇹"},
        {"num": "-", "nome": "João Teixeira", "pos": "Médio", "nac": "Portugal", "band": "🇵🇹"},
        
        # AVANÇADOS
        {"num": 11, "nome": "Pepê", "pos": "Avançado", "nac": "Brazil", "band": "🇧🇷"},
        {"num": 9, "nome": "Samu Omorodion", "pos": "Avançado", "nac": "Spain", "band": "🇪🇸"},
        {"num": 7, "nome": "William Gomes", "pos": "Avançado", "nac": "Brazil", "band": "🇧🇷"},
        {"num": 17, "nome": "Borja Sainz", "pos": "Avançado", "nac": "Spain", "band": "🇪🇸"},
        {"num": 26, "nome": "Luuk de Jong", "pos": "Avançado", "nac": "Netherlands", "band": "🇳🇱"},
        {"num": 29, "nome": "Terem Moffi", "pos": "Avançado", "nac": "Nigeria", "band": "🇳🇬"},
        {"num": 77, "nome": "Oskar Pietuszewski", "pos": "Avançado", "nac": "Poland", "band": "🇵🇱"},
        {"num": 27, "nome": "Deniz Gül", "pos": "Avançado", "nac": "Sweden", "band": "🇸🇪"},
        {"num": 72, "nome": "André Miranda", "pos": "Avançado", "nac": "Portugal", "band": "🇵🇹"},
        {"num": "-", "nome": "Tiago Andrade", "pos": "Avançado", "nac": "Portugal", "band": "🇵🇹"}
    ]

    html = """
    <table class="fcp-table">
        <tr style="background-color: #002d5c; color: #ffd700;">
            <th style="width: 10%;">No.</th>
            <th style="text-align: left; width: 40%;">Nome</th>
            <th style="width: 25%;">Posição</th>
            <th style="width: 25%;">Nacionalidade</th>
        </tr>"""
    
    for j in meu_plantel:
        html += f"""
        <tr>
            <td><b>{j['num']}</b></td>
            <td style="text-align: left;">{j['nome']}</td>
            <td>{j['pos']}</td>
            <td>{j['band']} {j['nac']}</td>
        </tr>"""
    
    html += "</table>"
    st.markdown(html, unsafe_allow_html=True)
# --- ABA: CALENDÁRIO (Com Horários e Símbolos) ---
elif aba == "Calendário":
    st.title("📅 Próximos Jogos")
    data = get_data(f"teams/{PORTO_ID}/matches?status=SCHEDULED")
    if 'matches' in data:
        html = "<table class='fcp-table'><tr><th>Data/Hora</th><th>Confronto</th></tr>"
        for m in data['matches'][:10]:
            dt = datetime.strptime(m['utcDate'], "%Y-%m-%dT%H:%M:%SZ")
            html += f"""
            <tr>
                <td>{dt.strftime("%d/%m %H:%M")}</td>
                <td>
                    <div style="display: flex; justify-content: center; align-items: center; gap: 10px;">
                        {m['homeTeam']['shortName']} <img src="{m['homeTeam']['crest']}" width="20">
                        <b>vs</b>
                        <img src="{m['awayTeam']['crest']}" width="20"> {m['awayTeam']['shortName']}
                    </div>
                </td>
            </tr>"""
        html += "</table>"
        st.markdown(html, unsafe_allow_html=True)
        
