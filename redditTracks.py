import praw
from redditSecrets import client_id, client_secret, username


def redditGetter():
    reddit = praw.Reddit(client_id=client_id, client_secret=client_secret,
                         username=username, user_agent='redditGetterv1')

    subredditList = ['House', 'electronicmusic', 'Techno',
                     'listentothis', 'trap', 'indieheads', 'hiphopheads']
    for subreddit in subredditList:
        subredditName = reddit.subreddit(subreddit)
        hotPosts = subredditName.hot(limit=30)
        filename = str(subreddit) + ".txt"
        file = open(filename, 'w')
        # Get only the posts that have youtube videos on them
        for post in hotPosts:
            hasMedia = post.media != None
            if hasMedia:
                media = post.media
                if 'type' in media and media['type'] == 'youtube.com':
                    mediaEmbed = post.secure_media_embed
                    mediaContent = mediaEmbed['content']
                    contentList = mediaContent.split()
                    videoSrc = contentList[3]
                    videoCleanSrc = videoSrc.split("\"")
                    videoID = videoCleanSrc[1]
                    videoID2 = videoID.split("/")
                    try:
                        videoID3 = videoID2[4]
                        videoID4 = videoID3.split("?")
                        finalVideoID = videoID4[0]
                        file.write(finalVideoID)
                        file.write("\n")
                    except IndexError:
                        pass
    file.close()
