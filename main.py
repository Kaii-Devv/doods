# main
from flask import Flask, send_file, request, jsonify, render_template, Response
import requests, re, io,os
import random
import numpy as np
from concurrent.futures import ThreadPoolExecutor,as_completed

app = Flask(__name__)


def dump(tok):
  proxy = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&timeout=10000&country=all&ssl=all&anonymity=all').text
  proxies = np.char.replace(proxy.split('\n')[:-1],'\r','')
  with ThreadPoolExecutor(max_workers=500) as pool:
    futures = [pool.submit(check, proxy, tok) for proxy in proxies]
    for future in as_completed(futures):
        result = future.result()
        if result:
            return Response(result.iter_content(chunk_size=2000), content_type='video/mp4')

        

def check(proxy,tok):
  proxy = {
    'http': 'socks4://'+proxy,
    'https': 'socks4://'+proxy
}
  try:
    ses=requests.Session()
    host= 'https://d0o0d.com'
    ses.proxies.update(proxy)
    log2=ses.get(host+"/e/"+tok,headers={'Host': 'd0o0d.com', 'referer': 'https://d0o0d.com/e/', 'accept-encoding': 'gzip', 'user-agent': 'okhttp/4.9.0'},timeout=10)
    if not 'ddos' in log2.text.lower():
        link=host+"/pass_md5/"+re.search("/pass_md5/(.*?)', function",str(log2.text)).group(1)
        result = ses.get(link,headers={"Host": host.replace('https://',''),"referer": log2.url,"accept-encoding": "gzip","cookie": "lang=1","user-agent": "okhttp/4.9.0"}).text+"".join([random.choice('abcdefghijklmnopqrstuvwxyz1234567890') for _ in range(10)])+"?token="+link.split("/")[-1]+"&expiry=1"+"".join([str(random.randrange(1,9)) for _ in range(12)])
        videos = ses.get(result,headers={'Range': 'bytes=0-', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/83.0.144 Chrome/77.0.3865.144 Safari/537.36', 'Referer': 'https://dooood.com/', 'Connection': 'Keep-Alive', 'Accept-Encoding': 'gzip'},stream=True)
        return videos
        #myresult = {'result': result,'IP':proxy['http']}
        # bagaimana agar saya bisa me return myresult ke user
        # dan jika tidak ada error maka ThreadPoolExecutor akan berhenti
    else:pass
  except Exception as e :pass
@app.route('/d/')
def unduh():
  log2=""
  try:
    tok=request.args.get('token')
    if tok:pass
    else:return {'return':'need params token'}
    proxy = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&timeout=10000&country=all&ssl=all&anonymity=all').text
    proxies = np.char.replace(proxy.split('\n')[:-1],'\r','')
    with ThreadPoolExecutor(max_workers=500) as pool:
      futures = [pool.submit(check, proxy, tok) for proxy in proxies]
      for future in as_completed(futures):
          result = future.result()
          try:
                if result.headers['Content-Type']=='video/mp4':
                    pool.shutdown(wait=True)
                    return Response(result.raw, content_type='video/mp4')
          except Exception as e:pass
  except Exception as e:
    return {'result':str(e)}

@app.route('/')
def index():
  return """
  <div>getlink<br>
  <br>
  https://domain/d/<br>

  params : token<br></div>
  <br>
  <br>
  <div>read videos<br>
  <br>
  https://domain/e/<br>
  params : link<br>
  </div>
  """
@app.route('/e/')
def read():
  link = request.args.get('link')
  ip = request.args.get('ip')
  print(request.args)
  if link and ip:
    result = requests.get(link,headers={'Range': 'bytes=0-', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/83.0.144 Chrome/77.0.3865.144 Safari/537.36', 'Referer': 'https://dooood.com/', 'Host': 'no951gt.video-delivery.net', 'Connection': 'Keep-Alive', 'Accept-Encoding': 'gzip','X-Forwarded-For':ip},stream=True)
    return result.raw
  else:return {'return':'need params link'}
#app.run(port=8880,debug=True)

