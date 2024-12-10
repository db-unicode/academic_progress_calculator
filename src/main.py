import yaml
import json
from pathlib import Path
from csv_reader.csv_reader import CSVReader
from student_registry_manager.student_registry_manager import StudentRegistryManager
from deserialization.complete_data import CompleteData
from report_logic.complete_report_logic import CompleteReportLogic
from output_printer.output_printer import save_report

def main(config_path: Path) -> None:
    """
    Main function to generate and save the complete report for each student in the list.
    
    :param config_path: Path to the YAML configuration file.
    """
    # Load configuration from YAML file
    with config_path.open('r', encoding='utf-8') as file:
        config = yaml.safe_load(file)
    
    csv_path = Path(config['data_set_path'])
    specified_period = config['report_until_date']
    json_path = Path(config['curriculum_structure_path'])
    output_dir = Path(config['output_path'])
    student_codes_path = Path(config['student_codes'])
    report_name = config['report_name']
    
    # Load CSV data into a singleton CSVReader
    CSVReader(csv_path)
    
    # Load CompleteData from the JSON file
    complete_data = CompleteData.from_json_file(json_path)
    
    # Load student codes from the JSON file
    with student_codes_path.open('r', encoding='utf-8') as file:
        student_codes = json.load(file)
    
    # Generate and save a report for each student
    for student_code in student_codes:
        student_registry_manager = StudentRegistryManager(str(student_code), specified_period)
        complete_report = CompleteReportLogic.get_complete_report(complete_data, student_registry_manager)
        save_report(complete_report, output_dir, report_name, str(student_code))

if __name__ == "__main__":
    # Define the path to the configuration file
    config_path = Path("src/config.yml")

    # Run the main function
    main(config_path)