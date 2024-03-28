import json

import requests
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


class OAuth:
    """Handles OAuth authentication and token management for accessing YouTube Analytics API."""
    
    def __init__(self, client_id, client_secret):
        """Initializes the OAuth object with the provided client ID and client secret."""
        self.client_id = client_id
        self.client_secret = client_secret
        self.scopes = ["https://www.googleapis.com/auth/yt-analytics.readonly"]
        self.credentials = self.get_credentials()

    def get_credentials(self):
        """Retrieves or creates OAuth credentials."""
        try:
            with open("token.json", "r") as token_file:
                token = json.load(token_file)
            credentials = Credentials(
                token["token"],
                refresh_token=token.get("refresh_token"),
                id_token=token.get("id_token"),
                token_uri=token.get("token_uri"),
                client_id=self.client_id,
                client_secret=self.client_secret,
                scopes=self.scopes
            )
        except FileNotFoundError:
            flow = InstalledAppFlow.from_client_secrets_file(
                "secrets.json", scopes=self.scopes,
                redirect_uri='http://localhost:8080'
            )
            credentials = flow.run_local_server(port=8080)
            token = {
                "token": credentials.token,
                "refresh_token": credentials.refresh_token,
                "id_token": credentials.id_token,
                "token_uri": credentials.token_uri
            }
            with open("token.json", "w") as token_file:
                json.dump(token, token_file)
        return credentials

    def get_access_token(self):
        """Obtains a new access token using the refresh token."""
        response = requests.post(
            "https://www.googleapis.com/oauth2/v4/token",
            data={
                "client_id": self.client_id,
                "client_secret": self.client_secret,
                "refresh_token": self.credentials.refresh_token,
                "grant_type": "refresh_token"
            }
        )
        if response.status_code == 200:
            token_data = json.loads(response.content)
            return token_data.get("access_token")
        else:
            raise Exception(f"Erro ao obter token de acesso: {response.status_code} - {response.content}")

    def build_service(self, service_name):
        """Builds and returns a service object for the specified Google API."""
        return build(service_name, "v3", credentials=self.credentials)
