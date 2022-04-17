import streamlit as st
import streamlit.components.v1 as components
import nse
import configurations as config

st.set_page_config(layout="wide", page_title="Random Stock Picker")

st.title("Random Stock Picker 📈 ")

# hide menu
st.markdown(
    """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
    """,
    unsafe_allow_html=True,
)

# hide metric arrow
st.write(
    """
        <style>
        [data-testid="stMetricDelta"] svg {
            display: none;
        }
        </style>
    """,
    unsafe_allow_html=True,
)

stock_exchange_option = st.selectbox(
    "Stock exchange: ", map(lambda x: x.get("display"), config.stock_exchanges.values())
)

refresh_btn = st.button("Pick another Random Stock", key="refresher1")

refresh_btn = True
while refresh_btn:
    refresh_btn = False
    if stock_exchange_option == config.stock_exchanges["NSE"].get("display"):
        nse.show_random_stocks(st, components)
    elif stock_exchange_option == config.stock_exchanges["NASDAQ"].get("display"):
        st.write(f'{config.stock_exchanges["NASDAQ"].get("display")} Coming soon...')
    pass


refresh_btn = st.button("Pick another Random Stock", key="refresher2")

st.markdown("""---""")

st.info(
    """ 
        👉 Buy your own stocks from 
        [Groww](https://groww.app.link/refe/kuldeep8939658), [IndMoney](https://indmoney.onelink.me/RmHC/81a4b732), [Zerodha](https://zerodha.com/?c=NO1458)
    """
)

st.success(
    """
        Share this page: 
        https://share.streamlit.io/singhsidhukuldeep/random-stock-picker/main/app.py
    """
)

with st.expander("How this works"):
    st.info(
        """
            There has been ample study where absolutely random selection beats 
            the stock picks/portfolios created by experts

            So just trying that ¯\_(ツ)_/¯
        """
    )

with st.expander("Where is the source code"):
    st.info(
        """
            ⭐Star⭐ the code at: 
            https://github.com/singhsidhukuldeep/random-stock-picker
        """
    )
