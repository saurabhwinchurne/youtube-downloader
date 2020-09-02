from tkinter import *
from threading import *
from pytube import YouTube
from tkinter import messagebox, filedialog, ttk

def thread_downloader():
    thread = Thread(target=downloader)
    thread.start()

def browse():
    download_path = filedialog.askdirectory()
    download_directory.set(download_path)

file_size = 0
def progress(stream=None, chunk=None, remaining=None):
    global file_size
    file_downloaded = file_size - remaining
    per = file_downloaded / file_size * 100
    B2.config(text=('{:00.0f} % Downloaded'.format(per)), state=DISABLED)

def downloader():
    global file_size
    if len(link.get()) == 0:
        messagebox.showwarning('Error', 'Please Enter Correct Link.')
        sys.exit(downloader)
    
    if len(download_directory.get()) == 0:
        messagebox.showwarning('Error', 'Please Select Download Path.')
        sys.exit(downloader)

    try:
        download_folder = download_directory.get()
        video_link = YouTube((link.get()), on_progress_callback=progress)
        get_video = video_link.streams.filter(file_extension='mp4').first()
        file_size = get_video.filesize
        download_video = get_video.download(download_folder)
        B2.config(text='Download')
        messagebox.showinfo('Notification', 'Video Downloaded Successfully!')
        B2.config(state=NORMAL)
        B2.focus_set()
        E1.delete(0, END)
        E2.delete(0, END)
    except:
        messagebox.showerror('Error', 'Something Went Wrong!')
        B2.config(text='Download', state=NORMAL)
        B2.focus_set()
        E1.delete(0, END)
        E2.delete(0, END)


root = Tk()

root.iconbitmap('logo.ico')
root.title('Youtube Downloader')
root.geometry('360x250')
root.resizable(width=False, height=False)
root.config(background='white')

img = PhotoImage(file='./ytd.png')
myimg = Label(root, image=img, relief=RIDGE).grid(padx=100)

link_label = Label(text='Enter video link Here :', font='Comicsans 10 bold', bg='grey',
fg='white', borderwidth=2, relief=GROOVE, padx=10)
link_label.grid(row=2, column=0, pady=5, sticky=W)

path_label = Label(text='Select Download Path :', font='Comicsans 10 bold', relief=GROOVE,
borderwidth=2, bg='grey', fg='white')
path_label.grid(row=4, pady=10, column=0, sticky=W)

link = StringVar()
E1 = Entry(textvariable=link, relief=SUNKEN, borderwidth=2)
E1.grid(row=2, column=0, padx=70, sticky=E)

download_directory = StringVar()
E2 = Entry(textvariable=download_directory, relief=SUNKEN, borderwidth=2)
E2.grid(row=4, column=0, sticky=E, padx=80)

B1 = Button(text='Browse', font='Comicsans 10 bold', borderwidth=2, command=browse, relief=GROOVE)
B1.grid(row=4, column=0, sticky=E, padx=15)

B2 = Button(text='Download', font='Comicsans 10 bold', command=thread_downloader, relief=GROOVE)
B2.focus_set()
B2.grid(row=6, column=0, pady=25)

root.mainloop()
