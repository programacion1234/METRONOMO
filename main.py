#Realizado por: Diego Lozano, Ivan Herrera, Ximena Medina
# Importamos las librerias y clases necesarias

# NOTA: Al oprimir el boton Grabar el programa primero reproduce
# el metronomo por completo, luego de esto graba, al oprimir parar para la grabacion
#y al oprimir reproducir reproduce la grabacion.
#Al cerrar la ventana guarda el audio grabado y el metronomo reproducido al principio.

from archivo import Archivo
from seno import Seno
from Tkinter import *
from Tkinter import Tk
import tkMessageBox
from grabar import Grabar
import pyaudio
from Audiosystem import Audio

wavearray=[]

def main():


    buffer = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    MaxBits = 16
    level=-5
    # Creacion de la ventana

    ventana = Tk()

    ventana.title("Metronomo")

    audio1 = Grabar(buffer, FORMAT, CHANNELS, RATE)

    d = BooleanVar(ventana)
    e = BooleanVar(ventana)
    e.set(False)
    f = BooleanVar(ventana)
    f.set(False)

    print("Las opciones de nota se ingresaran como y son: 'do'  're'  'mi'  'fa'  'sol'  'la'  'si'")
    print("Las opciones de metrica son: 1. 4/4   2. 3/4  3. 2/4  4. 6/8 ")
    global arreglo1

    arreglo1 = []

    # Uso de frames para organizar la ventana.
    frame1 = Frame(ventana)
    frame1.pack(side=TOP)
    frame2 = Frame(ventana)
    frame2.pack(side=TOP)

    # Creacion e insercion del cuadro de texto 1.
    cuadro1= Label(frame1, fg="black", padx=15, pady=10, text="Digite el nombre del archivo 1:")
    cuadro1.pack(side=LEFT)

    # Creacion e insercion de cuadro de entrada 1.
    e1 = Entry(frame1, bd=5, insertwidth=1)
    e1.pack(side=LEFT, padx=5, pady=10)

    # Creacion e insercion del cuadro de texto 2.
    cuadro2= Label(frame1, fg="black", padx=15, pady=10, text="Ingrese la nota deseada:")
    cuadro2.pack(side=LEFT)

    # Creacion e insercion de cuadro de entrada 2.
    e2 = Entry(frame1, bd=5, insertwidth=1)
    e2.pack(side=LEFT, padx=5, pady=10)

     # Creacion e insercion del cuadro de texto 3.
    cuadro3= Label(frame1, fg="black", padx=1, pady=10, text="Ingrese el bpm deseado:")
    cuadro3.pack(side=LEFT)

    # Creacion e insercion de cuadro de entrada 3.
    e3 = Entry(frame1, bd=5, insertwidth=1)
    e3.pack(side=LEFT, padx=5, pady=10)

    # Creacion e insercion del cuadro de texto 4.
    cuadro4= Label(frame1, fg="black", padx=15, pady=10, text="Ingrese la metrica deseada:")
    cuadro4.pack(side=TOP)

    # Creacion e insercion de cuadro de entrada 4.
    e4 = Entry(frame1, bd=5, insertwidth=1)
    e4.pack(side=LEFT, padx=5, pady=10)


    Nombre='metro.wav'


    # Mensajes de grabacion activada.
    mensaje1 = Label(frame1, fg='red', padx=15, pady=10, text='Grabando...')

    # Funcion que activa el mensaje error,genera la onda del metronomo,
    # archiva el metronomo, reproduce el metronomo y luego graba un audio

    def activasms1():
        if e1.get()== '':
            print 'error'
            tkMessageBox._show('Error', 'No ingreso el nombre del audio a grabar.')
        elif e2.get()== '':
            print 'error'
            tkMessageBox._show('Error', 'No ingreso la nota del metronomo.')
        elif e3.get()== '':
            print 'error'
            tkMessageBox._show('Error', 'No ingreso el bpm del metronomo.')
        elif e4.get()== '':
            print 'error'
            tkMessageBox._show('Error', 'No ingreso la metrica del metronomo.')
        else:
            d.set(True)


            g=e2.get()

            if g=="do":
                frecFundamental=261.63
                print("La nota escogida es: do")
            if g=="re":
                frecFundamental=293.66
                print("La nota escogida es: re")
            if g=="mi":
                frecFundamental=329.63
                print("La nota escogida es: mi")
            if g=="fa":
                frecFundamental=349.23
                print("La nota escogida es: fa")
            if g=="sol":
                frecFundamental=392.00
                print("La nota escogida es: sol")
            if g=="la":
                frecFundamental=440.00
                print("La nota escogida es: la")
            if g=="si":
                frecFundamental=493.88
                print("La nota escogida es: si")


            t=float(e3.get())

            tiempo=(60/t)
            negra=tiempo/2
            corchea=tiempo/4

            print("El bpm es:")
            print(t)

            m=float(e4.get())

            if m == 1:
                onda = Seno(RATE, MaxBits, frecFundamental, m,negra)
                print("Metrica de: 4/4")
            if m == 2:
                onda = Seno(RATE, MaxBits, frecFundamental, m,negra)
                print("Metrica de: 3/4")
            if m == 3:
                onda = Seno(RATE, MaxBits, frecFundamental, m,negra)
                print("Metrica de: 2/4")
            if m == 4:
                onda = Seno(RATE, MaxBits, frecFundamental, m,corchea)
                print("Metrica de: 6/8")


            e1.configure(state='disabled')
            e2.configure(state='disabled')
            e3.configure(state='disabled')
            e4.configure(state='disabled')

            datos = onda.generar()
            datosAjustados = onda.leveladjust(datos,MaxBits,level)
            archivo = Archivo(RATE, MaxBits,Nombre)
            archivo.archivar(datosAjustados)


            audio = Audio(buffer)
            Datos = audio.abrir(Nombre)
            audio.inicio(Datos[0],Datos[1],Datos[2])
            audio.reproducir(Datos[3])

            audio1.inicio()
            mensaje1.pack(side=BOTTOM)

            print("G R A B A N D O...")

            while d.get():

                audio1.grabacion()
                ventana.update()
                if d.get() is False:
                    break
            audio.cerrar()

    # Funcion desactiva mensaje y para de grabar.
    def desactivasms1():
        d.set(False)
        e.set(True)
        mensaje1.pack_forget()
        global  arreglo1
        arreglo1 = audio1.parar()

        audio1.creaAudio(e1.get())
        grabarButton1.pack_forget()
        pararButton1.pack_forget()

    def reproduccion1():
        audio1.reproduce(e1.get())

    # Creacion de botones.
    grabarButton1 = Button(frame2, padx=30, pady=2, text="Grabar", command=activasms1)
    grabarButton1.pack(side=LEFT)

    pararButton1 = Button(frame2, padx=30, pady=2, text="Parar", command=desactivasms1)
    pararButton1.pack(side=LEFT)

    reproducirButton1 = Button(frame2, padx=30,pady=2, text="Reproducir", command=reproduccion1)
    reproducirButton1.pack(side=RIGHT)

    ventana.mainloop()

if __name__ == "__main__":
    main()