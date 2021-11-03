import requests
import json

PROVINCES = {
    1 : "Қорақолпоғистон Респ.",
    2 : "Андижон вилояти",
    3 : "Бухоро вилояти",
    4 : "Жиззах вилояти",
    5 : "Қашқадарё вилояти",
    6 : "Навоий вилояти",
    7 : "Наманган вилояти",
    8 : "Самарқанд вилояти",
    9 : "Сурхондарё вилояти",
    10 : "Сирдарё вилояти",
    11 : "Тошкент вилояти",
    12 : "Фарғона вилояти",
    13 : "Хоразм вилояти"
}

def get_token(exp):
    url = "https://lis.agro.uz/portal/sharing/rest/generateToken"

    payload = "username=portaladmin&password=AGSPortalUZagro2021&client=referer&referer=https%3A%2F%2Flis.agro.uz%2Fserver%2Frest%2Fservices%2FHosted%2F%D0%9C%D0%BE%D0%BD%D0%B8%D1%82%D0%BE%D1%80%D0%B8%D0%BD%D0%B3%2FFeatureServer%2F0&experies="+ str(exp) + "&f=pjson"
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache"
        }

    response = requests.request("POST", url, data=payload, headers=headers)

    resp = response.json()
    token = resp['token']
    return token, resp['expires']


def get_monitoring(token):
    url = "https://lis.agro.uz/server/rest/services/Hosted/%D0%9C%D0%BE%D0%BD%D0%B8%D1%82%D0%BE%D1%80%D0%B8%D0%BD%D0%B3/FeatureServer/0/query"

    querystring = {"where":"1=1","outFields":"*","returnGeometry":"false","f":"json"}

    headers = {
        'token': token,
        'cache-control': "no-cache"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response.json())
    return response.json()
