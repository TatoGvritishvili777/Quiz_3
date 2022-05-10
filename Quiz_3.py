import requests

#მაგალითად USD, EUR, GEL და ა.შ
valuta = input("შეიყვანეთ თქვენთვის სასურველი ვალუტა: ")
raodenoba = int(input("რამდენი კრიპტოვალუტის ფასის ნახვა გსურთ: "))

headers = {
  'X-CMC_PRO_API_KEY': '95450855-34b5-492c-892a-675f371fb73b',
  'Accepts': 'application/json'
}


#მომხმარებელს შეჰყავს რამდენი კრიპტოვალუტის ფასის ნახვა სურს, ათვლა იწყება COINMARKETCAP.COM ზე განთავსებული
#კრიპტოვალუტების მიხედვით, აგრეთვე შეჰყავს რომელ ვალუტაში სურს ფასის ნახვა
params = {
    'start' : '1',
    'limit' : raodenoba,
    'convert' : valuta
}

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

res = requests.get(url, params=params, headers=headers).json()

coins = res['data']

for i in coins:
    print(i['symbol'], i['quote'][valuta]['price'])
