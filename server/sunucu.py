from flask import Flask
from flask import request
import deprem

app = Flask(__name__)

@app.route('/sorgu', methods=['GET'])
def sorgu():
    # Kullanıcı Lokasyon Gönderecek Sen Kritik Olup Olmadığına Bakıp ona göre veri göndereceksin
    lng = float(request.args.get('lng'))
    lat = float(request.args.get('lat'))
    tehlike = deprem.sorgula(lng,lat)
    if tehlike:
        return '{"status":"1"}'
    else:
        return '{"status":"0"}'

@app.route('/kayit')
def kayit():
    lng = float(request.args.get('lng'))
    lat = float(request.args.get('lat'))
    risk = bool(request.args.get('risk'))
    telefon = int(request.args.get('telefon')) 
    durum = deprem.kayit(lng,lat,risk,telefon)
    if durum:
        return  '{"status":"1"}'
    else:
        return  '{"status":"0"}'

app.run(host='192.168.8.142', port=80)