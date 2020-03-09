import os
import sqlite3

from mydb.dbcore import TbNamesKategori, TbNamesPlayAppList, TbNamesSorgu
from mydb.dbmodals import ModalTbPlayAppList, ModalTbSorgu, ModalTbKategori, GetModal
from returnmodals.myReturn import MyReturn


class MyDb:
    def __init__(self):
        self.dbState = False
        path = os.path.dirname(os.path.abspath(__file__))
        dbName = os.path.join(path + "/", 'analizdb.sqlite')
        self.db = sqlite3.connect(dbName)
        self.cursor = self.db.cursor()
        self.cursor.execute(TbNamesKategori.tbCreate)
        self.cursor.execute(TbNamesSorgu.tbCreate)
        self.cursor.execute(TbNamesPlayAppList.tbCreate)
        self.dbState = True

    # GET
    # ALL
    # MyReturn.val = ListModal
    def main_getAll_TbSorgu(self) -> MyReturn:
        return self.getAll(TbNamesSorgu.tableName)

    # MyReturn.val = ListModal
    def main_getAll_TbKategori(self) -> MyReturn:
        return self.getAll(TbNamesKategori.tableName)

    # MyReturn.val = ListModal
    def main_getAll_TbPlayAppList(self) -> MyReturn:
        return self.getAll(TbNamesPlayAppList.tableName)

    # MyReturn.val = ModalOne
    def main_getOneByX_TbNamesSorgu(self, colName: str, colValue) -> MyReturn:
        return self.getOneByXe(TbNamesSorgu.tableName, colName, colValue)

    # MyReturn.val = ModalOne
    def main_getOneByX_TbKategori(self, colName: str, colValue) -> MyReturn:
        return self.getOneByXe(TbNamesKategori.tableName, colName, colValue)

    # myReturn.val = ListModal
    def main_getAllByX_TbPlayAppList(self, columName, columValue, orderBy = None) -> MyReturn:
        return self.getAllByXe(TbNamesPlayAppList.tableName, columName, columValue, orderBy)

    # myReturn.val = ListModal
    def main_getAllByLastDate_TbPlayAppList(self) -> MyReturn:
        rtnLastTbNamesSorgu = self.main_getOneByLastDate_TbNamesSorgu()

        if rtnLastTbNamesSorgu.isOK:
            return self.getAllByXe(TbNamesPlayAppList.tableName, TbNamesPlayAppList.sorgukimlik_id,rtnLastTbNamesSorgu.val.sorgukimlik)
        else:
            return rtnLastTbNamesSorgu

    # myReturn.val = OneModal
    def main_getOneByLastDate_TbNamesSorgu(self) -> MyReturn:
        return self.getOneByXLastDate(TbNamesSorgu.tableName)

    # INSERT
    # myReturn.val = lastrowid
    def main_insert_TbPlayAppList(self, modalTbPlayAppList: ModalTbPlayAppList) -> MyReturn:

        tableName = TbNamesPlayAppList.tableName
        colNameList = TbNamesPlayAppList.colNameList
        colValueList = [ modalTbPlayAppList.sorgukimlik_id,
                         modalTbPlayAppList.kategori_id,
                         modalTbPlayAppList.str_ad,
                         modalTbPlayAppList.str_gelistirici,
                         modalTbPlayAppList.str_boyut,
                         modalTbPlayAppList.str_icon,
                         modalTbPlayAppList.str_resimler,
                         modalTbPlayAppList.str_version,
                         modalTbPlayAppList.str_minandroid,
                         modalTbPlayAppList.float_puan,
                         modalTbPlayAppList.int_indirilme,
                         modalTbPlayAppList.str_yuklemetarihi,
                         modalTbPlayAppList.str_gunceltarih,
                         modalTbPlayAppList.int_fark_gun, modalTbPlayAppList.float_yil,
                         modalTbPlayAppList.int_gunluk_ort_indirme,
                         modalTbPlayAppList.int_siralamasi,
                         modalTbPlayAppList.str_link,
                         modalTbPlayAppList.str_ucret
                         ]

        myreturn_insert = self.insert(tableName, colNameList, colValueList)

        return myreturn_insert

    # myReturn.val = lastrowid
    def main_insert_TbSorgu(self, modalTbSorgu: ModalTbSorgu) -> MyReturn:

        tableName = TbNamesSorgu.tableName
        colNameList = TbNamesSorgu.colNameList
        colValueList = [ modalTbSorgu.sorgukimlik, modalTbSorgu.aranan, modalTbSorgu.ekparams, modalTbSorgu.sonucadet, modalTbSorgu.sorgutarihi ]

        myreturn_insert = self.insert(tableName, colNameList, colValueList)

        return myreturn_insert

    # myReturn.val = lastrowid
    def main_insert_TbKategori(self, modalTbKategori: ModalTbKategori) -> MyReturn:
        myReturn = MyReturn()
        myReturn.isOK = False
        myReturn.val = None

        if modalTbKategori.kategoriadi.strip() is None:
            myReturn.msg = "Hata: main_insertTbKategori()  'arananKategori' boş, Db ye girilmedi!"
            myReturn.isOK = False
            myReturn.val = None
        else:
            tableName = TbNamesKategori.tableName
            colName = TbNamesKategori.kategoriadi
            colNameList = TbNamesKategori.colNameList

            colValue = modalTbKategori.kategoriadi

            myreturn_getOneByXe = self.getOneByXe(tableName, colName, colValue)

            if myreturn_getOneByXe.isOK:
                myReturn.isOK = myreturn_getOneByXe.isOK
                myReturn.val = myreturn_getOneByXe.val.id
                myReturn.msg = myreturn_getOneByXe.msg
            else:
                myreturn_insert = self.insert(tableName, colNameList, [ colValue ])
                myReturn.isOK = myreturn_insert.isOK
                myReturn.val = myreturn_insert.val
                myReturn.msg = myreturn_insert.msg

        return myReturn

    # INOP
    # myReturn.val = lastrowid
    def insert(self, tableName: str, colNameList: list, colValueList_withoutId: list) -> MyReturn:
        self.dbConnect()
        myReturn = MyReturn()
        myReturn.isOK = False
        myReturn.val = None
        myReturn.msg = ''

        # print("----------------------------------")
        # print(" İnsert için Tablo ismi:" + str(tableName))
        # for i in colValueList_withoutId:
        #     print(str(i))
        #
        #
        # # colNameList id dahil yazılmalı
        # # colValueList id hariç yazılmalı
        #
        # tre = ","
        # ncols = tre.join(colNameList)

        cols = ''
        for i in colNameList:
            cols += '?,'
        qcols = cols.strip(",")

        # c.execute('''INSERT INTO students VALUES(1, 'Alex', 8)''')
        # sql = "INSERT INTO " + tableName + " ( " + ncols + " ) VALUES ( NULL ," + qcols + " );"
        # sql = "INSERT INTO {} ( {} ) VALUES ({});".format(tableName,ncols,qcols)


        val = colValueList_withoutId.insert(0, None)
        newval = tuple(colValueList_withoutId)

        sql = "INSERT INTO " + tableName + "  VALUES ( " + qcols + " );"

        try:
            self.cursor.execute(sql, newval)
            lastrowid = self.cursor.lastrowid
            if lastrowid is not None:
                myReturn.val = lastrowid
                myReturn.isOK = True
                myReturn.msg = "Son Eklenen id" + str(myReturn.val)
                self.db.commit()
            else:
                myReturn.isOK = False
                myReturn.msg = "Hata: insert() id {} tablosuna {} değerleri Eklenemedi".format(tableName,newval)
        except:
            myReturn.msg = "Hata: insert() Error Db: " + str(sqlite3.Error)
            myReturn.isOK = False
            myReturn.val = None
            return  myReturn

        return myReturn

    # myReturn.val = ListModal
    def getAllByXe(self, tableName: str, xcolName: str, xcolValue, orderBy = None) -> MyReturn:

        self.dbConnect()
        myReturn = MyReturn()
        myReturn.isOK = False
        myReturn.val = None

        if xcolValue is None:
            myReturn.isOK = False
            myReturn.msg = "Hata: getAllByXe(), Db den getirilemedi! {} is None".format(xcolValue)
        else:
            #sql = "SELECT * FROM " + tableName + " WHERE " + xcolName + " = '" + xcolValue + "';"
            # sql = "SELECT * FROM {} WHERE {} = {} ;".format(tableName, xcolName, xcolValue)
            # val = (xcolValue)
            # sql = "'SELECT * FROM {} WHERE {} = ? '".format(tableName, xcolName)


           # cursor.execute("SELECT * FROM tbPlayAppList WHERE id = "ID from application")

            val = (xcolValue,)
            # sql = """select * from """ + tableName + """ where """ + xcolName + """ = ?"""
            if orderBy is not None:
                orderby =" " + orderBy
            else:
                orderby = " order by id asc"

            sql = """select * from  """ + tableName + """ where """ + xcolName + """ = ? """ + orderby
            try:
                self.cursor.execute(sql,val)
                fetchallListTuple = self.cursor.fetchall()

                if len(fetchallListTuple) > 0:
                    # print(fetchallListTuple)
                    getListModal = GetModal.getModalList(tableName, fetchallListTuple)
                    # print(getListModal)
                    myReturn.isOK = True
                    myReturn.val = getListModal
                    myReturn.msg = "Veriler {} Tablosundan başarıyla çekildi. Çekilen adet: {} ".format(tableName, len(
                        fetchallListTuple))
                    # print(str(val))
                else:
                    myReturn.isOK = False
                    myReturn.msg = "{}  Tablosunda hiç veri yok!".format(tableName)
            except:
                myReturn.isOK = False
                myReturn.msg = "Hata: getAllByXe(), Db den getirilemedi! except " + str(sqlite3.Error)
        return myReturn

    def getAll(self, tableName: str):
        self.dbConnect()
        myReturn = MyReturn()
        myReturn.isOK = False
        myReturn.val = None

        sql = "SELECT * FROM " + tableName + ";"
        # sql = "SELECT * FROM {} ;".format(tableName)
        try:
            self.cursor.execute(sql)
            fetchallListTuple = self.cursor.fetchall()
            if len(fetchallListTuple) > 0:
                getListModal = GetModal.getModalList(tableName, fetchallListTuple)
                myReturn.isOK = True
                myReturn.val = getListModal
                myReturn.msg = "Veriler {} Tablosundan başarıyla çekildi. Çekilen adet: {} ".format(tableName, len(
                    fetchallListTuple))
            else:
                myReturn.isOK = False
                myReturn.msg = str(tableName) + " Tablosunda kayıtlı hiç veri yok! "
        except:
            myReturn.isOK = False
            myReturn.msg = "Hata: getAll(), Db den getirilemedi! except" + str(sqlite3.Error)

        return myReturn

    def getCount(self, tableName: str):
        self.dbConnect()
        myReturn = MyReturn()
        myReturn.isOK = False
        myReturn.val = None
        sql = "SELECT count(*) FROM {} ;".format(tableName)
        try:
            self.cursor.execute(sql)
            fetchallListTuple = self.cursor.fetchall()
            if len(fetchallListTuple) > 0:
                myReturn.isOK = True
                myReturn.val = len(fetchallListTuple)
                myReturn.msg = "Veriler {} Tablosun  adet: {} veri var ".format(tableName, len(fetchallListTuple))
            else:
                myReturn.isOK = False
                myReturn.msg =  str(tableName) + "Tablosunda hiç veri yok! "
        except:
            myReturn.isOK = False
            myReturn.msg = "Hata: getAll(), Db den seçilemedi! except" + str(sqlite3.Error)

        return myReturn

    # MyReturn.val = oneModal
    def getOneByXLastDate(self, tableName: str):
        self.dbConnect()
        myReturn = MyReturn()
        myReturn.isOK = False
        myReturn.val = None


        # sql = "SELECT * FROM  " + tableName + " ORDER BY  " + colName + " DESC LIMIT 1 "
        sql = "SELECT * FROM  {} ORDER BY  id DESC LIMIT 1 ".format(tableName)

        try:
            self.cursor.execute(sql)
            fetchoneTuple = self.cursor.fetchone()
            if fetchoneTuple is not None:
                oneModal = GetModal.getModalOne(tableName, fetchoneTuple)
                myReturn.isOK = True
                myReturn.val = oneModal
                myReturn.msg = "Veriler {} Tablosundan başarıyla çekildi. Çekilen veriler: {} ".format(tableName,
                                                                                                       fetchoneTuple)
            else:
                myReturn.isOK = False
                myReturn.msg = str(tableName) + " Tablosunda hiç veri yok! "
        except:
            myReturn.isOK = False
            myReturn.msg = "Hata: getOneByXLastDate(), Db den getirilemedi! except" + str(sqlite3.Error)

        return myReturn

    # MyReturn.val = ModalOne
    def getOneByXe(self, tableName: str, xcolName: str, xcolValue: str) -> MyReturn:
        self.dbConnect()
        myReturn = MyReturn()
        myReturn.isOK = False
        myReturn.val = None

        if xcolValue is None:
            myReturn.isOK = False
            myReturn.msg = "Hata: getOneByXe(), Db den getirilemedi! " + str(xcolValue) + " is None"
        else:
            sql = "SELECT * FROM " + tableName + " WHERE " + xcolName + " = '" + xcolValue + "';"
            # sql = "SELECT * FROM {} WHERE {} = {} ;".format(tableName, xcolName, xcolValue)

            try:
                self.cursor.execute(sql)
                fetchoneTuple = self.cursor.fetchone()
                if fetchoneTuple is not None:
                    OneModal = GetModal.getModalOne(tableName, fetchoneTuple)
                    myReturn.isOK = True
                    myReturn.val = OneModal
                    myReturn.msg = "Veriler {} Tablosundan başarıyla çekildi. Çekilen veriler: {} ".format(tableName,
                                                                                                           fetchoneTuple)
                else:
                    myReturn.isOK = False
                    myReturn.msg = str(tableName) + " Tablosunda hiç veri yok! "
            except:
                myReturn.isOK = False
                myReturn.msg = "Hata: getOneByXe(), Db den getirilemedi! except" + str(sqlite3.Error)
        return myReturn

    def deleteAllByXe(self, tableName: str, xcolName: str, xcolValue) -> MyReturn:

        self.dbConnect()
        myReturn = MyReturn()
        myReturn.isOK = False
        myReturn.val = None

        if tableName is None or xcolName is None or xcolValue is None:
            myReturn.isOK = False
            myReturn.msg = "Hata: deleteAllByXe(), {} tablosundan, {} {} olan değerlere sahip satırlar silinemedi! tableName is None or xcolName is None or xcolValue is None".format(
                tableName, xcolName, xcolValue)
        else:
            val = (xcolValue,)
            sql = """DELETE FROM  """ + tableName + """ WHERE """ + xcolName + """ = ? """
            try:
                self.cursor.execute(sql, val)
                self.db.commit()
                myReturn.isOK = True
                myReturn.val = None
                myReturn.msg = "Başarılı bir şekilde {} tablosundan, {} {} olan değerlere sahip satırlar silindi ".format(
                    tableName, xcolName, xcolValue)
            except:
                myReturn.isOK = False
                myReturn.msg = "Hata: deleteAllByXe(), {} tablosundan, {} {} olan değerlere sahip satırlar silinemedi! sq: {}".format(
                    tableName, xcolName, xcolValue, sqlite3.Error)

        return myReturn


    def deleteAllByTb(self, tableName: str) -> MyReturn:

        self.dbConnect()
        myReturn = MyReturn()
        myReturn.isOK = False
        myReturn.val = None

        if tableName is None:
            myReturn.isOK = False
            myReturn.msg = "Hata: deleteAllByTb(), {} tablosundan veriler silinemedi! tableName is None ".format(tableName)
        else:
            # val = (xcolValue,)
            sql = """DELETE FROM  """ + tableName
            try:
                self.cursor.execute(sql)
                self.db.commit()
                myReturn.isOK = True
                myReturn.val =  None
                myReturn.msg = "Başarılı bir şekilde {} tablosundantüm veriler silindi".format(tableName)
            except:
                myReturn.isOK = False
                myReturn.msg = "Hata: deleteAllByXe(), {} tablosundan veriler silinemedi! ! sq: {}".format(tableName,sqlite3.Error)

        return myReturn

    def dbConnect(self):
        if not self.dbState:
            try:
                path = os.path.dirname(os.path.abspath(__file__))
                dbName = os.path.join(path + "/dbfolder", 'analizdb.sqlite')
                self.db = sqlite3.connect(dbName)
                self.cursor = self.db.cursor()
                self.dbState = True
            except:
                print("Error Db connection: " + str(sqlite3.Error))

    def dbClose(self):
        if self.dbState:
            self.db.close()
            self.dbState = False

    # USING:
    # rtngetAll = getALLByXexactly(c, TbNamesKategori.tableName, TbNamesKategori.colNameList, TbNamesKategori.id, '8') yada
    # rtngetAll = getAll(c, TbNamesKategori.tableName, TbNamesKategori.colNameList )
    # count = rtngetAll['count']
    # dataListdict = rtngetAll['dataListdict']
    # for rowtuplee in dataListdict:
    #     for colName in TbNamesKategori.TbNamesKategoriList:
    #         colName = rowtuplee[colName]
    # print(dataListdict)

# FOR TEST :
#

# def printx( ListTuple):
#     for i in  ListTuple:
#         print(i)
#


# # alTbKategori =dbObj.main_getOneByX_TbKategori(TbNamesKategori.id,"1")
# alTbPlayAppList = dbObj.main_getAllByLastDate_TbPlayAppList()
# print(alTbPlayAppList.val)
#
# printx(alTbPlayAppList.val)

# alTbKategori.xprint()
# for i in alTbKategori.val:
#     i.id
#     i.kategoriadi
#
#     kat ="id: {}, kategoriadi{}".format(i.id, i.kategoriadi)
#     print(kat)


#
# for i in alTbPlayAppList.val:
#     i.id
#     i.str_ad
#
#     kat = "id: {}, kategoriadi{}".format(i.id, i.str_ad)
#     print(kat)
#
#

