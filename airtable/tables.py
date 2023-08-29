from pyairtable.orm import Model, fields as F
from airtable_auth import AirtableAuth

TOKEN = AirtableAuth().token()

BASE_ID = 'appinOK2QUUgmh6ou'
NETWORK_ID = 'tblFrcw35eqbfQZvv'
SEGMENTS_ID = 'tblPuCiBSV9igr46r'


class FinancialDate(Model):
    yyyymm = F.TextField('YYYYMM')

    class Meta:
        base_id = BASE_ID
        api_key = TOKEN
        table_name = 'tblhrTWWPQ7gL17fy'

class Engagement(Model):
    engagement = F.TextField('Engagement')
    start = F.DateField('Start')
    end = F.DateField('End')
    total_amount = F.CurrencyField('Total Amount')

    class Meta:
        base_id = BASE_ID
        api_key = TOKEN
        table_name = 'tblZVLUpKGYjK8mc8'

class EngagementByMonth(Model):
    name = F.TextField("Name")
    month = F.LinkField("Month", FinancialDate)
    engagement = F.LinkField("Engagement", Engagement)
    amount = F.CurrencyField("Amount")

    class Meta:
        base_id = BASE_ID
        api_key = TOKEN
        table_name = "tblBtkWwq2pSz0tNG"