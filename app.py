from flask import Flask, render_template,request,redirect
from flask_mysqldb import MySQL
from wazirx_sapi_client.rest import Client
import hmac
import hashlib
import base64
import json
import time
from matplotlib.font_manager import json_load
import requests
import yaml
coin=1
app = Flask(__name__)
#configure db

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'aayushdrisk03'
app.config['MYSQL_DB'] = 'driskapp'

mysql=MySQL(app)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/',methods=['GET','POST']) 

def getValue():
    api_key= request.form['api-key']
    secret_key= request.form['secret-key']
    key = api_key
    secret = secret_key
    secret_bytes = bytes(secret, encoding='utf-8')
    timeStamp = int(round(time.time() * 1000))
    body = {
        "timestamp": timeStamp
    }
    json_body=json.dumps(body,separators=(',', ':'))
    signature = hmac.new(secret_bytes, json_body.encode(), hashlib.sha256).hexdigest()
    if (coin==1):
        url = "https://api.coindcx.com/exchange/v1/users/info"
        url1= "https://api.coindcx.com/exchange/v1/orders/trade_history"
        headers = {
            'Content-Type': 'application/json',
            'X-AUTH-APIKEY': key,
            'X-AUTH-SIGNATURE': signature
        }
        response=requests.post(url,data=json_body,headers=headers)
        response1=requests.post(url1,data=json_body,headers=headers)
        data=response.json();
        data1=response1.json();
        #dummy line, delete later 
        data1=[ { "id": 564389, "order_id": "ee060ab6-40ed-11e8-b4b9-3f2ce29cd280", "side": "buy", "fee_amount": "0.00001129", "ecode": "B", "quantity": 67.9, "price": 0.00008272, "symbol": "SNTBTC", "timestamp":1533700109811} ]
        #print(data['first_name'])
        if (data1 !=None):
            cur=mysql.connection.cursor()
            cur.execute("INSERT INTO user_info(user_id, first_name, last_name, mobile_number,email,id,order_id,side,fee_amount, ecode,quantity,price,symbol,timestamp) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",(data['coindcx_id'],data['first_name'], data['last_name'],data['mobile_number'],data['email'],data1[0]['id'],data1[0]['order_id'],data1[0]['side'],data1[0]['fee_amount'],data1[0]['ecode'],data1[0]['quantity'],data1[0]['price'],data1[0]['symbol'],data1[0]['timestamp']))
            mysql.connection.commit()
            cur.close()
        #data2=json.loads(data)
#       if(data["code"]!=401):
        return redirect('/user_info')
        #return render_template('pass.html', d=data,d1=data1)
#       else :
            #return render_template('index.html',err='Invalid Credentials. Try Again')
        
@app.route('/user_info')
def users():
    cur=mysql.connection.cursor()
    result=cur.execute("SELECT * FROM user_info")
    if result>0:
        userdetails=cur.fetchall()
        return render_template('users.html',u=userdetails)

# main driver function
if __name__ == '__main__':
  
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run()