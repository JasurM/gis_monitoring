from flask import *
import datetime
from core import *
app = Flask(__name__)


@app.route("/")
def main():
    return "Hello Uzbekistan"

@app.route("/monitoring")
def p_mon():
    return render_template("index.html")

@app.route("/api/monitoring")
def monitoring():
    token, expires = get_token(86400)
    print(token)
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

if __name__ == '__main__':
    app.run(port=1234)

