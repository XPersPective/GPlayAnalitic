import os
import re
import shutil
import uuid
from datetime import datetime

import wget
from selenium import webdriver

from mydb.dbmodals import ModalTbKategori
from mydb.mydb import MyDb


class SearchSpiders:
    def getSorguKimlik(self, sorgukimlik):
        try:
            return self.in_typeAndnonzeroControl(str, sorgukimlik)
        except:
            return None

    def getAdi(self, browser: webdriver):
        try:
            adi = browser.find_element_by_tag_name('h1').text
            adi = adi.strip()
            return self.in_typeAndnonzeroControl(str, adi)
        except:
            return None

    def getKategori_id(self, mydb: MyDb, browser: webdriver):
        try:
            kategori = browser.find_element_by_css_selector('span.T32cc:nth-child(2) > a:nth-child(1)').text
            kategori = kategori.strip()
            kategori = self.in_typeAndnonzeroControl(str, kategori)
            if kategori is not None:
                myreturn = mydb.main_insert_TbKategori(ModalTbKategori(kategori))
                if myreturn.isOK:
                    return myreturn.val
                else:
                    return None
        except:
            return None


    def getGelistirici(self, browser):
        try:
            gelistirici = browser.find_element_by_css_selector('span.T32cc:nth-child(1) > a:nth-child(1)').text
            gelistirici = gelistirici.strip()
            return self.in_typeAndnonzeroControl(str, gelistirici)
        except:
            return None

    def getIcon(self, browser):
        try:
            firsturl = browser.find_element_by_xpath("//div[@class='xSyT2c']/img[@class='T75of sHb2Xb']").get_property(
                'src')

            firsturl = firsturl.strip()
            firsturllist = firsturl.rsplit('=', 1)
            if len(firsturllist) > 0:
                url = firsturllist[ 0 ].strip()
            else:
                url = firsturl

            son_url = self.in_typeAndnonzeroControl(str, url)
            if son_url is None:
                return None
            else:

                tempPath = "gplay/mytemp"
                tempimages = "gplay/tempimages"
                try:
                    if not os.path.isdir(tempimages):
                        os.mkdir(tempimages)

                    if not os.path.isdir(tempPath):
                        os.mkdir(tempPath)
                except:
                    pass
                lasttempPath = wget.download(son_url, tempPath)

                extention = lasttempPath.rsplit('.', 1)[ 1 ].strip()
                if extention is not None:
                    uu = str(uuid.uuid4())
                    newextention = "." + extention
                    uu = str(uuid.uuid4())
                    generated = tempimages + "/" + uu + newextention
                    generatedfordb = "gplay/images/" + uu + newextention
                    shutil.move(lasttempPath, generated)
                    try:
                        shutil.rmtree(tempPath)
                    except:
                        pass
                    return generatedfordb
                else:
                    try:
                        shutil.rmtree(tempPath)
                    except:
                        pass
                    return None
        except:
            return None

    def getGuncelTarih(self, browser):
        try:
            gunceltarih1 = browser.find_element_by_css_selector(
                ".IxB2fe > div:nth-child(1) > span:nth-child(2) > " "div:nth-child(1) > span:nth-child(1)").text
            gtarih = datetime.strptime(gunceltarih1.strip(), '%B %d, %Y')
            gunceltarih = "{} {} {} {} ".format(gtarih.year, gtarih.month, gtarih.day, gtarih.hour)

            gunceltarihson = gunceltarih.strip()
            return self.in_typeAndnonzeroControl(str, gunceltarihson)
        except:
            return None

    def getPuan(self, browser):
        try:
            puan1 = browser.find_element_by_xpath("//div[@class='K9wGie']/div[@class='BHMmbe']").text
            puan = float(puan1)
            return self.in_typeAndnonzeroControl(float, puan)
        except:
            return None

    def getYuklemeTarihi(self,gelistirici:str, browser):
        try:
            gelistiricison = self.in_typeAndnonzeroControl(str, gelistirici)
            if gelistiricison is None:
                return None
            input_data = browser.page_source
            pattern = r'(?<=\["' + gelistirici + '"\])(\s.+)?]\n'
            rare = re.findall(pattern, input_data)
            rt = ""
            s1 = rt.join(rare)
            s2 = s1.replace(",", "")
            s3 = s2.replace('"', '')
            realist = list(s3.split(" "))

            gun = realist[ 1 ].strip()
            ay = realist[ 0 ].strip()
            yil = realist[ 2 ].strip()
            tarih = yil + " " + ay + " " + gun
            ytarihi = datetime.strptime(tarih, '%Y %b %d')
            ytarihidate = datetime(year=ytarihi.year, month=ytarihi.month, day=ytarihi.day, hour=0)
            yuklemetarihi = "{} {} {} {} ".format(ytarihidate.year, ytarihidate.month, ytarihidate.day, ytarihidate.hour)
            return yuklemetarihi
        except:
            return None


    def getBoyut(self, browser):
        try:
            boyut = browser.find_element_by_css_selector(
                "div.hAyfc:nth-child(2) > span:nth-child(2) > div:nth-child(1) > " "span:nth-child(1)").text
            boyut = boyut.strip()
            return self.in_typeAndnonzeroControl(str, boyut)
        except:
            return None


    def getIndirilme(self, browser):
        try:
            indirilme1 = browser.find_element_by_css_selector(
                "div.hAyfc:nth-child(3) > span:nth-child(2) > div:nth-child(1) > " "span:nth-child(1)").text
            ind = str(indirilme1).strip()
            ind1 = ind.rstrip("+")
            ind2 = ind1.replace(",", "")
            indirilme = int(ind2)
            return self.in_typeAndnonzeroControl(int, indirilme)
        except:
            return None

    def getVersion(self, browser):
        try:
            version1 = browser.find_element_by_css_selector(
                "div.hAyfc:nth-child(4) > span:nth-child(2) > div:nth-child(1) > "
                "span:nth-child(1)").text
            versionx = str(version1)
            version = versionx.strip()
            return self.in_typeAndnonzeroControl(str, version)
        except:
            return None

    def getMinAnd(self, browser):
        try:

            minandroidx = browser.find_element_by_css_selector(
                "div.hAyfc:nth-child(5) > span:nth-child(2) > div:nth-child(1) " "> span:nth-child(1)").text
            minandroidy = str(minandroidx)
            minandroid = minandroidy.strip()
            return self.in_typeAndnonzeroControl(str, minandroid)
        except:
            return None

    def getResimler(self, browser: webdriver):
        try:
            temizresimlist = [ ]
            resimlerList = browser.find_elements_by_css_selector(
                "#fcxH9b > div.WpDbMd > c-wiz > div > div.ZfcPIb > div > div.JNury.Ekdcne > div > c-wiz:nth-child(1) > c-wiz:nth-child(2) > c-wiz > div > div.JiLaSd.u3EI9e > div > button > img")
            for resim in resimlerList:
                resmialx = resim.get_property('srcset')
                resmitrasla = resmialx.strip()
                resmitraslabitti = self.in_typeAndnonzeroControl(str, resmitrasla)
                if resmitraslabitti is not None:
                    temizresimlist.append(resmitraslabitti)

            temizlocalresimler = [ ]
            for birresim in temizresimlist:
                firsturl = birresim

                firsturl = firsturl.strip()
                firsturllist = firsturl.rsplit('=', 1)
                if len(firsturllist) > 0:
                    url = firsturllist[ 0 ].strip()
                else:
                    url = firsturl

                son_url = self.in_typeAndnonzeroControl(str, url)
                if son_url is None:
                    return None
                else:
                    tempPath = "gplay/mytemp"
                    tempimages = "gplay/tempimages"
                    try:
                        if not os.path.isdir(tempimages):
                            os.mkdir(tempimages)

                        if not os.path.isdir(tempPath):
                            os.mkdir(tempPath)
                    except:
                        pass

                    lasttempPath = wget.download(son_url, tempPath)
                    print("indildi" + tempPath)

                    extention = lasttempPath.rsplit('.', 1)[ 1 ].strip()
                    if extention is not None:
                        uu = str(uuid.uuid4())
                        newextention = "." + extention
                        uu = str(uuid.uuid4())
                        generated = tempimages + "/" + uu + newextention
                        generatedfordb = "gplay/images/" + uu + newextention
                        shutil.move(lasttempPath, generated)
                        try:
                            shutil.rmtree(tempPath)
                        except:
                            pass
                        temizlocalresimler.append(generatedfordb)
                    else:
                        try:
                            shutil.rmtree(tempPath)
                        except:
                            pass

            print("\n temizlocalresimler : {}".format(temizlocalresimler))
            resimlerson = ','.join(temizlocalresimler)
            resimlerson = resimlerson.strip(',')

            return self.in_typeAndnonzeroControl(str, resimlerson)
        except:
            return None

    def getFarkGun(self,gelistirici,browser):
        try:
            gelistiricison = self.in_typeAndnonzeroControl(str, gelistirici)
            if gelistiricison is None:
                return None
            input_data = browser.page_source
            pattern = r'(?<=\["' + gelistirici + '"\])(\s.+)?]\n'
            rare = re.findall(pattern, input_data)
            rt = ""
            s1 = rt.join(rare)
            s2 = s1.replace(",", "")
            s3 = s2.replace('"', '')
            realist = list(s3.split(" "))

            gun = realist[ 1 ].strip()
            ay = realist[ 0 ].strip()
            yil = realist[ 2 ].strip()
            tarih = yil + " " + ay + " " + gun
            ytarihi = datetime.strptime(tarih, '%Y %b %d')
            yuklemeTarihiformatDate = datetime(year=ytarihi.year, month=ytarihi.month, day=ytarihi.day, hour=0)

            bugun = datetime(year=datetime.today().year, month=datetime.today().month, day=datetime.today().day, hour=0)
            fark = bugun - yuklemeTarihiformatDate
            fark_gun = fark.days
            fark_gun_son = self.in_typeAndnonzeroControl(int, fark_gun)
            return fark_gun_son
        except:
            return None

    def getFarkYil(self,fark_gun,yuklemeTarihiformatDate):
        try:
            if fark_gun is None:
                return None
            fark_yil1 = round((fark_gun / 360), 1)
            fark_yil = float(fark_yil1)
            fark_yil_son = self.in_typeAndnonzeroControl(float, fark_yil)
            return fark_yil_son
        except:
            return None

    def getPageUrl(self,url:str):
        try:
            urlson = url.strip()
            urlson = self.in_typeAndnonzeroControl(str, urlson)
            return urlson
        except:
            return None

    def getSira(self, sira):
        try:
            sira = self.in_typeAndnonzeroControl(int, sira)
            return sira
        except:
            return None

    def getUcret(self,browser:webdriver):
        try:
            ucret = browser.find_element_by_css_selector("div.hAyfc:nth-child(7) > span:nth-child(2) > div:nth-child(1) > span:nth-child(1)").text
            ucretx = str(ucret)
            ucretx = ucretx.strip()
            return self.in_typeAndnonzeroControl(str, ucretx)
        except:
            return None

    def getGunlukOrtalama(self, toplamIndirilme, fark_gun):
        try:
            if toplamIndirilme is None:
                return None
            if fark_gun is None:
                return None
            gunluk_ort_indirme = round(toplamIndirilme / fark_gun)
            gunluk_ort_indirme_son = self.in_typeAndnonzeroControl(int, gunluk_ort_indirme)
            return gunluk_ort_indirme_son
        except:
            return None



    # controls : int, float, list, str  > 0 and type is ...type(arg) -> val Or None
    def in_typeAndnonzeroControl(self, myType: type, val):

        if myType is not type(val):
            return None
        else:
            if myType is int or myType is float:
                if float(val) > 0.0:
                    return val
                else:
                    return None

            if myType == list or myType is str:
                if len(val) > 0:
                    return val
                else:
                    return None

        return None



