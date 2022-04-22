import requests
import argparse
import json
import sys
import webbrowser

def parser_error(errmsg):
    print("\tEjemplo: \r\npython " + sys.argv[0] + " -p 3000 -m ARS -t SELL [[USA -h para sabr como usar los parametros]]")
    print("Error: " + errmsg)
    sys.exit()


def parse_args():
    # parse the arguments
    parser = argparse.ArgumentParser(epilog='\tEjemplo: \r\npython ' + sys.argv[0] + " -p 3000 -m ARS -t SELL")
    parser.error = parser_error
    parser._optionals.title = "OPTIONS"
    parser.add_argument('-c', '--cantidad', help="Cantidad a vender", required=False, default= "0")
    parser.add_argument('-m', '--moneda', help='Moneda que quieras obtener (Por defecto: ARS)', required=False, default="ARS")
    parser.add_argument('-t', '--tipo', help='Tipo de operacion BUY/SELL (Por defecto: SELL)', required=False, default="SELL")
    return parser.parse_args()

def peticion(moneda,tipo,cantidad):
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
        "tradeType": tipo,
        "transAmount":  cantidad
    }

    r = requests.post(url, headers=headers, json=data)
    r = json.loads(r.text)
    return r

def procesar_peticion(r):
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

def ejecutar():
    argumentos = parse_args()
    moneda = argumentos.moneda
    tipo = argumentos.tipo
    cantidad = argumentos.cantidad
    todos_los_vendedores = peticion(moneda,tipo,cantidad)
    procesar_peticion(todos_los_vendedores)


if __name__ == "__main__":
    ejecutar()
