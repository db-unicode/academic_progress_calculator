import pandas as pd
from queries.student_queries import StudentQueries  
from queries.period_queries import PeriodQueries  
from queries.subject_queries import SubjectQueries  
from approve_subject_logic.approve_subject_logic import ApproveSubjectLogic  

class StudentRegistryManager:
    def __init__(self, student_code: str, specified_period: str) -> None:
        """
        Initializes the student registry manager with the full records for a student and the
        records up to a specified period.

        :param student_code: The student code to retrieve records.
        :param specified_period: The period up to which to filter records.
        """
        # Initialize attributes
        self.student_code: str = student_code
        self.specified_period: str = specified_period
        
        # Use StudentQueries to get the complete student records
        self.full_student_dataframe: pd.DataFrame = StudentQueries.get_student_records(student_code)
        
        # Use PeriodQueries to filter records up to the specified period
        self.student_dataframe_until_specified_period: pd.DataFrame = (
            PeriodQueries.filter_records_before_period(self.full_student_dataframe, specified_period)
        )

    def approve_subject_until_specified_period(self, subject_code: str) -> bool:
        """
        Checks if the student has passed or homologated a specific subject before the specified period.

        :param subject_code: The subject code to check for approval.
        :return: True if the student has passed or homologated the subject before the specified period, False otherwise.
        """
        # Filter the subject records until the specified period
        subject_records = SubjectQueries.get_subject(self.student_dataframe_until_specified_period, subject_code)
        
        # Use ApproveSubjectLogic to determine if the student passed the subject
        return ApproveSubjectLogic.has_passed_subject(subject_records)

    def get_subject_credits(self, subject_code: str) -> float:
        """
        Retrieves the number of credits for a specific subject for this student.

        :param subject_code: The code of the subject to retrieve credits for.
        :return: The number of credits for the specified subject as a float. Returns 0.0 if not found.
        """
        return SubjectQueries.get_subject_credits(self.full_student_dataframe, subject_code)

    def __repr__(self) -> str:
        return (f"StudentRegistryManager(student_code={self.student_code}, "
                f"specified_period={self.specified_period}, "
                f"full_student_dataframe=DataFrame with {len(self.full_student_dataframe)} records, "
                f"student_dataframe_until_specified_period=DataFrame with "
                f"{len(self.student_dataframe_until_specified_period)} records)")
