# app.py

import json

from ytb_analytcs import YouTubeAnalytics
from ytb_oauth import OAuth

# Carregue as credenciais (melhore a segurança)
with open("secrets.json", "r") as f:
    secrets = json.load(f)

# Crie uma instância da classe OAuth
oauth = OAuth(secrets["installed"]["client_id"], secrets["installed"]["client_secret"])

# Crie uma instância da classe YouTubeAnalytics
youtube_analytics = YouTubeAnalytics(oauth)

# Defina as datas de início e fim
start_date = "2024-01-01"
end_date = "2024-03-26"

# Extraia os dados
try:
    data = youtube_analytics.extract_data(start_date, end_date)
    print("Dados extraídos com sucesso!")
    print(data)
except Exception as e:
    print(f"Erro ao extrair dados: {e}")
