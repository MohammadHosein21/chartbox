import yfinance as yf


def get_price():
    AAPL = yf.download('AAPL', period='1y')
    AAPL['Candle Type'] = ['Bullish' if close > open else 'Bearish' for close, open in zip(AAPL['Close'], AAPL['Open'])]
    AAPL.index = AAPL.index.strftime('%Y-%m-%d %I:%M:%S %p')
    AAPL.to_excel('AAPL.xlsx')
    print(AAPL)


if __name__ == '__main__':
    get_price()
