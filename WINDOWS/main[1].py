from flask import Flask, json, request
import time

app = Flask(__name__)

@app.route('/<digital_currency>/<physical_currency>')
def index(digital_currency, physical_currency):
    currencies = {

  'BTC':{
  'AUD':'46271.31',
  'BRL':'147381.81',
  'CAD':'40675.43',
  'CNY':'221345.55',
  'EUR':'28290.54',
  'GBP':'24304.97',
  'HKD':'241976.91',
  'IDR':'465266573.90',
  'USD':'30902.30'},
    
  'ETH':{
  'AUD':'2846.56',
  'BRL':'9084.46',
  'CAD':'2508.03',
  'CNY':'13651.79',
  'EUR':'1743.89',
  'GBP':'1493.40',
  'HKD':'14875.52',
  'IDR':'28599474.24',
  'USD':'1899.54',},

  'LTC':{
  'AUD':'137.47',
  'BRL':'438.82',
  'CAD':'121.15',
  'CNY':'659.40',
  'EUR':'84.31',
  'GBP':'72.19',
  'HKD':'719.20',
  'IDR':'1382811.92',
  'USD':'91.84',

    }}

    return json.dumps({
        'digital_currency': f'{digital_currency}',
        'physical_currency': f'{physical_currency}',
        'ammount': f'{currencies[digital_currency][physical_currency]}'}
    )

if __name__ == '__main__':
    app.run(port=5000, debug=True, threaded=True)
