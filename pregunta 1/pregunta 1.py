import requests

def get_bitcoin_price():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()  # Raises an exception if there's an HTTP error
        data = response.json()
        bitcoin_price = data["bpi"]["USD"]["rate_float"]
        return bitcoin_price
    except requests.RequestException as e:
        print("Error fetching Bitcoin price:", e)
        return None

def main():
    n_bitcoins = float(input("Ingrese la cantidad de Bitcoins que posee: "))
    bitcoin_price = get_bitcoin_price()

    if bitcoin_price is not None:
        total_cost_usd = n_bitcoins * bitcoin_price
        formatted_cost = "${:,.4f}".format(total_cost_usd)
        print(f"El costo actual de {n_bitcoins:.8f} Bitcoins es {formatted_cost} USD.")

if __name__ == "__main__":
    main()
