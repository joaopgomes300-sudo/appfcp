import streamlit as st
import requests
import pandas as pd

# Configuração de ecrã largo para caber a tabela
st.set_page_config(page_title="FCP Professional Dashboard", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #1a2634; color: white; }
    .status-w { background-color: #2ecc71; color: white; padding: 2px 6px; border-radius: 4px; font-weight: bold; }
    .status-d { background-color: #f1c40f; color: black; padding: 2px 6px; border-radius: 4px; font-weight: bold; }
    .status-l { background-color: #e74c3c; color: white; padding: 2px 6px; border-radius: 4px; font-weight: bold; }
    table { width: 100%; border-collapse: collapse; color: white; }
    th { background-color: #2c3e50; padding: 10px; text-align: left; }
    td { padding: 10px; border-bottom: 1px solid #34495e; }
    </style>
    """, unsafe_allow_html=True)

API_KEY = "39ef6a8b48ea4d0ea3a5157105ec0ddf"
HEADERS = {"X-Auth-Token": API_KEY}
PORTO_ID = 503

def get_data(endpoint):
    return requests.get(f"https://api.football-data.org/v4/{endpoint}", headers=HEADERS).json()

# --- SIDEBAR ---
st.sidebar.image("https://upload.wikimedia.org/wikipedia/pt/1/1c/FC_Porto.png", width=80)
menu = st.sidebar.radio("Vista:", ["Visão Geral", "Calendário & Odds", "Plantel Pro"])

# --- VISTA: VISÃO GERAL (Simulando o teu print) ---
if menu == "Visão Geral":
    st.title("🔵 FC Porto - Overview")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### Performance")
        st.write("**League table position:** 1. place")
        st.write("**Est. squad market value:** n/a (Free API limit)")
        
        # Simulando a "Forma" (Last 10)
        forma_html = """
        <span class="status-w">W</span> <span class="status-w">W</span> 
        <span class="status-d">D</span> <span class="status-w">W</span> 
        <span class="status-w">W</span> <span class="status-w">W</span> 
        <span class="status-d">D</span> <span class="status-l">L</span> 
        <span class="status-w">W</span> <span class="status-w">W</span>
        """
        st.markdown(f"**Last 10:** {forma_html}", unsafe_allow_html=True)
        st.progress(0.76, text="Seasonal progress: 26 of 34 matches")

# --- VISTA: CALENDÁRIO & ODDS ---
elif menu == "Calendário & Odds":
    st.title("📅 Fixtures & Results")
    data = get_data(f"teams/{PORTO_ID}/matches")
    
    matches = data.get('matches', [])
    
    table_html = "<table><tr><th>Date</th><th>Competition</th><th>Label</th><th>Score</th><th>Odds</th></tr>"
    
    for m in matches[-15:]: # Mostrar últimos 15
        date = m['utcDate'][:10]
        comp = m['competition']['code']
        home = m['homeTeam']['shortName']
        away = m['awayTeam']['shortName']
        score = f"{m['score']['fullTime']['home']}-{m['score']['fullTime']['away']}" if m['status'] == "FINISHED" else "-:-"
        
        # Odds (A API gratuita não dá odds reais, vamos simular o campo como no teu print)
        odds = "1.20 / 4.50 / 9.00"
        
        table_html += f"<tr><td>{date}</td><td>{comp}</td><td>{home} vs {away}</td><td><b>{score}</b></td><td>{odds}</td></tr>"
    
    table_html += "</table>"
    st.markdown(table_html, unsafe_allow_html=True)

# --- VISTA: PLANTEL PRO ---
elif menu == "Plantel Pro":
    st.title("👥 Squad Details")
    data = get_data(f"teams/{PORTO_ID}")
    squad = data.get('squad', [])
    
    df = pd.DataFrame(squad)
    if not df.empty:
        # Selecionar e renomear colunas para o estilo do print
        df_display = df[['jerseyNumber', 'name', 'position', 'nationality']]
        df_display.columns = ['No.', 'Name', 'Position', 'Nationality']
        st.table(df_display)
