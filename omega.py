import os
import telebot
import requests
import re
import wikipedia
from datetime import datetime
from urllib.parse import unquote
from urllib.parse import urlparse
from urllib.parse import parse_qs
import json
import pymongo
from telebot.types import InputMediaPhoto
import random
import cloudscraper

# translator = Translator(service_urls=[
# 'translate.google.com',
# 'translate.google.co.id',
# ])
client = pymongo.MongoClient(
  "")
db = client.rara

def database(message):
  try:
    if str(message.chat.id) != "group4" or '654251221' or '991258050' or '1567254941':
      mycol = db[f"{message.chat.id}"]
      print(message)
      msg = message.json
      p = mycol.insert_one(msg).inserted_id
      print("MongoDB Action : " + p)
  except:
    print("Failed MongoDB")


while True:
  ip = str(random.randint(0, 255)) + "." + str(random.randint(0, 255)) + "." + str(random.randint(0, 255)) + "." + str(
    random.randint(0, 255))
  HEADERS = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-language": "en-US,en;q=0.9",
    "sec-ch-ua": "\"Chromium\";v=\"94\", \"Google Chrome\";v=\"94\", \";Not A Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": "\"Android\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1"
  }

  HEADERSTOKOPEDIA = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
    'Origin': 'https://www.tokopedia.com'
  }

  HEADERSANTERAJA = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
    'Origin': 'https://paketmu.com'
  }

  HEADERSIDEXPRESS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
    'Origin': 'https://idexpress.com',
    'Host': 'rest.idexpress.com',
    'Timezone': 'GMT+0700',
    'Referer': 'https://idexpress.com/'
  }

  HEADERSSHOPEESCRAPPER = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
    'Host': 'shopee.co.id',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Sec-Fetch-Dest': 'id,en-US;q=0.7,en;q=0.3',
    'Connection': 'keep-alive',
    'Accept-Encoding': 'gzip, deflate, br',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1'
  }

  wikipedia.set_lang("id")
  username = 'Rxp69'
  userId = '654251221'
  userId2 = '1332705903'
  group1 = -1001681705401  # main group

  # os.environ['TZ'] = 'Asia/Jakarta'
  # time.tzset()
  now = datetime.now()
  current_date = now.strftime("%Y/%m/%d")

  API_KEY = os.getenv('API_KEY')

  # PRIMARY TOKEN
  bot = telebot.TeleBot('')

  # second bot
  # bot = telebot.TeleBot('')

  banned = client.banned
  shopeeDatabase = client.shopee
  happyhour = client.happyhours


  def block(user, message):
    blockedUser = banned.list_collection_names()
    mycol = banned[f"{user}"]
    print(message)
    msg = message.json
    p = mycol.insert_one(msg).inserted_id
    print('done')


  def remove(user):
    blockedUser = banned.list_collection_names()
    bannedCol = banned[user]
    bannedCol.drop()


  def show():
    blockedUser = banned.list_collection_names()
    return blockedUser


  def updateList():
    blockedUser = banned.list_collection_names()


  # lazada aff

  def get_final_url(url):
    """
    Mengembalikan URL tujuan akhir dari request URL
    """
    session = requests.Session()
    response = session.get(url, allow_redirects=False)

    # Jika ada redirect, maka lakukan redirect secara rekursif
    if response.status_code in [301, 302, 303, 307, 308]:
      redirect_url = response.headers['Location']
      if re.match(r'^https?://', redirect_url):
        return get_final_url(redirect_url)
      else:
        base_url = re.match(r'(https?://[^/]+)/.*', url).group(1)
        return get_final_url(f'{base_url}{redirect_url}')
    else:
      return url


  def check_redirect(url, message):
    """
    Melakukan pengecekan redirect pada URL
    """
    session = requests.Session()
    response = session.get(url, allow_redirects=False)

    if response.status_code in [301, 302, 303, 307, 308]:
      redirect_url = response.headers['Location']
      if re.match(r'^https?://', redirect_url):
        final_url = get_final_url(redirect_url)
        bot.reply_to(message, f"Redirected to: {final_url.split('?')[0]}")
        return final_url.split('?')[0]
      else:
        base_url = re.match(r'(https?://[^/]+)/.*', url).group(1)
        final_url = get_final_url(f'{base_url}{redirect_url}')
        bot.reply_to(message, f"Redirected to: {final_url.split('?')[0]} ")
        return final_url.split('?')[0]
    elif 'text/html' in response.headers.get('Content-Type', ''):

      match = re.search(r'<meta.*?http-equiv=["\']?refresh["\']?.*?content=["\']?\d+;.*?url=(.*?)["\']', response.text,
                        flags=re.I)
      if match:
        aff = 0;
        redirect_url = match.group(1)
        final_url = get_final_url(redirect_url)
        if ('https://c.lazada.co.id' in redirect_url):
          aff = 1;
          flag = True

        if aff == 1 and flag:
          ##bot.reply_to(message, f"Link ini mengandung aff")
          if ('s.lazada.co.id' not in final_url):
            bot.reply_to(message, f"⚠️LAZADA AFFILIATE DETECTED ⚠️ \n\n {final_url.split('?')[0]} ")
          aff = 0;
        else:
          if ('s.lazada.co.id' not in final_url):
            bot.reply_to(message, f"{final_url.split('?')[0]} ")
        check_redirect(final_url, message)
        return final_url.split('?')[0]
    else:
      print("No redirect detected.")


  def tokopedia(url):
    if 'http' not in url:
      url = "https://" + url
    s = cloudscraper.create_scraper()
    k = url.split('/')
    p = s.get("https://tokopedia.app.link/" + k[3], allow_redirects=False)
    n = p.headers['Location']
    lo = n.split("?")
    use_affiliate = "aff_unique_id" in lo[1]
    if use_affiliate == True:
      # print(ca)
      ca = '⚠️ TOKOPEDIA AFFILIATE DETECTED️ ⚠️ \n\n' + str(lo[0])
      return ca
    else:
      # head, sep, tail = url.partition('?')
      # print(head)
      ca = str(lo[0])
      return ca


  def shopee(url):
    if 'http' not in url:
      url = "https://" + url
    j = requests.get(url, allow_redirects=False)
    k = urlparse(j.headers["Location"])
    if ('&redir=' in k.query):
      slink = str(unquote(k.query.split('&')[2].replace('redir=', '')))
      sl = slink.split('?')[0]
    else:
      slink = str(k.scheme) + "://" + str(k.netloc) + str(k.path.replace('/universal-link/', '/'))
      sl = '⚠️ SHOPEE AFFILIATE DETECTED ⚠️ \n\n' + str(slink)
    # nr = requests.get(sl, allow_redirects=False)
    # nh = nr.headers
    # st = urlparse(nr.headers["Location"])
    # fl = st.scheme + "://" + st.netloc + st.path
    return sl


  def blibli(url):
    if 'http' not in url:
      url = "https://" + url
    s = cloudscraper.create_scraper()
    k = url.split('/')
    p = s.get("https://blibli.app.link/" + k[3], allow_redirects=False)
    n = p.headers['Location']
    lo = n.split("?")
    return lo


  def tiktok(url):
    if 'http' not in url:
      url = "https://" + url
    j = requests.get(url, headers=HEADERS, allow_redirects=False)
    k = urlparse(j.headers["Location"])
    url = str(k.scheme) + "://" + str(k.netloc) + str(k.path)
    return url


  def spesificUrl(url):
    if 'http' not in url:
      url = "https://" + url
    j = requests.get(url, headers=HEADERS, allow_redirects=False)
    k = urlparse(j.headers["Location"])
    url = str(k.scheme) + "://" + str(k.netloc) + str(k.path)
    return url


  def premiumUrl(url):
    if 'http' not in url:
      url = "https://" + url
    j = requests.get(url, headers=HEADERS, allow_redirects=False)
    k = urlparse(j.headers["Location"])
    sl = str(k.scheme) + "://" + str(k.netloc) + str(k.path)
    if 'tokopedia.link' in sl:
      sl = tokopedia(sl)
      return sl
    elif 'shp.ee' in sl or 'shop.ee' in sl or 'shpe.ee' in sl or 'shope.ee' in sl:
      sl = shopee(sl)
      return sl
    elif '3.jd.id' in sl:
      sl = spesificUrl(sl)
      return sl
    elif 'c.lazada.co.id' in sl:
      sl = spesificUrl(sl)
      return sl
    elif 'blibli.app.link' in sl:
      sl = spesificUrl(sl)
      return sl
    else:
      return sl


  def shortLink(url, message):
    if 'http' not in url:
      url = "https://" + url
    r = requests.get(url, headers=HEADERS, allow_redirects=False)
    k = urlparse(r.headers["Location"])
    sl = str(k.scheme) + "://" + str(k.netloc) + str(k.path)

    if 'styledo.co' in sl:
      sl = premiumUrl(sl)
      return sl
    elif 'invol.co' in sl or 'invl.io' in sl or 'invle.co' in sl:
      sl = premiumUrl(sl)
      return sl
    elif 'tokopedia.link' in sl:
      sl = tokopedia(sl)
      return sl
    elif 'shp.ee' in sl or 'shop.ee' in sl or 'shpe.ee' in sl or 'shope.ee' in sl:
      sl = shopee(sl)
      return sl
    elif '3.jd.id' in sl:
      sl = spesificUrl(sl)
      return sl
    elif 'c.lazada.co.id' in sl:
      sl = spesificUrl(sl)
      return sl
    elif 'blibli.app.link' in sl:
      sl = spesificUrl(sl)
      return sl
    else:
      return sl


  def findUrl(text):
    urlText = str(text)
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex, urlText)
    return [x[0] for x in url]

  def cuaca(message):
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    # City Name CITY = "Hyderabad"
    # API key API_KEY = "Your API Key"
    # upadting the URL
    user_sender = message.from_user.username or message.from_user.first_name
    block = banned.list_collection_names()
    if user_sender not in block:
      try:
        kota = message.text[6:]
        URL = BASE_URL + "q=" + kota + "&appid=" + "484810e5eae2f09da5be5e325bc8ad2f" + "&lang=id"
        # HTTP request
        response = requests.get(URL)
        # checking the status code of the request
        # getting data in the json format
        data = response.json()
        # getting the main dict block
        main = data['main']
        # getting temperature
        temperature = main['temp'] - 273
        # getting the humidity
        humidity = main['humidity']
        # getting the pressure
        pressure = main['pressure']
        # weather report
        report = data['weather']
        # kecepatan angin
        angin = response.json()['wind']['speed']

        # bot.reply_to(message,f"Cuaca s-saat di kota {kota} kurasa: {report[0]['main']} Lebih Lengkapnya a-akan kukirim ")
        bot.reply_to(message,
                     f"{kota:-^30}\nTemperatur: {temperature} C\nKelembapan: {humidity}%\nTekanan: {pressure} hpa\nLaporan cuaca: {report[0]['description']}\nkecepatan Angin:{angin}m/s")
      except:
        print('nothing')
    else:
      bot.reply_to(message, 'Anda diblokir menggunakan fitur ini')

  def sicepat(message):
    x = message.text.replace('/sicepat ', '')
    url = requests.get('https://content-main-api-production.sicepat.com/public/check-awb/%20' + x).content
    data = json.loads(url)
    user_sender = message.from_user.username or message.from_user.first_name
    data = data['sicepat']
    block = banned.list_collection_names()
    if user_sender not in block:
      if data['status']['code'] == 200:
        data = data['result']
        nomer_resi = 'Nomer resi : ' + data['waybill_number']
        sender = 'Pengirim : ' + data['sender']
        receiver = 'Nama penerima : ' + data['receiver_name']
        receiver_adress = 'Alamat penerima : ' + data['receiver_address']
        # print(data['track_history'])
        tracking = []
        for track in data['track_history']:
          if track['status'] == 'DELIVERED':
            tracking.append(track['date_time'] + ' : ' + track['receiver_name'])
          else:
            tracking.append(track['date_time'] + ' : ' + track['city'])
        tracking = '\n'.join(tracking)
        # print(track['date_time'] + ' : ' + track['city'])
        bot.reply_to(message, f'{nomer_resi: ^30}\n{sender}\n{receiver}\n{receiver_adress}\n\n{tracking}')
      else:
        bot.reply_to(message, 'Nomer resi tidak ditemukan!')
    else:
      bot.reply_to(message, 'Anda diblokir menggunakan fitur ini')


  def sholat(message):
    user_sender = message.from_user.username or message.from_user.first_name
    block = banned.list_collection_names()
    if user_sender not in block:
      BASE_URL = "https://api.myquran.com/v1/"
      # City Name CITY = "Hyderabad"
      # API key API_KEY = "Your API Key"
      # upadting the URL
      kota = message.text[14:]
      kotalen = len(kota)
      print(kotalen)
      if kotalen >= 4:
        kota = kota.replace(' ', '%20')
        URL = BASE_URL + "sholat/kota/cari/" + kota
        # HTTP request
        response = requests.get(URL)
        # checking the status code of the request
        # getting data in the json format
        data = response.json()
        if data['status'] == True:
          # getting the main dict block
          cityList = data["data"]
          for city in cityList:
            cityId = city['id']
            jadwal = requests.get(f'{BASE_URL}sholat/jadwal/{cityId}/{current_date}').content
            url = json.loads(jadwal)
            data = url['data']
            daerah = data['lokasi'] + ', ' + data['daerah']
            tanggal = data["jadwal"]["tanggal"]
            imsak = 'Imsak  : ' + data["jadwal"]["imsak"]
            subuh = 'Subuh  : ' + data["jadwal"]["subuh"]
            terbit = 'Terbit : ' + data["jadwal"]["terbit"]
            dhuha = 'Dhuha  : ' + data["jadwal"]["dhuha"]
            dzuhur = 'Dzuhur : ' + data["jadwal"]["dzuhur"]
            ashar = 'Ashar  : ' + data["jadwal"]["ashar"]
            maghrib = 'Maghrib: ' + data["jadwal"]["maghrib"]
            isya = 'Isya   : ' + data["jadwal"]["isya"]
            bot.reply_to(message,
                         f"{daerah: ^30}\n{tanggal: ^30}\n\n{imsak}\n{subuh}\n{terbit}\n{dhuha}\n{dzuhur}\n{ashar}\n{maghrib}\n{isya}\n")
        else:
          bot.reply_to(message, 'Kota tidak ditemukan.')
      else:
        bot.reply_to(message, 'Masukkan minimal 4 huruf')
    else:
      bot.reply_to(message, '')


  def sendMessage(group, message, text, user_sender):
    text = text.replace('njor', 'redacted')
    text = text.replace('Njor', 'redacted')
    text = text.replace('NJOR', 'redacted')
    if message.photo:
      if message.caption:
        if message.from_user.username:
          bot.send_photo(group, message.photo[-1].file_id, '@' + user_sender + ' : ' + text)
        else:
          bot.send_photo(group, message.photo[-1].file_id,
                         'tg://openmessage?user_id=' + str(message.from_user.id) + ' : ' + text)
      else:
        if message.from_user.username:
          bot.send_photo(group, message.photo[-1].file_id, '@' + user_sender)
        else:
          bot.send_photo(group, message.photo[-1].file_id,
                         'tg://openmessage?user_id=' + str(message.from_user.id))
    else:
      if message.from_user.username:
        bot.send_message(group, '@' + user_sender + ' : ' + text)
      else:
        bot.send_message(group,
                         'tg://openmessage?user_id=' + str(message.from_user.id) + ' : ' + text)


  def tokopediaFind(main, second, message, text, user_sender):
    urlArray = findUrl(text)
    # print(urlArray)
    for url in urlArray:
      try:
        tokopediaUrl = tokopedia(url)
        bot.reply_to(message, tokopediaUrl)
        if message.from_user.username:
          bot.send_message(second, str(tokopediaUrl) + ' message from @' + user_sender)
          bot.send_message(main, str(tokopediaUrl) + ' message from @' + user_sender)
        else:
          bot.send_message(second,
                           str(tokopediaUrl) + ' message from tg://openmessage?user_id=' + str(message.from_user.id))
          bot.send_message(main,
                           str(tokopediaUrl) + ' message from tg://openmessage?user_id=' + str(message.from_user.id))
      except:
        if 'group' in message.chat.type or 'supergroup' in message.chat.type:
          print('wkwkwk')
        else:
          bot.reply_to(message, f"URl Tidak Dapat diproses {url}")


  def shopeeFind(main, second, message, text, user_sender):
    urlArray = findUrl(text)
    for url in urlArray:
      try:
        shopeeUrl = shopee(url)
        bot.reply_to(message, shopeeUrl)
        if message.from_user.username:
          bot.send_message(main, str(shopeeUrl) + ' message from @' + user_sender)
          bot.send_message(second, str(shopeeUrl) + ' message from @' + user_sender)
        else:
          bot.send_message(main, str(shopeeUrl) + ' message from tg://openmessage?user_id=' + str(message.from_user.id))
          bot.send_message(second,
                           str(shopeeUrl) + ' message from tg://openmessage?user_id=' + str(message.from_user.id))
      except:
        if 'group' in message.chat.type or 'supergroup' in message.chat.type:
          print('wkwkwk')
        else:
          bot.reply_to(message, f"URl Tidak Dapat diproses {url}")


  def blibliFind(main, second, message, text, user_sender):
    urlArray = findUrl(text)
    for url in urlArray:
      try:
        blibliUrl = blibli(url)
        bot.reply_to(message, blibliUrl)
        if message.from_user.username:
          bot.send_message(main, str(blibliUrl) + ' message from @' + user_sender)
          bot.send_message(second, str(blibliUrl) + ' message from @' + user_sender)
        else:
          bot.send_message(main,
                           str(blibliUrl) + ' message from tg://openmessage?user_id=' + str(
                             message.from_user.id))
          bot.send_message(second,
                           str(blibliUrl) + ' message from tg://openmessage?user_id=' + str(
                             message.from_user.id))
      except:
        if 'group' in message.chat.type or 'supergroup' in message.chat.type:
          print('wkwkwk')
        else:
          bot.reply_to(message, f"URl Tidak Dapat diproses {url}")


  def premiumFind(main, message, text, user_sender):
    urlArray = findUrl(text)
    for url in urlArray:
      try:
        prioritasUrl = premiumUrl(url)
        bot.reply_to(message, prioritasUrl)
        if message.from_user.username:
          bot.send_message(main, str(prioritasUrl) + ' message from @' + user_sender)
        else:
          bot.send_message(main,
                           str(prioritasUrl) + ' message from tg://openmessage?user_id=' + str(
                             message.from_user.id))
      except:
        if 'group' in message.chat.type or 'supergroup' in message.chat.type:
          print('wkwkwk')
        else:
          bot.reply_to(message, f"URl Tidak Dapat diproses {url}")


  def shortenerFind(main, second, message, text, user_sender):
    urlArray = findUrl(text)
    for url in urlArray:
      try:
        sl = shortLink(url, message)
        bot.reply_to(message, sl)
        if message.from_user.username:
          bot.send_message(main, str(sl) + ' message from @' + user_sender)
          bot.send_message(second, str(sl) + ' message from @' + user_sender)
        else:
          bot.send_message(main,
                           str(sl) + ' message from tg://openmessage?user_id=' + str(
                             message.from_user.id))
          bot.send_message(second, str(sl) + ' message from tg://openmessage?user_id=' + str(
            message.from_user.id))
      except:
        if 'group' in message.chat.type or 'supergroup' in message.chat.type:
          print('wkwkwk')
        else:
          bot.reply_to(message, f"URl Tidak Dapat diproses {url}")


  def lazadaFind(main, second, message, text, user_sender):
    urlArray = findUrl(text)
    for url in urlArray:
      try:
        refferUrl = spesificUrl(url)
        bot.reply_to(message, refferUrl)
        if message.from_user.username:
          bot.send_message(main, str(refferUrl) + ' message from @' + user_sender)
          bot.send_message(second, str(refferUrl) + ' message from @' + user_sender)
        else:
          bot.send_message(main,
                           str(refferUrl) + ' message from tg://openmessage?user_id=' + str(
                             message.from_user.id))
          bot.send_message(second,
                           str(refferUrl) + ' message from tg://openmessage?user_id=' + str(
                             message.from_user.id))
      except:
        if 'group' in message.chat.type or 'supergroup' in message.chat.type:
          print('wkwkwk')
        else:
          bot.reply_to(message, f"URl Tidak Dapat diproses {url}")


  def specialLazadaFind(main, second, message, text, user_sender):
    urlArray = findUrl(text)
    for url in urlArray:
      try:
        refferUrl = check_redirect(url, message)
        if message.from_user.username:
          bot.send_message(main, str(refferUrl) + ' message from @' + user_sender)
          bot.send_message(second, str(refferUrl) + ' message from @' + user_sender)
        else:
          bot.send_message(main,
                           str(refferUrl) + ' message from tg://openmessage?user_id=' + str(
                             message.from_user.id))
          bot.send_message(second,
                           str(refferUrl) + ' message from tg://openmessage?user_id=' + str(
                             message.from_user.id))
      except:
        if 'group' in message.chat.type or 'supergroup' in message.chat.type:
          print('wkwkwk')
        else:
          bot.reply_to(message, f"URl Tidak Dapat diproses {url}")


  @bot.message_handler(commands=['start'])
  def send_welcome(message):
    database(message)
    if message.from_user.username:
      bot.send_message(group1, '@' + message.from_user.username + ' : ' + message.text)
    else:
      bot.send_message(group1, 'tg://openmessage?user_id=' + str(message.from_user.id) + ' : ' + message.text)
    bot.reply_to(message, 'Ini adalah bot pribadi, bot akan merespon apabila anda termasuk dalam whitelist.')

  @bot.message_handler(content_types=["text", "sticker", "pinned_message", "photo", "audio","document"])
  def action_start(message):
    id_grup = str(message.chat.id)
    user_sender = message.from_user.username or message.from_user.first_name
    user_id = str(message.from_user.id)
    shopeeUrl = ['shp.ee', 'shope.ee', 'shpe.ee', 'Shp.ee', 'Shopee.ee', 'Shpe.ee']
    adminChannel = False
    if message.caption:
      text = message.caption
    elif message.text:
      text = message.text
    else:
      text = 'null'
    try:
      if '1001504966450' in id_grup or '1001571254101' in id_grup or '1001561463847' in id_grup :
        if text == 'tag' or text == 'Tag':
          if '1001504966450' in id_grup or '1001571254101' in id_grup or '1001561463847' in id_grup:
            bot.reply_to(message, '⚠️ TAG️ ⚠️ \n\n@trustyfriend @mretinap @Anakmamahcory @faizfanaufa @xarief')
            bot.reply_to(message, '⚠️ TAG️ ⚠️ \n\n@philadelhpia @kurniatot @Rnxp5 @yowazzzup ')
        elif 'tokopedia.link' in text:
          # print(text)
          urlArray = findUrl(text)
          # print(urlArray)
          for url in urlArray:
            try:
              tokopediaUrl = tokopedia(url)
              bot.reply_to(message, tokopediaUrl)
            except:
              bot.reply_to(message, f"URl Tidak Dapat diproses {url}")
        elif 'shp.ee' in text or 'shop.ee' in text or 'shpe.ee' in text or 'shope.ee' in text:
          urlArray = findUrl(text)
          for url in urlArray:
            try:
              shopeeUrl = shopee(url)
              bot.reply_to(message, shopeeUrl)
            except:
              if 'group' in message.chat.type or 'supergroup' in message.chat.type:
                print('wkwkwk')
              else:
                bot.reply_to(message, f"URl Tidak Dapat diproses {url}")
        elif '3.jd.id' in text:
          urlArray = findUrl(text)
          for url in urlArray:
            try:
              refferUrl = spesificUrl(url)
              bot.reply_to(message, refferUrl)
            except:
              bot.reply_to(message, f"URl Tidak Dapat diproses {url}")
        elif 'c.lazada.co.id' in text:
          urlArray = findUrl(text)
          for url in urlArray:
            try:
              refferUrl = spesificUrl(url)
              bot.reply_to(message, refferUrl)
            except:
              bot.reply_to(message, f"URl Tidak Dapat diproses {url}")
        elif 's.lazada.co.id' in text or 'racun.id' in text or 'goeco.mobi' in text:
          urlArray = findUrl(text)
          for url in urlArray:
            try:
              check_redirect(url, message)
            except Exception as e:
              bot.reply_to(message, f"URl Tidak Dapat diproses {url}")
        elif 's.id' in text or 'bit.ly' in text:
          urlArray = findUrl(text)
          for url in urlArray:
            try:
              sl = shortLink(url, message)
              bot.reply_to(message, sl)
            except:
              bot.reply_to(message, f"URl Tidak Dapat diproses {url}")
        elif 'blibli.app.link' in text:
          urlArray = findUrl(text)
          for url in urlArray:
            try:
              blibliUrl = blibli(url)
              bot.reply_to(message, blibliUrl)
            except:
              bot.reply_to(message, f"URl Tidak Dapat diproses {url}")
        elif 'invol.co' in text or 'styledo.co' in text or 'invl.io' in text or 'invle.co' in text:
          urlArray = findUrl(text)
          for url in urlArray:
            try:
              premiumLink = premiumUrl(url)
              print(premiumLink)
              bot.reply_to(message, premiumLink)
            except:
              bot.reply_to(message, f"URl Tidak Dapat diproses {url}")
        elif 'shopee.co.id' in text:
          urlArray = findUrl(text)
          for url in urlArray:
            try:
              if 'wallet/angbao' in url:
                print('nothing')
              elif '?' in url:
                head, sep, tail = url.partition('?')
                bot.reply_to(message, head)
            except:
              bot.reply_to(message, f"URl Tidak Dapat diproses {url}")
        elif 'tokopedia.com' in text:
          urlArray = findUrl(text)
          for url in urlArray:
            try:
              if '?' in url:
                head, sep, tail = url.partition('?')
                bot.reply_to(message, head)
            except:
              bot.reply_to(message, f"URl Tidak Dapat diproses {url}")
        elif '!banuser' in text:
          x = text.replace('!banuser ', '')
          if 'Rnxp5' in user_sender or 'Rxp69' in user_sender or 'mretinap' in user_sender:
            user_id = str(x)
            df = requests.get(
              'https://api.telegram.org/bot5297390328:AAFt7HUBnr2oPfsxYerNDq7Lcy3jBDZFvzM/BanChatMember?chat_id=-1001494559873&user_id=' + user_id).content
            bs = requests.get(
              'https://api.telegram.org/bot5297390328:AAFt7HUBnr2oPfsxYerNDq7Lcy3jBDZFvzM/BanChatMember?chat_id=-1001333654036&user_id=' + user_id).content
            dfCh = requests.get(
              'https://api.telegram.org/bot5297390328:AAFt7HUBnr2oPfsxYerNDq7Lcy3jBDZFvzM/BanChatMember?chat_id=-1001183067327&user_id=' + user_id).content
            bsCh = requests.get(
              'https://api.telegram.org/bot5297390328:AAFt7HUBnr2oPfsxYerNDq7Lcy3jBDZFvzM/BanChatMember?chat_id=-1001701785578&user_id=' + user_id).content
            dataDF = json.loads(df)
            bot.reply_to(message, 'DF ' + str(dataDF))
            dataBS = json.loads(bs)
            bot.reply_to(message, 'BS ' + str(dataBS))
            dataDFCH = json.loads(dfCh)
            bot.reply_to(message, 'DF ' + str(dataDFCH))
            dataBSCH = json.loads(bsCh)
            bot.reply_to(message, 'BS ' + str(dataBSCH))
        elif '!banch' in text:
          x = text.replace('!banch ', '')
          if 'Rnxp5' in user_sender or 'Rxp69' in user_sender or 'mretinap' in user_sender:
            user_id = str(x)
            df = requests.get(
              'https://api.telegram.org/bot5297390328:AAFt7HUBnr2oPfsxYerNDq7Lcy3jBDZFvzM/banChatSenderChat?chat_id=-1001183067327&sender_chat_id=-100' + user_id).content
            bs = requests.get(
              'https://api.telegram.org/bot5297390328:AAFt7HUBnr2oPfsxYerNDq7Lcy3jBDZFvzM/banChatSenderChat?chat_id=-1001494559873&sender_chat_id=-100' + user_id).content
            dataDF = json.loads(df)
            bot.reply_to(message, 'DF ' + str(dataDF))
            dataBS = json.loads(bs)
            bot.reply_to(message, 'BS ' + str(dataBS))

            dfCH = requests.get(
              'https://api.telegram.org/bot5297390328:AAFt7HUBnr2oPfsxYerNDq7Lcy3jBDZFvzM/banChatSenderChat?chat_id=-1001494559873&sender_chat_id=-100' + user_id).content
            bsCH = requests.get(
              'https://api.telegram.org/bot5297390328:AAFt7HUBnr2oPfsxYerNDq7Lcy3jBDZFvzM/banChatSenderChat?chat_id=-1001701785578&sender_chat_id=-100' + user_id).content
            dataDFCH = json.loads(dfCH)
            bot.reply_to(message, 'DF ' + str(dataDFCH))
            dataBSCH = json.loads(bsCH)
            bot.reply_to(message, 'BS ' + str(dataBSCH))

        elif text == 'null':
          print('')
        else:
          print('')
      else:
        database(message)
        sendMessage(group1, message, text, user_sender)
    except KeyError:
      if '1001504966450' in id_grup or username in user_sender:
        print('nothing we can do')
      else:
        # bot.reply_to(message, 'vania gagal memproses pesan ini, harap kirimkan ulang. apabila error masih berlanjut silahkan hubungi @Rnxp5')
        if message.from_user.username:
          bot.send_message(group1, 'Pesan ini gagal diproses: @' + user_sender + ' : ' + text)
        else:
          bot.send_message(group1, 'Pesan ini gagal diproses: tg://openmessage?user_id=' + str(
            message.from_user.id) + ' : ' + text)


  print('bot start running')
  while True:
    try:
      bot.polling()
    except:
      continue

