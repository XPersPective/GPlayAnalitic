import os
import shutil
import time
import uuid
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

from gplay.SearchSpiders import SearchSpiders
from mydb.dbcore import TbNamesSorgu, TbNamesPlayAppList
from mydb.dbmodals import ModalTbSorgu, ModalTbPlayAppList
from mydb.mydb import MyDb
from returnmodals.myReturn import MyReturn
from returnmodals.optracking import OpTracking


# if self.isCancel:
#     self.mainMyReturn.opTracking.signalTrackingemit()
#     return
# else:
#     self.mainMyReturn.opTracking.signalTrackingemit()

class GooglePlaySearch:
    def __init__(self):
        self.mainMyReturn = MyReturn(OpTracking())
        self.browser = None
        self.mydb = None
        self.isCancel = False
        self.sorgukimlik = None


    def finish(self):
        if self.browser is not None:
            # PROCNAME = "geckodriver"  # or chromedriver or IEDriverServer
            # for proc in psutil.process_iter():
            #     # check whether the process name matches
            #     if proc.name() == PROCNAME:
            #         proc.kill()



            # self.browser.delete_all_cookies()
            # self.browser.close()
            self.browser.quit()
            # os.system("taskkill /f /im geckodriver.exe /T")
            # os.system("taskkill /f /im chromedriver.exe /T")
            # os.system("taskkill /f /im IEDriverServer.exe /T")
            self.browser = None
        self.gPlayCancel(self.sorgukimlik)
        if self.mydb is not None:
            self.mydb.dbClose()
            self.mydb = None
        self.mainMyReturn.opTracking.isdone = True
        self.mainMyReturn.opTracking.signalTrackingemit()
        self.isCancel = False
        self.sorgukimlik = None

    def resetmainMyReturn(self):
        self.mainMyReturn.isOK = False
        self.mainMyReturn.val = None
        self.mainMyReturn.msg = ''
        if self.mainMyReturn.opTracking is not None:
            self.mainMyReturn.opTracking.isdone = False
            self.mainMyReturn.opTracking.percentInt = 0
            self.mainMyReturn.opTracking.percentFloat = 0.0
        self.isCancel = False
        self.sorgukimlik = None




    def googlePlaySearchRun(self, aramaSozcugu: str, maxForTest=10):
        self.mainMyReturn.isOK = False
        self.mainMyReturn.msg = None
        self.mainMyReturn.val = None

        myReturn_firstControl = self.firstControl(aramaSozcugu, maxForTest)
        # print("Test myReturn_firstControl,  Return.isOk : {},  Return.val : {}, Return.msg : {},  : " .format(myReturn_firstControl.isOK, myReturn_firstControl.val, myReturn_firstControl.msg))
        if not myReturn_firstControl.isOK:
            self.mainMyReturn.isOK = myReturn_firstControl.isOK
            self.mainMyReturn.msg = myReturn_firstControl.msg
            self.mainMyReturn.val = myReturn_firstControl.val
            return

        # ***************************************************************************
        if self.isCancel:
            return
        # ***************************************************************************

        self.mydb = MyDb()
        myReturn_PlaySearch = self.gPlaySearch(self.mydb, aramaSozcugu, maxForTest)
        # print("Test myReturn_PlaySearch,  Return.isOk : {},  Return.val : {}, Return.msg : {},  : " .format(myReturn_PlaySearch.isOK, myReturn_PlaySearch.val, myReturn_PlaySearch.msg))
        if not myReturn_PlaySearch.isOK:
            self.mainMyReturn.isOK = myReturn_PlaySearch.isOK
            self.mainMyReturn.msg = myReturn_PlaySearch.msg
            self.mainMyReturn.val = myReturn_PlaySearch.val
            return

        # ***************************************************************************
        if self.isCancel:
            return
        # ***************************************************************************

        movetoImages_myReturn = self.movetoImages()
        if not movetoImages_myReturn.isOK:
            self.mainMyReturn.isOK = movetoImages_myReturn.isOK
            self.mainMyReturn.msg = movetoImages_myReturn.msg
            self.mainMyReturn.val = movetoImages_myReturn.val
            return

        # ***************************************************************************
        if self.isCancel:
            return
        # ***************************************************************************

        # least operation end of method
        myReturn_gPlayinsertDb = self.gPlayinsertDb(self.mydb, myReturn_PlaySearch)
        # print("Test myReturn_gPlayinsertDb,  Return.isOk : {},  Return.val : {}, Return.msg : {},  : " .format(myReturn_gPlayinsertDb.isOK, myReturn_gPlayinsertDb.val, myReturn_gPlayinsertDb.msg))
        self.mainMyReturn.isOK = myReturn_gPlayinsertDb.isOK
        self.mainMyReturn.msg = myReturn_gPlayinsertDb.msg
        self.mainMyReturn.val = myReturn_gPlayinsertDb.val
        return

    # #  MyReturn.val = aramasozcugu
    # def movetoImages(self):
    #     tempMyReturn = MyReturn()
    #     ent_dir_path = "tempimages/"
    #     out_dir_path = "images/"
    #
    #     entries = os.listdir(ent_dir_path)
    #     for entry in entries:
    #         print(str(entry))
    #         shutil.move(ent_dir_path + entry, out_dir_path)
    #     shutil.rmtree(ent_dir_path)
    #     tempMyReturn.isOK = True
    #     tempMyReturn.msg = "Ok : Resimler Taşındı"
    #     tempMyReturn.val = None
    #     self.mainMyReturn.opTracking.setPercent(10,1)


    #  MyReturn.val = aramasozcugu
    def movetoImages(self):
        tempMyReturn = MyReturn()
        ent_dir_path = "gplay/tempimages"
        out_dir_path = "gplay/images"
        try:
            if os.path.isdir(ent_dir_path):
                entries = os.listdir(ent_dir_path)
                for entry in entries:
                    print(str(entry))
                    shutil.move(ent_dir_path + "/" + entry, out_dir_path)

                shutil.rmtree(ent_dir_path)
                tempMyReturn.isOK = True
                tempMyReturn.msg = "Ok : Resimler Taşındı"
                tempMyReturn.val = None
                self.mainMyReturn.opTracking.setPercent(10,1)
            else:
                tempMyReturn.isOK = True
                tempMyReturn.msg = "Ok : Hiç resim yok"
                tempMyReturn.val = None

        except:
            tempMyReturn.isOK = False
            tempMyReturn.msg = "Hata :Resimler taşınamadı!"
            tempMyReturn.val = None

        return tempMyReturn


    #  MyReturn.val = aramasozcugu
    def firstControl(self, aramaSozcugu: str, maxForTest=0):
        tempMyReturn = MyReturn()
        aramasozcugu = (str(aramaSozcugu)).strip()
        if len(aramasozcugu) <= 2:
            tempMyReturn.isOK = False
            tempMyReturn.msg = "Hata :Google Play için girilen {} arama sözcüğü 3 karakterden büyük olmalı ".format(aramasozcugu)
            tempMyReturn.val = None
        else:
            tempMyReturn.isOK = True
            tempMyReturn.msg = "Ok : firstControl: aramasozcugu :{}".format(aramasozcugu)
            tempMyReturn.val = aramasozcugu

        return tempMyReturn

    # tempMyReturn.val = {'modalTbSorgu': modalTbSorgu, 'ListModalTbPlayAppList': tempListModalTbPlayAppList}
    # tempMyReturn.val =None
    def gPlaySearch(self, mydb: MyDb, aramaSozcugu: str, maxForTest=0) -> MyReturn:
        tempMyReturn = MyReturn()
        try:
            firefox_binary = FirefoxBinary("C:/Program Files/Mozilla Firefox/firefox.exe")
            executable_path = "webdrivers/geckodriver.exe"
            service_log_path = os.devnull
            self.browser = webdriver.Firefox( firefox_binary=firefox_binary, executable_path= executable_path,service_log_path= service_log_path)
            # self.browser = webdriver.Firefox(service_log_path= os.devnull)
            self.browser.maximize_window()
            self.browser.implicitly_wait(20)

            # ***************************************************************************
            if self.isCancel:
                return tempMyReturn
            # ***************************************************************************

            playSorguAra = "https://play.google.com/store/search?q="
            self.browser.get(playSorguAra + aramaSozcugu)

            # ***************************************************************************
            if self.isCancel:
                return tempMyReturn
            # ***************************************************************************

            digerlerini_goster = self.browser.find_element_by_xpath("/html/body/div[1]/div[4]/c-wiz/div/div[2]/div/c-wiz/c-wiz[1]/c-wiz/div/div[1]/div[2]/a")
            digerlerini_goster.click()

            # # script begin
            lenOfPage = self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
            match = False
            while (match == False):
                lastCount = lenOfPage
                time.sleep(3)
                lenOfPage = self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
                if lastCount == lenOfPage:
                    match = True
            # # script end

        except:
            tempMyReturn.isOK = False
            tempMyReturn.msg = "Hata : gPlaySearch: Başlangıç Hatası - İnternet Bağlantısı olmayabilir!!! "
            tempMyReturn.val = None
            return tempMyReturn
        try:
            links = self.browser.find_elements_by_xpath("//div[@class='b8cIId ReQCgd Q9MA7b']/a")
            allUrl = [ ]
            for link in links:
                pageUrl = link.get_property('href') + "&hl=en_US"
                allUrl.append(pageUrl)
        except:
            tempMyReturn.isOK = False
            tempMyReturn.msg = "Hata : gPlaySearch: links ayıklanamadı. hatalı değer links "
            tempMyReturn.val = None
            return tempMyReturn

        opCount = len(allUrl)
        if type(opCount) is not int or opCount <= 0:
            self.browser.quit()
            tempMyReturn.isOK = False
            tempMyReturn.msg = "Hata : gPlaySearch: sayfa Linkleri ayıklanamadı.Bulunan sayfa sayısı :{}: hatalı değer allUrl: {} ".format(opCount, allUrl)
            tempMyReturn.val = None
            return tempMyReturn
        else:
            if maxForTest > 0:
                opCount = maxForTest
                urlList = allUrl[ 0:opCount ]
            else:
                urlList = allUrl

        now = datetime.now()
        sorgukimlik = str(uuid.uuid4())
        self.sorgukimlik = sorgukimlik
        aranan = aramaSozcugu
        ekparams = ''
        sonucadet = opCount
        sorgutarihi = "{} {} {} {} ".format(now.year, now.month, now.day, now.hour)

        modalTbSorgu = ModalTbSorgu(sorgukimlik, aranan, ekparams, sonucadet, sorgutarihi)
        tempListModalTbPlayAppList = []
        sira = 1
        for url in urlList:
            myreturn_gPlayGetOnePage = self.gPlayGetOnePage(mydb, url, self.browser, sorgukimlik, sira)

            if not myreturn_gPlayGetOnePage.isOK:
                sonucadet -= 1
                tempMyReturn.isOK = False
                tempMyReturn.msg = "Hata : gPlaySearch: Bulunan sayfa sayısı :{}, Başarılı çekilen sayfa sayısı :{}: Hata Kaynağı : {} ".format(sonucadet, sira - 1, myreturn_gPlayGetOnePage.msg)
                tempMyReturn.val = None
                # self.browser.quit()
                # return tempMyReturn
            else:
                tempListModalTbPlayAppList.append(myreturn_gPlayGetOnePage.val)

                # ***************************************************************************
                self.mainMyReturn.opTracking.setPercent(80, opCount)
                print("gplayeden isCancel = "+ str(self.isCancel))
                # ***************************************************************************
                if self.isCancel:
                    return tempMyReturn
                # ***************************************************************************

                sira += 1

        self.browser.quit()
        tempMyReturn.isOK = True
        tempMyReturn.msg = "Ok : gPlaySearch: Bulunan sayfa sayısı :{}, Başarılı çekilen sayfa sayısı :{}: ".format(sonucadet, sira - 1)
        tempMyReturn.val = {'modalTbSorgu': modalTbSorgu, 'listModalTbPlayAppList': tempListModalTbPlayAppList}
        return tempMyReturn

        # MyReturn.val = modalTbPlayAppList

    def gPlayGetOnePage(self, mydb: MyDb, url: str, browser: webdriver, sorgukimlik: str, sira: int) -> MyReturn:
        tempMyReturn = MyReturn()

        try:
            browser.execute_script("window.open('https://play.google.com', 'new_window')")
            browser.switch_to.window(browser.window_handles[ 1 ])
            browser.get(url)
            browser.implicitly_wait(5)
            resimlercerkaydir = browser.find_element_by_css_selector(
                "#fcxH9b > div.WpDbMd > c-wiz > div > div.ZfcPIb > div > div.JNury.Ekdcne > div > c-wiz:nth-child(1) > c-wiz:nth-child(2) > c-wiz > div > div:nth-child(3)")

            for i in range(300):
                if resimlercerkaydir.is_displayed():
                    resimlercerkaydir.click()
                else:
                    break

        except:
            tempMyReturn.isOK = False
            tempMyReturn.msg = "Hata : gPlayGetOnePage:{} Adresi çekilirken sorun  Döndü- browser.execute_script driver hatası!!!  ".format(
                url)
            tempMyReturn.val = None
            return tempMyReturn

        # controls : int, float, list, str  > 0 and type is ...type(arg)-> val Or None
        searchSpiders = SearchSpiders()

        c_adi = searchSpiders.getAdi(browser)
        c_sorgukimlik_id = searchSpiders.getSorguKimlik(sorgukimlik)
        c_kategori_id = searchSpiders.getKategori_id(mydb, browser)
        c_gelistirici = searchSpiders.getGelistirici(browser)
        c_puan = searchSpiders.getPuan(browser)
        c_icon = searchSpiders.getIcon(browser)
        c_gunceltarih = searchSpiders.getGuncelTarih(browser)
        c_yuklemetarihi = searchSpiders.getYuklemeTarihi(c_gelistirici, browser)
        c_boyut = searchSpiders.getBoyut(browser)
        c_indirilme = searchSpiders.getIndirilme(browser)
        c_version = searchSpiders.getVersion(browser)
        c_minandroid = searchSpiders.getMinAnd(browser)
        c_resimler = searchSpiders.getResimler(browser)
        c_fark_gun = searchSpiders.getFarkGun(c_gelistirici, browser)
        c_fark_yil = searchSpiders.getFarkYil(c_fark_gun, browser)
        c_pageUrl = searchSpiders.getPageUrl(url)
        c_siralamasi = searchSpiders.getSira(sira)
        c_ucret = searchSpiders.getUcret(browser)
        c_gunluk_ort_indirme = searchSpiders.getGunlukOrtalama(c_indirilme, c_fark_gun)

        state = True
        hataParamKey = None
        hataParamValue = None
        listforStateControl = {
            "c_sorgukimlik_id": c_sorgukimlik_id,
            "c_adi": c_adi,
            "c_kategori_id": c_kategori_id,
            "c_yuklemetarihi": c_yuklemetarihi,
            "c_indirilme": c_indirilme,
            "c_fark_gun": c_fark_gun,
            "c_fark_yil": c_fark_yil,
            "c_siralamasi": c_siralamasi,
            "c_gunluk_ort_indirme": c_gunluk_ort_indirme}
        for k, v in listforStateControl.items():
            if v is None:
                hataParamKey = k
                hataParamValue = v
                state = False
                break

        if not state:
            tempMyReturn.isOK = False
            tempMyReturn.msg = "Hata : gPlayGetOnePage:{} Adresi çekilirken sorun  None Döndü- hataParamKey:  {} hataParamValue: {} !!!  ".format(
                c_pageUrl, hataParamKey, hataParamValue)
            tempMyReturn.val = None
        else:
            sorgukimlik_id = c_sorgukimlik_id
            kategori_id = c_kategori_id
            str_ad = c_adi
            str_gelistirici = c_gelistirici
            str_boyut = c_boyut
            str_icon = c_icon
            str_resimler = c_resimler
            str_version = c_version
            str_minandroid = c_minandroid
            float_puan = c_puan
            int_indirilme = c_indirilme
            str_yuklemetarihi = c_yuklemetarihi
            str_gunceltarih = c_gunceltarih
            int_fark_gun = c_fark_gun
            float_yil = c_fark_yil
            int_gunluk_ort_indirme = c_gunluk_ort_indirme
            int_siralamasi = c_siralamasi
            str_link = c_pageUrl
            str_ucret = c_ucret

            modalTbPlayAppList = ModalTbPlayAppList(sorgukimlik_id, kategori_id, str_ad, str_gelistirici, str_boyut,
                                                    str_icon, str_resimler,
                                                    str_version, str_minandroid, float_puan, int_indirilme,
                                                    str_yuklemetarihi, str_gunceltarih,
                                                    int_fark_gun, float_yil, int_gunluk_ort_indirme, int_siralamasi,
                                                    str_link, str_ucret)

            tempMyReturn.isOK = True
            tempMyReturn.msg = "Ok : gPlayGetOnePage:{} Adres Başarıyla Çekildi ".format(str_link)
            tempMyReturn.val = modalTbPlayAppList

        browser.switch_to.window(browser.window_handles[ 0 ])
        return tempMyReturn

    # INSERT Db
    # myReturn.val = insertRowsCount
    # myReturn_Gplay.val = {'modalTbSorgu': modalTbSorgu, 'listModalTbPlayAppList': tempListModalTbPlayAppList}
    def gPlayinsertDb(self, mydb: MyDb, myReturn_googlePlaySearchRun) -> MyReturn:
        myReturn = MyReturn()
        myReturn.isOK = False
        myReturn.val = None

        modalTbSorgu = myReturn_googlePlaySearchRun.val['modalTbSorgu']
        listModalTbPlayAppList = myReturn_googlePlaySearchRun.val['listModalTbPlayAppList']

        myReturn_main_insert_TbSorgu = mydb.main_insert_TbSorgu(modalTbSorgu)
        if not myReturn_main_insert_TbSorgu.isOK:
            return myReturn_main_insert_TbSorgu
        else:
            insertedRowsCount = 0
            for modalTbPlayAppList in listModalTbPlayAppList:
                myreturn_main_insert_TbPlayAppList = mydb.main_insert_TbPlayAppList(modalTbPlayAppList)
                if not myreturn_main_insert_TbPlayAppList.isOK:
                    return myreturn_main_insert_TbPlayAppList

                insertedRowsCount += 1

                # ***************************************************************************
                self.mainMyReturn.opTracking.setPercent(10, modalTbSorgu.sonucadet)
                # ***************************************************************************
                if self.isCancel:
                    return myReturn
                # ***************************************************************************

        myReturn.isOK = True
        myReturn.val = insertedRowsCount
        myReturn.msg = "Ok: Db ye Başarıyla Girildi : Verileb Satır Sayısı: {}, Girilen satır sayısı: {}, Hatalı Satır Sayısı: {} ".format(modalTbSorgu.sonucadet, insertedRowsCount, modalTbSorgu.sonucadet - insertedRowsCount)
        return myReturn


    # gPlayCancel---------------------------------------------------son

    def gPlayCancel(self, sorgukimlik = None):
        cancelMyreturn = MyReturn()
        cancelMyreturn.isOK = False
        cancelMyreturn.msg = ""
        cancelMyreturn.val = None


        ent_dir_path = "gplay/tempimages"

        if not self.mainMyReturn.isOK:
            try:
                if os.path.isdir(ent_dir_path):
                    shutil.rmtree(ent_dir_path)

                self.mainMyReturn.opTracking.setPercent(self.mainMyReturn.opTracking.percentInt,-2)

            except:
                cancelMyreturn.msg = "Hata: İptal edilirken hata oluştu! Resimler ve Tablolardan veriler silinemedi!"

            if sorgukimlik is not None:
                getCount_TbNamesSorgu = self.mydb.getCount(TbNamesSorgu.tableName)
                if getCount_TbNamesSorgu.isOK:
                    tempMyreturn_deleteAllByXe_TbNamesSorgu = self.mydb.deleteAllByXe(TbNamesSorgu.tableName,
                                                                                      TbNamesSorgu.sorgukimlik,
                                                                                      sorgukimlik)
                    if tempMyreturn_deleteAllByXe_TbNamesSorgu.isOK:
                        getCount_TbNamesPlayAppList = self.mydb.getCount(TbNamesPlayAppList.tableName)
                        if getCount_TbNamesPlayAppList.isOK:
                            tempMyreturn_deleteAllByXe_TbNamesPlayAppList = self.mydb.deleteAllByXe(
                                TbNamesPlayAppList.tableName, TbNamesPlayAppList.sorgukimlik_id, sorgukimlik)
                            if tempMyreturn_deleteAllByXe_TbNamesPlayAppList.isOK:
                                cancelMyreturn.msg = "İptal edildi"
                                self.mainMyReturn.opTracking.setPercent(self.mainMyReturn.opTracking.percentInt,-1)
                            else:
                                cancelMyreturn.msg = "Hata: İptal edilirken hata oluştu! PlayAppList tablosundan silinemedi!"
                        else:
                            cancelMyreturn.msg = "İptal edildi"
                    else:
                        cancelMyreturn.msg = "Hata: İptal edilirken hata oluştu! Sorgu ve PlayAppList tablosundan silinemedi!"
                else:
                    cancelMyreturn.msg = "İptal edildi"
            else:
                cancelMyreturn.msg = "İptal edildi"

        if self.isCancel:
            self.mainMyReturn.isOK = cancelMyreturn.isOK
            self.mainMyReturn.msg = cancelMyreturn.msg
            self.mainMyReturn.val = None


    # gPlayCancel---------------------------------------------------son





# For Test:
# gps = GooglePlaySearch()
# gps.googlePlaySearchRun("blue filter", 2)

