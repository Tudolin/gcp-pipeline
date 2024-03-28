import json
import os

from ytb_analytics import YouTubeAnalytics
from ytb_oauth import OAuth


def data_management(filename):
        """Manages the data extracted from YouTube Analytics API."""
        if not os.path.exists('reports'):
            os.makedirs('reports')

        with open(filename, 'r') as file:
            data = json.load(file)
            for row in data['rows']:
                date = row[0]
                report_data = {
                    'date': date,
                    'views': row[1],
                    'likes': row[2],
                    'dislikes': row[3],
                    'comments': row[4],
                    'estimatedMinutesWatched': row[5],
                    'subscribersGained': row[6],
                    'subscribersLost': row[7],
                    'annotationClickThroughRate': row[8],
                    'annotationCloseRate': row[9]
                }
                report_filename = f'reports/{date}.json'
                with open(report_filename, 'w') as report_file:
                    json.dump(report_data, report_file, indent=4)

""" Load credentials (improve security)"""
with open("secrets.json", "r") as f:
    secrets = json.load(f)

"""Create an instance of the OAuth class"""
oauth = OAuth(secrets["installed"]["client_id"], secrets["installed"]["client_secret"])

"""Create an instance of the YouTubeAnalytics class"""
youtube_analytics = YouTubeAnalytics(oauth)

"""Set start and end dates"""
start_date = "2023-01-01"
end_date = "2024-03-26"

"""Extract data"""
try:
    data = youtube_analytics.extract_data(start_date, end_date)
    data_management('data.json')
    print("Data successfully extracted!")
except Exception as e:
    print(f"A error as occurred while the execution: {e}")
