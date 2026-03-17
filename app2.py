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
