import pandas as pd
from utils.period import Period

class PeriodQueries:
    
    @staticmethod
    def filter_records_before_period(records: pd.DataFrame, period: str) -> pd.DataFrame:
        """
        Filters records to include only those before a specified period.
        
        :param records: The DataFrame containing the records to filter.
        :param period: A string in YYYYXZ format (e.g., "202120") as the exclusive upper limit.
        :return: A DataFrame with records before the specified period.
        """
        # Apply the filtering function using Period's is_before_period
        filtered_records = records[records['PERIODO'].apply(lambda p: Period.is_before_period(p, period))]
        
        if filtered_records.empty:
            print(f"No records found before period: {period}")
        
        return filtered_records.reset_index(drop=True)
