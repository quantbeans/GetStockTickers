## Get Stock Tickers

### Overview
This library scrapes [Nasdaq's Stock Screener](https://www.nasdaq.com/market-activity/stocks/screener) for a daily list 
of tickers for the NYSE, NASDAQ amd AMEX exchanges.

Inspired by [get-all-tickers](https://github.com/shilewenuw/get_all_tickers)

### Download
This library is not available on PyPi. To include it in your venv, run:
```
pip install git+https://github.com/estepehcorlin/GetStockTickers.git
```

### Use
Get tickers across NYSE, NASDAQ and AMEX exchanges:
```
from GetStockTickers.GetStockTickers import GetStockTickers
```

*get_stock_tickers* is the main method, it returns a list of tickers:
```
GetStocktickers(nyse=True, nasdaq=True, amex=True).get_stock_tickers()
```

Return full data-set as dataframe: 
symbol|name|lastsale|netchange|pctchange|volume|marketCap|country|ipoyear|industry|sector|url|exchange
```
GetStocktickers().get_stock_tickers(return_full_df=True)
```

Filter tickers by market cap in millions:
```
GetStocktickers().get_stock_tickers(mcap_min = 1000, mcap_max = 10000)
```

Filtering by Region and Sector requires the use of the config in the *filter.py* module.
These ENUMs define the available regions and sectors to filter by.
```
from filters import Sectors, Regions
```

Filter by Region and Sector:
```
GetStocktickers().get_stock_tickers(Regions.NORTH_AMERICA)
GetStocktickers().get_stock_tickers(Sectors.TECHNOLOGY)
```
