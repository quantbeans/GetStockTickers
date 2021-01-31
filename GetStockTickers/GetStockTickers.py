import logging
from typing import List

import pandas as pd
import requests

from GetStockTickers.filters import Sectors, Regions


class GetStockTickers:

    def __init__(self,
                 nyse: bool = True,
                 nasdaq: bool = True,
                 amex: bool = True):
        """
        Get stock tickers for nyse, nasdaq and amex exchanges
        :param nyse: get tickers for nyse
        :param nasdaq: get tickers for nasdaq
        :param amex: get tickers for amex
        """
        self.logger = logging.getLogger('GetTickers')

        assert nyse or nasdaq or amex, "Must specify at least one exchange"

        self.dict_exchanges = {'nyse': nyse, 'nasdaq': nasdaq, 'amex': amex}
        self.exchanges = (exchange for exchange, include in self.dict_exchanges.items() if include)

        self.session = requests.Session()
        self.session.headers = {
            'authority': 'old.nasdaq.com',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'cross-site',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'accept-language': 'en-US,en;q=0.9',
            'cookie': 'AKA_A2=A; NSC_W.TJUFEFGFOEFS.OBTEBR.443=ffffffffc3a0f70e45525d5f4f58455e445a4a42378b',
        }
        self.api = 'https://api.nasdaq.com/api/screener/stocks'
        self.base_params = {'download': 'true'}

        self.logger.info(self)

    def __str__(self):
        return f"Get tickers in {self.exchanges} from {self.api}"

    def get_stock_tickers(self,
                          *,
                          region: Regions = None,
                          mcap_min: int = None,
                          mcap_max: int = None,
                          sector: Sectors = None,
                          return_full_df: bool = False
                          ) -> pd.DataFrame or List[str]:
        """
        Get stock tickers for exchanges instantiated.
        Filter by parameters specified.
        :param region: member of Regions ENUM in filter module
        :param mcap_min: market cap in millions
        :param mcap_max: market cap in millions
        :param sector: member of Sectors ENUM in filter module
        :param return_full_df: return full data as df or list of tickers
        :return: tickers as dataframe or list
        """

        params = self.base_params

        if region:
            assert isinstance(region, Regions), \
                'Not a valid region, must be a member of Regions ENUM under the filters module'
            params['region'] = str(region)

        df_data = pd.DataFrame()
        for exchange in self.exchanges:
            params['exchange'] = exchange
            response = self.session.get(self.api, params=params)

            self.logger.info(response.url, response.status_code)

            json = response.json()['data']['rows']
            df = pd.DataFrame(json)
            df['exchange'] = exchange

            if df_data.empty:
                df_data = df
            else:
                df_data = df_data.append(df)

        if mcap_min:
            df_data = df_data[df_data['marketCap'] >= mcap_min]

        if mcap_max:
            df_data = df_data[df_data['marketCap'] <= mcap_max]

        if sector:
            assert isinstance(sector, Sectors), \
                'Not a valid sector, must be a member of Sectors ENUM under the filters module'
            df_data = df_data[df_data['sector'] == str(sector)]

        self.logger.info(f'Returning {len(df_data)} tickers')

        breakpoint()

        if return_full_df:
            return df_data
        else:
            return df_data.symbol.to_list()


if __name__ == '__main__':
    all_tickers = GetStockTickers().get_stock_tickers()
