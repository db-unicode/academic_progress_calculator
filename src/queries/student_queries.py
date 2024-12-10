import pandas as pd
from csv_reader.csv_reader import CSVReader  
from utils.period import Period  

class StudentQueries:
    
    @staticmethod
    def get_student_records(student_code: str) -> pd.DataFrame:
        """
        Retrieves records for a specific student by their student code.
        
        :param student_code: The student code to filter records.
        :return: A DataFrame containing the student's records, or logs if not found.
        """
        # Fetch the main data using CSVReader
        df = CSVReader.get_data()
        if df is None:
            print("No data found in CSV.")
            return pd.DataFrame()  # Return an empty DataFrame if no data

        # Ensure student_code is a string for correct comparison
        student_code = str(student_code)
        
        # Filter records for the specified student
        student_records = df[df['CODIGO'].astype(str) == student_code].copy()
        
        if student_records.empty:
            print(f"No records found for student code: {student_code}")
            return pd.DataFrame()  # Return empty DataFrame if no records are found
        
        # Ensure 'PERIODO' is treated as a string
        student_records['PERIODO'] = student_records['PERIODO'].astype(str)
        return student_records.reset_index(drop=True)
