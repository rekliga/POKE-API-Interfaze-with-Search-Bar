import requests


url = "https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0"

respuesta = requests.get(url)
respuesta = respuesta.json()

cuenta_hab = int()
cuenta_tot = respuesta["count"]
nombres_= respuesta["results"]


from tkinter import *
from tkinter import ttk

ws = Tk()
ws.title('PythonGuides')
ws.geometry('400x250')
ws['bg']='#fb0'
entrada =ttk.Entry(ws)
entrada.pack(pady=10)
def buscar():
    print(entrada.get())
    
   

    for i in tv.get_children():
        tv.delete(i)
    for i in range(1000):
        busqueda =nombres_[i]["name"]
        try:
            if str(busqueda).startswith(entrada.get()):
                tv.insert(parent='', index=i, iid=i, text='', values=(i,nombres_[i]["name"]))
        except:
            pass

    
bt1 = ttk.Button(ws,text="Try",command=buscar)
bt1.pack(pady=10)
tv = ttk.Treeview(ws)
tv['columns']=('Rank', 'Name')
tv.column('#0', width=0, stretch=NO)
tv.column('Rank', anchor=CENTER, width=80)
tv.column('Name', anchor=CENTER, width=80)


tv.heading('#0', text='', anchor=CENTER)
tv.heading('Rank', text='Id', anchor=CENTER)
tv.heading('Name', text='Name', anchor=CENTER)




for i in range(1000):
    tv.insert(parent='', index=i, iid=i, text='', values=(i,nombres_[i]["name"]))

tv.pack()


ws.mainloop()