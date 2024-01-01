# main
from flask import Flask, send_file, request, jsonify, render_template, Response
import requests, re, io, magic,os
import random
import numpy as np
from concurrent.futures import ThreadPoolExecutor

app = Flask(__name__)


proxynp={}
def dump():
  proxy = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&timeout=10000&country=all&ssl=all&anonymity=all').textq
  proxies = np.char.replace(proxy.split('\n')[:-1],'\r','')
  result={}
  with ThreadPoolExecutor(max_workers=500) as pool:
    for proxy in proxies:
      try:
          result = pool.submit(check, proxy)
          if result not False:
              break
      except Exception as e:pass
  return result

def check(proxy):
  global proxynp
  proxy = {
    'http': 'socks4://'+proxy,
    'https': 'socks4://'+proxy
}
  try:
    ses=requests.Session()
    host= 'https://ds2play.com'
    ses.proxies.update(proxy)
    tok=request.args.get('token')
    log2=ses.get(host+"/e/"+tok,headers={"Host": host.replace('https://',''),"referer": host+"/e/"+tok,"accept-encoding": "gzip","cookie": "lang=1; referer=","user-agent": "okhttp/4.9.0"})
    if not 'ddos' in log2.text.lower():
        link=host+"/pass_md5/"+re.search("/pass_md5/(.*?)', function",str(log2.text)).group(1)
        result = ses.get(link,headers={"Host": host.replace('https://',''),"referer": log2.url,"accept-encoding": "gzip","cookie": "lang=1; referer=","user-agent": "okhttp/4.9.0"}).text+"".join([random.choice('abcdefghijklmnopqrstuvwxyz1234567890') for _ in range(10)])+"?token="+link.split("/")[-1]+"&expiry=1"+"".join([str(random.randrange(1,9)) for _ in range(12)])
        return {'result': result,'IP':proxy['http'].replace('socks4://','')}
    else:return False
  except Exception as e :return False

@app.route('/d/')
def unduh():
  log2=""
  try:
    tok=request.args.get('token')
    if tok:pass
    else:return {'return':'need params token'}
    return dump()
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
  print(request.remote_addr)
  if link and ip:
    result = requests.get(link,headers={'Accept': '*/*', 'Accept-Encoding': 'deflate,gzip', 'referer': 'https://doodstream.com', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36', 'Host': re.search('https://(.*?)/',link, 'Connection': 'Keep-Alive','X-Forwarded-For':ip},stream=True)
    return result.raw
  else:return {'return':'need params link'}
#dump()
app.run(host='0.0.0.0', port=81)
#dump()
#print(proxynp)
#unduh('ollbtbz0n0u7')