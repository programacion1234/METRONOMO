
import math
import numpy as np

wavearray=[]
class Seno:


        def __init__(self, sampling, bits,chord,metrica,duraci):
            self.SamplingRate = sampling
            self.NumeroBit = bits
            self.fq1=chord
            self.met=metrica
            self.durak=duraci

        def generar(self):
            print self.durak

            tempo=int(44100*self.durak)
            loop=5
            if self.met==1:
                for i in range(0, loop):

                    for i in range(0, tempo):
                            datos = math.sin((2*math.pi*(self.fq1*float(1.059463**12))*i)/44100)
                            wavearray.append(datos)
                    for i in range(0, tempo):
                            datos =0
                            wavearray.append(datos)
                    for i in range(0, tempo):
                            datos = math.sin((2*math.pi*(self.fq1)*i)/44100)
                            wavearray.append(datos)
                    for i in range(0, tempo):
                            datos = 0
                            wavearray.append(datos)
                    for i in range(0, tempo):
                            datos = math.sin((2*math.pi*(self.fq1)*i)/44100)
                            wavearray.append(datos)
                    for i in range(0, tempo):
                            datos = 0
                            wavearray.append(datos)
                    for i in range(0, tempo):
                            datos = math.sin((2*math.pi*(self.fq1)*i)/44100)
                            wavearray.append(datos)
                    for i in range(0, tempo):
                            datos = 0
                            wavearray.append(datos)
            if self.met==2:
                for i in range(0, loop):

                    for i in range(0, tempo):
                            datos = math.sin((2*math.pi*(self.fq1*float(1.059463**12))*i)/44100)
                            wavearray.append(datos)
                    for i in range(0, tempo):
                            datos =0
                            wavearray.append(datos)
                    for i in range(0, tempo):
                            datos = math.sin((2*math.pi*(self.fq1)*i)/44100)
                            wavearray.append(datos)
                    for i in range(0, tempo):
                            datos = 0
                            wavearray.append(datos)
                    for i in range(0, tempo):
                            datos = math.sin((2*math.pi*(self.fq1)*i)/44100)
                            wavearray.append(datos)
                    for i in range(0, tempo):
                            datos = 0
                            wavearray.append(datos)
            if self.met==3:
                for i in range(0, loop):

                    for i in range(0, tempo):
                            datos = math.sin((2*math.pi*(self.fq1*float(1.059463**12))*i)/44100)
                            wavearray.append(datos)
                    for i in range(0, tempo):
                            datos =0
                            wavearray.append(datos)
                    for i in range(0, tempo):
                            datos = math.sin((2*math.pi*(self.fq1)*i)/44100)
                            wavearray.append(datos)
                    for i in range(0, tempo):
                            datos = 0
                            wavearray.append(datos)
            if self.met==4:
                for i in range(0, loop):

                    for i in range(0, tempo):
                            datos = math.sin((2*math.pi*(self.fq1*float(1.059463**12))*i)/44100)
                            wavearray.append(datos)
                    for i in range(0, tempo):
                            datos =0
                            wavearray.append(datos)
                    for i in range(0, tempo):
                            datos = math.sin((2*math.pi*(self.fq1)*i)/44100)
                            wavearray.append(datos)
                    for i in range(0, tempo):
                            datos = 0
                            wavearray.append(datos)
                    for i in range(0, tempo):
                            datos = math.sin((2*math.pi*(self.fq1)*i)/44100)
                            wavearray.append(datos)
                    for i in range(0, tempo):
                            datos = 0
                            wavearray.append(datos)
                    for i in range(0, tempo):
                            datos = math.sin((2*math.pi*(self.fq1)*i)/44100)
                            wavearray.append(datos)
                    for i in range(0, tempo):
                            datos = 0
                            wavearray.append(datos)
                    for i in range(0, tempo):
                            datos = math.sin((2*math.pi*(self.fq1)*i)/44100)
                            wavearray.append(datos)
                    for i in range(0, tempo):
                            datos = 0
                            wavearray.append(datos)
                    for i in range(0, tempo):
                            datos = math.sin((2*math.pi*(self.fq1)*i)/44100)
                            wavearray.append(datos)
                    for i in range(0, tempo):
                            datos = 0
                            wavearray.append(datos)
            FinalData = np.asarray(wavearray)
            return FinalData


        def leveladjust(self, datos, bits, level):
            peaklevel = max(abs(datos))
            print peaklevel
            valueLevel = (10**(level/20))*((2**16)/2.0)
            valueAdjust = valueLevel / float(peaklevel)
            datosAjustados = datos * valueAdjust
            print max(datosAjustados)
            return datosAjustados