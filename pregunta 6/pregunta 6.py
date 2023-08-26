import requests
import sqlite3
from datetime import datetime

def get_bitcoin_price():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()
        data = response.json()
        bitcoin_prices = {
            "USD": data["bpi"]["USD"]["rate_float"],
            "GBP": data["bpi"]["GBP"]["rate_float"],
            "EUR": data["bpi"]["EUR"]["rate_float"]
        }
        return bitcoin_prices
    except requests.RequestException as e:
        print("Error fetching Bitcoin price:", e)
        return None

def create_table(conn):
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS bitcoin
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       timestamp TEXT,
                       usd_price REAL,
                       gbp_price REAL,
                       eur_price REAL)''')
    conn.commit()

def insert_data(conn, prices):
    cursor = conn.cursor()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute('''INSERT INTO bitcoin (timestamp, usd_price, gbp_price, eur_price)
                      VALUES (?, ?, ?, ?)''', (timestamp, prices["USD"], prices["GBP"], prices["EUR"]))
    conn.commit()

def main():
    bitcoin_prices = get_bitcoin_price()

    if bitcoin_prices is not None:
        print(f"Bitcoin price (USD): {bitcoin_prices['USD']}")
        
        conn = sqlite3.connect("cryptos.db")
        create_table(conn)
        insert_data(conn, bitcoin_prices)
        conn.close()

        print("Data saved to database.")

if __name__ == "__main__":
    main()
