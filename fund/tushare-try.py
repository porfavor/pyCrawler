import tushare as ts

ts.set_token('24d3f9090c9ca88a79ac7d10bfa22fec410b3cd3f12c624e3e82f924621fc8ba')

st = ts.Market()
df = st.MktEqud(ticker='002024', tradeDate='20160119', field='ticker,secShortName,preClosePrice,openPrice,highestPrice,lowestPrice,closePrice,turnoverVol,turnoverRate')
df['ticker'] = df['ticker'].map(lambda x: str(x).zfill(6))
