from pytube import YouTube
from tkinter import Tk, Label, Entry, Button, filedialog

def video_download():
    url = url_entry.get()
    save_path = filedialog.askdirectory()

    try:
        youtube = YouTube(url)
        streams = youtube.streams.filter(progressive=True, file_extension="mp4")
        high_res_stream = streams.get_highest_resolution()
        high_res_stream.download(output_path=save_path)

    except Exception as e:
        print(e)

# Create GUI window
window = Tk()
window.title("YouTube Video Downloader")

# URL label and entry field
url_label = Label(window, text="YouTube URL:")
url_label.pack()
url_entry = Entry(window)
url_entry.pack()

# Download button
download_button = Button(window, text="Download", command=video_download)
download_button.pack()

# Run the GUI window
window.mainloop()
