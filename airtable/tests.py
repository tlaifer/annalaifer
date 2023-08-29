import pandas as pd
from util import Util

assert(Util.is_month_start(pd.Timestamp("2014-01-02"))==False)
assert(Util.is_month_start(pd.Timestamp("2014-01-01"))==True)
assert(Util.is_month_end(pd.Timestamp("2014-01-02"))==False)
assert(Util.is_month_end(pd.Timestamp("2014-01-31"))==True)
assert(Util.fractional_month_len(pd.Timestamp("2014-01-01"), pd.Timestamp("2014-01-31")) == 1)
assert(Util.fractional_month_len(pd.Timestamp("2014-01-01"), pd.Timestamp("2014-04-30")) == 4)
assert(Util.fractional_month_len(pd.Timestamp("2014-01-01"), pd.Timestamp("2014-12-31")) == 12)
assert(Util.fractional_month_len(pd.Timestamp("2020-04-15"), pd.Timestamp("2020-09-15")) == 5)
assert(Util.fractional_month_len(pd.Timestamp("2014-01-01"), pd.Timestamp("2014-04-15")) == 3.5)
assert(Util.days_in_month(pd.Timestamp("2014-04-01"))==30)