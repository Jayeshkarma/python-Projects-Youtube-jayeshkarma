import requests
import json 
import math
import random
URL = 'https://www.sms4india.com/api/v1/sendCampaign'

# get request
def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
  req_params = {
  'apikey':apiKey,
  'secret':secretKey,
  'usetype':useType,
  'phone': phoneNo,
  'message':textMessage,
  'senderid':senderId
  }
  return requests.post(reqUrl, req_params)
data ="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
leng = len(data)
otp =""

for i in range(6):
  otp +=data[math.floor(random.random()*leng)]
# get response
response = sendPostRequest(URL, 'FH0BPB79NFEKGMRTG5Y3Q19NQ2NH15TL', 'AAEEV4CXGIQCKE8R', 'stage', '6265971215', 'JAYESH', ' your 6-digit otp is '+str(otp) )
"""
  Note:-
    you must provide apikey, secretkey, usetype, mobile, senderid and message values
    and then requst to api
"""
