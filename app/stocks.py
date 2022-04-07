
from app.alpha_vantage_service import fetch_stock_data

print("STOCKS REPORT...")

symbol = input("Please input a crypto symbol (default: 'NFLX'): ") or "NFLX"

fetch_stock_data(symbol)