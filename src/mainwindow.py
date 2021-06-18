# PyQt5 modules
import urllib
from src.shazamtools import *
import contextlib

from PyQt5.QtWidgets import QMainWindow, QFileDialog, QDialog, QApplication, QWidget, QPushButton, QAction, \
    QLineEdit, \
    QMessageBox
from PyQt5.QtCore import QCoreApplication, QObject, QRunnable, QThread, QThreadPool, pyqtSignal, pyqtSlot
from PyQt5 import uic, QtGui
from PyQt5.QtGui import QFont, QPixmap

# Python modules
import matplotlib.pyplot as plt
import sounddevice as sd
from scipy.io.wavfile import write
from pydub import AudioSegment
import os
import asyncio

# Project modules
import shazamio as sh
from src.ui.mainwindow import Ui_MainWindow
from PIL import Image
import urllib


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setFixedSize(1200, 600)
        self.setupUi(self)
        self.openbtn.clicked.connect(self.openFile)
        self.recordbtn.clicked.connect(self.StartRecording)
        self.beginbtn.clicked.connect(self.begin)
        self.file_data.setText("No file selected!")
        self.filename = None
        self.shazam = sh.Shazam()
        self.out = None
        self.audio_data = None
        self.im = None
        self.a=0
        self.text_out = None

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
            self.filename = QFileDialog.getOpenFileName(self, "Abrir Archivo", "")[0]
            if self.filename:
                self.clear_screen()
                self.file_data.setText("Audio Selected")

    def clear_screen(self):
        self.image_out.clear()
        self.title_out.clear()
        self.subtitle_out.clear()

    def StartRecording(self, seconds=int(3), fs=44100):
        """"
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
        """
        d = QDialog()
        d.setWindowTitle("Recording...")
        d.resize(300, 200)
        d.show()
        myrecording = create_audio_recording(3)
        sd.wait()  # Wait until recording is finished
        self.clear_screen()
        self.file_data.setText("Audio selected.")

    def begin(self):
        if self.filename:
            self.file_data.setText("Finding song...")
            loop = asyncio.get_event_loop()
            loop.run_until_complete(self.get_shazam_data())
            self.file_data.setText("Song found!")
            track = self.out.get("track")
            images = track.get("images")
            cover_image = images.get("coverart")
            urllib.request.urlretrieve(cover_image, "sample.png")
            self.im = QPixmap("sample.png")
            self.image_out.setPixmap(self.im)
            title = track.get("title")
            subtitle = track.get("subtitle")
            self.title_out.setText(title)
            self.subtitle_out.setText(subtitle)
            self.spectrogram()
        else:
            msgbox = QMessageBox(QMessageBox.Information, "No File Selected!", "No se seleccionó un archivo!")
            msgbox.addButton(QMessageBox.Close)
            msgbox.setDefaultButton(QMessageBox.Close)
            msgbox.exec()

    async def get_shazam_data(self):
        if self.filename:
            file = await sh.utils.load_file(self.filename, 'rb')
            self.audio_data = sh.converter.Converter.normalize_audio_data(file).raw_data
            self.out = await self.shazam.recognize_song(self.filename)

    def spectrogram(self):

        fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(10, 6))
        fig.patch.set_facecolor((0.75, 0.75, 0.75))
        ax.patch.set_facecolor((0.0, 0.0, 0.0))
        Pxx, freqs, bins, im = ax.specgram(self.audio_data, NFFT=1024, Fs=16000, noverlap=900)
        ax.set_ylabel('Frecuencia [Hz]')
        ax.set_xlabel('Tiempo [s]')
        plt.show()
