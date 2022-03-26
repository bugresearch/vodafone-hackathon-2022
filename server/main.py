while True:
    buyukluk = 0
    gps1 = 0
    gps2 = 0
    kullanici_gps1= 0
    kullanici_gps2= 0
    tarih = 0

    def fonksiyon():
        url = 'https://api.orhanaydogdu.com.tr/deprem/live.php?limit=1'
        response = requests.get(url)
        b = json.loads(response.text)
        lng =b['result'][0]['lng']
        lat =b['result'][0]['lat']
        mag =b['result'][0]['mag']
        date =b['result'][0]['date']
        time.sleep(5)
        buyukluk = int(mag)
        gps1 = int(lng)
        gps2 = int(lat)
        tarih = int(date)

    def alinan():
        if buyukluk > 4.8:
            if (gps1 - 0.008983) <= kullanici_gps1 <= (gps1 + 0.008983) and (gps2 - 0.015060) <= kullanici_gps2 <= (gps2 + 0.015060):
                print("Bildirim yolla")
            else:
                print("Bildirim Yollama")

    def bildirim_yolla():
        return kullanici_gps1, kullanici_gps2, tarih