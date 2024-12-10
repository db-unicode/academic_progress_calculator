from typing import List, Dict
from student_registry_manager.student_registry_manager import StudentRegistryManager  # Import your StudentRegistryManager

class SimpleCoursesLogic:
    
    @staticmethod
    def get_approved_courses_summary(student_manager: StudentRegistryManager, course_codes: List[str]) -> Dict[str, any]:
        """
        Returns a summary of approved courses for a student based on provided course codes.
        
        :param student_manager: An instance of StudentRegistryManager.
        :param course_codes: List of course codes to check for approval.
        :return: A dictionary with:
                - 'approved_courses': List of approved course codes.
                - 'total_approved_courses': Total number of approved courses.
                - 'total_courses': Total number of courses in the input list.
                - 'approval_percentage': Percentage of courses approved.
        """
        approved_courses = []

        # Check each course code for approval
        for course_code in course_codes:
            if student_manager.approve_subject_until_specified_period(course_code):
                approved_courses.append(course_code)

        # Calculate summary values
        total_approved_courses = len(approved_courses)
        total_courses = len(course_codes)
        approval_percentage = (total_approved_courses / total_courses * 100) if total_courses > 0 else 0

        # Return summary as dictionary
        return {
            "approved_courses": approved_courses,
            "total_approved_courses": total_approved_courses,
            "total_courses": total_courses,
            "approval_percentage": approval_percentage
        }
