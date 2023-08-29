import pandas as pd
import datetime
from util import Util
from tables import FinancialDate, Engagement, EngagementByMonth    

def records_by_field(records, field):
    by_field = dict()
    for record in records:
        by_field[str(getattr(record, field))] = record
    return by_field

def records_by_id(records):
    return records_by_field(records, 'id')

def month_engagement_df_to_records(df):
    records = []
    for _, row in df.iterrows():
        month = row['month']
        engagement_id = row['engagement_id']
        name = str(month) + ' - ' + engagements_by_id[engagement_id].engagement
        records.append(EngagementByMonth(
            name = name,
            engagement = [Engagement(id=engagement_id)],
            month = [FinancialDate(id=dates_by_yyyymm[month].id)],
            amount = row['amount']
        ))
    return records

def engagement_to_month_engagements(engagement):
    date_range = pd.date_range(engagement.start, engagement.end)
    daily_amount = engagement.total_amount / len(date_range)
    daily_rev = []
    for date in date_range:
        daily_rev.append({
            'engagement_id': engagement.id,
            'date': date,
            'amount': daily_amount
        })
    daily_rev_df = pd.DataFrame(daily_rev).set_index('date')
    daily_rev_df['month'] = daily_rev_df.index.to_period('M').to_timestamp().strftime('%Y%m')
    monthly_rev_df = daily_rev_df.groupby(['month','engagement_id'])['amount'].sum().reset_index()
    return month_engagement_df_to_records(monthly_rev_df)

def remove_existing():
    existing_records = EngagementByMonth.all()
    EngagementByMonth.batch_delete(existing_records)

remove_existing()
engagements = Engagement.all()
financial_dates = FinancialDate.all()
dates_by_yyyymm = records_by_field(financial_dates, 'yyyymm')
engagements_by_id = records_by_id(engagements)
new_records = []
for engagement in engagements:
    if (engagement.start and engagement.end and engagement.total_amount):
        new_records.extend(engagement_to_month_engagements(engagement))
EngagementByMonth.batch_save(new_records)