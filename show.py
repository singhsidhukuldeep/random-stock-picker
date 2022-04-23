from utils import select_one_ranom_stock
import configurations as config
import os.path


def show_exchange(st, components, exchange):
    if os.path.isfile(config.stock_exchanges[exchange].get("data")):
        show_random_stocks(st, components, exchange)
    else:
        show_coming_soon(st, exchange)


def show_random_stocks(st, components, exchange):

    random_result = select_one_ranom_stock(config.stock_exchanges[exchange]["data"])

    st.metric(
        label=f'{random_result["name"]}',
        value=random_result["symbol"],
        delta=config.stock_exchanges[exchange]["display"],
        delta_color="off",
    )

    with st.expander(f"More details about the {random_result['symbol']} stock:"):

        try:
            for fnc in config.stock_exchanges[exchange]["information_display"]:
                fnc(st, components, exchange, symbol=random_result["symbol"])

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


def show_coming_soon(st, exchange):
    with st.expander(f"{config.stock_exchanges[exchange]['display']} coming soon..."):
        st.info(
            f"""
                Want to contribute?

                If you want you can add functionality directly to the code!
            """
        )
        st.success(
            f"""
                See the source code at: 
                https://github.com/singhsidhukuldeep/random-stock-picker
            """
        )
