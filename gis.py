from flask import *
from core import *
import datetime
from caching import cache
gis = Blueprint('gis', __name__,
    template_folder='templates',
    static_folder='static')

@cache.memoize(3500)
def get_token(exp=3600):
    url = "https://lis.agro.uz/portal/sharing/rest/generateToken"

    payload = "username=portaladmin&password=AGSPortalUZagro2021&client=referer&referer=https%3A%2F%2Flis.agro.uz%2Fserver%2Frest%2Fservices%2FHosted%2F%D0%9C%D0%BE%D0%BD%D0%B8%D1%82%D0%BE%D1%80%D0%B8%D0%BD%D0%B3%2FFeatureServer%2F0&experies="+ str(exp) + "&f=pjson"
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache"
        }

    response = requests.request("POST", url, data=payload, headers=headers)

    resp = response.json()
    token = resp['token']
    print("I called and token : %s "%(token))
    return token


def get_monitoring(token):
    url = "https://lis.agro.uz/server/rest/services/Hosted/%D0%9C%D0%BE%D0%BD%D0%B8%D1%82%D0%BE%D1%80%D0%B8%D0%BD%D0%B3/FeatureServer/0/query"

    querystring = {"where":"1=1","outFields":"*","returnGeometry":"false","f":"json"}

    headers = {
        'token': token,
        'cache-control': "no-cache"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.json()


@gis.route("/page/monitoring")
def p_mon():
    return render_template("gis/index.html")

@gis.route("/test")
def test_s():
    token = get_token()
    
    data = get_monitoring(token)
    return jsonify(data)

@gis.route("/monitoring")
def g_monitoring():
    token = get_token()
    
    data = get_monitoring(token)

    ret_data = []
    data = data['features']
    
    
    today = datetime.date.today()        
    for pr_id,pr_name in PROVINCES.items():
        yes_sum = sum([ x['attributes']['maydoni'] for x in data if x['attributes']['viloyat'] == pr_id and x['attributes']['maydoni'] is not None] )
        today_sum = sum([ x['attributes']['maydoni'] for x in data if x['attributes']['viloyat'] == pr_id and x['attributes']['maydoni'] is not None and datetime.date.fromtimestamp( x['attributes']['created_date'] /1000) == today ] )
        if yes_sum > 0:
            ret_data.append({
                "viloyat" : pr_name,
                "viloyat_id" : pr_id,
                "sum" : yes_sum,
                "sum_today" : today_sum
            })
    return jsonify(ret_data)