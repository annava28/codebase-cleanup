

from app.alpha_vantage_service import fetch_crypto_data

print("CRYPTO REPORT...")

symbol = input("Please input a crypto symbol (default: 'BTC'): ") or "BTC"

fetch_crypto_data(symbol)