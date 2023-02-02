'''
need pip install flask、requests
'''
import requests as req
import json
from flask import Flask, make_response
#make_response is to resolve cross-origin resource sharing problems
#cross-origin resource sharing (same origin policy)
#1.http(s)
#2.Domain name
#3.port default http port:80 https port:443

'''
Flask initialize
'''
app = Flask(__name__)


'''
Web API (source: https://cafenomad.tw/)
'''
#self made route
#http://192.168.39.130:5000/cafe/taipei<--in html fetch url
@app.route('/taipei', methods=['GET']) # send get request to taipei
def taipei():
    url = 'https://cafenomad.tw/api/v1.2/cafes/taipei'

    res=req.get(url)
    # self-made response and attach cafe list in the response at the same time
    response = make_response(json.dumps(res.json(), ensure_ascii=False))
    response.headers["Content-Type"] = "application/json"
    response.headers['Access-Control-Allow-Origin'] = '*' #allow all access
    return response

@app.route('/hsinchu', methods=['GET'])
#http://192.168.39.130:5000/cafe/hsinchu
def hsinchu():
    url = 'https://cafenomad.tw/api/v1.2/cafes/hsinchu'

    res=req.get(url)
    response = make_response(json.dumps(res.json(), ensure_ascii=False))
    response.headers["Content-Type"] = "application/json"
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response
#http://192.168.39.130:5000/cafe/kaohsiung
@app.route('/kaohsiung', methods=['GET'])
def kaohsiung():
    url = 'https://cafenomad.tw/api/v1.2/cafes/kaohsiung'

    res=req.get(url)
    response = make_response(json.dumps(res.json(), ensure_ascii=False))
    response.headers["Content-Type"] = "application/json"
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


'''
main
'''
if __name__ == '__main__':
    #debug=true will show python err msg otherwise is normal internet err Internal Server Error
    #0.0.0.0 represent all ip can access
    # port need to larger than 1023
    app.run(
        debug=True,
        host='0.0.0.0', 
        port=5000
    )