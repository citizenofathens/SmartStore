from store_token import get_token
import sys
import pybase64
import os
import time
import requests
print(os.getcwd()) 

url = "https://api.commerce.naver.com/external/v2/products"
access_token = get_token(client_id='3lBotoGaXnCVyi4gHQTwPD', client_secret='$2a$04$/luz.NNHJfCzpKxYpWX8N.') 
# 반품교환지 주소와 출고지 주소 스토어에서 확인하거나 get_exist_product로 등록된 상품으로부터 json 정보 가져와서 어떻게 등록되어있는 지 확인한다

#returnAddressId :104889787
#shippingAddressId :104889788
data='{"originProduct":{"statusType":"SALE","saleType":"NEW","leafCategoryId":"50001064","name":"천장몰딩 마이너스몰딩","images":{"representativeImage":{"url":"http://shop1.phinf.naver.net/20221201_9/1669872265481Sj4K3_JPEG/2502711482344407_1905494223.jpg"},"optionalImages":[]},"detailContent":"세부내용입력","salePrice":4000,"stockQuantity":2997,"deliveryInfo":{"deliveryType":"DELIVERY","deliveryAttributeType":"NORMAL","deliveryCompany":"KDEXP","deliveryBundleGroupUsable":false,"deliveryFee":{"deliveryFeeType":"UNIT_QUANTITY_PAID","baseFee":3500,"repeatQuantity":10,"deliveryFeePayType":"COLLECT_OR_PREPAID","deliveryFeeByArea":{"deliveryAreaType":"AREA_2","area2extraFee":5000},"differentialFeeByArea":"8000"},"claimDeliveryInfo":{"returnDeliveryCompanyPriorityType":"PRIMARY","returnDeliveryFee":6000,"exchangeDeliveryFee":12000,"shippingAddressId":104889788,"returnAddressId":104889787,"freeReturnInsuranceYn":false},"installationFee":false},"detailAttribute":{"afterServiceInfo":{"afterServiceTelephoneNumber":"063-111-2222","afterServiceGuideContent":"A/S안내"},"originAreaInfo":{"originAreaCode":"00","content":"국산","plural":false},"optionInfo":{"simpleOptionSortType":"CREATE","optionSimple":[],"optionCustom":[],"optionCombinationSortType":"CREATE","optionCombinationGroupNames":{"optionGroupName1":"색상"},"optionCombinations":[{"id":"","optionName1":"중백색","stockQuantity":999,"price":0,"usable":true},{"id":"","optionName1":"노랑","stockQuantity":999,"price":0,"usable":true},{"id":"","optionName1":"파랑","stockQuantity":999,"price":0,"usable":true}],"standardOptionGroups":[],"useStockManagement":true,"optionDeliveryAttributes":[]},"supplementProductInfo":{"sortType":"CREATE","supplementProducts":[]},"purchaseReviewInfo":{"purchaseReviewExposure":true},"taxType":"TAX","certificationTargetExcludeContent":{"kcCertifiedProductExclusionYn":"TRUE"},"sellerCommentUsable":false,"minorPurchasable":true,"productInfoProvidedNotice":{"productInfoProvidedNoticeType":"FURNITURE","furniture":{"returnCostReason":"0","noRefundReason":"0","qualityAssuranceStandard":"0","compensationProcedure":"0","troubleShootingContents":"0","itemName":"상품상세참조","certificationType":"상품상세참조","color":"상품상세참조","components":"상품상세참조","material":"상품상세참조","manufacturer":"상품상세참조","importer":"상품상세참조","producer":"상품상세참조","size":"상품상세참조","installedCharge":"상품상세참조","warrantyPolicy":"상품상세참조","afterServiceDirector":"상품상세참조"}},"itselfProductionProductYn":false,"seoInfo":{"pageTitle":"영림 천장몰딩","metaDescription":"영림 천장 마이너스 몰딩 다양한 색상 제작 가능","sellerTags":[{"code":308797,"text":"천장몰딩"},{"text":"마이너스"},{"text":"천장마이너스"}]}},"customerBenefit":{}},"smartstoreChannelProduct":{"storeKeepExclusiveProduct":false,"naverShoppingRegistration":true,"channelProductDisplayStatusType":"ON"}}'

headers = {
    'Authorization': f"Bearer {access_token}" ,
    'content-type': "application/json"
    }

response = requests.request("POST", url, headers=headers, data=data.encode('utf-8'))

print(response.text)

