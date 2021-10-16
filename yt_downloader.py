from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, filedialog
import pytube
import os

win = tk.Tk()
win.title("Youtube Downloader")
win.geometry("700x380")
win.wm_iconbitmap('main.ico')
win.maxsize(700, 330)
win.minsize(700, 380)

label1 = tk.Label(win, background="black", width="300", height="2")
label1.place(x=0, y=0)

yt_icon1 = tk.PhotoImage(file='icons/yt.png')
logo = tk.Label(win, image=yt_icon1, borderwidth=0)
logo.place(x=0, y=-6)

caption = tk.Label(win, text="Youtube  Downlader",
                   font=("verdana", 10, "bold"), height=2)
caption.place(x=270, y=5)

# caption youtube image---------------------------------
yt_image2 = tk.PhotoImage(file='icons/yt.png')
logo = tk.Label(win, image=yt_image2, borderwidth=0)
logo.place(x=653, y=-6)

# youtube logo-------------------------------------------
yt_image3 = tk.PhotoImage(file='icons/big1.png')
big_logo = tk.Label(win, image=yt_image3, borderwidth=0)
big_logo.place(x=270, y=30)

# link limage---------------------------------------------
link_image = tk.PhotoImage(file='icons/link.png')
link_img = tk.Label(win, image=link_image, borderwidth=0)
link_img.place(x=45, y=138)

# link textbox---------------------------------------------
textl = tk.Text(win, width=60, height=2)
textl.place(x=95, y=135)
textl.insert("end", " Paste video link here ")

# path image-----------------------------------------------
choosepath_img = tk.PhotoImage(file='icons/path.png')
pathimage = tk.Label(win, image=choosepath_img, borderwidth=0)
pathimage.place(x=43, y=185)

# input box for path---------------------------------------
pathvar = tk.StringVar()
textp = Entry(win, width=45, textvariable=pathvar, font=('verdana', 10))
textp.place(x=95, y=185, height=37, width=360)
textp.insert("end", " choose path ")

# Quality label-------------------------------------------
quality_lbl = ttk.Label(win, text=' Quality ', font=('verdana', 10, 'bold'))
quality_lbl.place(x=30, y=240)

# quality combobox-----------------------------------------
quality_var = tk.StringVar()
quality_combobox = ttk.Combobox(
    win, width=14, textvariable=quality_var, background='white', state='readonly')
values = quality_combobox['values'] = (
    'low quality', 'high quality', 'Only audio')
# quality_combobox.current(0)
quality_combobox.place(x=95, y=240)

# download image-------------------------------------------
download_image = tk.PhotoImage(file='icons/download.png')
download_img = tk.Label(win, image=download_image, borderwidth=0)
download_img.place(x=250, y=291)

# developer code label -------------------------------------
dev_name = tk.Label(win, text='coded by : Lakshya verma',
                    font=('High Tower', 10, 'bold', 'underline'), foreground='darkgreen')
dev_name.place(x=528, y=356)

# note label------------------------------------------------
note_lbl = tk.Label(win, text='NOTE : Do not exit if application is Not Responding.',
                    font=('verdana', 9, 'bold', 'underline'), foreground='red')
note_lbl.place(x=5, y=356)

# browse button Functionality--------------------------------
download_dir = ''


def open_path():
    global download_dir
    download_dir = filedialog.askdirectory(initialdir=os.getcwd(
    ), title='Select Path')
    pathvar.set(download_dir)
    textp.config(foreground='darkgreen')

# download button functionality------------------------------

def downloads():
    quality = quality_var.get()
    link = textl.get("1.0", "end-1c")
    download_path = pathvar.get()
    if len(link) < 1:
        messagebox.showerror("Youtube Downloader", "please paste link below")
    if len(download_path) < 1:
        messagebox.showerror("Path not found ", "select the path")
    try:
        yt = pytube.YouTube(link)
        try:
            if (quality == values[0]):
                stream = yt.streams.filter(
                    mime_type="video/mp4", progressive=True).first()
            elif(quality == values[1]):
                stream = yt.streams.filter(
                    mime_type="video/mp4", progressive=True).last()
            elif(quality == values[2]):
                stream = yt.streams.filter(only_audio=True).first()
            try:
                stream.download(download_path)
                messagebox.showinfo("Youtube Downloader",
                                    f"successfully downloaded \n Title :{stream.title} \n size : {round(stream.filesize/1024000,1)} mb \n path :{download_dir}")
            except:
                messagebox.showerror(
                    'path not found', 'Select valid download path')
        except:
            messagebox.showerror('QualityError', 'select quality')
    except:
        messagebox.showerror('invalid link', 'please input url')


# Download button------------------------------------------------------------
download_btn = tk.Button(win, text="Download", command=downloads,
                         relief=RIDGE, bg='#9c2d2c', fg='white', font=('verdana', 11, 'bold'))
download_btn.place(x=290, y=290)

# browse button--------------------------------------------------------------
browse_btn = tk.Button(win, text="Browse", width=10, command=open_path,
                       relief=RIDGE, bg='#9c2d2c', fg='white', font=('verdana', 11, 'bold'))
browse_btn.place(x=473, y=188)


win.mainloop()
