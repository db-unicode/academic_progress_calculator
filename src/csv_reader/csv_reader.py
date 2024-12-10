import pandas as pd
from pathlib import Path
from typing import Optional

class CSVReader:
    _instance: Optional['CSVReader'] = None
    _csv_data: Optional[pd.DataFrame] = None

    def __new__(cls, file_path: Path) -> 'CSVReader':
        if cls._instance is None:
            cls._instance = super(CSVReader, cls).__new__(cls)
            cls._instance._load_csv(file_path)
        return cls._instance

    def _load_csv(self, file_path: Path) -> None:
        if CSVReader._csv_data is None:
            try:
                CSVReader._csv_data = pd.read_csv(file_path, sep=';', encoding='utf-8')
                print("CSV file loaded successfully.")
            except pd.errors.ParserError as e:
                print(f"Error loading CSV file: {e}")
                CSVReader._csv_data = None
        else:
            print("CSV file already loaded.")

    @staticmethod
    def get_data() -> Optional[pd.DataFrame]:
        if CSVReader._csv_data is not None:
            return CSVReader._csv_data
        else:
            print("No CSV file loaded.")
            return None
