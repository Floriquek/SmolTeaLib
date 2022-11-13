from expensive_tea import expensive_tea_decorator
from expensive_tea import _tea_df

import pandas as pd 

# apply expensive tea decorator 

@expensive_tea_decorator
def expensive_tea( df: pd.DataFrame) -> pd.DataFrame:
    return df

# output expensive cup of tea
print(expensive_tea(df=_tea_df()))