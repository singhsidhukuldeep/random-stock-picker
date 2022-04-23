from tickertape import *

stock_exchanges = {
    "NSE": {
        "display": "NSE (🇮🇳)",
        "data": "data/NSE.json",
        "information_display": [
            tickertape_company_profile,
            tickertape_technical_analysis,
            tickertape_fundamental_data,
        ],
    },
    "BSE": {"display": "BSE (🇮🇳)", "data": "data/BSE.json"},
    "NASDAQ": {"display": "NASDAQ (🇺🇸)", "data": "data/NASDAQ.json"},
    "NYSE": {"display": "NYSE (🇺🇸)", "data": "data/NYSE.json"},
}

display_2_exchange = {
    details.get("display"): exchange for exchange, details in stock_exchanges.items()
}
