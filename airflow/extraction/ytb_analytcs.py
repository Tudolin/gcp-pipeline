import json

import pandas as pd
import requests
from ytb_oauth import OAuth


# Classe YouTubeAnalytics
class YouTubeAnalytics:
    def __init__(self, oauth):
        self.oauth = OAuth

    # Extrair dados
    def extract_data(self, start_date, end_date):
        params = {
            "ids": "channel==MINE",
            "start-date": start_date,
            "end-date": end_date,
            "metrics": 'estimatedMinutesWatched,views,likes,subscribersGained',
        }

        with open('token.json') as f:
            token = json.load(f)
        headers = {
            "Authorization": f"Bearer {self.oauth.get_access_token}",
        }

        try:
            response = requests.get("https://youtubeanalytics.googleapis.com/v3/data", params=params, headers=headers)
        except Exception as e:
            raise e
        else:
            if response.status_code == 200:
                data = response.json()
                return pd.DataFrame(data["items"])
            else:
                raise ValueError(f"Erro na API: {response.status_code} - {response.text}")

    # Salvar dados (opcional)
    def load_data(self, dataframe, output_path):
        if output_path.endswith(".csv"):
            dataframe.to_csv(output_path, index=False)
        elif output_path.endswith(".db"):
            # Implementar a lógica de conexão e salvamento no banco de dados
            pass
        else:
            raise ValueError(f"Formato de saída inválido: {output_path}")

