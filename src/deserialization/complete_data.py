import json
from dataclasses import dataclass, field
from typing import List, Dict, Type
from pathlib import Path

from deserialization.course_bundle import CourseBundle
from deserialization.group_of_related_course_bundles import GroupOfRelatedCourseBundles


@dataclass
class CompleteData:
    """
    Represents the complete data structure with three main properties:
    - simple_courses: List of course codes.
    - course_bundles: Dictionary of CourseBundle instances.
    - group_of_related_course_bundles: Instance of GroupOfRelatedCourseBundles that contains grouped related course bundles.
    """
    simple_courses: List[str]
    course_bundles: Dict[str, CourseBundle]
    group_of_related_course_bundles: GroupOfRelatedCourseBundles = field(init=False)

    @classmethod
    def from_json_file(cls: Type['CompleteData'], file_path: Path) -> 'CompleteData':
        """
        Loads the data from a JSON file and initializes the CompleteData instance.
        
        :param file_path: The Path to the JSON file containing the data.
        :return: An instance of CompleteData with course bundles and related course bundle groups initialized.
        """
        with file_path.open('r', encoding='utf-8') as file:  # Se especifica la codificación utf-8
            data = json.load(file)
        
        # Convert the new simple_courses format into a list of course codes
        simple_courses = [course["code"] for course in data["simple_courses"]]
        
        # Convert each course bundle in JSON to a CourseBundle instance
        course_bundles: Dict[str, CourseBundle] = {
            name: CourseBundle.from_json(bundle_data)
            for name, bundle_data in data["course_bundles"].items()
        }
        
        # Initialize the instance with simple_courses and course_bundles
        instance = cls(
            simple_courses=simple_courses,
            course_bundles=course_bundles
        )
        
        # Initialize group_of_related_course_bundles as a GroupOfRelatedCourseBundles instance
        instance.group_of_related_course_bundles = GroupOfRelatedCourseBundles(course_bundles)
        
        return instance

    def get_group_of_related_course_bundles(self) -> GroupOfRelatedCourseBundles:
        """
        Returns the GroupOfRelatedCourseBundles instance.
        
        :return: An instance of GroupOfRelatedCourseBundles.
        """
        return self.group_of_related_course_bundles

    def __str__(self) -> str:
        simple_courses_str = ", ".join(self.simple_courses)
        course_bundles_str = "\n\n".join(f"{name}:\n{bundle}" for name, bundle in self.course_bundles.items())
        related_bundles_str = str(self.group_of_related_course_bundles)
        
        return (
            f"CompleteData:\n"
            f"  Simple Courses: {simple_courses_str}\n"
            f"  Course Bundles:\n{course_bundles_str}\n\n"
            f"  Group of Related Course Bundles:\n{related_bundles_str}"
        )
