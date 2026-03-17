import streamlit as st

# 1. CONFIGURAÇÃO DA PÁGINA (O básico para o site funcionar)
st.set_page_config(page_title="FC Porto Hub v2", layout="centered")

# Cores oficiais para usarmos no código
AZUL_PORTO = "#001e3d"
BRANCO = "#ffffff"
CINZA_FUNDO = "#f0f2f6"

# CSS para deixar o visual mais "Premium"
st.markdown(f"""
    <style>
    .stApp {{ background-color: {CINZA_FUNDO}; }}
    .main-title {{ color: {AZUL_PORTO}; font-size: 40px; font-weight: bold; text-align: center; margin-bottom: 20px; }}
    </style>
""", unsafe_allow_html=True)

# 2. MENU LATERAL (SIDEBAR)
st.sidebar.image("https://crests.football-data.org/503.png", width=120)
st.sidebar.title("FC Porto Hub")
aba = st.sidebar.radio("Escolhe a secção:", ["Estatísticas", "Resultados", "Plantel", "Calendário"])

# ---------------------------------------------------------
# ABA 1: ESTATÍSTICAS (CLASSIFICAÇÃO MANUAL)
# ---------------------------------------------------------
if aba == "Estatísticas":
    st.markdown('<p class="main-title">📊 Classificação Liga Portugal</p>', unsafe_allow_html=True)

    # Tabela em HTML para total controlo visual
    html_tabela = f"""
    <table style="width:100%; border-collapse: collapse; background: white; border-radius: 15px; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
        <tr style="background-color: {AZUL_PORTO}; color: white; text-align: center;">
            <th style="padding: 15px;">Pos</th>
            <th style="padding: 15px; text-align: left;">Clube</th>
            <th style="padding: 15px;">J</th>
            <th style="padding: 15px;">V</th>
            <th style="padding: 15px;">E</th>
            <th style="padding: 15px;">D</th>
            <th style="padding: 15px;">Pts</th>
        </tr>
    """

    # LISTA MANUAL - Podes atualizar estes números aqui sempre que quiseres
    # [Pos, Nome, Logo, Jogos, V, E, D, Pontos]
    classificacao = [
        [1, "Sporting CP", "https://crests.football-data.org/498.png", 25, 21, 2, 2, 65],
        [2, "FC Porto", "https://crests.football-data.org/503.png", 25, 20, 3, 2, 63],
        [3, "SL Benfica", "https://crests.football-data.org/1903.png", 25, 18, 4, 3, 58],
        [4, "SC Braga", "https://crests.football-data.org/5613.png", 25, 15, 5, 5, 50],
        [5, "Vitória SC", "https://crests.football-data.org/5543.png", 25, 13, 6, 6, 45]
    ]

    for c in classificacao:
        # Destaca o Porto com um fundo azul clarinho
        bg = "#e8f0fe" if c[1] == "FC Porto" else "white"
        bold = "bold" if c[1] == "FC Porto" else "normal"
        
        html_tabela += f"""
        <tr style="background-color: {bg}; border-bottom: 1px solid #eee; text-align: center; font-weight: {bold};">
            <td style="padding: 12px;">{c[0]}º</td>
            <td style="padding: 12px; text-align: left;">
                <img src="{c[2]}" width="25" style="vertical-align: middle; margin-right: 10px;"> {c[1]}
            </td>
            <td style="padding: 12px;">{c[3]}</td>
            <td style="padding: 12px;">{c[4]}</td>
            <td style="padding: 12px;">{c[5]}</td>
            <td style="padding: 12px;">{c[6]}</td>
            <td style="padding: 12px; color: {AZUL_PORTO}; font-size: 1.1em;"><b>{c[7]}</b></td>
        </tr>
        """

    html_tabela += "</table>"
    st.markdown(html_tabela, unsafe_allow_html=True)
    st.caption("Última atualização: 17 de Março de 2026")

elif aba == "Plantel":
    st.markdown('<p class="main-title">👥 Squad Details</p>', unsafe_allow_html=True)
    
    # CSS para tornar a tabela profissional e legível
    st.markdown("""
        <style>
            .squad-container {
                background-color: white;
                border-radius: 15px;
                overflow: hidden;
                box-shadow: 0 4px 15px rgba(0,0,0,0.1);
                margin-bottom: 20px;
            }
            .fcp-table {
                width: 100%;
                border-collapse: collapse;
                font-family: 'sans-serif';
            }
            /* Cor do texto de todas as células para garantir visibilidade */
            .fcp-table td {
                padding: 12px 15px;
                border-bottom: 1px solid #eee;
                color: #001e3d !important; /* Azul escuro */
                text-align: center;
                font-size: 0.95em;
            }
            /* Cabeçalhos de posição (Guarda-redes, etc) */
            .pos-header {
                background-color: #001e3d !important;
                color: white !important;
                font-weight: bold;
                text-transform: uppercase;
                letter-spacing: 1px;
            }
            /* Sub-cabeçalho (No, Nome, etc) */
            .sub-header th {
                background-color: #002d5c;
                color: #ffd700 !important; /* Dourado */
                padding: 8px;
                font-size: 0.8em;
                text-transform: uppercase;
            }
            /* Efeito ao passar o rato */
            .fcp-table tr:hover {
                background-color: #f8f9fa;
            }
        </style>
    """, unsafe_allow_html=True)

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

    # Início da Tabela com Wrapper para bordas arredondadas
    html = """<div class="squad-container"><table class="fcp-table">"""
    
    for posicao, jogadores in meu_plantel.items():
        # Cabeçalho da Categoria
        html += f"""
        <tr class="pos-header">
            <td colspan="4" style="text-align: left; padding-left: 15px;">{posicao}</td>
        </tr>
        <tr class="sub-header">
            <th>No.</th><th style="text-align: left;">Nome</th><th>Nacionalidade</th><th>Status</th>
        </tr>"""
        
        for j in jogadores:
            html += f"""
            <tr>
                <td style="font-weight: bold; color: #00428c;">{j['num']}</td>
                <td style="text-align: left; font-weight: 500;">{j['nome']}</td>
                <td>{j['band']} <span style="font-size: 0.9em; color: #555;">{j['nac']}</span></td>
                <td style="color: #28a745 !important; font-weight: bold;">✔</td>
            </tr>"""
    
    html += "</table></div>"
    st.markdown(html, unsafe_allow_html=True)
