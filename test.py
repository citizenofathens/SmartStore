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


client_id = "3lBotoGaXnCVyi4gHQTwPD"
client_secret = "$2a$04$/luz.NNHJfCzpKxYpWX8N."

# 스마트스토어에 등록할 상품 데이터
# data = {
#     "productId": "상품 ID",
#     "productName": "상품 이름",
#     "productPrice": "상품 가격",
#     # 추가적인 상품 정보들
# }
data='{"originProduct":' \
     '{"statusType":"SALE",' \
     '"saleType":"NEW",' \
     '"leafCategoryId":"50001064",' \
     '"name":"천장몰딩 마이너스몰딩",' \
     '"images":{"representativeImage":{"url":"http://shop1.phinf.naver.net/20221201_9/1669872265481Sj4K3_JPEG/2502711482344407_1905494223.jpg"},' \
     '"optionalImages":[]},' \
     '"detailContent":"세부내용입력",' \
     '"salePrice":4000,' \
     '"stockQuantity":2997,' \
     '"deliveryInfo":' \
     '{"deliveryType":"DELIVERY","deliveryAttributeType":"NORMAL","deliveryCompany":"KDEXP","deliveryBundleGroupUsable":false,"deliveryFee":' \
     '{"deliveryFeeType":"UNIT_QUANTITY_PAID",' \
     '"baseFee":3500,' \
     '"repeatQuantity":10,' \
     '"deliveryFeePayType":"COLLECT_OR_PREPAID",' \
     '"deliveryFeeByArea":{"deliveryAreaType":"AREA_2","area2extraFee":5000},"differentialFeeByArea":"8000"},' \
     '"claimDeliveryInfo":{"returnDeliveryCompanyPriorityType":"PRIMARY","returnDeliveryFee":6000,"exchangeDeliveryFee":12000,"shippingAddressId":936882,"returnAddressId":936883,"freeReturnInsuranceYn":false},"installationFee":false},"detailAttribute":{"afterServiceInfo":{"afterServiceTelephoneNumber":"063-111-2222","afterServiceGuideContent":"A/S안내"},"originAreaInfo":{"originAreaCode":"00","content":"국산","plural":false},"optionInfo":{"simpleOptionSortType":"CREATE","optionSimple":[],"optionCustom":[],"optionCombinationSortType":"CREATE","optionCombinationGroupNames":{"optionGroupName1":"색상"},"optionCombinations":[{"id":"","optionName1":"중백색","stockQuantity":999,"price":0,"usable":true},{"id":"","optionName1":"노랑","stockQuantity":999,"price":0,"usable":true},{"id":"","optionName1":"파랑","stockQuantity":999,"price":0,"usable":true}],"standardOptionGroups":[],"useStockManagement":true,"optionDeliveryAttributes":[]},"supplementProductInfo":{"sortType":"CREATE","supplementProducts":[]},"purchaseReviewInfo":{"purchaseReviewExposure":true},"taxType":"TAX","certificationTargetExcludeContent":{"kcCertifiedProductExclusionYn":"TRUE"},"sellerCommentUsable":false,"minorPurchasable":true,"productInfoProvidedNotice":{"productInfoProvidedNoticeType":"FURNITURE","furniture":{"returnCostReason":"0","noRefundReason":"0","qualityAssuranceStandard":"0","compensationProcedure":"0","troubleShootingContents":"0","itemName":"상품상세참조","certificationType":"상품상세참조","color":"상품상세참조","components":"상품상세참조","material":"상품상세참조","manufacturer":"상품상세참조","importer":"상품상세참조","producer":"상품상세참조","size":"상품상세참조","installedCharge":"상품상세참조","warrantyPolicy":"상품상세참조","afterServiceDirector":"상품상세참조"}},"itselfProductionProductYn":false,"seoInfo":{"pageTitle":"영림 천장몰딩","metaDescription":"영림 천장 마이너스 몰딩 다양한 색상 제작 가능","sellerTags":[{"code":308797,"text":"천장몰딩"},{"text":"마이너스"},{"text":"천장마이너스"}]}},"customerBenefit":{}},"smartstoreChannelProduct":{"storeKeepExclusiveProduct":false,"naverShoppingRegistration":true,"channelProductDisplayStatusType":"ON"}}'


# API 호출
# url = "https://openapi.naver.com/v1/product/"
url = "https://api.commerce.naver.com/external/v2/products"

# headers = {
#     "Content-Type": "application/json",
#     "X-Naver-Client-Id": client_id,
#     "X-Naver-Client-Secret": client_secret,
# }
headers = {
    'Authorization': access_token,
    'content-type': "application/json"
    }

# response = requests.post(url, headers=headers, data=json.dumps(data))




response = requests.request("POST", url, headers=headers, data=data.encode('utf-8'))


# API 호출 결과 출력
print(response.json())