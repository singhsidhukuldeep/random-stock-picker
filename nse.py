from utils import select_one_ranom_stock
import configurations as config


def show_random_stocks(st, components):
    random_result = select_one_ranom_stock(config.stock_exchanges["NSE"]["data"])

    st.metric(
        label=f'{random_result["name"]}',
        value=random_result["symbol"],
        delta=config.stock_exchanges["NSE"]["display"],
        delta_color="off",
    )

    with st.expander(f"More details about the {random_result['symbol']} stock:"):

        try:

            st.write("### Company Profile")
            components.html(
                """
                    <div class="tradingview-widget-container">
                        <div class="tradingview-widget-container__widget"></div>
                        <div class="tradingview-widget-copyright">
                            <a href="https://in.tradingview.com/symbols/NSE-$$symbol$$/" rel="noopener" target="_blank">
                            <!-- <span class="blue-text">$$symbol$$ Profile</span></a> Powered by TradingView -->
                        </div>
                        <script type="text/javascript" 
                        src="https://s3.tradingview.com/external-embedding/embed-widget-symbol-profile.js" async>
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
                    <div class="tradingview-widget-container">
                        <div class="tradingview-widget-container__widget"></div>
                        <div class="tradingview-widget-copyright">
                            <a href="https://in.tradingview.com/symbols/NSE-$$symbol$$/technicals/" 
                                rel="noopener" target="_blank">
                        </div>
                        <script type="text/javascript" 
                            src="https://s3.tradingview.com/external-embedding/embed-widget-technical-analysis.js" async>
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
                """.replace(
                    "$$symbol$$", random_result["symbol"]
                ),
                height=450,
                scrolling=True,
            )
            st.write("### Fundamental Data")
            components.html(
                """
                    <div class="tradingview-widget-container">
                        <div class="tradingview-widget-container__widget"></div>
                        <div class="tradingview-widget-copyright">
                            <a href="https://in.tradingview.com/symbols/NSE-$$symbol$$/financials-overview/" rel="noopener" target="_blank">
                        </div>
                        <script type="text/javascript" 
                        src="https://s3.tradingview.com/external-embedding/embed-widget-financials.js" async>
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
                """.replace(
                    "$$symbol$$", random_result["symbol"]
                ),
                height=450,
                scrolling=True
            )

        except Exception as exp:
            st.error(
                """
                    Too many people are using, cannot fetch the results
                """
            )
            st.info(
                f"""
                    OOPs something isn't right..
                    Here are more details if you are a nerd:
                    {exp}

                        See the source code at: 
                        https://github.com/singhsidhukuldeep/random-stock-picker
                """
            )
