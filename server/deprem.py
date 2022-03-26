import json
import requests
import sqlite3
import time

afad_api_url = ""
afad_api_token = ""

def sorgula(lng_user,lat_user):
    url = 'https://api.orhanaydogdu.com.tr/deprem/live.php?limit=1'
    response = requests.get(url)
    list = json.loads(response.text)
    lng =list['result'][0]['lng']
    lat =list['result'][0]['lat']
    mag =list['result'][0]['mag']
    if mag > 4.8 or 1<2:
        if (lng - 0.008983) <= lng_user <= (lng + 0.008983) and (lat - 0.015060) <= lat_user <= (lat + 0.015060):
            return True
        else:
            return False
    else:
        return False

def kayit(lng, lat, risk, telefon):
    if sorgula(lng,lat):
        datetime = time.time()

        # Kendi veritabanımıza kaydediyoruz
        con = sqlite3.connect('veritabani.db')
        cur = con.cursor()  
        cur.execute("INSERT INTO veriler VALUES (NULL,'"+str(telefon)+"','"+str(lng)+"','"+str(lat)+"','"+str(risk)+"', '"+str(datetime)+"')")
        con.commit()
        con.close()
        # Afada gönderiyoruz
        return True
    else:
        return False