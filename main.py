from pytube import YouTube

url = input("Enter URL from YouTube: ")

def download_video(url):
    yt = YouTube(url)
    video = yt.streams.get_highest_resolution()
    video.download(output_path ="results/")
download_video(url)
print("Download Successfully")