from pytube import Playlist
pl = Playlist("Your-youtube-video-link")
print("Download Started..")
pl.download_all("D:/your-destination/")
print("Download finished")