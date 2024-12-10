import pandas as pd

class SubjectQueries:
    @staticmethod
    def get_subject(df: pd.DataFrame, subject_code: str) -> pd.DataFrame:
        """
        Filters records for a specific subject based on the subject code.
        
        :param df: The DataFrame containing student and subject records.
        :param subject_code: The code of the subject to filter.
        :return: A DataFrame with the records for the specified subject.
        """
        # Ensure subject_code is a string for correct comparison
        subject_code = str(subject_code)
        
        # Filter records for the specified subject
        subject_records = df[df['MATERIA'] == subject_code].copy()
        
        # Check if records are found for the subject
        if subject_records.empty:
            print(f"No records found for subject code: {subject_code}")
        
        return subject_records.reset_index(drop=True)

    @staticmethod
    def get_subject_credits(df: pd.DataFrame, subject_code: str) -> float:
        """
        Retrieves the number of credits for a specific subject based on the subject code.
        
        :param df: The DataFrame containing student and subject records.
        :param subject_code: The code of the subject to retrieve credits for.
        :return: The number of credits for the specified subject as a float. Returns 0.0 if not found.
        """
        # Filter for the specific subject
        subject_records = SubjectQueries.get_subject(df, subject_code)
        
        # Check if the "NUMERO_CREDITOS" column exists and retrieve the credits
        if not subject_records.empty and "NUMERO_CREDITOS" in subject_records.columns:
            return subject_records["NUMERO_CREDITOS"].iloc[0]  # Retrieve the first credit value found
        else:
            print(f"No credit information found for subject code: {subject_code}")
            return 0.0
