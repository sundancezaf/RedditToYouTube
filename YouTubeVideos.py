
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from YouTubeAuth import authorize

# -------------------- Insert videos -----------

creds = authorize()

def videos():
    youtube = build('youtube', 'v3', credentials=creds)
    with open("House.txt", "r") as tracks:
        for line in tracks:
            videoID = line
            request = youtube.playlistItems().insert(
                part="snippet",
                body={
                    "snippet": {
                        "playlistId": "YOUR-ID-HERE",
                        "position": 0,
                        "resourceId": {
                            "kind": "youtube#video",
                            "videoId": videoID
                        }
                    }
                }
            )
        response = request.execute()
