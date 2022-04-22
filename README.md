# Sobre la herramienta

Esta herramienta está programada en Python 3.10 y está diseñada para obtener la cotización del USDT de Binance P2P

# Argumentos

La herramienta tiene tres argumentos posibles:
- -c CANTIDAD [Dentro de este argumento se ingresa la cantidad de dinero] (No es obligatorio)
- -t TIPO [Este argumento determina el tipo de operación, puede ser BUY para compra o SELL para venta] (No es obligatorio)
- -m MONEDA [Este argumento determina la moneda FIAT que se quiere utilizar, por defecto es ARS] (No es obligatorio)

# Instalar

`git clone https://github.com/rodriguezd0/Precios-de-Binance/`

# Modulos que se necesitan

Esta herramienta necesita **argparse** y **requests**, puede instarlas con
`pip install -r requirements.txt`
