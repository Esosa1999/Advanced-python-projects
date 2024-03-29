from pytube import YouTube
import tkinter as tk
from tkinter import filedialog


# This is the function to download video at high resolution.
def download_video(url,save_path):
    try:
        yt=YouTube(url)
        streams=yt.streams.filter(progressive=True, file_extension='mp4')
        highest_res_stream= streams.get_highest_resolution()
        highest_res_stream.download(output_path=save_path)
        print('Video downloaded successfully!')
    except Exception  as e:
        print(e)  


# This is the function to choose the folder where the youtube video will be stored.
def open_file_dialog():
    folder= filedialog.askdirectory()
    if folder:
        print(f'Selected folder: {folder}')

    return folder



root=tk.Tk()
root.withdraw()

video_url=input('please enter a youtube url: ')
save_dir=open_file_dialog()

if save_dir:
    print('Started Download.......')
    download_video(video_url,save_dir)
else:
    print('Invalid save location')

