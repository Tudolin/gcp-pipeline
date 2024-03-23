import json

from ytb_analytcs import YouTubeAnalytics
from ytb_oauth import OAuth

# Carregar credenciais (melhorar segurança)
with open("secrets.json", "r") as f:
    secrets = json.load(f)

# Parâmetros da extração
start_date = "2023-01-01"
end_date = "2023-12-31"
metrics = 'estimatedMinutesWatched,views,likes,subscribersGained'

# OAuth (melhorar segurança)
oauth = OAuth(secrets["installed"]["client_id"], secrets["installed"]["client_secret"])

# Extrair, transformar e carregar dados
try:
    data = YouTubeAnalytics.extract_data(start_date, end_date, metrics)
except Exception as e:
    print(f"Erro ao extrair dados: {e}")
else:
    # Implementar lógica de transformação de dados
    # ...

    # Salvar dados (CSV ou banco de dados)
    output_path = "output.csv"
    if output_path.endswith(".csv"):
        data.to_csv(output_path, index=False)
    elif output_path.endswith(".db"):
        # Implementar salvamento no banco de dados
        pass
    else:
        raise ValueError(f"Formato de saída inválido: {output_path}")

