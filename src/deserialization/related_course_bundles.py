from typing import Dict, Set
from deserialization.course_bundle import CourseBundle

class RelatedCourseBundles:
    group_name: str
    related_bundles: Dict[str, CourseBundle]
    common_courses: Set[str]

    def __init__(self, group_name: str, course_bundles: Dict[str, CourseBundle], related_names: Set[str]):
        """
        Initializes a RelatedCourseBundles instance for a single group of related CourseBundle instances.

        :param group_name: The concatenated name of all related course bundles for this group.
        :param course_bundles: All CourseBundle instances in CompleteData.
        :param related_names: A set of course bundle names that are mutually related to the group_name.
        """
        self.group_name = group_name
        self.related_bundles = {name: course_bundles[name] for name in related_names if name in course_bundles}
        self.common_courses = self._find_common_courses()

    def _find_common_courses(self) -> Set[str]:
        """
        Finds common courses among all CourseBundle instances in related_bundles.

        :return: A set of course codes that are common across all related CourseBundle instances.
        """
        # Initialize with the course set from the first CourseBundle, or an empty set if none
        if not self.related_bundles:
            return set()
        
        # Start with the course codes from the first CourseBundle
        common_courses = set(next(iter(self.related_bundles.values())).courses.keys())
        
        # Intersect with the course codes from each subsequent CourseBundle
        for bundle in self.related_bundles.values():
            common_courses.intersection_update(bundle.courses.keys())

        return common_courses

    def get_related_bundles(self) -> Dict[str, CourseBundle]:
        """
        Returns the dictionary of related course bundles.

        :return: A dictionary of related CourseBundle instances.
        """
        return self.related_bundles

    def get_common_courses(self) -> Set[str]:
        """
        Returns the set of common course codes across all related CourseBundle instances.

        :return: A set of common course codes.
        """
        return self.common_courses

    def __getitem__(self, bundle_name: str) -> CourseBundle:
        return self.related_bundles[bundle_name]

    def __iter__(self):
        return iter(self.related_bundles.items())

    def __len__(self) -> int:
        return len(self.related_bundles)

    def __str__(self) -> str:
        related_bundles_str = ", ".join(self.related_bundles.keys())
        common_courses_str = ", ".join(self.common_courses)
        return f"RelatedCourseBundles({self.group_name}): Related Bundles: [{related_bundles_str}], Common Courses: [{common_courses_str}]"
