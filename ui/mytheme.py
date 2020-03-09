from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QSizePolicy, QVBoxLayout, QDialogButtonBox, QDialog


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(580, 407)
        MainWindow.setStyleSheet("""
background-color: rgb(255, 255, 255);
color:#5d5d5d;
font:  "Tahoma";
font-size:14px;

 """)
        self.mytema_CENTRALWIDGET = QtWidgets.QWidget(MainWindow)
        self.mytema_CENTRALWIDGET.setStyleSheet("background-color: rgb(247, 247, 247);")
        self.mytema_CENTRALWIDGET.setObjectName("mytema_CENTRALWIDGET")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.mytema_CENTRALWIDGET)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        # self.mytema_text_appbaslik = QtWidgets.QLabel(self.mytema_CENTRALWIDGET)
        # font = QtGui.QFont()
        # font.setFamily("Segoe UI Semibold")
        # font.setPointSize(16)
        # font.setBold(False)
        # font.setItalic(True)
        # font.setUnderline(False)
        # font.setWeight(50)
        # font.setKerning(True)
        # self.mytema_text_appbaslik.setFont(font)
        # self.mytema_text_appbaslik.setStyleSheet("color: rgb(85, 170, 0);")
        # self.mytema_text_appbaslik.setAlignment(QtCore.Qt.AlignCenter)
        # self.mytema_text_appbaslik.setObjectName("mytema_text_appbaslik")
        # self.verticalLayout_10.addWidget(self.mytema_text_appbaslik)
        self.mytema_TAB = QtWidgets.QTabWidget(self.mytema_CENTRALWIDGET)
        self.mytema_TAB.setStyleSheet("""
color:#5d5d5d;
font:  "Tahoma";
font-size:12px;""")
        self.mytema_TAB.setObjectName("mytema_TAB")
        self.mytema_TABara = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.mytema_TABara.setFont(font)
        self.mytema_TABara.setStyleSheet("")
        self.mytema_TABara.setObjectName("mytema_TABara")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.mytema_TABara)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0,10,0,0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.mytema_TABara_lineEditAra = QtWidgets.QLineEdit(self.mytema_TABara)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.mytema_TABara_lineEditAra.setFont(font)
        self.mytema_TABara_lineEditAra.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.mytema_TABara_lineEditAra.setStyleSheet(""" 
background-color: rgb(255, 255, 255);
color:#5d5d5d;
font:  "Tahoma";
font-size:14px;
padding:3px 17px;
border-radius: 10px;""")
        self.mytema_TABara_lineEditAra.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.mytema_TABara_lineEditAra.setObjectName("mytema_TABara_lineEditAra")
        self.horizontalLayout.addWidget(self.mytema_TABara_lineEditAra)
        self.mytema_TABara_pushButtonara = QtWidgets.QPushButton(self.mytema_TABara)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.mytema_TABara_pushButtonara.setFont(font)
        self.mytema_TABara_pushButtonara.setStyleSheet(""" QPushButton { 
font:  "Tahoma";
font-size:15px;
padding:3px 19px;
border-radius: 10px;
background-color:#0087ca;
color:#ffffff;}

QPushButton:pressed {
background-color:#00aaff;
}
QPushButton:disabled {
 background-color:#7e94aa;
color:#d6d6d6;
}""")
        self.mytema_TABara_pushButtonara.setObjectName("mytema_TABara_pushButtonara")
        self.horizontalLayout.addWidget(self.mytema_TABara_pushButtonara)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.mytema_TABara_WIDGETsonuc = QtWidgets.QWidget(self.mytema_TABara)
        self.mytema_TABara_WIDGETsonuc.setEnabled(True)
        self.mytema_TABara_WIDGETsonuc.setObjectName("mytema_TABara_WIDGETsonuc")
        self.mytema_TABara_WIDGETsonuc_2 = QtWidgets.QVBoxLayout(self.mytema_TABara_WIDGETsonuc)
        self.mytema_TABara_WIDGETsonuc_2.setObjectName("mytema_TABara_WIDGETsonuc_2")
        self.mytema_TABara_labelbaslik = QtWidgets.QLabel(self.mytema_TABara_WIDGETsonuc)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.mytema_TABara_labelbaslik.setFont(font)
        self.mytema_TABara_labelbaslik.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.mytema_TABara_labelbaslik.setStyleSheet("""
background-color: rgb(255, 255, 255);
padding:3px 17px;
border-radius: 10px;""")
        self.mytema_TABara_labelbaslik.setText("")
        self.mytema_TABara_labelbaslik.setAlignment(QtCore.Qt.AlignCenter)
        self.mytema_TABara_labelbaslik.setObjectName("mytema_TABara_labelbaslik")
        self.mytema_TABara_WIDGETsonuc_2.addWidget(self.mytema_TABara_labelbaslik)
        self.mytema_TABara_PROGRESVlayout = QtWidgets.QVBoxLayout()
        self.mytema_TABara_PROGRESVlayout.setContentsMargins(0, 0, 0, 0)
        self.mytema_TABara_PROGRESVlayout.setObjectName("mytema_TABara_PROGRESVlayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.mytema_TABara_PROGRESprogressBar = QtWidgets.QProgressBar(self.mytema_TABara_WIDGETsonuc)
        self.mytema_TABara_PROGRESprogressBar.setStyleSheet(" ")
        self.mytema_TABara_PROGRESprogressBar.setProperty("value", 0)
        self.mytema_TABara_PROGRESprogressBar.setObjectName("mytema_TABara_PROGRESprogressBar")
        self.horizontalLayout_4.addWidget(self.mytema_TABara_PROGRESprogressBar)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label = QtWidgets.QLabel(self.mytema_TABara_WIDGETsonuc)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_6.addWidget(self.label)
        self.mytema_TABara_PROGRESradioButton = QtWidgets.QRadioButton(self.mytema_TABara_WIDGETsonuc)
        self.mytema_TABara_PROGRESradioButton.setText("")
        self.mytema_TABara_PROGRESradioButton.setObjectName("mytema_TABara_PROGRESradioButton")
        self.horizontalLayout_6.addWidget(self.mytema_TABara_PROGRESradioButton)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_6)
        self.mytema_TABara_PROGRESVlayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_5.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.mytema_TABara_PROGRESpushButtonaraiptal = QtWidgets.QPushButton(self.mytema_TABara_WIDGETsonuc)
        self.mytema_TABara_PROGRESpushButtonaraiptal.setStyleSheet(
"""QPushButton {

 background-color:#aa0000;
color:#ffffff;
 
font-size:13px;
padding:6px 27px;
border-radius: 13px;
   }

QPushButton:pressed {
background-color:#e70000;
}
QPushButton:disabled {
background-color:#a43837;
color:#d8d8d8;

}""")
        self.mytema_TABara_PROGRESpushButtonaraiptal.setObjectName("mytema_TABara_PROGRESpushButtonaraiptal")
        self.horizontalLayout_5.addWidget(self.mytema_TABara_PROGRESpushButtonaraiptal)
        # ---------------------
        self.mytema_TABara_tablo_esnet = QtWidgets.QPushButton(self.mytema_TABara_WIDGETsonuc)
        self.mytema_TABara_tablo_esnet.setText("Genişlet")
        self.mytema_TABara_tablo_esnet.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Fixed)
        self.mytema_TABara_tablo_esnet.setStyleSheet(
"""QPushButton {background-color:#00aa00;
padding:0px;
margin:0px;
color:#ffffff;
border-top-left-radius:9px;
border-top-right-radius:9px;
border:1px solid #dcdcdc;
background-color:#ededed;
color:#777777;
font-size:12px;
font-weight:normal;
font-style:normal;
width:50px;
}

QPushButton:pressed {
background-color:#dfdfdf;
}""")
        self.horizontalLayout_5.addWidget( self.mytema_TABara_tablo_esnet)
        # ------------------------------------------------
        self.mytema_TABara_PROGRESVlayout.addLayout(self.horizontalLayout_5)
        self.mytema_TABara_WIDGETsonuc_2.addLayout(self.mytema_TABara_PROGRESVlayout)
        self.mytema_TABara_tablo = QtWidgets.QTableWidget(self.mytema_TABara_WIDGETsonuc)

        self.mytema_TABara_tablo.setStyleSheet("""
        QTableWidget
        {
         color:black;
         border-color: #eaeaea;
border-width: 1px; 
border-style: solid;

}
        
        QScrollBar {
 background-color: #eaeaea;
 border-color: #eaeaea;
border-width: 1px; 
border-style: solid;
 
}


QScrollBar::handle {
border-color:#dedede;
background-color: #dedede;
border-width: 1px; 
border-style: solid;
}



             
""")
        self.mytema_TABara_tablo.setObjectName("mytema_TABara_tablo")
        self.mytema_TABara_tablo.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        # self.mytema_TABara_tablo.setColumnCount(0)
        # self.mytema_TABara_tablo.setRowCount(0)
        self.mytema_TABara_WIDGETsonuc_2.addWidget(self.mytema_TABara_tablo)


        self.verticalLayout.addWidget(self.mytema_TABara_WIDGETsonuc)

        spacerItem = QtWidgets.QSpacerItem(0,0,  QSizePolicy.Expanding,  QSizePolicy.Maximum)

        self.verticalLayout.addSpacerItem(spacerItem)

        self.mytema_TAB.addTab(self.mytema_TABara, "")
        self.mytema_TABgecmis = QtWidgets.QWidget()
        self.mytema_TABgecmis.setObjectName("mytema_TABgecmis")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.mytema_TABgecmis)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.mytema_TABgecmis_labelbaslik = QtWidgets.QLabel(self.mytema_TABgecmis)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.mytema_TABgecmis_labelbaslik.setFont(font)
        self.mytema_TABgecmis_labelbaslik.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.mytema_TABgecmis_labelbaslik.setStyleSheet(

            """
            background-color: rgb(255, 255, 255);
            padding:3px 17px;
            border-radius: 10px;"""
        )
        self.mytema_TABgecmis_labelbaslik.setFrameShadow(QtWidgets.QFrame.Plain)
        self.mytema_TABgecmis_labelbaslik.setAlignment(QtCore.Qt.AlignCenter)
        self.mytema_TABgecmis_labelbaslik.setObjectName("mytema_TABgecmis_labelbaslik")
        self.verticalLayout_3.addWidget(self.mytema_TABgecmis_labelbaslik)
        #
        # # mytema_TABgecmis_tablo_deleteOneTbSorgu_button---------------------------Basladı

        self.mytema_TABgecmis_tablo_delete_horizontalWidget = QtWidgets.QWidget(self.mytema_TABgecmis)
        self.mytema_TABgecmis_tablo_delete_horizontalWidget.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.mytema_TABgecmis_tablo_delete_horizontalWidget.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
        self.mytema_TABgecmis_tablo_delete_horizontalWidget.setObjectName("mytema_TABgecmis_tablo_delete_horizontalWidget")

        self.mytema_TABgecmis_tablo_delete_horizontalWidget_2 = QtWidgets.QHBoxLayout( self.mytema_TABgecmis_tablo_delete_horizontalWidget)
        self.mytema_TABgecmis_tablo_delete_horizontalWidget_2.setObjectName( "mytema_TABgecmis_tablo_delete_horizontalWidget_2")

        self.mytema_TABgecmis_tablo_deleteAllTbSorgu_button = QtWidgets.QPushButton( self.mytema_TABgecmis_tablo_delete_horizontalWidget)
        self.mytema_TABgecmis_tablo_deleteAllTbSorgu_button.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        # font.setWeight(50)
        self.mytema_TABgecmis_tablo_deleteAllTbSorgu_button.setContentsMargins(0,0,0,0)
        self.mytema_TABgecmis_tablo_deleteAllTbSorgu_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.mytema_TABgecmis_tablo_deleteAllTbSorgu_button.setStyleSheet("QPushButton {background-color:#00aa00;\n"
                                                                          " padding:2px;\n"
                                                                          "            padding-left:5px;\n"
                                                                          "            padding-right:5px;\n"
                                                                          "            margin:0px;\n"
                                                                          "            color:#ffffff;\n"
                                                                          "            border-top-left-radius:9px;\n"
                                                                          "            border-top-right-radius:9px;\n"
                                                                          "            border:1px solid #dcdcdc;\n"
                                                                          "            background-color:#ededed;\n"
                                                                          "            color:#777777;\n"
                                                                          "            font-size:9px;\n"
                                                                          "            font-weight:normal;\n"
                                                                          "            font-style:normal;\n"
                                                                          " \n"
                                                                          "            }\n"
                                                                          "\n"
                                                                          "            QPushButton:pressed {\n"
                                                                          "            background-color:#dfdfdf;\n"
                                                                          "            }")
        self.mytema_TABgecmis_tablo_deleteAllTbSorgu_button.setObjectName("mytema_TABgecmis_tablo_deleteAllTbSorgu_button")

        self.mytema_TABgecmis_tablo_delete_horizontalWidget_2.addWidget(self.mytema_TABgecmis_tablo_deleteAllTbSorgu_button)


        self.mytema_TABgecmis_tablo_deleteOneTbSorgu_button = QtWidgets.QPushButton(self.mytema_TABgecmis_tablo_delete_horizontalWidget)
        self.mytema_TABgecmis_tablo_deleteOneTbSorgu_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        self.mytema_TABgecmis_tablo_deleteOneTbSorgu_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.mytema_TABgecmis_tablo_deleteOneTbSorgu_button.setStyleSheet("QPushButton {background-color:#00aa00;\n"
                                                                          " padding:2px;\n"
                                                                        "            margin-right:5px;\n"
                                                                          "            padding-left:5px;\n"
                                                                          "            padding-right:5px;\n"
                                                                          "            margin:0px;\n"
                                                                          "            color:#ffffff;\n"
                                                                          "            border-top-left-radius:9px;\n"
                                                                          "            border-top-right-radius:9px;\n"
                                                                          "            border:1px solid #dcdcdc;\n"
                                                                          "            background-color:#ededed;\n"
                                                                          "            color:#777777;\n"
                                                                          "            font-size:9px;\n"
                                                                          "            font-weight:normal;\n"
                                                                          "            font-style:normal;\n"
                                                                          " \n"
                                                                          "            }\n"
                                                                          "\n"
                                                                          "            QPushButton:pressed {\n"
                                                                          "            background-color:#dfdfdf;\n"
                                                                          "            }")
        self.mytema_TABgecmis_tablo_deleteOneTbSorgu_button.setFlat(False)
        self.mytema_TABgecmis_tablo_deleteOneTbSorgu_button.setObjectName("mytema_TABgecmis_tablo_deleteOneTbSorgu_button")

        self.mytema_TABgecmis_tablo_delete_horizontalWidget_2.addWidget(self.mytema_TABgecmis_tablo_deleteOneTbSorgu_button)

        spacerItem = QtWidgets.QSpacerItem(197, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.mytema_TABgecmis_tablo_delete_horizontalWidget_2.addItem(spacerItem)

        # # mytema_TABgecmis_tablo_deleteOneTbSorgu_button---------------------------Bitti

        self.mytema_TABgecmis_tablo = QtWidgets.QTableWidget(self.mytema_TABgecmis)
        font = QtGui.QFont()
        font.setPointSize(9)
        # font.setBold(True)
        # font.setWeight(75)
        self.mytema_TABgecmis_tablo.setFont(font)
        self.mytema_TABgecmis_tablo.setObjectName("mytema_TABgecmis_tablo")
        self.mytema_TABgecmis_tablo.setStyleSheet("""   
        QTableWidget{
        border-color: #eaeaea;
        border-width: 1px;
        border-style: solid;
        }
        """)


        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setContentsMargins(0, 10, 0, 0)
        self.mytema_TABgecmis_tablo_delete_horizontalWidget_2.setSpacing(3)
        self.mytema_TABgecmis_tablo_delete_horizontalWidget_2.setContentsMargins(0, 13, 16, 0)


        self.verticalLayout_3.addWidget(self.mytema_TABgecmis_tablo_delete_horizontalWidget)
        self.verticalLayout_3.addWidget(self.mytema_TABgecmis_tablo)

        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.mytema_TAB.addTab(self.mytema_TABgecmis, "")
        self.verticalLayout_10.addWidget(self.mytema_TAB)

        MainWindow.setCentralWidget(self.mytema_CENTRALWIDGET)

        self.retranslateUi(MainWindow)
        self.mytema_TAB.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "🅖🅟🅛🅐🅨 🅐🅝🅐🅛🅘🅣🅘🅒 V1.0 :: flutterdersleri.com"))
        # self.mytema_text_appbaslik.setText(_translate("MainWindow", "--- Play Analiz ---"))
        self.mytema_TABara_lineEditAra.setPlaceholderText(_translate("MainWindow", "ara"))
        self.mytema_TABara_pushButtonara.setText(_translate("MainWindow", "ara"))
        # self.label.setText(_translate("MainWindow", "Arama:"))
        self.label.setText(_translate("MainWindow", "🅖🅟🅛🅐🅨 🅐🅝🅐🅛🅘🅣🅘🅒 V1.0 :: flutterdersleri.com"))
        self.mytema_TABara_PROGRESpushButtonaraiptal.setText(_translate("MainWindow", "aramayi iptal et"))
        self.mytema_TAB.setTabText(self.mytema_TAB.indexOf(self.mytema_TABara), _translate("MainWindow", "Sorgu Dökümü"))
        self.mytema_TABgecmis_labelbaslik.setText(_translate("MainWindow", "Tüm Sorgular"))
        self.mytema_TAB.setTabText(self.mytema_TAB.indexOf(self.mytema_TABgecmis), _translate("MainWindow", "Geçmiş Sorgular"))

        self.mytema_TABgecmis_tablo_deleteAllTbSorgu_button.setText(_translate("MainWindow", "Tümünü Sil"))
        self.mytema_TABgecmis_tablo_deleteOneTbSorgu_button.setText(_translate("MainWindow", "Seçileni Sil"))



class CustomDialog(QDialog):

    def __init__(self,mytitle, mytext, *args, **kwargs):
        super(CustomDialog, self).__init__(*args, **kwargs)

        self.setWindowTitle(mytitle)
        self.mylabelText = QtWidgets.QLabel()
        self.mylabelText.setText(mytext)

        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.mylabelText)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)