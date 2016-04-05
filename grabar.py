


import pyaudio
import wave
#import numpy as np


class Grabar:

    def __init__(self, BUFFER, FORMAT, CHANNELS, RATE):
        self.BUFFER = BUFFER
        self.FORMAT = FORMAT
        self.CHANNELS = CHANNELS
        self.RATE = RATE
        self.audio = pyaudio.PyAudio()

    def inicio(self):
        self.arreglo = []
        data = self.audio.get_default_host_api_info()
        print data
        self.transferencia = self.audio.open(format=self.FORMAT, channels=self.CHANNELS, rate=self.RATE, input=True, frames_per_buffer=self.BUFFER)

    def grabacion(self):
        datos = self.transferencia.read(self.BUFFER)
        self.arreglo.append(datos)

    def parar(self):
        self.transferencia.stop_stream()
        self.transferencia.close()
        self.audio.terminate()
        return self.arreglo

    def creaAudio(self, nombre):
        wf = wave.open(nombre+'.wav', 'wb')
        wf.setnchannels(self.CHANNELS)
        wf.setframerate(self.RATE)
        wf.setsampwidth(self.audio.get_sample_size(self.FORMAT))
        wf.writeframes(b''.join(self.arreglo))
        wf.close()

    def reproduce(self, nombre):
        rf = wave.open(nombre+'.wav', 'rb')
        prof = rf.getsampwidth()
        channels = rf.getnchannels()
        rate = rf.getframerate()
        audioN = pyaudio.PyAudio()
        streamN = audioN.open(format=audioN.get_format_from_width(prof), channels=channels, rate=rate, output=True)
        datos = rf.readframes(self.BUFFER)
        while datos != '':
            streamN.write(datos)
            datos = rf.readframes(self.BUFFER)

        rf.close()
        streamN.stop_stream()
        streamN.close()
        audioN.terminate()