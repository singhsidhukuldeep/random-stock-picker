import streamlit as st
import streamlit.components.v1 as components
from utils import select_one_ranom_stock


st.set_page_config(layout="wide")
st.title("Random Stock Picker")
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)
option = st.selectbox("Stock exchange: ", tuple(["NSE (🇮🇳)"]))
refresh_btn = st.button("Pick another Random Stock", key="refresher1")
refresh_btn = True
while refresh_btn:
    random_result = select_one_ranom_stock()
    st.metric(label=f'{random_result["name"]}', value=random_result["symbol"])
    st.write('Get more details on Google')
    refresh_btn = False

    with st.expander(f"More details about the {random_result['symbol']} stock:"):

        try:
            st.write("### Stock Info")
            components.html(
                """
            <!-- TradingView Widget BEGIN -->
<div class="tradingview-widget-container">
  <div class="tradingview-widget-container__widget"></div>
  <div class="tradingview-widget-copyright"><a href="https://in.tradingview.com/symbols/NSE-$$symbol$$/" rel="noopener" target="_blank"><span class="blue-text">$$symbol$$ Price Today</span></a> by TradingView</div>
  <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-symbol-info.js" async>
  {
  "symbol": "NSE:$$symbol$$",
  "width": "100%",
  "locale": "in",
  "colorTheme": "dark",
  "isTransparent": false
}
  </script>
</div>
<!-- TradingView Widget END -->
            """.replace(
                    "$$symbol$$", random_result["symbol"]
                ),
                height=200,
            )

            st.write("### Company Profile")
            components.html(
                """
                <div class="tradingview-widget-container">
                <div class="tradingview-widget-container__widget"></div>
                <div class="tradingview-widget-copyright">
                <a href="https://in.tradingview.com/symbols/NSE-$$symbol$$/" rel="noopener" target="_blank">
                <span class="blue-text">$$symbol$$ Profile</span></a> Powered by TradingView</div>
                <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-symbol-profile.js" async>
                {
                "symbol": "NSE:$$symbol$$",
                "width": "100%",
                "height": 300,
                "colorTheme": "dark",
                "isTransparent": false,
                "locale": "in"
                }
                </script>
                </div>
                """.replace(
                    "$$symbol$$", random_result["symbol"]
                ),
                height=300,
                scrolling=True,
            )

            st.write("### Technical Analysis")
            components.html(
                """
            <!-- TradingView Widget BEGIN -->
<div class="tradingview-widget-container">
  <div class="tradingview-widget-container__widget"></div>
  <div class="tradingview-widget-copyright"><a href="https://in.tradingview.com/symbols/NSE-$$symbol$$/technicals/" rel="noopener" target="_blank"><span class="blue-text">Technical Analysis for $$symbol$$</span></a> by TradingView</div>
  <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-technical-analysis.js" async>
  {
  "interval": "1m",
  "width": "100%",
  "isTransparent": false,
  "height": 500,
  "symbol": "NSE:$$symbol$$",
  "showIntervalTabs": true,
  "locale": "in",
  "colorTheme": "dark"
}
  </script>
</div>
<!-- TradingView Widget END -->
            """.replace(
                    "$$symbol$$", random_result["symbol"]
                ),
                height=450,
                scrolling=True,
            )
            st.write("### Fundamental Data")
            components.html(
                """
            <!-- TradingView Widget BEGIN -->
<div class="tradingview-widget-container">
  <div class="tradingview-widget-container__widget"></div>
  <div class="tradingview-widget-copyright"><a href="https://in.tradingview.com/symbols/NSE-$$symbol$$/financials-overview/" rel="noopener" target="_blank"><span class="blue-text">$$symbol$$ Fundamental Data</span></a> by TradingView</div>
  <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-financials.js" async>
  {
  "symbol": "NSE:$$symbol$$",
  "colorTheme": "dark",
  "isTransparent": false,
  "largeChartUrl": "",
  "displayMode": "regular",
  "width": "100%",
  "height": 450,
  "locale": "in"
}
  </script>
</div>
<!-- TradingView Widget END -->
            """.replace(
                    "$$symbol$$", random_result["symbol"]
                ),
                height=450,
                scrolling=True,
            )

        except Exception as exp:
            st.write(
                """
                Too many people are using, cannot fetch the results
            """
            )
            st.info(
                f"""Here are more details if you are a nerd:
            {exp}

            See the source code at: 
            https://github.com/singhsidhukuldeep/random-stock-picker"""
            )


refresh_btn = st.button("Pick another Random Stock", key="refresher2")

st.markdown("""---""")

st.write(""" 👉
Buy your own stocks from 
[Groww](https://groww.app.link/refe/kuldeep8939658), [IndMoney](https://indmoney.onelink.me/RmHC/81a4b732), [Zerodha](https://zerodha.com/?c=NO1458)
""")

st.markdown("""---""")

with st.expander("How this works"):
    st.write(
        """
         There has been ample study where absolutely random selection beats 
         the stock picks/portfolios created by experts

		 So just trying that!...
     """
    )

st.write(
    """See the source code at: 
            https://github.com/singhsidhukuldeep/random-stock-picker"""
)
