import requests
import argparse
import json
import sys
import webbrowser

def parser_error(errmsg):
    print("\tEjemplo: \r\npython " + sys.argv[0] + " -p 3000 -m ARS -t SELL [[Usa -h para sabr como usar los parametros]]")
    print("Error: " + errmsg)
    sys.exit()


def parse_args():
    parser = argparse.ArgumentParser(epilog='\tEjemplo: \r\npython ' + sys.argv[0] + " -p 3000 -m ARS -t SELL")
    parser.error = parser_error
    parser._optionals.title = "OPTIONS"
    parser.add_argument('-c', '--cantidad', help="Cantidad a vender", required=False, default= "0")
    parser.add_argument('-f', '--fiat', help='Moneda que quieras obtener (Por defecto: ARS)', required=False, default="ARS")
    parser.add_argument('-t', '--tipo', help='Tipo de operacion BUY/SELL (Por defecto: SELL)', required=False, default="SELL")
    return parser.parse_args()


def peticion(fiat,tipo,cantidad):
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
        "fiat": fiat,
        "merchantCheck": True,
        "page": 1,
        "payTypes": None,
        "publisherType": None ,
        "rows": 20,
        "tradeType": tipo,
        "transAmount":  cantidad
    }
    r = requests.post(url, headers=headers, json=data)
    r = json.loads(r.text)
    return r


def imprimir_metodos_de_pago(metodos):
    todos_los_metodos = ""
    for i in metodos:
        todos_los_metodos += i+' '
    return todos_los_metodos


def procesar_peticion(r):
    lista_de_comerciantes = []
    for i in r['data']:
        comerciante = []
        metodos = []
        comerciante.append(i['adv']['price'])
        for k in i['adv']['tradeMethods']:
            metodos.append(k['payType'])
        comerciante.append(metodos)
        comerciante.append(i['advertiser']['nickName'])
        comerciante.append(i['advertiser']['userNo'])
        lista_de_comerciantes.append(comerciante)


    print("COMERCIANTES")
    for i in range(len(lista_de_comerciantes)):
        print(f"{i+1}. El precio es de ${lista_de_comerciantes[i][0]}.   Comerciante: {lista_de_comerciantes[i][2]}.   Metodos de pago: {imprimir_metodos_de_pago(lista_de_comerciantes[i][1])}")
    print()
    try:
        eleccion = int(input("Ingresa el numero (ENTER para salir) : "))-1
        webbrowser.open("https://p2p.binance.com/es/advertiserDetail?advertiserNo="+lista_de_comerciantes[eleccion][3], new=2, autoraise=True)
    except:
        return


def ejecutar():
    argumentos = parse_args()
    fiat = argumentos.fiat
    tipo = argumentos.tipo
    cantidad = argumentos.cantidad
    todos_los_comerciantes = peticion(fiat,tipo,cantidad)
    procesar_peticion(todos_los_comerciantes)


if __name__ == "__main__":
    ejecutar()
