import pyaudio
import wave


class Audio:
    def __init__(self, CHUNK):
        self.CHUNK = CHUNK


    def abrir(self, Nombre):

        self.wf = wave.open(Nombre, 'rb')
        sampwidth = self.wf.getsampwidth()
        channels = self.wf.getnchannels()
        rate = self.wf.getframerate()
        return (sampwidth, channels, rate, self.wf)


    def inicio(self, sampwidth, channels, framerate):
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=self.p.get_format_from_width(sampwidth),
                        channels=channels,
                        rate=framerate,
                        output=True)

    def reproducir(self, audiofile):
        data = audiofile.readframes(self.CHUNK)
        while data != '':
            self.stream.write(data)
            data = self.wf.readframes(self.CHUNK)




    def cerrar(self):

        self.wf.close()
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()