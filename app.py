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

# --- ABA: PLANTEL (Ordenado por Posição, Bandeiras e Números Manuais) ---
elif aba == "Plantel":
    st.title("👥 Squad Details")
    
    # 1. O teu dicionário de números manuais (podes continuar a encher aqui)
    numeros_manuais = {
        "Diogo Costa": 99,
        "Cláudio Ramos": 14,
        "Diogo Fernandes": 51,
        "João Costa": 24,
        "Thiago Silva": 3,
        "Jakub Kiwior":4,
        "Jan Bednarek": 5,
        "Zaidu Sanusi": 12,
        "Nehuen Perez": 18, 
        "Alberto Costa": 20,
        "Dominik Prpic": 21,
        "Martim Fernandes": 52,
        "Otávio": 31,
        "Alan Varela": 22,
        "Nico González": 16,
        "Pepê": 11,
        "Galeno": 13,
        "Samu Omorodion": 9,
        "Deniz Gül": 27,
        "Rodrigo Mora": 86 # Exemplo
    }

    # 2. Mapeamento para tradução e ORDENAÇÃO
    # Atribuímos um peso (0 a 3) para forçar a ordem na lista
    ordem_posicoes = {
        "Goalkeeper": {"label": "Guarda-redes", "peso": 0},
        "Defence": {"label": "Defesa", "peso": 1},
        "Midfield": {"label": "Médio", "peso": 2},
        "Offence": {"label": "Avançado", "peso": 3}
    }

    # 3. Dicionário de Bandeiras (conforme o nome da API)
    bandeiras = {
        "Portugal": "🇵🇹", "Brazil": "🇧🇷", "Argentina": "🇦🇷", 
        "Spain": "🇪🇸", "Sweden": "🇸🇪", "Denmark": "🇩🇰", 
        "Croatia": "🇭🇷", "Nigeria": "🇳🇬", "Canada": "🇨🇦"
    }

    data = get_data(f"teams/{PORTO_ID}")
    squad = data.get('squad', [])

    # Lógica de Ordenação: Primeiro GK, depois Defesa, etc.
    # Usamos o 'peso' que definimos acima para ordenar
    squad_ordenado = sorted(
        squad, 
        key=lambda x: ordem_posicoes.get(x['position'], {"peso": 4})["peso"]
    )

    html = """
    <table class="fcp-table">
        <tr>
            <th style="width: 10%;">No.</th>
            <th style="text-align: left; width: 40%;">Nome</th>
            <th style="width: 25%;">Posição</th>
            <th style="width: 25%;">Nacionalidade</th>
        </tr>"""
    
    for j in squad_ordenado:
        nome = j['name']
        
        # Busca número (Manual > API > Traço)
        num = j.get('jerseyNumber')
        if not num or num == '-':
            num = numeros_manuais.get(nome, "-")
            
        # Tradução da Posição
        pos_info = ordem_posicoes.get(j['position'], {"label": j['position'], "peso": 4})
        pos_pt = pos_info["label"]
        
        # Bandeira
        nacionalidade = j.get('nationality', '')
        bandeira = bandeiras.get(nacionalidade, "🏳️")
        
        html += f"""
        <tr>
            <td><b>{num}</b></td>
            <td style="text-align: left;">{nome}</td>
            <td>{pos_pt}</td>
            <td>{bandeira} <small>{nacionalidade}</small></td>
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
        
