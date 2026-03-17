import streamlit as st
import requests

# Configurações iniciais
API_KEY = "39ef6a8b48ea4d0ea3a5157105ec0ddf"
PORTO_ID = 503  # ID do FC Porto na Football-Data
URL = f"https://api.football-data.org/v4/teams/{PORTO_ID}/matches?status=FINISHED"

st.title("🔵 FC Porto - Resultados Recentes")

headers = {"X-Auth-Token": API_KEY}
response = requests.get(URL, headers=headers)

if response.status_code == 200:
    jogos = response.json()['matches']
    for jogo in jogos[-5:]:  # Mostra os últimos 5 jogos
        casa = jogo['homeTeam']['name']
        fora = jogo['awayTeam']['name']
        gols_casa = jogo['score']['fullTime']['home']
        gols_fora = jogo['score']['fullTime']['away']
        data = jogo['utcDate'][:10]
        
        st.write(f"**{data}**: {casa} {gols_casa} - {gols_fora} {fora}")
else:
    st.error("Erro ao carregar dados. Verifica a tua API Key.")
