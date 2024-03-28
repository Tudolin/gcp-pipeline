# gcp-pipeline

ytb_oauth.py
Classe OAuth
Esta classe gerencia as credenciais OAuth necessárias para autenticação e autorização com a API do YouTube Analytics.

Métodos:
__init__(self, client_id, client_secret): Inicializa a classe com as informações do cliente (client_id e client_secret).
get_credentials(self): Obtém as credenciais OAuth necessárias para autenticação.
get_access_token(self): Obtém um novo token de acesso usando o refresh token.
build_service(self, service_name): Constrói e retorna um serviço da API do YouTube Analytics usando as credenciais OAuth.
ytb_analytics.py
Classe YouTubeAnalytics
Esta classe é responsável por extrair dados da API do YouTube Analytics.

Métodos:
__init__(self, oauth): Inicializa a classe com um objeto OAuth para autenticação.
extract_data(self, start_date, end_date): Extrai os dados do YouTube Analytics para um intervalo de datas especificado.
app.py
Este arquivo é o ponto de entrada da sua aplicação e utiliza as classes OAuth e YouTubeAnalytics para extrair e gerenciar os dados do YouTube Analytics.

Funções:
data_management(filename): Lê um arquivo JSON, cria um relatório para cada linha de dados e salva os relatórios em arquivos JSON separados na pasta 'reports'.
Carrega as credenciais do arquivo "secrets.json".
Cria uma instância da classe OAuth com as credenciais carregadas.
Cria uma instância da classe YouTubeAnalytics com a instância OAuth criada.
Define as datas de início e fim para a extração de dados.
Tenta extrair os dados do YouTube Analytics e gerar os relatórios usando a função data_management.
Observações
Certifique-se de proteger o arquivo "secrets.json" que contém as credenciais do cliente.
Este código assume que o arquivo "token.json" é usado para armazenar o token de acesso e o refresh token para reutilização.
A função data_management cria relatórios individuais para cada linha de dados extraídos, salvando-os na pasta 'reports'.