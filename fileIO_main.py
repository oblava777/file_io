from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk
import requests
from tkinter import messagebox as mb


def upload():
    try:
        filepath = fd.askopenfilename()
        if filepath:
            with open(filepath, 'rb') as f:
                files = {'file': f}
                response = requests.post('http://file.io', files=files)
                response.raise_for_status()
                link = response.json()['link']
                entry.delete(0, END)
                entry.insert(0, link)
    except Exception as e:
        mb.showerror('Ошибка!', f'Произошла ошибка {e}')




win = Tk()
win.title('Сохранение файлов в облаке')
win.geometry('400x200')

button = ttk.Button(text='Загрузить файл', command=upload)
button.pack()

entry = ttk.Entry()
entry.pack()

win.mainloop()
