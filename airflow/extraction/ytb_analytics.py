import json

import googleapiclient.discovery
import googleapiclient.errors


class YouTubeAnalytics:
    """Handles extraction of data from YouTube Analytics API."""
    
    def __init__(self, oauth):
        """Initializes the YouTubeAnalytics object with the provided OAuth object."""
        self.oauth = oauth
        self.api_base_url = "https://youtubeanalytics.googleapis.com/v2/reports"

    def extract_data(self, start_date, end_date):
        """Extracts data from YouTube Analytics API for the specified date range."""
        api_service_name = "youtubeAnalytics"
        api_version = "v2"
        
        credentials = self.oauth.get_credentials()
        youtube_analytics = googleapiclient.discovery.build(
            api_service_name, api_version, credentials=credentials)

        metrics = "views,likes,dislikes,comments,estimatedMinutesWatched,subscribersGained,subscribersLost,annotationClickThroughRate,annotationCloseRate,annotationCloseRate"
        dimensions = "day"
        
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
