import pymongo
from flask import Flask, request, redirect, render_template
import time
from hashids import Hashids
import random
import datetime
import requests
import secrets
hashids = Hashids(salt="bebektest")
client = pymongo.MongoClient("mongodb+srv://bebekbengil:BebekCRUD@cluster0.mvr0yit.mongodb.net/?retryWrites=true&w=majority")
dbmain = client.main
dbstats = client.stats
dbval = client.validate
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
@app.route('/')
def hello():
    return {"msg":"OK!"}

@app.route('/validate', methods=["POST"])
def validate():
    origin = request.json["validate"]
    result = dbval.indexCol.insert_one({"url":origin, "ts":time.time(), "date":datetime.datetime.utcfromtimestamp(time.time())})
    print(result, origin)
    return {"status": 200}
headers={
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-language": "en-US,en;q=0.9",
    "sec-ch-ua": "\"Not_A Brand\";v=\"99\", \"Google Chrome\";v=\"109\", \"Chromium\";v=\"109\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
  }

@app.route('/check', methods=["GET"])
def helloa():
  id = request.args["params"]
  print(id)
  if "intip.in" in id:
    if "intip.in" in id:
      pr = requests.get(id, headers=headers).content
      if "Intip.in - 404!" in str(pr):
        return {"status": 404}, 404
      else:
        return {"status": 200}, 200
  elif "tiny.cc" in id:
    p = requests.get(id, headers=headers, allow_redirects=False)
    print(p.status_code)
    if str(p.status_code)[0] == '3' or str(p.status_code)[0] == '2':
      return {"status": 200}, 200
    else:
      return {"status": 404}, 404
  elif "its.id/m" in id:
    pr = requests.get(id, headers=headers).content
    if "Halaman yang Anda cari tidak bisa kami temukan. Mohon cek URL." in str(pr):
      return {"status": 404}, 404
    else:
      return {"status": 200}, 200
  elif "s.id" in id:
    p = requests.get(id, headers=headers, allow_redirects=False)
    print(p.headers["Location"])
    if str(p.headers["Location"]) == "https://home.s.id/404#action":
      return {"status": 404}, 404
    else:
      return {"status": 200}, 200
  p = requests.get(id, headers=headers, allow_redirects=False)
  print(p.status_code)
  if str(p.status_code)[0] == '3' or str(p.status_code)[0] == '2':
    return {"status": 200}, 200
  else:
    return {"status": 404}, 404