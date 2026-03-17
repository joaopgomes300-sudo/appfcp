import pandas as pd
import streamlit as st

# 1. CONFIGURAÇÃO DA PÁGINA (O básico para o site funcionar)
st.set_page_config(page_title="FC Porto v2", layout="centered")

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

elif aba == "Resultados":
    st.markdown('<p class="main-title">⚽ Últimos 10 Resultados</p>', unsafe_allow_html=True)

    ultimos_jogos = [
        {"dt": "15/03/26", "cp": "Liga Portugal Betclic 🇵🇹", "cs": "Porto", "lc": "https://tmssl.akamaized.net/images/wappen/head/720.png", "fr": "Moreirense", "lf": "https://tmssl.akamaized.net/images/wappen/head/979.png", "res": "3 - 0", "cor": "#28a745"},
        {"dt": "12/03/26", "cp": "UEFA Europa League 🇪🇺", "cs": "Stuttgart", "lc": "https://tmssl.akamaized.net/images/wappen/head/79.png", "fr": "Porto", "lf": "https://tmssl.akamaized.net/images/wappen/head/720.png", "res": "1 - 2", "cor": "#28a745"},
        {"dt": "08/03/26", "cp": "Liga Portugal Betclic 🇵🇹", "cs": "Benfica", "lc": "https://tmssl.akamaized.net/images/wappen/head/294.png", "fr": "Porto", "lf": "https://tmssl.akamaized.net/images/wappen/head/720.png", "res": "2 - 2", "cor": "#6c757d"},
        {"dt": "03/03/26", "cp": "Taça de Portugal 🏆", "cs": "Sporting", "lc": "https://tmssl.akamaized.net/images/wappen/head/336.png", "fr": "Porto", "lf": "https://tmssl.akamaized.net/images/wappen/head/720.png", "res": "1 - 0", "cor": "#dc3545"},
        {"dt": "27/02/26", "cp": "Liga Portugal Betclic 🇵🇹", "cs": "Porto", "lc": "https://tmssl.akamaized.net/images/wappen/head/720.png", "fr": "Arouca", "lf": "https://tmssl.akamaized.net/images/wappen/head/8024.png", "res": "3 - 1", "cor": "#28a745"},
        {"dt": "22/02/26", "cp": "Liga Portugal Betclic 🇵🇹", "cs": "Porto", "lc": "https://tmssl.akamaized.net/images/wappen/head/720.png", "fr": "Rio Ave", "lf": "https://tmssl.akamaized.net/images/wappen/head/2425.png", "res": "1 - 0", "cor": "#28a745"},
        {"dt": "15/02/26", "cp": "Liga Portugal Betclic 🇵🇹", "cs": "Nacional", "lc": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b2/CD_Nacional_Logo.png/200px-CD_Nacional_Logo.png", "fr": "Porto", "lf": "https://tmssl.akamaized.net/images/wappen/head/720.png", "res": "0 - 1", "cor": "#28a745"},
        {"dt": "09/02/26", "cp": "Liga Portugal Betclic 🇵🇹", "cs": "Porto", "lc": "https://tmssl.akamaized.net/images/wappen/head/720.png", "fr": "Sporting", "lf": "https://tmssl.akamaized.net/images/wappen/head/336.png", "res": "1 - 1", "cor": "#6c757d"},
        {"dt": "02/02/26", "cp": "Liga Portugal Betclic 🇵🇹", "cs": "Casa Pia", "lc": "https://cdn.footystats.org/img/teams/portugal-casa-pia-ac.png", "fr": "Porto", "lf": "https://tmssl.akamaized.net/images/wappen/head/720.png", "res": "2 - 1", "cor": "#dc3545"},
        {"dt": "29/01/26", "cp": "UEFA Europa League 🇪🇺", "cs": "Porto", "lc": "https://tmssl.akamaized.net/images/wappen/head/720.png", "fr": "Rangers", "lf": "https://tmssl.akamaized.net/images/wappen/head/124.png", "res": "3 - 1", "cor": "#28a745"}
    ]

for j in ultimos_jogos:
        # Colocamos tudo numa string sem quebras de linha para o Streamlit não pensar que é código
        card = f"<div style='background-color:white; border-radius:12px; padding:15px; margin-bottom:10px; border-left:8px solid {j['cor']}; box-shadow: 2px 2px 5px rgba(0,0,0,0.1); color:#001e3d;'><div style='display:flex; justify-content:space-between; font-size:11px; color:gray; margin-bottom:5px;'><b>{j['cp']}</b><span>{j['dt']}</span></div><div style='display:flex; justify-content:space-between; align-items:center;'><div style='width:40%; text-align:right; font-weight:bold;'>{j['cs']} <img src='{j['lc']}' width='25' style='vertical-align:middle;'></div><div style='background-color:{j['cor']}; color:white; padding:4px 10px; border-radius:5px; font-weight:bold;'>{j['res']}</div><div style='width:40%; text-align:left; font-weight:bold;'><img src='{j['lf']}' width='25' style='vertical-align:middle;'> {j['fr']}</div></div></div>"
        
        # O unsafe_allow_html=True é que faz a magia
        st.write(card, unsafe_allow_html=True)

elif aba == "Estatísticas":
    st.markdown('<p class="main-title">📊 Classificação em Tempo Real</p>', unsafe_allow_html=True)

    try:
        # 1. PEGAR OS DADOS (Scraping automático da ESPN)
        url = "https://www.espn.com.pt/futebol/classificacao/_/liga/por.1"
        tabelas = pd.read_html(url)
        
        # Juntamos nomes das equipas com os números
        df_nomes = tabelas[0]
        df_stats = tabelas[1]
        df_liga = pd.concat([df_nomes, df_stats], axis=1)

        # 2. LIMPAR A TABELA
        # Vamos manter apenas o essencial: Nome, Jogos, Vitórias, Empates, Derrotas, Pontos
        df_liga = df_liga.iloc[:, [0, 1, 2, 3, 4, 7]] 
        df_liga.columns = ['Equipa', 'J', 'V', 'E', 'D', 'PTS']

        # 3. MOSTRAR A TABELA NO ESTILO DO STREAMLIT
        # O 'style.apply' serve para destacar o Porto automaticamente
        def destacar_porto(val):
            color = '#e6f0ff' if 'Porto' in str(val) else ''
            return f'background-color: {color}'

        st.dataframe(
            df_liga.style.applymap(destacar_porto, subset=['Equipa']),
            use_container_width=True,
            hide_index=True
        )
        st.caption("✅ Dados sincronizados com a Liga Portugal via ESPN")

    except Exception as e:
        st.error("⚠️ Não foi possível carregar os dados automáticos.")
        st.info("A mostrar dados de reserva...")
        # Se o site falhar, ele mostra estes:
        st.table({"Equipa": ["Sporting CP", "FC Porto", "SL Benfica"], "PTS": [63, 61, 59]})

        st.write(card, unsafe_allow_html=True) # <-- Vê se este parêntese está lá!
