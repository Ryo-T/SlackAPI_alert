#coding: utf-8

import urllib
import urllib2
import platform

url = "https://slack.com/api/chat.postMessage"

params = {'token':'',   # トークン
          'channel':'', # チャンネルID
          'text': ''    # 送信するテキスト
}



def set_text():
    hostname = platform.uname()
    text = "host:"+hostname[1]+"-"
    return text


# 各種パラメータの設定
def set_parameters(params,text):
    alert_params = params
    alert_params['token'] = ''
    alert_params['channel'] = '' 
    alert_params['text'] = text
    return alert_params
     

def send_alert(text):
    global params
    alert_params = set_parameters(params,text)
    
    alert_params = urllib.urlencode(alert_params)
    
    req = urllib2.Request(url)
    
    # ヘッダ追加
    req.add_header('Content-Type', 'application/x-www-form-urlencoded')
    
    # パラメータ追加
    req.add_data(alert_params)
    
    res = urllib2.urlopen(req)
    
    # レスポンス取得
    body = res.read()
    
    # レスポンス表示
    print body

if __name__ == "__main__":
    text = "test"
    send_alert(text)


