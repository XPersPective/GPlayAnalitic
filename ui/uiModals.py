from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QTableWidget, QLabel, QAbstractItemView

from mydb.mydb import MyDb


class UiModalTbKategori:
    def __init__(self):
        self.uiName = "uiKategori"
        self.no = 'No'
        self.kategoriadi = 'Kategori'
        self.header = [self.no, self.kategoriadi ]

    def in_HeaderUi(self, qTableWidget:QTableWidget):
        qTableWidget.verticalHeader().hide()
        countColumn = len(self.header)
        qTableWidget.setColumnCount(countColumn)
        for ncol in range(countColumn):
            item = QtWidgets.QTableWidgetItem()
            qTableWidget.setHorizontalHeaderItem(ncol, item)
            item.setText(self.header[ncol])
            qTableWidget.setItem(0,ncol, item)

    def getUi(self, qTableWidget: QTableWidget, listModal: list):
        self.in_HeaderUi(qTableWidget)
        countColumn = len(self.header)
        countRow = len(listModal)
        qTableWidget.setRowCount(countRow)
        for nrow in range(countRow):
            itemlist = listModal[nrow].itemListforUi(nrow)
            for ncol in range(countColumn):
                item = QtWidgets.QTableWidgetItem()
                item.setText(itemlist[ncol])
                qTableWidget.setItem(nrow, ncol, item)

class UiModalTbSorgu:
    def __init__(self):
        self.uiName = "uiSorgu"
        self.no = 'No'
        self.sorgukimlik = 'Sorgu Kimlik'
        self.aranan = 'Aranan'
        self.ekparams = 'Ek Params'
        self.sonucadet = 'Sonuç'
        self.sorgutarihi = 'Sorgu Tarihi'
        self.header = [ self.no, self.aranan, self.sonucadet, self.sorgutarihi, self.ekparams, self.sorgukimlik ]

    def in_HeaderUi(self, qTableWidget:QTableWidget):
        qTableWidget.verticalHeader().hide()
        countColumn = len(self.header)
        qTableWidget.setColumnCount(countColumn)
        for ncol in range(countColumn):
            item = QtWidgets.QTableWidgetItem()
            qTableWidget.setHorizontalHeaderItem(ncol, item)
            item.setText(self.header[ncol])
            qTableWidget.setItem(0,ncol, item)

    def getUi(self, qTableWidget: QTableWidget, listModal: list):
        sorgukimlikdictfromrowid ={}
        self.in_HeaderUi(qTableWidget)
        countColumn = len(self.header)
        countRow = len(listModal)
        qTableWidget.setRowCount(countRow)
        for nrow in range(countRow):
            itemlist = listModal[nrow].itemListforUi(nrow)
            for ncol in range(countColumn):
                item = QtWidgets.QTableWidgetItem()
                item.setText(itemlist[ncol])
                qTableWidget.setItem(nrow, ncol, item)
            sorgukimlikdictfromrowid[nrow] =  itemlist[5]

        qTableWidget.setProperty("sorgukimlikdictfromrowid",sorgukimlikdictfromrowid)
        qTableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        qTableWidget.resizeColumnsToContents()
        qTableWidget.resizeRowsToContents()

class UiModalTbPlayAppList:
    def __init__(self):
        self.uiName = "uiPlayAppList"
        self.no = 'No'
        self.str_ad = 'Adı'
        self.kategori_adi = 'Kategori'
        self.str_yuklemetarihi = 'Çikis Tarihi'
        self.int_indirilme = 'Download'
        self.int_gunluk_ort_indirme = 'Günlük Ort. Download'
        self.int_fark_gun = 'Gün Yaş'
        self.float_yil = 'Gün Yıl'
        self.float_puan = 'Puan'
        self.int_siralamasi = 'Sıralaması'
        self.str_icon = 'İcon'
        self.str_resimler = 'Resimler'
        self.str_ucret = 'Ücret Durumu'
        self.str_boyut = 'Boyut'
        self.str_version = 'Versiyon'
        self.str_minandroid = 'Min And'
        self.str_gelistirici = 'Gelistirici'
        self.str_gunceltarih = 'GÜncellenme Tarihi'
        self.str_link = 'Link'
        self.sorgukimlik_id = 'Sorgu id'
        self.id ="id"
        self.header = [ self.no, self.str_ad, self.kategori_adi, self.str_yuklemetarihi, self.int_indirilme, self.int_gunluk_ort_indirme, self.int_fark_gun,
               self.float_yil, self.float_puan, self.int_siralamasi, self.str_ucret, self.str_boyut, self.str_version, self.str_minandroid,
               self.str_gelistirici, self.str_gunceltarih, self.str_link, self.sorgukimlik_id,self.id ]

    def in_HeaderUi(self, qTableWidget:QTableWidget):
        qTableWidget.verticalHeader().hide()
        countColumn = len(self.header)
        qTableWidget.setColumnCount(countColumn)
        for ncol in range(countColumn):
            item = QtWidgets.QTableWidgetItem()
            qTableWidget.setHorizontalHeaderItem(ncol, item)
            item.setText(self.header[ncol])
            qTableWidget.setItem(0,ncol, item)

    def getUi(self, qTableWidget: QTableWidget, listModal: list, dbobj: MyDb):
        showableRowList =[]
        if dbobj is not None:
            myreturnmodalListKategori = dbobj.main_getAll_TbKategori()
            for k in listModal:
                k.in_getkategori_adi(myreturnmodalListKategori.val)


        self.in_HeaderUi(qTableWidget)
        countColumn = len(self.header)
        countRow = len(listModal)
        insertcountRow = len(listModal) * 2
        qTableWidget.setRowCount(insertcountRow)

        qTableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        nexrow = 0
        for nrow in range(countRow):
            itemlist = listModal[nrow].itemListforUi(nrow)

            for ncol in range(countColumn):

                item = QtWidgets.QTableWidgetItem()

                itemncol =ncol
                if  ncol >=10:
                    itemncol= ncol+2
                item.setText(itemlist[itemncol])

                qTableWidget.setItem(nexrow,ncol, item)

            nexrow += 1
            showableRowList.append(nexrow)
            resimler = itemlist[ 11 ]
            resimListesi = list(resimler.split(","))
            if len(resimListesi) > 18:
                rescount = 18
            else:
                rescount = len(resimListesi)


            label = QLabel()
            pixmap = QPixmap(itemlist[ 10 ])
            scaledPix = pixmap.scaled(50, 50, Qt.KeepAspectRatio, transformMode=Qt.SmoothTransformation)
            label.setPixmap(scaledPix)
            label.setMargin(5)
            qTableWidget.setCellWidget(nexrow, 0, label)


            for i in range(rescount):

                label = QLabel()

                pixmap = QPixmap(resimListesi[ i ])
                scaledPix = pixmap.scaled(300,300, Qt.KeepAspectRatio, transformMode=Qt.SmoothTransformation)
                label.resize(250, 500)
                label.setPixmap(scaledPix)
                qTableWidget.setCellWidget(nexrow, i+1, label)
            qTableWidget.hideRow(nexrow)


            nexrow += 1

        qTableWidget.setProperty('sorgukimlik', listModal[0].sorgukimlik_id)
        qTableWidget.setProperty('showableRowList', showableRowList)
        qTableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        qTableWidget.resizeColumnsToContents()
        qTableWidget.resizeRowsToContents()












