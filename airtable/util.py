import pandas as pd
import numpy as np

class Util:
    @classmethod
    def create_df_entry(cls, rec):
        '''
        collapses airtable record into a single dictionary with id & all named fields
        '''
        entry = dict()
        entry.update({'id': rec['id']})
        entry.update({rec['fields']})

    @classmethod
    def is_month_end(cls, d):
        '''
        returns true if date is last day of month
        '''
        return d == d + pd.offsets.MonthEnd(n=0)

    @classmethod
    def is_month_start(cls, d):
        '''
        returns true if date is first day of month
        '''
        return d == d + pd.offsets.MonthBegin(n=0)
    
    @classmethod
    def days_in_month(cls, d):
        '''
        returns number of days in month
        '''
        return d.to_period(freq='D').days_in_month
    
    @classmethod
    def fractional_month_len(cls, start, end):
        months = 0
        if not cls.is_month_start(start):
            months += start.day / cls.days_in_month(start)
            start = start + pd.offsets.MonthBegin(n=1)
        if not (cls.is_month_end(end) or cls.is_month_start(end)):
            months += end.day / cls.days_in_month(end)
            end = end - pd.offsets.MonthBegin(n=1)
        if cls.is_month_end(end):
            end = end + pd.offsets.MonthBegin(n=1)
        months += np.ceil((end - start) / np.timedelta64(1, 'M'))
        return months
