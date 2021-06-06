import YouTubeVideos
import YouTubePlaylistMaker
import redditTracks


class YouTubeAutomate:
    def __init__(self):
        self.title = "new"

    def reddit(self):
        redditTracks.redditGetter()

    def createPlaylist(self):
        YouTubePlaylistMaker.playlistMaker()

    def addVideos(self):
        YouTubeVideos.Videos()

    def execute(self):
        self.reddit()
        self.createPlaylist()
        self.addVideos()


test1 = YouTubeAutomate()
# test1.reddit()
# test1.createPlaylist()
