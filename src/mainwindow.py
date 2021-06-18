# PyQt5 modules
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QDialog, QApplication, QWidget, QPushButton, QAction, \
    QLineEdit, \
    QMessageBox
from PyQt5.QtCore import QCoreApplication, QObject, QRunnable, QThread, QThreadPool, pyqtSignal, pyqtSlot
from PyQt5 import uic, QtGui
from PyQt5.QtGui import QFont

# Python modules
import matplotlib.pyplot as plt
import sounddevice as sd
from scipy.io.wavfile import write
from pydub import AudioSegment
import os

# Project modules
from src.ui.mainwindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setFixedSize(1200, 600)
        self.setupUi(self)
        self.openbtn.clicked.connect(self.openFile)
        self.recordbtn.clicked.connect(self.StartRecording)
        self.filename = None

    def openFile(self):
        open = True
        if self.filename:
            open = False
            msgbox = QMessageBox(QMessageBox.Question, "Confirmación",
                                 "¿Seguro que quiere abrir un archivo?\nSe perderá el progreso actual.")
            msgbox.addButton(QMessageBox.Yes)
            msgbox.addButton(QMessageBox.No)
            msgbox.setDefaultButton(QMessageBox.No)
            reply = msgbox.exec()
            if reply == QMessageBox.Yes:
                open = True
        if open:
            self.filename = QFileDialog.getOpenFileName(self, "Abrir Archivo", "", "Archivo de Audio (*.mp3, *.wav, "
                                                                                   "*.ogg)",
                                                        "Archivo de Audio (*.mp3, *.wav, *.ogg)")[0]

    def StartRecording(self, seconds = 3, fs = 44100):
        open = True
        if self.filename:
            open = False
            msgbox = QMessageBox(QMessageBox.Question, "Confirmación",
                                 "¿Seguro que quiere realizar una grabación?\nSe perderá el progreso actual.")
            msgbox.addButton(QMessageBox.Yes)
            msgbox.addButton(QMessageBox.No)
            msgbox.setDefaultButton(QMessageBox.No)
            reply = msgbox.exec()
            if reply == QMessageBox.Yes:
                open = True
        if open:
            d = QDialog()
            d.setWindowTitle("Recording...")
            d.resize(300, 200)
            d.show()
            myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
            sd.wait()  # Wait until recording is finished
            d.close()
            current_path = os.path.dirname(os.path.abspath(__file__))
            self.filename = os.path.join(current_path, "recording.ogg")
            write(self.filename, fs, myrecording)  # Save as WAV file

    def spectrogram(self, data):

            fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(10, 6))
            fig.patch.set_facecolor((0.75, 0.75, 0.75))
            ax.patch.set_facecolor((0.0, 0.0, 0.0))
            Pxx, freqs, bins, im = ax.specgram(data, NFFT=1024, Fs=16000, noverlap=900)
            ax.set_ylabel('Frecuencia [Hz]')
            ax.set_xlabel('Tiempo [s]')
            plt.show()
