from tkinter import ttk
import ModTkinter as tk
from pytube import YouTube

# where to save
SAVE_PATH = "E:/"  # to_do


class tkinterApp(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting of the different page layouts
        for F in (StartPage, Page1, Page2):
            frame = F(container, self)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    # to display the current frame passed as parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


# first window frame startpage

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # label of frame Layout 2
        label = ttk.Label(self, text="Bienvenue dans le convertisseur de vidéos YouTube en fichier MP3 !")

        # putting the grid in its place by using grid
        label.grid(row=0, column=4, padx=10, pady=10)

        button1 = ttk.Button(self, text="Une seule musique",
                             command=lambda: controller.show_frame(Page1))

        # putting the button in its place by using grid
        button1.grid(row=1, column=4, padx=10, pady=10)

        ## button to show frame 2 with text layout2
        button2 = ttk.Button(self, text="Plusieurs musiques",
                             command=lambda: controller.show_frame(Page2))

        # putting the button in its place by using grid
        button2.grid(row=2, column=4, padx=10, pady=10)


# second window frame page1
class Page1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Un seul lien")
        label.grid(row=0, column=4, padx=10, pady=10)

        ask = ttk.Label(self, text="Veuillez entrer le lien de la vidéo YouTube")
        ask.grid(row=1, column=4, padx=10, pady=10)

        # get youtube link
        entry = ttk.Entry()
        entry.pack()
        link = entry.get()

        downloadButton = ttk.Button(self, text="Télécharger")
        # command=self.downloadSingleLink(link))
        downloadButton.grid(row=3, column=4, padx=10, pady=10)

        returnButton = ttk.Button(self, text="Retour",
                                  command=lambda: controller.show_frame(StartPage))
        returnButton.grid(row=4, column=4, padx=10, pady=10)

    def downloadSingleLink(self, l):
        yt = YouTube(l)

        ym = yt.streams.get_audio_only()
        print("downloading...")
        ym.download("C:/Users/zirco/Downloads/")
        print("download completed")


# third window frame page2
class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Plusieurs liens")
        label.grid(row=0, column=4, padx=10, pady=10)

        ask = ttk.Label(self, text="Veuillez entrer le nom du fichier contenant les liens des vidéos à transformer",
                        justify="center")
        ask.grid(row=1, column=4, padx=10, pady=10)

        # get youtube link
        entry2 = ttk.Entry()
        entry2.pack()
        file = entry2.get()

        downloadButton = ttk.Button(self, text="Télécharger")
        # command=self.downloadMultipleLinks(file))
        downloadButton.grid(row=3, column=4, padx=10, pady=10)

        returnButton = ttk.Button(self, text="Retour",
                                  command=lambda: controller.show_frame(StartPage))

        returnButton.grid(row=4, column=4, padx=10, pady=10)

    def downloadMultipleLinks(self, file):
        global yt
        link = open(file, 'r')

        for i in link:
            try:
                yt = YouTube(i)
            except:
                # to handle exception
                print("Connection Error")

            # get the video with the extension and resolution passed in the get() function
            d_video = yt.streams.get_audio_only()
            try:
                # downloading the video
                d_video.download(SAVE_PATH)
            except:
                print("Some Error!")
        print('Task Completed!')


# Driver Code
app = tkinterApp()
app.title("YouTubeToMP3")
app.mainloop()
