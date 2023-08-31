# import requests
# from bs4 import BeautifulSoup


# response = requests.get('https://www.kayak.nl/flights/EIN-SOF/2023-08-31?sort=bestflight_a')
# print(response.text)

# soup = BeautifulSoup(response.content, 'html.parser')
# print(soup.title)

# with open("file_path.txt", 'w') as file:
#     file.write(soup.prettify())


# import youtube_dl

# def download_mp3_by_name(song_name):
#     options = {
#         'format': 'bestaudio/best',  # Choose the best audio quality
#         'extractaudio': True,        # Extract audio only
#         'audioformat': 'mp3',        # Set audio format to mp3
#         'outtmpl': f'%(title)s.%(ext)s',  # Save the file with the title as filename
#     }

#     with youtube_dl.YoutubeDL(options) as ydl:
#         search_query = f"ytsearch1:{song_name}"  # Search YouTube for the given song name
#         info_dict = ydl.extract_info(search_query, download=False)

#         if 'entries' in info_dict:
#             video_url = info_dict['entries'][0]['url']
#             ydl.download([video_url])

# song_name = "Doja Cat - Streets"
# download_mp3_by_name(song_name)



# import os
# import yt_dlp

# def search_and_download_song(song_name, output_filename):
#     ydl_opts = {
#         'format': 'bestaudio/best',
#         'extractaudio': True,
#         'audioformat': 'mp3',
#         'outtmpl': output_filename,
#     }

#     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#         search_query = f"ytsearch1:{song_name} audio"
#         info_dict = ydl.extract_info(search_query, download=False)
        
#         if 'entries' in info_dict:
#             video_url = info_dict['entries'][0]['url']
#             ydl.download([video_url])
#             print("Audio downloaded successfully.")
#         else:
#             print("Song not found on YouTube.")

# if __name__ == "__main__":
#     song_name = input("Enter the name of the song: ")
#     output_filename = f"{song_name}.mp3"
    
#     search_and_download_song(song_name, output_filename)


# import os
# import yt_dlp

# def download_progress_hook(d):
#     if d['status'] == 'downloading':
#         percent = d['_percent_str']
#         print(f"Download progress AAAAAAAAAAAAAAAAAAAA: {percent}", end='\r')
#     if d['status'] == 'finished':
#         print("Download completed!")

# def search_and_download_song(song_name, output_filename):
#     ydl_opts = {
#         'format': 'bestaudio/best',
#         'extractaudio': True,
#         'preferredcodec': 'wav',
#         'outtmpl': output_filename,
#         'progress_hooks': [download_progress_hook],
#     }
    
#     ydl_opts = {
#         'format': 'bestaudio/best',
#         'extractaudio': True,
#         'postprocessors': [{
#             'key': 'FFmpegExtractAudio',
#             'preferredcodec': 'mp3',
#             'preferredquality': '192',
#         }],
#         'outtmpl': output_filename,
#         'progress_hooks': [download_progress_hook]
#     }

#     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#         search_query = f"ytsearch1:{song_name} audio"
#         info_dict = ydl.extract_info(search_query, download=False)
        
#         if 'entries' in info_dict:
#             video_url = info_dict['entries'][0]['url']
#             ydl.download([video_url])
#         else:
#             print("Song not found on YouTube.")

# def ConvertTo8D(input_file_name, output_file_name, *, period = 200):
#     import numpy as np
#     from pydub import AudioSegment
    
#     if period < 0:
#         period = -period
#     elif period == 0:
#         period = 200
        
#     audio = AudioSegment.from_file(input_file_name)
#     audio = audio + AudioSegment.silent(duration = 150)
    
#     eightD = AudioSegment.empty()
#     pan = 0.9 * np.sin(np.linspace(0, 2. * np.pi, period))

#     for i, chunk in enumerate(audio[::100]):
#         if len(chunk) < 100:
#             continue
#         newChunk = chunk.pan(pan[i % period])
#         eightD = eightD + newChunk

#     eightD.export(output_file_name, format = output_file_name[output_file_name.rfind('.') + 1:])



# if __name__ == "__main__":
#     song_name = input("Enter the name of the song: ")
#     output_filename = f"{song_name}"
    
#     # Test Usage
    
#     search_and_download_song(song_name, output_filename)
#     # ConvertTo8D(output_filename, '2.wav')



# import os
# import tkinter as tk
# from tkinter import filedialog
# import pygame
# from pydub import AudioSegment
# from pydub.playback import play


# class MP3PlayerApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Simple MP3 Player")

#         self.song_path = ""
#         self.paused = False

#         self.init_gui()

#         pygame.mixer.init()

#     def init_gui(self):
#         self.play_button = tk.Button(self.root, text="Play", command=self.play_song)
#         self.play_button.pack()

#         self.pause_button = tk.Button(self.root, text="Pause/Resume", command=self.pause_resume_song)
#         self.pause_button.pack()

#         self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_song)
#         self.stop_button.pack()

#         self.load_button = tk.Button(self.root, text="Load Song", command=self.load_song)
#         self.load_button.pack()

#     def load_song(self):
#         self.song_path = filedialog.askopenfilename(filetypes=[("MP3 Files", "*.mp3")])
#         if self.song_path:
#             pygame.mixer.music.load(self.song_path)
#             self.root.title("Simple MP3 Player - " + os.path.basename(self.song_path))
    
#     def play_song(self):
#         if self.song_path:
#             sound = AudioSegment.from_mp3(self.song_path)
#             play(sound)
    
#     def stop_song(self):
#         play(AudioSegment.silent())
    
#     def pause_resume_song(self):
#         if self.song_path:
#             if pygame.mixer.music.get_busy() and not self.paused:
#                 pygame.mixer.music.pause()
#                 self.paused = True
#             elif self.paused:
#                 pygame.mixer.music.unpause()
#                 self.paused = False
    
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = MP3PlayerApp(root)
#     root.mainloop()





import yt_dlp
import threading

def download_song(song_name, output_filename):
    ydl_opts = {
        'format': 'bestaudio/best',
        'extractaudio': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': output_filename,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        search_query = f"ytsearch1:{song_name} audio"
        info_dict = ydl.extract_info(search_query, download=False)
        
        if 'entries' in info_dict:
            video_url = info_dict['entries'][0]['url']
            print(f"Downloading '{song_name}'...")
            ydl.download([video_url])
            print(f"'{song_name}' downloaded successfully.")
        else:
            print(f"Song '{song_name}' not found on YouTube.")

def download_multiple_songs(song_list):
    threads = []
    
    for song_name, output_filename in song_list:
        thread = threading.Thread(target=download_song, args=(song_name, output_filename))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    songs_to_download = [
        ("Asap Rocky - Purple Swag", "output_file_1"),
        ("Kanye West - Follow God", "output_file_2"),
        # Add more songs as needed
    ]
    
    download_multiple_songs(songs_to_download)