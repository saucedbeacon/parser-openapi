from flask import Flask, request, redirect, render_template
from flask_cors import CORS
from urllib.parse import unquote, urlparse, parse_qs
import cloudscraper, requests
#client = pymongo.MongoClient("")
#db = client.webapi

app = Flask(__name__)
CORS(app)

def buildReturn(affiliateState:bool, parsedLink, error):
    if error:
        return {
            "error":error,
            "data":None
        }
    else:
        return {
            "error":error,
            "data":{
                "useAffiliate":affiliateState,
                "parsedLink":parsedLink
            }
        }

@app.route('/ping')
def hello():
    return {"msg":"OK!"}

@app.route('/parse', methods=["POST"])
def parse():
    url = request.json["origLink"]
    try:
        if "tokopedia.link" in url:
            if 'http' not in url:
                url = "https://" + url
            s = cloudscraper.create_scraper()
            n = s.get("https://tokopedia.app.link/" + url.split('/')[3], allow_redirects=False).headers['Location']
            use_affiliate = "aff_unique_id" in n.split("?")[1]
            return buildReturn(use_affiliate, str(n.split("?")[0]), False)
        elif 'shp.ee' in url or 'shop.ee' in url or 'shpe.ee' in url or 'shope.ee' in url:
            if 'http' not in url:
                url = "https://" + url
            j = requests.get(url, allow_redirects=False)
            k = urlparse(j.headers["Location"])
            if ('&redir=' in k.query):
                slink = str(unquote(k.query.split('&')[2].replace('redir=', '')))
                sl = slink.split('?')[0]
                locAffState = False
            else:
                slink = str(k.scheme) + "://" + str(k.netloc) + str(k.path.replace('/universal-link/', '/'))
                sl = str(slink)
                locAffState = True
            return buildReturn(locAffState, sl, False)
        elif 'blibli.app.link' in url:
            if 'http' not in url:
                url = "https://" + url
            s = cloudscraper.create_scraper(browser={'browser':'chrome', 'platform':'windows', 'mobile':False, 'desktop':True})
            k = url.split('/')
            p = s.get("https://blibli.app.link/" + k[3], allow_redirects=False)
            n = p.headers['Location']
            lo = n.split("?")[0]
            return buildReturn(False, lo, False)
    except Exception as e:
        print(e)
        return buildReturn(False, False, True)