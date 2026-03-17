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

# --- ABA: RESULTADOS (Cores por Resultado + Logos + Competições) ---
if aba == "Resultados":
    st.title("⚽ Resultados e Marcadores")
    
    # Lista Manual de Resultados (Garante que a Europa e Taça aparecem com os marcadores reais)
    # Podes atualizar esta lista sempre que acabar um jogo!
    resultados_reais = [
        {
            "data": "2026-03-19",
            "comp": "Europa League 🇪🇺",
            "casa": "FC Porto", "fora": "VfB Stuttgart",
            "g_casa": 3, "g_fora": 1,
            "marcadores": "Samu Omorodion (2), Pepê"
        },
        {
            "data": "2026-03-15",
            "comp": "Liga Portugal 🇵🇹",
            "casa": "FC Porto", "fora": "Moreirense",
            "g_casa": 3, "g_fora": 0,
            "marcadores": "Samu Omorodion, Pepê, Galeno"
        },
        {
            "data": "2026-03-08",
            "comp": "Liga Portugal 🇵🇹",
            "casa": "Benfica", "fora": "FC Porto",
            "g_casa": 2, "g_fora": 2,
            "marcadores": "Samu Omorodion, Fábio Vieira"
        }
    ]

    for r in resultados_reais:
        # Lógica de Cores do Porto
        if r['casa'] == "FC Porto":
            if r['g_casa'] > r['g_fora']: cor = "#28a745" # Vitória
            elif r['g_casa'] < r['g_fora']: cor = "#dc3545" # Derrota
            else: cor = "#ffffff" # Empate
        else:
            if r['g_fora'] > r['g_casa']: cor = "#28a745"
            elif r['g_fora'] < r['g_casa']: cor = "#dc3545"
            else: cor = "#ffffff"
        
        txt_cor = "#001e3d" if cor == "#ffffff" else "white"

        st.markdown(f"""
        <div class="jogo-card" style="border-left: 8px solid {cor}; background: white; padding: 15px; border-radius: 12px; margin-bottom: 10px; color: #001e3d;">
            <div style="display: flex; justify-content: space-between; font-size: 0.8em; color: gray;">
                <span>{r['comp']}</span> <span>{r['data']}</span>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center; margin: 10px 0;">
                <div style="width: 35%; text-align: right; font-weight: bold;">{r['casa']}</div>
                <div style="background: {cor}; color: {txt_cor}; padding: 5px 15px; border-radius: 8px; font-weight: bold; border: 1px solid #ddd; min-width: 60px; text-align: center;">
                    {r['g_casa']} - {r['g_fora']}
                </div>
                <div style="width: 35%; text-align: left; font-weight: bold;">{r['fora']}</div>
            </div>
            <div style="text-align: center; font-size: 0.85em; color: #555;">
                ⚽ <small>{r['marcadores']}</small>
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

# --- ABA: CALENDÁRIO (Ordenado e com Todas as Provas) ---
elif aba == "Calendário":
    st.title("📅 Próximos Jogos")
    
    data = get_data(f"teams/{PORTO_ID}/matches?status=SCHEDULED")
    matches = data.get('matches', [])

    # INJEÇÃO MANUAL (Para garantir que Europa e Taça aparecem se a API falhar)
    jogos_extra = [
        {
            "utcDate": "2026-03-19T20:00:00Z",
            "competition": {"name": "Europa League 🇪🇺", "code": "EL"},
            "homeTeam": {"shortName": "FC Porto", "crest": "https://crests.football-data.org/503.png"},
            "awayTeam": {"shortName": "VfB Stuttgart", "crest": "https://crests.football-data.org/10.png"}
        },
        {
            "utcDate": "2026-04-05T18:00:00Z",
            "competition": {"name": "Taça de Portugal 🏆", "code": "TP"},
            "homeTeam": {"shortName": "Benfica", "crest": "https://crests.football-data.org/1903.png"},
            "awayTeam": {"shortName": "FC Porto", "crest": "https://crests.football-data.org/503.png"}
        }
    ]
    
    # Adiciona os extras se eles ainda não estiverem na lista
    for extra in jogos_extra:
        if not any(extra['utcDate'][:10] in m['utcDate'] for m in matches):
            matches.append(extra)

    # ORDENAR POR DATA (Importante para não aparecerem baralhados)
    matches = sorted(matches, key=lambda x: x['utcDate'])

    for m in matches[:10]:
        dt = datetime.strptime(m['utcDate'], "%Y-%m-%dT%H:%M:%SZ")
        comp = m['competition']['name']
        if "League" in comp: comp = "Europa League 🇪🇺"
        elif "Portugal" in comp: comp = "Liga Portugal 🇵🇹"

        st.markdown(f"""
        <div class="jogo-card" style="border-left: 5px solid #ffd700;">
            <div style="font-size: 0.8em; color: #666; margin-bottom: 8px;">{comp}</div>
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div style="width: 40%; text-align: right;">
                    {m['homeTeam']['shortName']} <img src="{m['homeTeam']['crest']}" width="20">
                </div>
                <div style="font-weight: bold; color: #001e3d;">{dt.strftime('%H:%M')}</div>
                <div style="width: 40%; text-align: left;">
                    <img src="{m['awayTeam']['crest']}" width="20"> {m['awayTeam']['shortName']}
                </div>
            </div>
            <div style="text-align: center; font-size: 0.7em; color: #999; margin-top: 5px;">
                {dt.strftime('%d de %B, %Y')}
            </div>
        </div>
        """, unsafe_allow_html=True)
