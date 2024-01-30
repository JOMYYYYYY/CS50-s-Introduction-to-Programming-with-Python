import requests
import sys
import json

try:
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
    else:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        # print(json.dumps(response.json(), indent=2))
        # print("-------")
        # print(response.json()["bpi"]["USD"]["rate"])
        rate_bitcoin_USD = response.json()["bpi"]["USD"]["rate"]
        rate_bitcoin_USD = float(rate_bitcoin_USD.replace(",", ""))
        # print("***->"+str(rate_bitcoin_USD))
        to_usd = rate_bitcoin_USD * n
        s = '{:,.4f}'.format(to_usd)
        print("$" + s)

except requests.RequestException:
    print("request exception.")
