import json

import googleapiclient.discovery
import googleapiclient.errors


class YouTubeAnalytics:
    def __init__(self, oauth):
        self.oauth = oauth
        self.api_base_url = "https://youtubeanalytics.googleapis.com/v2/reports"

    def extract_data(self, start_date, end_date):
        api_service_name = "youtubeAnalytics"
        api_version = "v2"
        
        credentials = self.oauth.get_credentials()
        youtube_analytics = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

        metrics = "views,likes,comments"
        dimensions = "day"
        filters = f"channel==MINE;startDate={start_date};endDate={end_date}"
        
        request = youtube_analytics.reports().query(
        dimensions=dimensions,
        endDate=end_date,
        ids="channel==MINE",
        metrics=metrics,
        startDate=start_date
    )

        filename = 'data.json'
        response = request.execute()
        with open(filename, 'w') as data:
            json.dump(response, data, indent = 4)