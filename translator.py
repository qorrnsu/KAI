import os
import sys
import urllib.request
import json

def translate(sentence):
    client_id = "7FaNuEs6sf81ZrJ9hZub"
    client_secret = "OKGyp9fgvy"
    encText = urllib.parse.quote(sentence)
    data = "source=ko&target=en&text=" + encText
    url = "https://openapi.naver.com/v1/papago/n2mt"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read().decode("utf-8")
        return json.loads(response_body)
    else:
        return rescode



