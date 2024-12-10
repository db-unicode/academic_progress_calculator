from pathlib import Path
from csv_reader.csv_reader import CSVReader
from student_registry_manager.student_registry_manager import StudentRegistryManager
from deserialization.complete_data import CompleteData
from report_logic.complete_report_logic import CompleteReportLogic

def main(csv_path: Path, student_code: str, specified_period: str, json_path: Path) -> None:
    """
    Main function to generate and print the complete report for a student.
    
    :param csv_path: Path to the CSV file containing student data.
    :param student_code: The code of the student to analyze.
    :param specified_period: The period up to which to filter records (e.g., "202120").
    :param json_path: Path to the JSON file containing course bundle data.
    """
    # Load CSV data into a singleton CSVReader
    CSVReader(csv_path)

    # Load CompleteData from the JSON file
    complete_data = CompleteData.from_json_file(json_path)

    # Create a StudentRegistryManager for the specified student and period
    student_registry_manager = StudentRegistryManager(student_code, specified_period)

    # Generate the complete report
    complete_report = CompleteReportLogic.get_complete_report(complete_data, student_registry_manager)

    # Print the complete report
    print(complete_report)

if __name__ == "__main__":
    # Define paths and parameters
    csv_path = Path("src/data/datos_investigacion.csv")
    student_code = "710220101"
    specified_period = "202520"  # Replace with the actual period you need
    json_path = Path("src/data/sistemas.json")

    # Run the main function
    main(csv_path, student_code, specified_period, json_path)
