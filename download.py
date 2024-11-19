import os
from pytube import YouTube

# Specify the folder to save videos
output_folder = "Lisan_ul_Quran_Course_2014"
os.makedirs(output_folder, exist_ok=True)

# Read URLs from the uploaded file
file_path = "output.txt"
with open(file_path, "r") as file:
    urls = [line.strip() for line in file if line.strip()]

# Function to download a video
def download_video(url, output_path):
    try:
        yt = YouTube(url)
        # Get the highest resolution stream
        stream = yt.streams.get_highest_resolution()
        print(f"Downloading: {yt.title}")
        stream.download(output_path)
        print(f"Downloaded: {yt.title}")
    except Exception as e:
        print(f"Failed to download {url}: {e}")

# Download each video
for url in urls:
    download_video(url.split("\\")[0], output_folder)

print("All downloads complete!")