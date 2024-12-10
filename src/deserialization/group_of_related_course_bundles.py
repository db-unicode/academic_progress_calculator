from typing import Dict, Set
from deserialization.course_bundle import CourseBundle
from deserialization.related_course_bundles import RelatedCourseBundles

class GroupOfRelatedCourseBundles:
    groups: Dict[str, RelatedCourseBundles]

    def __init__(self, course_bundles: Dict[str, CourseBundle]):
        """
        Initializes and creates all related course bundle groups from the given course bundles.

        :param course_bundles: All CourseBundle instances from CompleteData.
        """
        self.groups: Dict[str, RelatedCourseBundles] = {}
        self._create_groups(course_bundles)

    def _create_groups(self, course_bundles: Dict[str, CourseBundle]) -> None:
        """
        Creates groups of related CourseBundle instances and stores them in the `groups` attribute.

        :param course_bundles: A dictionary of CourseBundle instances.
        """
        visited: Set[str] = set()

        def explore_group(bundle_name: str, related_names: Set[str]) -> None:
            """
            Recursively collects related bundles for the current group.

            :param bundle_name: The name of the bundle to add to the current group.
            :param related_names: A set that accumulates all mutually related bundle names.
            """
            if bundle_name in visited:
                return
            visited.add(bundle_name)
            related_names.add(bundle_name)
            
            for related_name in course_bundles[bundle_name].related_bundles:
                if related_name in course_bundles:
                    explore_group(related_name, related_names)

        for bundle_name in course_bundles:
            if bundle_name not in visited:
                related_names = set()
                explore_group(bundle_name, related_names)
                if related_names:
                    # Create a concatenated name by joining all related names with "/"
                    concatenated_name = "/".join(sorted(related_names))
                    self.groups[concatenated_name] = RelatedCourseBundles(concatenated_name, course_bundles, related_names)

    def get_groups(self) -> Dict[str, RelatedCourseBundles]:
        """
        Returns the dictionary of grouped related course bundles.

        :return: A dictionary where each key is a group identifier and the value is a RelatedCourseBundles instance.
        """
        return self.groups

    def __getitem__(self, group_name: str) -> RelatedCourseBundles:
        return self.groups[group_name]

    def __iter__(self):
        return iter(self.groups.items())

    def __len__(self) -> int:
        return len(self.groups)

    def __str__(self) -> str:
        return "\n".join(str(group) for group in self.groups.values())
