from typing import Dict, Any
from student_registry_manager.student_registry_manager import StudentRegistryManager
from deserialization.complete_data import CompleteData
from report_logic.group_of_related_course_bundles_logic import GroupOfRelatedCourseBundlesLogic
from report_logic.simple_courses_logic import SimpleCoursesLogic

class CompleteReportLogic:
    @staticmethod
    def _generate_simple_courses_report(
        complete_data: CompleteData, 
        student_registry_manager: StudentRegistryManager
    ) -> Dict[str, Any]:
        """
        Generates a report for simple courses using SimpleCoursesLogic.

        :param complete_data: An instance of CompleteData.
        :param student_registry_manager: An instance of StudentRegistryManager.
        :return: A dictionary containing information about the simple courses.
        """
        return SimpleCoursesLogic.get_approved_courses_summary(
            student_registry_manager, 
            complete_data.simple_courses
        )

    @staticmethod
    def _generate_group_of_related_bundles_report(
        complete_data: CompleteData, 
        student_registry_manager: StudentRegistryManager
    ) -> Dict[str, Any]:
        """
        Generates a report for the group of related course bundles using GroupOfRelatedCourseBundlesLogic.

        :param complete_data: An instance of CompleteData.
        :param student_registry_manager: An instance of StudentRegistryManager.
        :return: A dictionary containing information about all related course bundles.
        """
        return GroupOfRelatedCourseBundlesLogic.get_full_report(
            complete_data.group_of_related_course_bundles, 
            student_registry_manager
        )

    @staticmethod
    def get_complete_report(
        complete_data: CompleteData, 
        student_registry_manager: StudentRegistryManager
    ) -> Dict[str, Any]:
        """
        Generates the complete report for both simple courses and related course bundles.

        :param complete_data: An instance of CompleteData.
        :param student_registry_manager: An instance of StudentRegistryManager.
        :return: A dictionary containing the complete report for both simple courses and related course bundles.
        """
        simple_courses_report = CompleteReportLogic._generate_simple_courses_report(
            complete_data, 
            student_registry_manager
        )
        group_of_related_bundles_report = CompleteReportLogic._generate_group_of_related_bundles_report(
            complete_data, 
            student_registry_manager
        )

        return {
            "simple_courses": simple_courses_report,
            "group_of_related_course_bundles": group_of_related_bundles_report
        }
