
import requests
import json
import time
import bcrypt
import pybase64
import urllib

def get_token(client_id, client_secret, type_="SELF") -> str:
    timestamp = str(int((time.time()-3) * 1000))
    pwd = f'{client_id}_{timestamp}'
    hashed = bcrypt.hashpw(pwd.encode('utf-8'), client_secret.encode('utf-8'))
    client_secret_sign = pybase64.standard_b64encode(hashed).decode('utf-8')

    headers = {"content-type": "application/x-www-form-urlencoded"}
    data_ = {
        "client_id": client_id,
        "timestamp": timestamp,
        "client_secret_sign": client_secret_sign,
        "grant_type": "client_credentials",
        "type": type_
    }

    query = urllib.parse.urlencode(data_)
    url = 'https://api.commerce.naver.com/external/v1/oauth2/token?' + query
    res = requests.post(url=url, headers=headers)
    res_data = res.json()

    while True:
        if 'access_token' in res_data:
            token = res_data['access_token']
            return token
        else:
            print(f'[{res_data}] 토큰 요청 실패')
            time.sleep(1)
#https://apicenter.commerce.naver.com/ko/member/application/manage/detail;id=3lBotoGaXnCVyi4gHQTwPD 애플리케이션ID, 애플리케이션시크릿
#token = get_token(client_id='애플리케이션ID', client_secret='애플리케이션시크릿')
access_token = get_token(client_id='3lBotoGaXnCVyi4gHQTwPD', client_secret='$2a$04$/luz.NNHJfCzpKxYpWX8N.')


originProductNo = "8013116003"


url = f"https://api.commerce.naver.com/external/v2/products/origin-products/{originProductNo}"


headers = { 'Authorization':access_token }

response = requests.get(url, headers=headers)
print(response.text)