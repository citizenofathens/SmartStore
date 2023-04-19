
# import requests
#
#
# # 인증 정보
# client_id = "클라이언트 아이디"
# client_secret = "클라이언트 시크릿"
#
# # access token 발급
# url = "https://nid.naver.com/oauth2.0/token"
# params = {
#     "grant_type": "client_credentials",
#     "client_id": client_id,
#     "client_secret": client_secret,
# }
# response = requests.get(url, params=params)
# access_token = response.json()["access_token"]
#
# # 상품 등록 API
# url = "https://api-seller.naver.com/rest/v1/goods"
# headers = {
#     "Authorization": f"Bearer {access_token}",
#     "Content-Type": "application/json",
# }

import json
import requests
import bcrypt
import pybase64
import time
import urllib.request
import urllib.parse

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
print(f'발급된 토큰 : ', access_token)
# 상품 등록 API 호출을 위한 URL
url = "https://api-seller.naver.com/rest/v1/goods"

# 상품 정보
product = {
    "vendorId": "YOUR_VENDOR_ID",
    "displayCategoryCode": "YOUR_DISPLAY_CATEGORY_CODE",
    "name": "Product A",
    "content": "This is a product A",
    "brand": "Brand A",
    "deliveryMethod": "DELIVERY",
    "deliveryCompanyCode": "YOUR_DELIVERY_COMPANY_CODE",
    "deliveryChargeType": "PAID",
    "deliveryCharge": "5000",
    "deliveryChargeOnReturn": "FREE",
    "remoteAreaDeliverable": "N",
    "returnCenterCode": "YOUR_RETURN_CENTER_CODE",
    "returnChargeName": "YOUR_RETURN_CHARGE_NAME",
    "returnCharge": "5000",
    "returnChargeVendor": "N",
    "afterServiceInformation": "YOUR_AFTER_SERVICE_INFORMATION",
    "afterServiceContactNumber": "YOUR_AFTER_SERVICE_CONTACT_NUMBER",
    "outboundShippingPlaceCode": "YOUR_OUTBOUND_SHIPPING_PLACE_CODE",
    "maximumBuyCount": "100",
    "searchTags": [
        "Product A",
        "Brand A"
    ],
    "images": [
        {
            "imageOrder": 0,
            "imageTypeCode": "MA",
            "vendorPath": "https://image1.jpg"
        },
        {
            "imageOrder": 1,
            "imageTypeCode": "ETC",
            "vendorPath": "https://image2.jpg"
        }
    ],
    "attributes": [
        {
            "attributeId": "COLOR",
            "attributeValue": "BLACK"
        },
        {
            "attributeId": "SIZE",
            "attributeValue": "M"
        }
    ],
    "options": [
        {
            "optionId": "COLOR",
            "optionValueId": "BLACK"
        },
        {
            "optionId": "SIZE",
            "optionValueId": "M"
        }
    ],
    "items": [
        {
            "itemName": "Product A - BLACK / M",
            "originalPrice": "10000",
            "salePrice": "9000",
            "maximumBuyCount": "10",
            "stockQuantity": "100",
            "sellerProductId": "YOUR_SELLER_PRODUCT_ID",
            "sellerProductItemCode": "YOUR_SELLER_PRODUCT_ITEM_CODE",
            "barcode": "YOUR_BARCODE",
            "certifications": [
                {
                    "certificationTypeCode": "ECO",
                    "certificationCode": "YOUR_CERTIFICATION_CODE"
                }
            ]
        }
    ]
}

# API 호출을 위한 headers 설정
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + access_token,
    "X-HTTP-Method-Override": "POST"
}

# API 호출
response = requests.post(url, headers=headers, data=json.dumps(product))

# API 호출 결과 출력
print(response.json())

