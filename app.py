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

# --- ABA: RESULTADOS (Corrigido para 'if') ---
if aba == "Resultados":
    st.title("⚽ Match Results")    
    data = get_data(f"teams/{PORTO_ID}/matches?status=FINISHED")
    matches = data.get('matches', [])
    
    if not matches:
        st.warning("Não foram encontrados resultados recentes.")
    else:
        comps = {
            "PPL": "Liga Portugal 🇵🇹",
            "EL": "Europa League 🇪🇺",
            "TP": "Taça de Portugal 🏆",
            "TL": "Taça da Liga 🏆"
        }

        for m in reversed(matches):
            comp_nome = comps.get(m['competition']['code'], m['competition']['name'])
            data_jogo = m['utcDate'][:10]
            casa = m['homeTeam']['shortName']
            fora = m['awayTeam']['shortName']
            golo_casa = m['score']['fullTime']['home']
            golo_fora = m['score']['fullTime']['away']
            
            cor_resultado = "#ffd700" if (m['homeTeam']['id'] == PORTO_ID and golo_casa > golo_fora) or \
                                         (m['awayTeam']['id'] == PORTO_ID and golo_fora > golo_casa) else "#fff"

            st.markdown(f"""
            <div style="border: 1px solid #ccc; border-radius: 10px; padding: 10px; margin-bottom: 10px;">
                <small style="color: gray;">{comp_nome} • {data_jogo}</small><br>
                <div style="display: flex; justify-content: space-between; align-items: center; font-size: 1.2em;">
                    <span style="width: 40%; text-align: right;">{casa}</span>
                    <span style="background: #002d5c; color: {cor_resultado}; padding: 5px 15px; border-radius: 5px; font-weight: bold;">
                        {golo_casa} - {golo_fora}
                    </span>
                    <span style="width: 40%; text-align: left;">{fora}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

# --- ABA: PLANTEL (Dividido por Posições) ---
elif aba == "Plantel":
    st.title("👥 Squad Details")
    
    # Lista organizada por blocos para facilitar a gestão
    meu_plantel = {
        "GUARDA-REDES": [
            {"num": 99, "nome": "Diogo Costa", "nac": "Portugal", "band": "🇵🇹"},
            {"num": 14, "nome": "Cláudio Ramos", "nac": "Portugal", "band": "🇵🇹"},
            {"num": 51, "nome": "Diogo Fernandes", "nac": "Portugal", "band": "🇵🇹"},
            {"num": 24, "nome": "João Costa", "nac": "Portugal", "band": "🇵🇹"},
        ],
        "DEFESAS": [
            {"num": 3, "nome": "Thiago Silva", "nac": "Brazil", "band": "🇧🇷"},
            {"num": 4, "nome": "Jakub Kiwior", "nac": "Poland", "band": "🇵🇱"},
            {"num": 5, "nome": "Jan Bednarek", "nac": "Poland", "band": "🇵🇱"},
            {"num": 12, "nome": "Zaidu Sanusi", "nac": "Nigeria", "band": "🇳🇬"},
            {"num": 18, "nome": "Nehuen Perez", "nac": "Argentina", "band": "🇦🇷"},
            {"num": 20, "nome": "Alberto Costa", "nac": "Portugal", "band": "🇵🇹"},
            {"num": 21, "nome": "Dominik Prpic", "nac": "Croatia", "band": "🇭🇷"},
            {"num": 52, "nome": "Martim Fernandes", "nac": "Portugal", "band": "🇵🇹"},
            {"num": 74, "nome": "Francisco Moura", "nac": "Portugal", "band": "🇵🇹"},
            {"num": 46, "nome": "Pedro Lima", "nac": "Brazil", "band": "🇧🇷"},
            {"num": "-", "nome": "Gabriel Brás", "nac": "Portugal", "band": "🇵🇹"},
        ],
        "MÉDIOS": [
            {"num": 8, "nome": "Victor Froholdt", "nac": "Denmark", "band": "🇩🇰"},
            {"num": 10, "nome": "Gabri Veiga", "nac": "Spain", "band": "🇪🇸"},
            {"num": 13, "nome": "Pablo Rosario", "nac": "Netherlands", "band": "🇳🇱"},
            {"num": 22, "nome": "Alan Varela", "nac": "Argentina", "band": "🇦🇷"},
            {"num": 16, "nome": "Nico González", "nac": "Spain", "band": "🇪🇸"},
            {"num": 31, "nome": "Otávio", "nac": "Brazil", "band": "🇧🇷"},
            {"num": 42, "nome": "Seko Fofana", "nac": "Ivory Coast", "band": "🇨🇮"},
            {"num": 86, "nome": "Rodrigo Mora", "nac": "Portugal", "band": "🇵🇹"},
            {"num": "-", "nome": "André Oliveira", "nac": "Portugal", "band": "🇵🇹"},
        ],
        "AVANÇADOS": [
            {"num": 11, "nome": "Pepê", "nac": "Brazil", "band": "🇧🇷"},
            {"num": 9, "nome": "Samu Omorodion", "nac": "Spain", "band": "🇪🇸"},
            {"num": 7, "nome": "William Gomes", "nac": "Brazil", "band": "🇧🇷"},
            {"num": 17, "nome": "Borja Sainz", "nac": "Spain", "band": "🇪🇸"},
            {"num": 26, "nome": "Luuk de Jong", "nac": "Netherlands", "band": "🇳🇱"},
            {"num": 29, "nome": "Terem Moffi", "nac": "Nigeria", "band": "🇳🇬"},
            {"num": 27, "nome": "Deniz Gül", "nac": "Sweden", "band": "🇸🇪"},
            {"num": 72, "nome": "André Miranda", "nac": "Portugal", "band": "🇵🇹"},
        ]
    }

    html = """<table class="fcp-table">"""
    
    for posicao, jogadores in meu_plantel.items():
        # Linha de separação por posição
        html += f"""
        <tr style="background-color: #00428c; color: white; font-weight: bold;">
            <td colspan="4" style="text-align: left; padding-left: 15px;">{posicao}</td>
        </tr>
        <tr style="background-color: #002d5c; color: #ffd700; font-size: 0.8em;">
            <th>No.</th><th style="text-align: left;">Nome</th><th>Nacionalidade</th><th>Info</th>
        </tr>"""
        
        for j in jogadores:
            html += f"""
            <tr>
                <td><b>{j['num']}</b></td>
                <td style="text-align: left;">{j['nome']}</td>
                <td>{j['band']} {j['nac']}</td>
                <td style="font-size: 0.8em; color: gray;">✔</td>
            </tr>"""
    
    html += "</table>"
    st.markdown(html, unsafe_allow_html=True)

# --- ABA: CALENDÁRIO ---
elif aba == "Calendário":
    st.title("📅 Upcoming Matches")
    data = get_data(f"teams/{PORTO_ID}/matches?status=SCHEDULED")
    matches = data.get('matches', [])

    if not any(m['competition']['name'] == "UEFA Europa League" for m in matches):
        matches.append({
            "utcDate": "2026-03-19T20:00:00Z",
            "competition": {"name": "UEFA Europa League", "code": "EL"},
            "homeTeam": {"shortName": "FC Porto"},
            "awayTeam": {"shortName": "VfB Stuttgart"},
            "status": "SCHEDULED"
        })

    for m in matches:
        comp = m['competition']['name']
        if "League" in comp: comp = "Europa League 🇪🇺"
        elif "Portugal" in comp: comp = "Liga Portugal 🇵🇹"
        
        data_f = m['utcDate'][:10]
        hora_f = m['utcDate'][11:16]
        
        st.markdown(f"""
        <div style="background-color: #f9f9f9; padding: 15px; border-radius: 10px; border-left: 5px solid #002d5c; margin-bottom: 10px;">
            <b style="color: #002d5c;">{comp}</b><br>
            <span style="font-size: 1.1em; color: black;">{m['homeTeam']['shortName']} vs {m['awayTeam']['shortName']}</span><br>
            <small style="color: black;">📅 {data_f} às {hora_f} (UTC)</small>
        </div>
        """, unsafe_allow_html=True)
