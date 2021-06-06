
from googleapiclient.discovery import build
from datetime import date
from YouTubeAuth import authorize

creds = authorize()


def playlistMaker():
    youtube = build('youtube', 'v3', credentials=creds)
    week = date.today()
    weekFormatted = week.strftime("%m/%d/%Y")
    title = "Week of " + weekFormatted
    request = youtube.playlists().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": title,
                "description": "Musiccc",
                "tags": [""
                         ],
                "defaultLanguage": "en"
            },
            "status": {
                "privacyStatus": "private"
            }
        }
    )

    response = request.execute()
    playlistFile = open("playlistID.txt", "w")
    playlistFile.write(response['id'])
    playlistFile.close()
