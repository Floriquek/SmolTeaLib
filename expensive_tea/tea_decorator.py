
import pandas as pd

# create our expensive tea decorator 

class expensive_tea_decorator:

    def __init__(self, f):
        self.f=f

    def __call__(self, *args, **kwargs):

        print("\n" + "Results from expensive tea decorator:" + "\n")
        
        _df = self.f(*args, **kwargs)
        return _df.where(_df.Price > 15, "NA")
        
