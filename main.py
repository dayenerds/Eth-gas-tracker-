import os
import requests
import time
from telegram import Bot

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
GAS_THRESHOLD = 30  # Alert if gas is below this value in Gwei

bot = Bot(token=BOT_TOKEN)

def fetch_gas_price():
    url = "https://api.etherscan.io/api?module=gastracker&action=gasoracle&apikey=YourEtherscanAPIKey"
    try:
        response = requests.get(url)
        data = response.json()
        if data["status"] == "1":
            return int(data["result"]["SafeGasPrice"])
    except Exception as e:
        print("Error fetching gas price:", e)
    return None

def main():
    while True:
        gas = fetch_gas_price()
        if gas and gas < GAS_THRESHOLD:
            bot.send_message(chat_id=CHAT_ID, text=f"⚠️ Low Gas Alert: {gas} Gwei")
        time.sleep(300)

if __name__ == "__main__":
    main()
