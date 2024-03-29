# GCP - Data Pipeline
### Conector - Youtube analytics API 


![Youtube Logo](https://github.com/Tudolin/gcp-pipeline/blob/main/img/ytb-logo.png)


![Badge em Desenvolvimento](http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge)


* [Introdução](#introdução)
* [Instalação de Dependencias](#instalação-de-dependencias)
* [Guia de Uso](#guia-de-uso)
* [Classes](#classes)
* [Métodos](#metodos)
* [Funcionalidades e Demonstração da Aplicação](#funcionalidades-e-demonstração-da-aplicação)
* [Conclusão](#conclusão)



# Introdução

Esse projeto tem o objetivo de realizar a extração, transformação e o carregamento de dados, estes extraidos do seu própio canal. Pra isto, utilizei a [Youtube Analytics API](https://developers.google.com/youtube/reporting?hl=pt-br) e [Google Cloud Console](https://console.cloud.google.com/).




# Instalação de Dependencias

> pip install --upgrade google-auth-oauthlib

> pip install google-api-python-client 


# Guia de Uso


Após ter realizado a clonagem do repositório em sua máquina local, você precisará criar um projeto utilizando [Google Cloud Console](https://console.cloud.google.com/).
![image](https://github.com/Tudolin/gcp-pipeline/assets/108036444/f696e0b5-f0ba-4f43-a718-1ed5da26db04)

Projeto criado, você seguira o seguinte caminho

![2](https://github.com/Tudolin/gcp-pipeline/assets/108036444/29786bca-3f89-440d-8b64-3072d3bdafab)![1](https://github.com/Tudolin/gcp-pipeline/assets/108036444/ee5c57e6-7feb-43a0-9f56-1b7a7c94129b)

Pesquise por "YouTube Analytics API" e clique em "Ativar" e em seguida "Gerenciar".

Na tela de gerenciamento, será necessário gerar nossa credencial de acesso Oauth2. Clique em "Credenciais" em seguida "Criar Credenciais" e "ID do Cliente OAuth".

![image](https://github.com/Tudolin/gcp-pipeline/assets/108036444/f7056183-cfcc-4c24-9019-f06c34b689dc)


Em tipo de aplicativo, selecione "App para computador", escolha o nome que desejar e Criar.

![image](https://github.com/Tudolin/gcp-pipeline/assets/108036444/89fc6598-085e-4ab2-9e52-9e3d0c87fae9)


Assim que criada, vai aparecer a tela mostrando o id e segredo do cliente, clique em Fazer download do Json e salve na pasta do projeto como "secrets.json"


![image](https://github.com/Tudolin/gcp-pipeline/assets/108036444/8949372c-e565-4602-b256-70ea4f642e9d)![image](https://github.com/Tudolin/gcp-pipeline/assets/108036444/6e53c5a1-9e58-4fe7-bf26-23972390745a)


Feito isso, seu código está pronto para rodar!




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
* Este código assume que o arquivo "secrets.json" está presente na pasta de execução.


# ✔️ Técnicas e tecnologias utilizadas

- ``Python``
- ``GCP``
- ``Youtube Analytics API - v2``
- ``Programação Orientada a objetos``
- ``Rest API``


# Conclusão


Este projeto se encontra em desenvolvimento ativo, com foco em aprimorar as funcionalidades e a usabilidade. As principais áreas de trabalho em andamento incluem:

Expansão das funcionalidades:


* Integração com outras APIs do Google Cloud e conectores para realizar análises mais complexas.
* Melhoria da experiência do desenvolvedor e usuário:


## Automação:

* Criação de scripts para automatizar a execução do pipeline de dados.
* Integração com ferramentas de CI/CD para garantir a entrega contínua de atualizações.


## Observações:

Este projeto é um trabalho em andamento e pode conter bugs ou funcionalidades incompletas.
É recomendável que você faça backup do seu arquivo "secrets.json" antes de realizar qualquer modificação no código.
Agradecemos a sua colaboração e feedback para que possamos continuar aprimorando este projeto.
Próximos passos:

Acompanhe o repositório no GitHub para receber notificações sobre novas atualizações.
Sinta-se à vontade para contribuir com o projeto reportando bugs, sugerindo novas funcionalidades ou enviando pull requests.
Compartilhe este projeto com outras pessoas que possam se interessar por ele.


## Agradecimentos:
Agradeço a todos que contribuíram para o desenvolvimento deste projeto, seja através de código, feedback ou sugestões.



## Recursos adicionais:


[Documentação da API do YouTube Analytics](https://developers.google.com/youtube/reporting?hl=pt-br)
[Tutoriais do Google Cloud Platform](https://cloud.google.com/docs/tutorials/)



> :construction: Projeto em construção :construction:
