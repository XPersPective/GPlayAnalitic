class TbNamesKategori:
    id = 'id'
    kategoriadi = 'Kategori'

    tableName = "tbKategoriler"
    colNameList = [id, kategoriadi]

    tbCreate = """  CREATE TABLE IF NOT EXISTS """ + tableName + """ (
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        """ + kategoriadi + """ TEXT  NULL ); """


class TbNamesSorgu:
    id = 'id'
    sorgukimlik = 'Sorgu_Kimlik'
    aranan = 'Aranan'
    ekparams = 'Ek_Params'
    sonucadet = 'Sonuc'
    sorgutarihi = 'Sorgu_Tarihi'

    tableName = "tbSorgu"
    colNameList = [ id, sorgukimlik, aranan, ekparams, sonucadet, sorgutarihi ]

    tbCreate = """  CREATE TABLE IF NOT EXISTS """ + tableName + """ (
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        """ + sorgukimlik + """ TEXT NOT NULL,
                                        """ + aranan + """ TEXT NOT NULL,
                                        """ + ekparams + """ TEXT NULL,
                                        """ + sonucadet + """ INTEGER NULL,
                                        """ + sorgutarihi + """ TEXT NOT NULL
                                    ); """



class TbNamesPlayAppList:
    id = 'id'
    sorgukimlik_id = 'sorgukimlik_id'
    kategori_id = 'kategori_id'
    str_ad = 'Ad'
    str_gelistirici = 'Gelistirici'
    str_boyut = 'Boyut'
    str_icon = 'Icon'
    str_resimler = 'Resimler'  # duzelt
    str_version = 'Versiyon'
    str_minandroid = 'Min_And'
    float_puan = 'Puan'
    int_indirilme = 'Toplam_Indirilme'
    str_yuklemetarihi = 'Cikis_Tarihi'
    str_gunceltarih = 'Guncellenme_Tarihi'
    int_fark_gun = 'Kac_Gunluk'
    float_yil = 'Kac_Yillik'
    int_gunluk_ort_indirme = 'Gunluk_Indirme'
    int_siralamasi = 'Siralamasi'
    str_link = 'GPlay_Adresi'
    str_ucret = 'Ucret_Durumu'

    tableName = "tbPlayAppList"
    colNameList = [ id, sorgukimlik_id, kategori_id, str_ad, str_gelistirici, str_boyut, str_icon, str_resimler,
                    str_version, str_minandroid, float_puan, int_indirilme, str_yuklemetarihi,
                    str_gunceltarih, int_fark_gun, float_yil, int_gunluk_ort_indirme, int_siralamasi, str_link,
                    str_ucret ]
    no = ''
    colNamesforsort = [ no, str_ad, kategori_id, str_yuklemetarihi, int_indirilme, int_gunluk_ort_indirme, int_fark_gun,
              float_yil, float_puan, int_siralamasi, str_ucret, str_boyut, str_version, str_minandroid,
              str_gelistirici, str_gunceltarih, str_link, sorgukimlik_id, id ]

    tbCreate = """  CREATE TABLE IF NOT EXISTS """ + tableName + """ (
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        """ + sorgukimlik_id + """ TEXT NOT NULL,
                                        """ + kategori_id + """  INTEGER NULL,
                                        """ + str_ad + """  TEXT NULL,
                                        """ + str_gelistirici + """  TEXT  NULL,
                                        """ + str_boyut + """ TEXT  NULL,
                                        """ + str_icon + """ TEXT  NULL,
                                        """ + str_resimler + """  TEXT  NULL,
                                        """ + str_version + """  TEXT  NULL,
                                        """ + str_minandroid + """  TEXT  NULL,
                                        """ + float_puan + """  REAL  NULL,
                                        """ + int_indirilme + """  INTEGER  NULL,
                                        """ + str_yuklemetarihi + """ TEXT NULL,
                                        """ + str_gunceltarih + """  TEXT NULL,
                                        """ + int_fark_gun + """   INTEGER NULL,
                                        """ + float_yil + """  REAL NULL,
                                        """ + int_gunluk_ort_indirme + """   INTEGER NULL,
                                        """ + int_siralamasi + """   INTEGER NULL,
                                        """ + str_link + """  TEXT  NULL,
                                        """ + str_ucret + """  TEXT  NULL
                                    ); """
