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

aba = st.sidebar.radio("Ir para:", ["Estatísticas", "Resultados", "Plantel", "Calendário"])

# --- 1. ABA: ESTATÍSTICAS (O PRIMEIRO É SEMPRE 'IF') ---
if aba == "Estatísticas":
    st.title("📊 Performance & Classificação")

    # Resumo da época (conforme o teu print original)
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Resumo da Época")
        st.markdown("""
        <div style="background: #002d5c; padding: 20px; border-radius: 10px; border-left: 5px solid #ffd700; color: white;">
            <p><b>Posição:</b> 1º Lugar (Liga Portugal)</p>
            <p><b>Progresso:</b> 26 de 34 jogos realizados</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.subheader("Marcos Recentes")
        st.success("✅ Vitória: 15 Mar 2026 (3-0 vs Moreirense)")
        st.error("❌ Derrota: 02 Fev 2026 (2-1 vs Casa Pia)")

    st.divider()

    # --- TABELA DA LIGA (ADICIONADA AQUI) ---
    st.subheader("🏆 Classificação Liga Portugal")
    data_standings = get_data("competitions/PPL/standings")
    
    if 'standings' in data_standings:
        tabela = data_standings['standings'][0]['table']
        html_tabela = """
        <table style="width:100%; border-collapse: collapse; background: white; color: #001e3d; border-radius: 10px; overflow: hidden;">
            <tr style="background: #001e3d; color: white;">
                <th style="padding: 10px;">Pos</th>
                <th style="text-align: left; padding: 10px;">Clube</th>
                <th>J</th><th>V</th><th>E</th><th>D</th><th>Pts</th>
            </tr>
        """
        for time in tabela:
            # Destaca o FC Porto (ID 503)
            bg = "#e3f2fd" if time['team']['id'] == PORTO_ID else "white"
            
            # ADICIONA CADA LINHA À VARIÁVEL
            html_tabela += f"""
            <tr style="background: {bg}; border-bottom: 1px solid #eee;">
                <td style="padding: 10px; text-align: center; font-weight: bold;">{time['position']}</td>
                <td style="padding: 10px; text-align: left;">
                    <img src="{time['team']['crest']}" width="20" style="vertical-align: middle; margin-right: 8px;">
                    {time['team']['shortName']}
                </td>
                <td style="text-align: center;">{time['playedGames']}</td>
                <td style="text-align: center;">{time['won']}</td>
                <td style="text-align: center;">{time['draw']}</td>
                <td style="text-align: center;">{time['lost']}</td>
                <td style="text-align: center; font-weight: bold;">{time['points']}</td>
            </tr>
            """

        # FORA DO FOR: Fecha a tabela e desenha
        st.markdown(html_tabela + "</table>", unsafe_allow_html=True)

        
# --- ABA: RESULTADOS (Cores por Resultado + Logos + Competições) ---
elif aba == "Resultados":
    st.title("⚽ Resultados")
    from datetime import datetime

    # 1. Puxar dados da API
    res_data = get_data(f"teams/{PORTO_ID}/matches?status=FINISHED")
    matches_api = res_data.get('matches', [])

    # 2. Teus jogos manuais (Europa e Taça)
    jogos_extra = [
        {
            "utcDate": "2026-03-04",
            "competition": {"name": "Taça de Portugal"},
            "homeTeam": {"shortName": "FC Porto", "id": PORTO_ID, "crest": "https://crests.football-data.org/503.png"},
            "awayTeam": {"shortName": "SL Benfica", "crest": "https://crests.football-data.org/1903.png"},
            "score": {"fullTime": {"home": 2, "away": 1}}
        },
        {
            "utcDate": "2026-02-18",
            "competition": {"name": "UEFA Europa League"},
            "homeTeam": {"shortName": "Stuttgart", "crest": "https://crests.football-data.org/10.png"},
            "awayTeam": {"shortName": "FC Porto", "id": PORTO_ID, "crest": "https://crests.football-data.org/503.png"},
            "score": {"fullTime": {"home": 1, "away": 2}}
        }
    ]

    # 3. Juntar as listas
    todos_jogos = matches_api + jogos_extra

    # 4. ORDENAÇÃO INFALÍVEL (Converte texto em Data Real)
    def converter_data(jogo):
        # Pega nos primeiros 10 caracteres (AAAA-MM-DD) e transforma em objeto de data
        return datetime.strptime(jogo['utcDate'][:10], '%Y-%m-%d')

    # Ordena usando a função de conversão
    todos_jogos.sort(key=converter_data, reverse=True)

    if todos_jogos:
        # Mostra os últimos 15
        for m in todos_jogos[:15]:
            # Formata a data para ficar bonita: DD/MM/AAAA
            data_obj = converter_data(m)
            data_exibicao = data_obj.strftime('%d/%m/%Y')
            
            comp_nome = m['competition']['name']
            g_h = m['score']['fullTime']['home']
            g_a = m['score']['fullTime']['away']
            
            # Lógica de cores
            if m['homeTeam'].get('id') == PORTO_ID:
                cor = "#28a745" if g_h > g_a else ("#dc3545" if g_h < g_a else "#ffffff")
            else:
                cor = "#28a745" if g_a > g_h else ("#dc3545" if g_a < g_h else "#ffffff")

            st.markdown(f"""
            <div style="border-left: 8px solid {cor}; background: white; padding: 15px; border-radius: 12px; margin-bottom: 12px; color: #001e3d; box-shadow: 2px 2px 5px rgba(0,0,0,0.1);">
                <div style="display: flex; justify-content: space-between; font-size: 0.8em; color: #666; margin-bottom: 5px; font-weight: bold;">
                    <span>🏆 {comp_nome}</span> <span>📅 {data_exibicao}</span>
                </div>
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div style="width: 38%; text-align: right; font-weight: bold;">
                        {m['homeTeam']['shortName']} <img src="{m['homeTeam']['crest']}" width="25">
                    </div>
                    <div style="background: {cor}; color: {'white' if cor != '#ffffff' else '#001e3d'}; padding: 5px 15px; border-radius: 8px; font-weight: bold; min-width: 50px; text-align: center; border: 1px solid #ddd;">
                        {g_h} - {g_a}
                    </div>
                    <div style="width: 38%; text-align: left; font-weight: bold;">
                        <img src="{m['awayTeam']['crest']}" width="25"> {m['awayTeam']['shortName']}
                    </div>
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
