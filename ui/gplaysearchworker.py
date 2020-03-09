from PyQt5.QtCore import QThread

from gplay.googlePlaySearch import GooglePlaySearch


class GPlaySearchWorker(QThread):
    def __init__(self):
        QThread.__init__(self)
        self.aranan = None
        self.maxforTest = 0
        self.gps = GooglePlaySearch()


    def run(self):
        print("THREAD BAŞLADI")
        self.gps.googlePlaySearchRun(self.aranan, self.maxforTest)
        print("THREAD finish BAŞLADI")
        self.gps.finish()
        print("THREAD finish BİTTİ ")
