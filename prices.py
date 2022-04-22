import requests
import json
import sys
import webbrowser


try:
    cantidad = sys.argv[1]
except:
    cantidad = "0"

try:
    moneda = sys.argv[2]
except:
    moneda = "ARS"

url = "https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search"
headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Length": "123",
    "content-type": "application/json",
    "Host": "p2p.binance.com",
    "Origin": "https://p2p.binance.com",
    "Pragma": "no-cache",
    "TE": "Trailers",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0"
}
data = {
    "asset": "USDT",
    "fiat": moneda,
    "merchantCheck": True,
    "page": 1,
    "payTypes": ["MercadoPago"],
    "publisherType": None ,
    "rows": 20,
    "tradeType": "SELL",
    "transAmount":  cantidad
}

r = requests.post(url, headers=headers, json=data)
r = json.loads(r.text)
lista_de_vendedores = []

for i in r['data']:
    vendedor = []
    vendedor.append(i['adv']['price'])
    vendedor.append(i['advertiser']['nickName'])
    vendedor.append(i['advertiser']['userNo'])
    lista_de_vendedores.append(vendedor)

print("VENDEDORES")
for i in range(len(lista_de_vendedores)):
    print(f"{i+1}. El precio es de {lista_de_vendedores[i][0]}. y el vendedor es {lista_de_vendedores[i][1]}.")
print()
eleccion = int(input("Ingresa el numero (0 para salir) : "))-1

if eleccion != -1:
    webbrowser.open("https://p2p.binance.com/es/advertiserDetail?advertiserNo="+lista_de_vendedores[eleccion][2], new=2, autoraise=True)
