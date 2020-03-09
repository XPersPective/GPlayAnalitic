from mydb.dbcore import TbNamesKategori, TbNamesPlayAppList, TbNamesSorgu


class ModalTbPlayAppList:

    def __init__(self, sorgukimlik_id, kategori_id, str_ad, str_gelistirici, str_boyut, str_icon, str_resimler,
                 str_version, str_minandroid, float_puan, int_indirilme, str_yuklemetarihi, str_gunceltarih,
                 int_fark_gun, float_yil, int_gunluk_ort_indirme, int_siralamasi, str_link, str_ucret, id=None):
        if id is not None:
            self.id = id
        self.sorgukimlik_id = sorgukimlik_id
        self.kategori_id = kategori_id
        self.str_ad = str_ad
        self.str_gelistirici = str_gelistirici
        self.str_boyut = str_boyut
        self.str_icon = str_icon
        self.str_resimler = str_resimler
        self.str_version = str_version
        self.str_minandroid = str_minandroid
        self.float_puan = float_puan
        self.int_indirilme = int_indirilme
        self.str_yuklemetarihi = str_yuklemetarihi
        self.str_gunceltarih = str_gunceltarih
        self.int_fark_gun = int_fark_gun
        self.float_yil = float_yil
        self.int_gunluk_ort_indirme = int_gunluk_ort_indirme
        self.int_siralamasi = int_siralamasi
        self.str_link = str_link
        self.str_ucret = str_ucret
        self.kategori_adi = None


    def in_getkategori_adi(self,listModalKategori:list):
        for i in listModalKategori:
            if i.id == self.kategori_id:
                self.kategori_adi = i.kategoriadi


    def itemListforUi(self, no:int) -> list:
        no += 1
        returnList = []
        items = [ no, self.str_ad, self.kategori_adi, self.str_yuklemetarihi, self.int_indirilme, self.int_gunluk_ort_indirme, self.int_fark_gun,
                   self.float_yil, self.float_puan, self.int_siralamasi, self.str_icon, self.str_resimler, self.str_ucret, self.str_boyut, self.str_version, self.str_minandroid,
                   self.str_gelistirici, self.str_gunceltarih, self.str_link, self.sorgukimlik_id, self.id ]
        for i in items:
            returnList.append(str(i))
        return returnList


class ModalTbKategori:
    def __init__(self, kategoriadi: str, id=None):
        if id is not None:
            self.id = id
        self.kategoriadi = kategoriadi

    def itemListforUi(self, no:int) -> list:
        returnList = []
        no += 1
        items = [ no, self.kategoriadi]
        for i in items:
            returnList.append(str(i))
        return returnList

class ModalTbSorgu:
    def __init__(self, sorgukimlik, aranan, ekparams, sonucadet, sorgutarihi, id=None):
        if id is not None:
            self.id = id
        self.sorgukimlik = sorgukimlik
        self.aranan = aranan
        self.ekparams = ekparams
        self.sonucadet = sonucadet
        self.sorgutarihi = sorgutarihi



    def itemListforUi(self, no:int) -> list:
        returnList = []
        no += 1
        items = [ no, self.aranan, self.sonucadet, self.sorgutarihi, self.ekparams, self.sorgukimlik ]
        for i in items:
            returnList.append(str(i))
        return returnList


class GetModal:
    def getModalList(tableName: str, fetchallListTuple) -> list:
        returnModal = []

        for tuplee in fetchallListTuple:

            returnModal.append(GetModal.getModalOne(tableName, tuplee))
        return  returnModal


    def getModalOne(tableName: str, tuplee):

        if tableName == TbNamesKategori.tableName:
            tempdict = {}
            i = 0
            for ix in TbNamesKategori.colNameList:
                tempdict[ ix ] = tuplee[ i ]
                i += 1

            modal = ModalTbKategori(
                tempdict[ 'Kategori' ],
                tempdict[ 'id' ]
            )

            return modal



        if tableName == TbNamesPlayAppList.tableName:
            tempdict = {}
            i = 0
            for ix in TbNamesPlayAppList.colNameList:
                tempdict[ ix ] = tuplee[ i ]
                i += 1

            modal = ModalTbPlayAppList(
                tempdict[ 'sorgukimlik_id' ],
                tempdict[ 'kategori_id' ],
                tempdict[ 'Ad' ],
                tempdict[ 'Gelistirici' ],
                tempdict[ 'Boyut' ],
                tempdict[ 'Icon' ],
                tempdict[ 'Resimler' ],
                tempdict[ 'Versiyon' ],
                tempdict[ 'Min_And' ],
                tempdict[ 'Puan' ],
                tempdict[ 'Toplam_Indirilme' ],
                tempdict[ 'Cikis_Tarihi' ],
                tempdict[ 'Guncellenme_Tarihi' ],
                tempdict[ 'Kac_Gunluk' ],
                tempdict[ 'Kac_Yillik' ],
                tempdict[ 'Gunluk_Indirme' ],
                tempdict[ 'Siralamasi' ],
                tempdict[ 'GPlay_Adresi' ],
                tempdict[ 'Ucret_Durumu' ],
                tempdict[ 'id' ]
            )

            return modal

        if tableName == TbNamesSorgu.tableName:
            tempdict = {}
            i = 0
            for ix in TbNamesSorgu.colNameList:
                tempdict[ ix ] = tuplee[ i ]
                i += 1

            modal = ModalTbSorgu(
                tempdict[ 'Sorgu_Kimlik' ],
                tempdict[ 'Aranan' ],
                tempdict[ 'Ek_Params' ],
                tempdict[ 'Sonuc' ],
                tempdict[ 'Sorgu_Tarihi' ],
                tempdict[ 'id' ]
            )

            return modal