## NSE
# https://www.nseindia.com/regulations/listing-compliance/nse-market-capitalisation-all-companies

in_link = "MCAP31032022.xlsx"
out_link = "stocks_data.json"
import pandas as pd

df = pd.read_excel(in_link).dropna()
df.columns = ["sno", "symbol", "name", "cap"]
df = (
    df[pd.to_numeric(df.cap, errors="coerce").notnull()]
    .drop(["sno", "cap"], axis=1)
    .drop_duplicates("symbol")
)  # .set_index('symbol')
df.to_json(out_link, orient="records")
