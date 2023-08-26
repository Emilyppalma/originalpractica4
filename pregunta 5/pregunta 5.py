import requests
import csv

def get_bitcoin_price():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()
        data = response.json()
        bitcoin_price = data["bpi"]["USD"]["rate_float"]
        return bitcoin_price
    except requests.RequestException as e:
        print("Error fetching Bitcoin price:", e)
        return None

def save_to_txt(price):
    with open("bitcoin_price.txt", "w") as file:
        file.write(str(price))

def save_to_csv(price):
    timestamp = get_timestamp()
    with open("bitcoin_price.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, price])

def get_timestamp():
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def main():
    bitcoin_price = get_bitcoin_price()

    if bitcoin_price is not None:
        print(f"Bitcoin price (USD): {bitcoin_price}")
        save_to_txt(bitcoin_price)
        save_to_csv(bitcoin_price)
        print("Data saved to files.")

if __name__ == "__main__":
    main()
