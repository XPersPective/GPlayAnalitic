from math import floor

from PyQt5.QtCore import QObject, pyqtSignal


class OpTracking(QObject):
    signalTracking = pyqtSignal(bool, int)

    def __init__(self):
        super().__init__()
        self.isdone = False
        self.percentInt = 0
        self.percentFloat = 0.0

    # örnek:
    # percentPart = 80 opCount = 200 -> percentFloat +=80/200
    # percentPart = 20 opCount = 150 -> percentFloat +=20/150
    # percentFloat += percentFloat
    def setPercent(self, percentPart, opCount):
        self.percentFloat += float(percentPart / opCount)
        self.percentInt = floor(self.percentFloat)
        if self.percentFloat == 100.0:
            self.percentInt = 100
        if self.percentFloat <= 0.0:
            self.percentInt = 0
        self.signalTrackingemit()

    def setisDone(self, isdone):
        self.isdone = isdone
        self.signalTrackingemit()

    def signalTrackingemit(self):
        print(" optrackingten   :isdone : " + str(self.isdone) + " percentInt : %" + str(self.percentInt))
        self.signalTracking.emit(self.isdone, self.percentInt)
