import ModTkinter as tk
from pytube import YouTube

"""
# where to save
SAVE_PATH = "E:/"  # to_do

# Single video downloading
link = input ("Copiez le lien de la musique")
yt = YouTube(link)

ym = yt.streams.get_audio_only()
print("downloading...")
ym.download("C:/Users/zirco/Downloads/")
print("download completed")

# link of the video to be downloaded
# opening the file
link = open('links_file.txt', 'r')

for i in link:
    try:

        # object creation using YouTube
        # which was imported in the beginning
        yt = YouTube(i)
    except:

        # to handle exception
        print("Connection Error")

    # get the video with the extension and
    # resolution passed in the get() function
    d_video = yt.streams.get_audio_only()
    try:

        # downloading the video
        d_video.download(SAVE_PATH)
    except:
        print("Some Error!")
print('Task Completed!')
"""

window = tk.Tk()
greeting = tk.Label(text="Hello world !")
greeting.pack()

oneLinkButton = tk.Button(
    text=">",
    width=25,
    height=5,
    bg="gray",
    fg="white"
).pack()

window.mainloop()
