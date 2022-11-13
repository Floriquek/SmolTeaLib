# this creates our dataframe of tea cups
# we'll just treat this as a module

import pandas as pd

def _tea_df() -> pd.DataFrame:
    tea = {
        "Type": ["black tea", "matcha", "white tea", "green tea"],
        "Price": [15, 20, 13, 15],
    }
    return pd.DataFrame(tea, columns=["Type", "Price"])


#Output for print(_tea_df())
#        Type  Price
# 0  black tea     15
# 1     matcha     20
# 2  white tea     13
# 3  green tea     15
