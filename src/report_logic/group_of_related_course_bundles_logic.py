from typing import Dict, Any
from deserialization.group_of_related_course_bundles import GroupOfRelatedCourseBundles
from student_registry_manager.student_registry_manager import StudentRegistryManager
from report_logic.related_course_bundles_logic import RelatedCourseBundlesLogic
from deserialization.related_course_bundles import RelatedCourseBundles

class GroupOfRelatedCourseBundlesLogic:
    @staticmethod
    def _get_related_bundle_summary(
        related_bundle_name: str, 
        related_course_bundle: 'RelatedCourseBundles',  # Use RelatedCourseBundles directly
        student_registry_manager: StudentRegistryManager
    ) -> Dict[str, Any]:
        """
        Generates a summary for a single related course bundle using RelatedCourseBundlesLogic.

        :param related_bundle_name: The name of the related course bundle.
        :param related_course_bundle: An instance of RelatedCourseBundles.
        :param student_registry_manager: The StudentRegistryManager instance.
        :return: A dictionary with information for a specific related course bundle.
        """
        # Generate the summary for the single RelatedCourseBundles instance
        return RelatedCourseBundlesLogic.get_course_bundles_summary(
            related_course_bundle,  # Pass the RelatedCourseBundles instance directly
            student_registry_manager
        )

    @staticmethod
    def _aggregate_summaries(
        group_of_related_bundles: GroupOfRelatedCourseBundles, 
        student_registry_manager: StudentRegistryManager
    ) -> Dict[str, Dict[str, Any]]:
        """
        Iterates over each related course bundle group and aggregates summaries for each group.

        :param group_of_related_bundles: An instance of GroupOfRelatedCourseBundles.
        :param student_registry_manager: An instance of StudentRegistryManager.
        :return: A dictionary containing summaries for all related course bundles.
        """
        summary_report: Dict[str, Dict[str, Any]] = {}

        # Iterate over each RelatedCourseBundles in the GroupOfRelatedCourseBundles
        for group_name, related_bundle in group_of_related_bundles.get_groups().items():
            summary_report[group_name] = GroupOfRelatedCourseBundlesLogic._get_related_bundle_summary(
                group_name, related_bundle, student_registry_manager
            )

        return summary_report

    @staticmethod
    def get_full_report(
        group_of_related_bundles: GroupOfRelatedCourseBundles, 
        student_registry_manager: StudentRegistryManager
    ) -> Dict[str, Any]:
        """
        Generates a complete report for all related course bundles.

        :param group_of_related_bundles: An instance of GroupOfRelatedCourseBundles.
        :param student_registry_manager: An instance of StudentRegistryManager.
        :return: A dictionary containing the full report for all related course bundles.
        """
        return GroupOfRelatedCourseBundlesLogic._aggregate_summaries(
            group_of_related_bundles, student_registry_manager
        )
