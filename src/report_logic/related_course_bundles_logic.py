from typing import Dict, Set, Any
from deserialization.related_course_bundles import RelatedCourseBundles
from student_registry_manager.student_registry_manager import StudentRegistryManager

class RelatedCourseBundlesLogic:
    @staticmethod
    def _get_total_credits(related_course_bundles: RelatedCourseBundles, course_bundle_name: str) -> int:
        """Retrieves the minimum credits to pass for a given course bundle."""
        bundle = related_course_bundles[course_bundle_name]
        return bundle.minimum_credits_to_pass  # Use minimum_credits_to_pass directly

    @staticmethod
    def _calculate_approved_credits(
        related_course_bundles: RelatedCourseBundles, 
        student_registry_manager: StudentRegistryManager, 
        course_bundle_name: str
    ) -> float:
        """Calculates the total approved credits for a given course bundle."""
        bundle = related_course_bundles[course_bundle_name]
        return sum(
            student_registry_manager.get_subject_credits(subject)
            for subject in bundle.courses.keys()
            if student_registry_manager.approve_subject_until_specified_period(subject)
        )

    @staticmethod
    def _get_approved_subject_codes(
        related_course_bundles: RelatedCourseBundles, 
        student_registry_manager: StudentRegistryManager, 
        course_bundle_name: str
    ) -> Set[str]:
        """Gets the set of approved subject codes for a given course bundle."""
        bundle = related_course_bundles[course_bundle_name]
        return {
            subject
            for subject in bundle.courses.keys()
            if student_registry_manager.approve_subject_until_specified_period(subject)
        }

    @staticmethod
    def _calculate_completion_percentage(total_credits: int, approved_credits: float) -> float:
        """Calculates the completion percentage for a bundle."""
        return (approved_credits / total_credits * 100) if total_credits > 0 else 0.0

    @staticmethod
    def _get_bundle_with_highest_approved_percentage(bundles_info: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
        """Finds the bundle with the highest approved percentage."""
        highest = max(
            bundles_info.items(),
            key=lambda x: x[1]["completion_percentage"]
        )
        bundle_name, bundle_info = highest
        return {
            "bundle_name": bundle_name,
            "approved_percentage": bundle_info["completion_percentage"],
            "total_credits": bundle_info["total_credits"],
            "approved_credits": bundle_info["approved_credits"],
            "approved_subject_codes": bundle_info["approved_subject_codes"],
        }

    @staticmethod
    def get_course_bundles_summary(
        related_course_bundles: RelatedCourseBundles, 
        student_registry_manager: StudentRegistryManager
    ) -> Dict[str, Any]:
        """
        Generates a summary dictionary of all course bundles with their total and approved credits and completion percentage.
        
        :param related_course_bundles: An instance of RelatedCourseBundles.
        :param student_registry_manager: An instance of StudentRegistryManager.
        :return: A dictionary summarizing each course bundle and the bundle with the highest approved percentage.
        """
        bundles_info: Dict[str, Dict[str, Any]] = {}
        
        for bundle_name in related_course_bundles.related_bundles.keys():
            # Use minimum_credits_to_pass directly for total credits
            total_credits = RelatedCourseBundlesLogic._get_total_credits(related_course_bundles, bundle_name)
            approved_credits = RelatedCourseBundlesLogic._calculate_approved_credits(
                related_course_bundles, student_registry_manager, bundle_name
            )
            approved_subject_codes = RelatedCourseBundlesLogic._get_approved_subject_codes(
                related_course_bundles, student_registry_manager, bundle_name
            )
            completion_percentage = RelatedCourseBundlesLogic._calculate_completion_percentage(total_credits, approved_credits)
            
            bundles_info[bundle_name] = {
                "total_credits": total_credits,
                "approved_credits": approved_credits,
                "approved_subject_codes": approved_subject_codes,
                "completion_percentage": completion_percentage,
            }
        
        highest_approved_percentage_info = RelatedCourseBundlesLogic._get_bundle_with_highest_approved_percentage(bundles_info)
        
        return {
            "course_bundles": bundles_info,
            "highest_approved_percentage": highest_approved_percentage_info
        }
