from dataclasses import dataclass
from typing import List, Dict, Literal, Type

# Define a literal type for "REQUIRED" and "OPTIONAL" status of a course
CourseType = Literal["REQUIRED", "OPTIONAL"]

@dataclass
class CourseBundle:
    """
    Represents a bundle of courses with the minimum credits required, 
    related course bundles, and a dictionary of courses with their type 
    (either "REQUIRED" or "OPTIONAL").
    """
    minimum_credits_to_pass: int
    related_bundles: List[str]
    courses: Dict[str, CourseType]

    @classmethod
    def from_json(cls: Type['CourseBundle'], data: dict) -> 'CourseBundle':
        return cls(
            minimum_credits_to_pass=data["minimum_credits_to_pass"],
            related_bundles=data["related_bundles"],
            courses=data["courses"]
        )

    def __str__(self) -> str:
        related_bundles_str = ", ".join(self.related_bundles)
        courses_str = "\n    ".join(f"{code}: {type_}" for code, type_ in self.courses.items())
        return (
            f"CourseBundle:\n"
            f"  Minimum Credits to Pass: {self.minimum_credits_to_pass}\n"
            f"  Related Bundles: {related_bundles_str}\n"
            f"  Courses:\n    {courses_str}"
        )
