# Gas Alert Bot

This bot checks Ethereum gas prices using Etherscan API and alerts users on Telegram when gas price drops below a threshold.

## Features
- Uses Etherscan API to fetch gas prices
- Sends alerts via Telegram when gas < 30 Gwei

## Setup
1. Clone this repo
2. Create a `.env` file using the `.env.example` as a template
3. Run the bot with Python 3

## Run
```bash
pip install -r requirements.txt
python main.py
```
