import json
from tkinter import *
from tkinter import ttk,messagebox
from urllib.request import urlopen
class Aplicacion():
    __ventana=None
    __dolar=None
    __peso=None
    __entrada1=None
    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.title('Conversor de moneda')
        self.__ventana.resizable(0,0)
        self.__dolar =DoubleVar()
        self.__peso =DoubleVar()
        contenedor = ttk.Frame(self.__ventana, borderwidth=2, relief="raised", padding=(10,10)).grid(column=0,row=0)
        self.__entrada1=ttk.Entry(contenedor, textvariable=self.__dolar,width=10)
        self.__entrada1.grid(padx=10,pady=10,column=1, row=0)
        dolarLavel=ttk.Label(contenedor, text="dólares").grid(column=2, row=0,sticky='w',padx=5)
        textoLabel=ttk.Label(contenedor, text="es equivalente a").grid(padx=5,column=0, row=1,sticky='e')
        pesoVLabel=ttk.Label(contenedor, textvariable=self.__peso,).grid(column=1, row=1)
        pesoLabel=ttk.Label(contenedor, text="pesos").grid(column=2, row=1,sticky='w',padx=5)
        boton1=ttk.Button(contenedor, text="Salir",padding=(5,5), command=quit).grid(padx=5,pady=5,column=2, row=2,sticky='w')
        self.__dolar.set('')
        self.__peso.set('')
        self.__dolar.trace('w',self.calcular)
        self.__entrada1.focus()
        self.__ventana.mainloop()
    def calcular(self, *args):
        if self.__entrada1.get()!='':
            try:
                valorPeso=float(self.__entrada1.get())
            except ValueError:
                messagebox.showerror(title='Error de tipo',message='Debe ingresar un valor numérico.')
                self.__dolar.set('')
                self.__peso.set('')
                self.__entrada1.focus()
            else:
                try:
                    url='https://www.dolarsi.com/api/api.php?type=dolar'
                    respuesta=urlopen(url)
                    dJson=json.loads(respuesta.read())
                    valorDolar=float(dJson[0]['casa']['venta'].replace(',','.'))
                    self.__peso.set(valorPeso*valorDolar)
                except  ValueError:
                    messagebox.showerror(title='Error de conexión a la api',message='Durante la conexión a la api, no se obtuvieron valores numéricos.')
                except:
                    messagebox.showerror(title='Error de conexión a la api',message='No se pudieron obtener datos de la api.')
        else:
            self.__peso.set('')