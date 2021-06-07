
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from YouTubeAuth import authorize

# This program inserts the actual youtube videos into the desired playlist

creds = authorize()
allTracks = ['House', 'electronicmusic', 'Techno',
                     'listentothis', 'trap', 'indieheads', 'hiphopheads']

def videos():
    youtube = build('youtube', 'v3', credentials=creds)
    # read the video Ids and set up the request
    for item in allTracks:
        with open(item + ".txt", "r") as tracks:
            line = tracks.readline()
            while line:
                videoID = line.strip()
                request = youtube.playlistItems().insert(
                part="snippet",
                body={
                "snippet": {
                    "playlistId": "INSERT-PLAYLIST-ID-HERE",
                    "position": 0,
                    "resourceId": {
                    "kind": "youtube#video",
                    "videoId": str(videoID)
                    }
                }
                }
                )
                try:
                    response = request.execute()
                except HttpError as error:
                    print("No video added")
                line = tracks.readline()
        tracks.close()


