# GCP - Pipeline
# Conector - Youtube analytics API ![Youtube_logo](https://github.com/Tudolin/gcp-pipeline/assets/108036444/80ea2e32-0652-431a-a616-931278ec4947)

![Badge em Desenvolvimento]<img src="[https://user-images.githubusercontent.com/105131652/186226747-206a5cb6-0390-445f-9ab7-aaa88827750e.jpg](http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge)" width="200" />


# Índice 

* [Título e Imagem de capa](#Título-e-Imagem-de-capa)
* [Índice](#índice)
* [Descrição do Projeto](#descrição-do-projeto)
* [Classes](#classes)
* [Métodos](#metodos)
* [Funções](#funções)
* [Funcionalidades e Demonstração da Aplicação](#funcionalidades-e-demonstração-da-aplicação)
* [Tecnologias utilizadas](#tecnologias-utilizadas)
* [Conclusão](#conclusão)


# Classes
* Classe OAuth -
Esta classe gerencia as credenciais OAuth necessárias para autenticação e autorização com a API do YouTube Analytics.

* Classe YouTubeAnalytics - 
Esta classe é responsável por extrair dados da API do YouTube Analytics.

# Metodos:

* get_credentials(self): Obtém as credenciais OAuth necessárias para autenticação.

* get_access_token(self): Obtém um novo token de acesso usando o refresh token.

* build_service(self, service_name): Constrói e retorna um serviço da API do YouTube Analytics usando as credenciais OAuth.

* extract_data(self, start_date, end_date): Extrai os dados do YouTube Analytics para um intervalo de datas especificado.

* data_management(filename): Lê um arquivo JSON, cria um relatório para cada linha de dados e salva os relatórios em arquivos JSON separados na pasta 'reports'.

# Observações 
* Certifique-se de proteger o arquivo "secrets.json" que contém as credenciais do cliente.
* Este código assume que o arquivo "secrets.json" contendo "client_id", "project_id", etc.


## ✔️ Técnicas e tecnologias utilizadas

- ``Python``
- ``GCP``
- ``Youtube Analytics API - v2``
- ``Programação Orientada a objetos``
- ``Rest API``
- ``Cloud computing``

> :construction: Projeto em construção :construction:
