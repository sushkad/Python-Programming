from pytube import Playlist

p= Playlist("https://www.youtube.com/watch?v=H9V2Af1wtgU&list=PLHT5rv7PEE4O8WXZkqCse0M3QvPHr_IlB")

for video in p.videos:
    video.streams.first().download()