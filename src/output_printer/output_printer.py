import json
from pathlib import Path
from typing import Dict, Any

def convert_sets_to_lists(data: Any) -> Any:
    """
    Recursively converts sets to lists in the given data structure.
    
    :param data: The data structure to convert.
    :return: The converted data structure with sets as lists.
    """
    if isinstance(data, dict):
        return {k: convert_sets_to_lists(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [convert_sets_to_lists(item) for item in data]
    elif isinstance(data, set):
        return list(data)
    else:
        return data

def save_report(report: Dict[str, Any], output_dir: Path, file_name: str, student_code: str) -> None:
    """
    Saves the report to a JSON file in the specified output directory.
    
    :param report: The report data to save.
    :param output_dir: The directory where the report file will be saved.
    :param file_name: The base name of the report file.
    :param student_code: The student code to include in the report file name.
    """
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / f"{file_name}-{student_code}.json"
    report = convert_sets_to_lists(report)
    with output_file.open('w', encoding='utf-8') as file:
        json.dump(report, file, ensure_ascii=False, indent=4)
    print(f"Report saved to {output_file}")