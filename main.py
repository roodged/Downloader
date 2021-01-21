from tkinter import *
import pytube

def descarga():
   video_url = url.get()
 
    try:
        pytube.YouTube(video_url)
        video = youtube.streams.first()
        video.download('C:\Users\Rood-Ged\Desktop/video download')
        notif.config(fg='green', text = 'descarga completa ')
 
    except expression as identifier:
        pass
    

root = Tk()
root.title = ('Youtube Downloader')

label = Label(root, text='Convertidor devideo youtube' ,fg ='red', font= 'calibri 15').grid(sticky=N, padx = 100, row=0)
label = Label(root, text='porfavor ingrese el enlace',font = 'calibri 12 ').grid(sticky=N, row=1, pady=15)
notif = Label(root, font= 'calibri 12')
notif.grid(sticky=N,pady=1,row=4)

url= StringVar

Entry(root, width = 50,textvariable=url).grid(sticky=N , row=2)
Button(root, width = 20, text='Descargar', font ='calibri 12', command=descarga).grid(sticky=N,row=3,pady=15)
root.mainloop()