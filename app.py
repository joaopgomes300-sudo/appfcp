import streamlit as st
import requests
from datetime import datetime

# Configuração e Estilo
st.set_page_config(page_title="Porto App Pro", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #001e3d; color: white; }
    /* Estilo para as tabelas ficarem centradas e organizadas */
    .fcp-table {
        width: 100%;
        border-collapse: collapse;
        margin-top: 20px;
        background-color: rgba(255,255,255,0.05);
    }
    .fcp-table th, .fcp-table td {
        padding: 12px;
        text-align: center; /* Centra tudo por padrão */
        border-bottom: 1px solid #34495e;
    }
    .fcp-table th { background-color: #002d5c; color: #ffd700; }
    .text-left { text-align: left !important; }
    </style>
    """, unsafe_allow_html=True)

API_KEY = "39ef6a8b48ea4d0ea3a5157105ec0ddf"
HEADERS = {"X-Auth-Token": API_KEY}
PORTO_ID = 503

def get_data(endpoint):
    return requests.get(f"https://api.football-data.org/v4/{endpoint}", headers=HEADERS).json()

# Menu
aba = st.sidebar.radio("Ir para:", ["Resultados", "Plantel", "Calendário"])

# --- ABA: PLANTEL (Centrado e Alinhado) ---
if aba == "Plantel":
    st.title("👥 Squad Details")
    data = get_data(f"teams/{PORTO_ID}")
    squad = data.get('squad', [])
    
    html = """
    <table class="fcp-table">
        <tr>
            <th style="width: 10%;">No.</th>
            <th class="text-left" style="width: 40%;">Name</th>
            <th style="width: 15%;">Pos.</th>
            <th style="width: 20%;">Contract</th>
            <th style="width: 15%;">on Pitch</th>
        </tr>"""
    
    for j in squad:
        html += f"""
        <tr>
            <td>{j.get('jerseyNumber', '-')}</td>
            <td class="text-left"><b>{j['name']}</b></td>
            <td>{j['position'][:3] if j['position'] else 'N/A'}</td>
            <td>2024-2028</td>
            <td>1850 min</td>
        </tr>"""
    html += "</table>"
    st.markdown(html, unsafe_allow_html=True)

# --- ABA: CALENDÁRIO (Com Símbolos e Horários) ---
elif aba == "Calendário":
    st.title("📅 Próximos Jogos")
    data = get_data(f"teams/{PORTO_ID}/matches?status=SCHEDULED")
    
    html = """
    <table class="fcp-table">
        <tr>
            <th style="width: 15%;">Data/Hora</th>
            <th style="width: 10%;">Comp.</th>
            <th style="width: 75%;">Confronto</th>
        </tr>"""
    
    for m in data.get('matches', [])[:12]:
        # Formatar Data e Hora (UTC para Local simples)
        dt = datetime.strptime(m['utcDate'], "%Y-%m-%dT%H:%M:%SZ")
        data_hora = dt.strftime("%d/%m %H:%M")
        
        comp = m['competition']['code']
        home_name = m['homeTeam']['shortName']
        home_logo = m['homeTeam']['crest']
        away_name = m['awayTeam']['shortName']
        away_logo = m['awayTeam']['crest']
        
        html += f"""
        <tr>
            <td>{data_hora}</td>
            <td><span style="background:#ffd700; color:black; padding:2px 5px; border-radius:3px; font-size:10px; font-weight:bold;">{comp}</span></td>
            <td>
                <div style="display: flex; justify-content: center; align-items: center; gap: 15px;">
                    <span style="width: 120px; text-align: right;">{home_name}</span>
                    <img src="{home_logo}" width="25">
                    <span style="color: #ffd700; font-weight: bold;">vs</span>
                    <img src="{away_logo}" width="25">
                    <span style="width: 120px; text-align: left;">{away_name}</span>
                </div>
            </td>
        </tr>"""
    html += "</table>"
    st.markdown(html, unsafe_allow_html=True)

# Repete a lógica para Resultados (Opcional, mantém o que tinhas)
elif aba == "Resultados":
    st.title("⚽ Resultados Recentes")
    # ... código de resultados que já tinhas ...
