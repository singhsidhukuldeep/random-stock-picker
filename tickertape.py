def tickertape_company_profile(st, components, exchange, symbol):
    st.write("### Company Profile")
    components.html(
        """
            <div class="tradingview-widget-container">
                <div class="tradingview-widget-container__widget"></div>
                <div class="tradingview-widget-copyright">
                    <a href="https://in.tradingview.com/symbols/$$exchange$$-$$symbol$$/" rel="noopener" target="_blank">
                    <!-- <span class="blue-text">$$symbol$$ Profile</span></a> Powered by TradingView -->
                </div>
                <script type="text/javascript" 
                src="https://s3.tradingview.com/external-embedding/embed-widget-symbol-profile.js" async>
                    {
                    "symbol": "$$exchange$$:$$symbol$$",
                    "width": "100%",
                    "height": 300,
                    "colorTheme": "dark",
                    "isTransparent": false,
                    "locale": "in"
                    }
                </script>
            </div>
        """.replace(
            "$$symbol$$", symbol
        ).replace(
            "$$exchange$$", exchange
        ),
        height=300,
        scrolling=True,
    )


def tickertape_technical_analysis(st, components, exchange, symbol):
    st.write("### Technical Analysis")
    components.html(
        """
            <div class="tradingview-widget-container">
                <div class="tradingview-widget-container__widget"></div>
                <div class="tradingview-widget-copyright">
                    <a href="https://in.tradingview.com/symbols/$$exchange$$-$$symbol$$/technicals/" 
                        rel="noopener" target="_blank">
                </div>
                <script type="text/javascript" 
                    src="https://s3.tradingview.com/external-embedding/embed-widget-technical-analysis.js" async>
                    {
                    "interval": "1m",
                    "width": "100%",
                    "isTransparent": false,
                    "height": 500,
                    "symbol": "$$exchange$$:$$symbol$$",
                    "showIntervalTabs": true,
                    "locale": "in",
                    "colorTheme": "dark"
                    }
                </script>
            </div>
        """.replace(
            "$$symbol$$", symbol
        ).replace(
            "$$exchange$$", exchange
        ),
        height=450,
        scrolling=True,
    )


def tickertape_fundamental_data(st, components, exchange, symbol):

    st.write("### Fundamental Data")
    components.html(
        """
            <div class="tradingview-widget-container">
                <div class="tradingview-widget-container__widget"></div>
                <div class="tradingview-widget-copyright">
                    <a href="https://in.tradingview.com/symbols/$$exchange$$-$$symbol$$/financials-overview/" rel="noopener" target="_blank">
                </div>
                <script type="text/javascript" 
                src="https://s3.tradingview.com/external-embedding/embed-widget-financials.js" async>
                    {
                    "symbol": "$$exchange$$:$$symbol$$",
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
            "$$symbol$$", symbol
        ).replace(
            "$$exchange$$", exchange
        ),
        height=450,
        scrolling=True,
    )
